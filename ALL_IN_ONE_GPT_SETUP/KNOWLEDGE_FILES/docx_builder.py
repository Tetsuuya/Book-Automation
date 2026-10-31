# -*- coding: utf-8 -*-
"""
DEPED MATATAG PUBLICATION-GRADE DOCX BUILDER & COMPILER ENGINE
Use this Python script in OpenAI Code Interpreter or local Python environment
to compile complete 40+ page interactive multimedia textbooks (.docx) with
verbatim content preservation, clean mathematical typography, and benchmark styling.

Supports both:
1. Direct CLI Compilation:
   python 03_DOCX_BUILDER_SCRIPT.py <input.md> [output.docx]
2. Programmatic API:
   from 03_DOCX_BUILDER_SCRIPT import compile_markdown_to_docx, initialize_document, add_formula_box
"""

import os
import sys
import re
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==========================================
# 1. XML STYLING UTILITIES
# ==========================================

def set_cell_shading(cell, color_hex):
    """Set background color fill for a table cell."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    """Set internal cell padding (in dxa: 20 dxa = 1 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_callout_border(cell, color_hex="1B365D", sz="36"):
    """Set a bold solid left border stripe for callout boxes (sz 36 = 4.5pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)

def set_dashed_border(cell, color_hex="CCCCCC", sz="12"):
    """Set dashed border around figure specification containers."""
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="dashed" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:left w:val="dashed" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:bottom w:val="dashed" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:right w:val="dashed" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)

def set_table_grid_borders(table, color_hex="D0D7DE", sz="4"):
    """Set crisp light-gray borders for tables."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def set_table_no_borders(table):
    """Remove all borders from a container table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="none"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="none"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

# ==========================================
# 2. MATHEMATICAL TYPOGRAPHY SANITIZER
# ==========================================

def clean_math_text(text):
    r"""
    Transforms LaTeX symbols and artifacts into clean, human-readable textbook typography.
    Never outputs raw LaTeX commands like \qquad or \frac in the Word document.
    """
    if not text:
        return ""
    
    # Horizontal spacing
    text = text.replace(r"\qquad", "    —    ")
    text = text.replace(r"\quad", "  ")
    text = text.replace(r"\hspace{1cm}", "    ")
    text = text.replace(r"\hspace{0.5cm}", "  ")
    
    # Operators and symbols
    text = text.replace(r"\times", "×")
    text = text.replace(r"\cdot", "·")
    text = text.replace(r"\div", "÷")
    text = text.replace(r"\pm", "±")
    text = text.replace(r"\pi", "π")
    text = text.replace(r"\theta", "θ")
    text = text.replace(r"\degree", "°")
    text = text.replace(r"^\circ", "°")
    text = text.replace(r"\le", "≤").replace(r"\leq", "≤")
    text = text.replace(r"\ge", "≥").replace(r"\geq", "≥")
    text = text.replace(r"\neq", "≠")
    text = text.replace(r"\approx", "≈")
    text = text.replace(r"\infty", "∞")
    
    # Fractions: \frac{a}{b} -> (a / b)
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1 / \2)', text)
    # Square roots: \sqrt{x} -> √(x)
    text = re.sub(r'\\sqrt\{([^}]+)\}', r'√(\1)', text)
    # Text wrappers
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)
    # Exponents
    text = re.sub(r'\^2\b', '²', text)
    text = re.sub(r'\^3\b', '³', text)
    
    # Delimiters
    text = text.replace(r"\[", "").replace(r"\]", "")
    text = text.replace("$$", "").replace("$", "")
    return text

# ==========================================
# 3. MODULAR API HELPERS
# ==========================================

def format_paragraph(p, space_before=0, space_after=4, line_spacing=1.15, align=WD_ALIGN_PARAGRAPH.LEFT):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    p.alignment = align

def set_outline_level(p, level):
    """Marks a paragraph as a heading level (0 = H1) without changing its banner styling."""
    p._p.get_or_add_pPr().append(parse_xml(f'<w:outlineLvl {nsdecls("w")} w:val="{level}"/>'))

def add_page_number_field(paragraph, size=8.5):
    """Appends a live PAGE field so printed page numbers match the TOC."""
    run = paragraph.add_run()
    run.font.name = 'Cambria'
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor(0x77, 0x77, 0x77)
    for kind, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if kind:
            el = OxmlElement('w:fldChar')
            el.set(qn('w:fldCharType'), kind)
        else:
            el = OxmlElement('w:instrText')
            el.set(qn('xml:space'), 'preserve')
            el.text = text
        run._r.append(el)

def add_hyperlink(paragraph, text, url, size=10.5, bold=False, italic=False):
    """Adds a clickable external hyperlink run (used for YouTube Direct Links and sources)."""
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    link = OxmlElement('w:hyperlink')
    link.set(qn('r:id'), r_id)
    r = OxmlElement('w:r')
    rPr = parse_xml(
        f'<w:rPr {nsdecls("w")}><w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/>'
        f'{"<w:b/>" if bold else ""}{"<w:i/>" if italic else ""}'
        f'<w:color w:val="0563C1"/><w:sz w:val="{int(size * 2)}"/><w:u w:val="single"/></w:rPr>'
    )
    r.append(rPr)
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    r.append(t)
    link.append(r)
    paragraph._p.append(link)

def add_heading_1(doc, text):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, "1B365D")
    set_cell_margins(c, top=120, bottom=120, left=180, right=180)
    set_table_no_borders(t)
    p = c.paragraphs[0]
    format_paragraph(p, space_before=2, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_outline_level(p, 0)
    run = p.add_run(clean_math_text(text).upper())
    run.font.name = 'Cambria'
    run.font.size = Pt(13.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p_sp = doc.add_paragraph()
    format_paragraph(p_sp, space_before=0, space_after=4)
    return p

def add_heading_2(doc, text):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, "EBF3FA")
    set_callout_border(c, color_hex="1B365D", sz="36")
    set_cell_margins(c, top=80, bottom=80, left=150, right=150)
    set_table_no_borders(t)
    p = c.paragraphs[0]
    format_paragraph(p, space_before=2, space_after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
    set_outline_level(p, 1)
    run = p.add_run(clean_math_text(text))
    run.font.name = 'Cambria'
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    p_sp = doc.add_paragraph()
    format_paragraph(p_sp, space_before=0, space_after=3)
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=6, space_after=2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(clean_math_text(text))
    run.font.name = 'Cambria'
    run.font.size = Pt(11.0)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x2A, 0x4B, 0x7C)
    return p

def add_body_p(doc, text, bold_prefix="", italic_prefix=""):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=0, space_after=3.5, line_spacing=1.15)
    if bold_prefix:
        r_b = p.add_run(clean_math_text(bold_prefix))
        r_b.font.name = 'Cambria'
        r_b.font.size = Pt(10.5)
        r_b.font.bold = True
        r_b.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    if italic_prefix:
        r_i = p.add_run(clean_math_text(italic_prefix))
        r_i.font.name = 'Cambria'
        r_i.font.size = Pt(10.5)
        r_i.font.italic = True
    run = p.add_run(clean_math_text(text))
    run.font.name = 'Cambria'
    run.font.size = Pt(10.5)
    run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

def add_callout_box(doc, title, items, bg_color="FAFAFA", border_color="1B365D"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, bg_color)
    set_callout_border(cell, border_color, "36")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p = cell.paragraphs[0]
    format_paragraph(p, space_before=2, space_after=4)
    run = p.add_run(clean_math_text(title))
    run.font.name = 'Cambria'
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    for item in items:
        pi = cell.add_paragraph()
        format_paragraph(pi, space_before=1, space_after=2)
        ri = pi.add_run(clean_math_text(item))
        ri.font.name = 'Cambria'
        ri.font.size = Pt(9.5)
        ri.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    p_sp = doc.add_paragraph()
    format_paragraph(p_sp, space_before=0, space_after=3)

def add_formula_box(doc, title, formula, where_items=None):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, "F4F7FA")
    set_callout_border(cell, "1B365D", "36")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p_title = cell.paragraphs[0]
    format_paragraph(p_title, space_before=2, space_after=3)
    r_t = p_title.add_run(clean_math_text(title))
    r_t.font.name = 'Cambria'
    r_t.font.size = Pt(10.5)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    p_eq = cell.add_paragraph()
    format_paragraph(p_eq, space_before=2, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_eq = p_eq.add_run(clean_math_text(formula))
    r_eq.font.name = 'Cambria'
    r_eq.font.size = Pt(12.0)
    r_eq.font.bold = True
    r_eq.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    if where_items:
        p_w = cell.add_paragraph()
        format_paragraph(p_w, space_before=2, space_after=1)
        rw = p_w.add_run("Where:")
        rw.font.name = 'Cambria'
        rw.font.size = Pt(9.5)
        rw.font.bold = True
        rw.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        for w in where_items:
            pw = cell.add_paragraph()
            format_paragraph(pw, space_before=1, space_after=1)
            rw2 = pw.add_run(f"• {clean_math_text(w)}")
            rw2.font.name = 'Cambria'
            rw2.font.size = Pt(9.0)
            rw2.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    p_sp = doc.add_paragraph()
    format_paragraph(p_sp, space_before=0, space_after=3)

def add_worked_example_box(doc, example_title, problem_text, given_items, formula_used, solution_steps, final_answer, verification=""):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, "F8FAFC")
    set_callout_border(cell, "2A4B7C", "36")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p_title = cell.paragraphs[0]
    format_paragraph(p_title, space_before=2, space_after=3)
    r_t = p_title.add_run(f"💡 {clean_math_text(example_title)}")
    r_t.font.name = 'Cambria'
    r_t.font.size = Pt(11.0)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    p_prob = cell.add_paragraph()
    format_paragraph(p_prob, space_before=2, space_after=3)
    rp_lbl = p_prob.add_run("Problem: ")
    rp_lbl.font.bold = True
    rp_lbl.font.color.rgb = RGBColor(0x2A, 0x4B, 0x7C)
    rp_txt = p_prob.add_run(clean_math_text(problem_text))
    rp_txt.font.name = 'Cambria'
    rp_txt.font.size = Pt(10.0)
    
    if given_items:
        p_g = cell.add_paragraph()
        format_paragraph(p_g, space_before=1, space_after=2)
        r_g = p_g.add_run(f"Step 1 (Given): {', '.join(clean_math_text(g) for g in given_items)}")
        r_g.font.name = 'Cambria'
        r_g.font.size = Pt(9.5)
        r_g.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
        
    if formula_used:
        p_f = cell.add_paragraph()
        format_paragraph(p_f, space_before=1, space_after=2)
        rf_lbl = p_f.add_run("Step 2 (Formula / Law): ")
        rf_lbl.font.bold = True
        rf_lbl.font.color.rgb = RGBColor(0x2A, 0x4B, 0x7C)
        rf_txt = p_f.add_run(clean_math_text(formula_used))
        rf_txt.font.name = 'Cambria'
        rf_txt.font.size = Pt(9.5)
        
    for s_idx, step in enumerate(solution_steps):
        ps = cell.add_paragraph()
        format_paragraph(ps, space_before=1, space_after=2)
        rs = ps.add_run(f"Step {s_idx + 3}: {clean_math_text(step)}")
        rs.font.name = 'Cambria'
        rs.font.size = Pt(9.5)
        rs.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        
    p_ans = cell.add_paragraph()
    format_paragraph(p_ans, space_before=3, space_after=2)
    ra_lbl = p_ans.add_run("✅ Final Answer: ")
    ra_lbl.font.bold = True
    ra_lbl.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    ra_txt = p_ans.add_run(clean_math_text(final_answer))
    ra_txt.font.name = 'Cambria'
    ra_txt.font.size = Pt(10.0)
    ra_txt.font.bold = True
    
    if verification:
        p_v = cell.add_paragraph()
        format_paragraph(p_v, space_before=1, space_after=2)
        rv_lbl = p_v.add_run("Verification: ")
        rv_lbl.font.bold = True
        rv_lbl.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
        rv_txt = p_v.add_run(clean_math_text(verification))
        rv_txt.font.name = 'Cambria'
        rv_txt.font.size = Pt(9.0)
        rv_txt.font.italic = True
    p_sp = doc.add_paragraph()
    format_paragraph(p_sp, space_before=0, space_after=3)

# ==========================================
# 4. MARKDOWN TO DOCX PARSER ENGINE
# ==========================================

def format_inline_runs(paragraph, text, default_size=10.5, default_color=None, default_bold=False, default_italic=False):
    """Parses inline bold, italic, code, and symbols within a paragraph run."""
    text = clean_math_text(text)
    pattern = r'(\[[^\]]+\]\(https?://[^)\s]+\)|https?://[^\s)|]+|\*\*[^*]+\*\*|\*[^*]+\*|_[^_]+_|`[^`]+`)'
    parts = re.split(pattern, text)
    
    for part in parts:
        if not part:
            continue
        link = re.fullmatch(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', part)
        if link or re.fullmatch(r'https?://[^\s)|]+', part):
            label, url = (link.group(1), link.group(2)) if link else (part, part)
            add_hyperlink(paragraph, label, url, size=default_size, bold=default_bold, italic=default_italic)
            continue
        if part.startswith('**') and part.endswith('**') and len(part) >= 4:
            r = paragraph.add_run(part[2:-2])
            r.bold = True
            r.italic = default_italic
        elif ((part.startswith('*') and part.endswith('*')) or (part.startswith('_') and part.endswith('_'))) and len(part) >= 2:
            r = paragraph.add_run(part[1:-1])
            r.bold = default_bold
            r.italic = True
        elif part.startswith('`') and part.endswith('`') and len(part) >= 2:
            r = paragraph.add_run(part[1:-1])
            r.font.name = 'Consolas'
            r.font.size = Pt(default_size - 1)
            continue
        else:
            r = paragraph.add_run(part)
            r.bold = default_bold
            r.italic = default_italic
            
        r.font.name = 'Cambria'
        r.font.size = Pt(default_size)
        if default_color:
            r.font.color.rgb = default_color
        else:
            r.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

def render_callout_box(doc, lines):
    """Renders blockquote callouts: YouTube modules, Figure specs, Formula cards, Worked examples."""
    all_text = " ".join(lines)
    is_youtube = any(k in all_text for k in ["INTERACTIVE MULTIMEDIA", "INTERAKTIBONG MULTIMEDIA", "🎥"])
    is_figure = any(k in all_text for k in ["Figure:", "Larawan:", "AI Generation Prompt", "Scene Specification", "🖼️", "📷"])
    is_formula = any(k in all_text for k in ["Formula Card", "FORMULA CARD", "📐"])
    is_example = any(k in all_text for k in ["Worked Example", "WORKED EXAMPLE", "💡"])
    
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_margins(c, top=120, bottom=120, left=180, right=180)
    
    if is_youtube:
        set_cell_shading(c, "FFF5F5")
        set_callout_border(c, color_hex="CC0000", sz="36")
    elif is_figure:
        set_cell_shading(c, "FAFAFA")
        set_dashed_border(c, color_hex="CCCCCC", sz="12")
    elif is_formula:
        set_cell_shading(c, "F4F7FA")
        set_callout_border(c, color_hex="1B365D", sz="36")
    elif is_example:
        set_cell_shading(c, "F8FAFC")
        set_callout_border(c, color_hex="2A4B7C", sz="36")
    else:
        set_cell_shading(c, "F4F7FA")
        set_callout_border(c, color_hex="1B365D", sz="36")
        
    for idx, line in enumerate(lines):
        clean_l = line.lstrip('> ').strip()
        if not clean_l:
            continue
        p = c.paragraphs[0] if idx == 0 and len(c.paragraphs) == 1 and not c.paragraphs[0].text else c.add_paragraph()
        format_paragraph(p, space_before=1, space_after=2, line_spacing=1.15)
        
        if clean_l.startswith('### '):
            clean_l = clean_l[4:]
            col = RGBColor(0xCC, 0x00, 0x00) if is_youtube else RGBColor(0x1B, 0x36, 0x5D)
            format_inline_runs(p, clean_l, default_size=10.5, default_color=col, default_bold=True)
        elif clean_l.startswith('## '):
            clean_l = clean_l[3:]
            format_inline_runs(p, clean_l, default_size=11.0, default_color=RGBColor(0x1B, 0x36, 0x5D), default_bold=True)
        elif clean_l.startswith('# '):
            clean_l = clean_l[2:]
            format_inline_runs(p, clean_l, default_size=11.5, default_color=RGBColor(0x1B, 0x36, 0x5D), default_bold=True)
        else:
            format_inline_runs(p, clean_l, default_size=9.5)
            
    p_sp = doc.add_paragraph()
    format_paragraph(p_sp, space_before=0, space_after=3)

def render_markdown_table(doc, table_lines):
    """Renders markdown tables with Navy header row, alternating zebra stripes, and clean cell padding."""
    rows_data = []
    for line in table_lines:
        line_s = line.strip()
        if not line_s.startswith('|'):
            continue
        if re.match(r'^\|[\s\-:|]+\|$', line_s):
            continue
        cells = [c.strip() for c in line_s.split('|')[1:-1]]
        if cells:
            rows_data.append(cells)
            
    if not rows_data:
        return
        
    num_cols = max(len(r) for r in rows_data)
    num_rows = len(rows_data)
    
    t = doc.add_table(rows=num_rows, cols=num_cols)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_grid_borders(t, color_hex="D0D7DE", sz="4")
    
    for r_idx, row in enumerate(rows_data):
        is_header = (r_idx == 0)
        for c_idx in range(num_cols):
            cell = t.cell(r_idx, c_idx)
            cell_text = row[c_idx] if c_idx < len(row) else ""
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            
            p = cell.paragraphs[0]
            format_paragraph(p, space_before=1, space_after=1, line_spacing=1.15)
            
            if is_header:
                set_cell_shading(cell, "1B365D")
                format_inline_runs(p, cell_text, default_size=9.5, default_color=RGBColor(0xFF, 0xFF, 0xFF), default_bold=True)
            else:
                bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
                set_cell_shading(cell, bg)
                format_inline_runs(p, cell_text, default_size=9.0)
                
    p_sp = doc.add_paragraph()
    format_paragraph(p_sp, space_before=0, space_after=3)

def extract_clean_markdown(text):
    """
    Cleans raw markdown or ChatGPT export files.
    Extracts response bodies, strips chat prompts, timestamps, and model thought logs.
    """
    if '## Prompt:' in text and '## Response:' in text:
        turns = text.split('## Prompt:')
        content_parts = []
        for t in turns[1:]:
            if '## Response:' in t:
                resp = t.split('## Response:')[1]
                lines = resp.splitlines()
                start_idx = 0
                while start_idx < len(lines) and (
                    not lines[start_idx].strip() or 
                    'PM' in lines[start_idx] or 
                    'AM' in lines[start_idx] or 
                    'gpt-' in lines[start_idx] or 
                    'Worked for' in lines[start_idx]
                ):
                    start_idx += 1
                
                end_idx = len(lines)
                while end_idx > start_idx and (
                    not lines[end_idx-1].strip() or 
                    lines[end_idx-1].strip().startswith('[Proceed') or 
                    lines[end_idx-1].strip().startswith('[Compile') or 
                    'Type `Proceed`' in lines[end_idx-1] or 
                    'Type Compile' in lines[end_idx-1]
                ):
                    end_idx -= 1
                
                cleaned_part = '\n'.join(lines[start_idx:end_idx]).strip()
                if cleaned_part:
                    # Ignore final stub confirmation
                    if 'Compilation and QA results' in cleaned_part and 'Download the complete textbook' in cleaned_part:
                        continue
                    content_parts.append(cleaned_part)
        return '\n\n[PAGE BREAK]\n\n'.join(content_parts)
    return text

def append_markdown_to_doc(doc, markdown_text):
    """
    Appends raw or cleaned markdown lines directly into an existing docx.Document.
    Preserves 100% of text, headings, callout boxes, and tables with zero truncation.
    """
    combined_md = extract_clean_markdown(markdown_text)
    lines = combined_md.splitlines()
    i = 0
    total = len(lines)

    while i < total:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if '[PAGE BREAK]' in stripped:
            doc.add_page_break()
            i += 1
            continue

        # Blockquote Containers (> ...)
        if stripped.startswith('>'):
            callout_lines = []
            while i < total and lines[i].strip().startswith('>'):
                callout_lines.append(lines[i])
                i += 1
            render_callout_box(doc, callout_lines)
            continue

        # Markdown Tables (| ... |)
        if stripped.startswith('|') and stripped.endswith('|'):
            table_lines = []
            while i < total and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i])
                i += 1
            render_markdown_table(doc, table_lines)
            continue

        # Heading 1 (# ...)
        if stripped.startswith('# '):
            h_text = stripped[2:].strip()
            if re.match(r'^PAGE \d+ -', h_text, re.IGNORECASE):
                pass
            else:
                add_heading_1(doc, h_text)
            i += 1
            continue

        # Heading 2 (## ...)
        if stripped.startswith('## '):
            h_text = stripped[3:].strip()
            add_heading_2(doc, h_text)
            i += 1
            continue

        # Heading 3 (### ...)
        if stripped.startswith('### '):
            h_text = stripped[4:].strip()
            add_heading_3(doc, h_text)
            i += 1
            continue

        # Bulleted Lists (* or - or •)
        if re.match(r'^[\*\-•]\s+', stripped):
            b_text = re.sub(r'^[\*\-•]\s+', '', stripped)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            format_paragraph(p, space_before=1, space_after=2, line_spacing=1.15)
            r_bullet = p.add_run("• ")
            r_bullet.font.name = 'Cambria'
            r_bullet.font.size = Pt(10.5)
            r_bullet.font.bold = True
            r_bullet.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
            format_inline_runs(p, b_text, default_size=10.5)
            i += 1
            continue

        # Numbered items / Quiz options ([  ] A., 1., etc.)
        if re.match(r'^(?:\[\s*\]|[0-9]+\.|\([a-z]\))\s+', stripped):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.2)
            format_paragraph(p, space_before=1, space_after=2, line_spacing=1.15)
            format_inline_runs(p, stripped, default_size=10.5)
            i += 1
            continue

        # Normal Paragraph
        p = doc.add_paragraph()
        format_paragraph(p, space_before=0, space_after=3.5, line_spacing=1.15)
        format_inline_runs(p, stripped, default_size=10.5)
        i += 1

def initialize_document(subject="Mathematics", grade="7", quarter="Quarter 3"):
    """
    Initializes a publication-grade Document with DepEd standard margins,
    running headers, and running footers.
    """
    doc = Document()
    for s in doc.sections:
        s.page_width = Inches(8.5)
        s.page_height = Inches(11.0)
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)
        s.different_first_page_header_footer = True

        # Running header on pages 2+
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr = hp.add_run(f"{subject} {grade} | {quarter}")
        hr.font.name = 'Cambria'
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(0x77, 0x77, 0x77)

        # Running footer on pages 2+
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        fr = fp.add_run(f"Grade {grade} {subject} • {quarter} • Page ")
        fr.font.name = 'Cambria'
        fr.font.size = Pt(8.5)
        fr.font.color.rgb = RGBColor(0x77, 0x77, 0x77)
        add_page_number_field(fp)

    return doc

def compile_markdown_to_docx(source_md_path_or_text, output_docx_path, subject="Mathematics", grade="7", quarter="Quarter 3"):
    """
    Main entry point: Compiles any markdown textbook file into a publication-grade DOCX.
    Preserves 100% of text and tables with zero truncation.
    """
    if os.path.exists(source_md_path_or_text):
        with open(source_md_path_or_text, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    else:
        raw_text = source_md_path_or_text

    doc = initialize_document(subject=subject, grade=grade, quarter=quarter)
    append_markdown_to_doc(doc, raw_text)
    doc.save(output_docx_path)
    print(f"Successfully compiled {output_docx_path} ({len(doc.paragraphs)} paragraphs, {len(doc.tables)} tables)")
    return output_docx_path

def append_markdown_to_docx(doc_path_or_doc, markdown_text, output_docx_path=None):
    """
    Progressively appends a markdown lesson chunk to an existing DOCX file.
    Enables multi-turn progressive compilation without token limits.
    """
    if isinstance(doc_path_or_doc, str):
        doc = Document(doc_path_or_doc)
        out_path = output_docx_path or doc_path_or_doc
    else:
        doc = doc_path_or_doc
        out_path = output_docx_path or "MATATAG_Textbook.docx"
        
    append_markdown_to_doc(doc, markdown_text)
    doc.save(out_path)
    return out_path

# ==========================================
# 5. CLI EXECUTION
# ==========================================

if __name__ == '__main__':
    if len(sys.argv) > 1:
        in_path = sys.argv[1]
        out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(in_path)[0] + ".docx"
        compile_markdown_to_docx(in_path, out_path)
    else:
        print("Usage: python 03_DOCX_BUILDER_SCRIPT.py <input_manuscript.md> [output_textbook.docx]")
