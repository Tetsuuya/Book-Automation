# -*- coding: utf-8 -*-
"""
Master Compiler for DepEd MATATAG Mathematics Grade 7 Quarter 3.
Compiles the complete 61,000+ word verbatim manuscript from
ChatGPT-Grade 7 Math Quarter 3-20261022-2138.md into a publication-grade DOCX.
"""

import sys
import os
import re
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

sys.stdout.reconfigure(encoding='utf-8')

# --- XML STYLING UTILITIES ---

def set_cell_shading(cell, color_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
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

# --- MATH SANITIZER ---

def clean_math_text(text):
    if not text:
        return ""
    text = text.replace(r"\qquad", "    —    ")
    text = text.replace(r"\quad", "  ")
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
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1 / \2)', text)
    text = re.sub(r'\\sqrt\{([^}]+)\}', r'√(\1)', text)
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\^2\b', '²', text)
    text = re.sub(r'\^3\b', '³', text)
    text = text.replace(r"\[", "").replace(r"\]", "")
    text = text.replace("$$", "")
    return text

# --- INLINE FORMATTING RUNS ---

def format_inline_runs(paragraph, text, default_size=10.5, default_color=None, default_bold=False, default_italic=False):
    text = clean_math_text(text)
    pattern = r'(\*\*[^*]+\*\*|\*[^*]+\*|_[^_]+_|`[^`]+`)'
    parts = re.split(pattern, text)
    
    for part in parts:
        if not part:
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

# --- BLOCKS BUILDER ---

def add_heading_1_banner(doc, text):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, "1B365D")
    set_cell_margins(c, top=120, bottom=120, left=180, right=180)
    set_table_no_borders(t)
    p = c.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    format_inline_runs(p, text.upper(), default_size=13.5, default_color=RGBColor(0xFF, 0xFF, 0xFF), default_bold=True)
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(4)

def add_heading_2_banner(doc, text):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, "EBF3FA")
    set_callout_border(c, color_hex="1B365D", sz="36")
    set_cell_margins(c, top=80, bottom=80, left=150, right=150)
    set_table_no_borders(t)
    p = c.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    format_inline_runs(p, text, default_size=11.5, default_color=RGBColor(0x1B, 0x36, 0x5D), default_bold=True)
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(3)

def add_heading_3_text(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    format_inline_runs(p, text, default_size=11.0, default_color=RGBColor(0x2A, 0x4B, 0x7C), default_bold=True)

def render_callout_box(doc, lines):
    # Determine type of callout
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
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        
        # Check sub-headers inside callout
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
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(3)

def render_markdown_table(doc, table_lines):
    rows_data = []
    for line in table_lines:
        line_s = line.strip()
        if not line_s.startswith('|'):
            continue
        # Check delimiter row
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
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.15
            
            if is_header:
                set_cell_shading(cell, "1B365D")
                format_inline_runs(p, cell_text, default_size=9.5, default_color=RGBColor(0xFF, 0xFF, 0xFF), default_bold=True)
            else:
                bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
                set_cell_shading(cell, bg)
                format_inline_runs(p, cell_text, default_size=9.0)
                
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(3)

def compile_math_quarter_3(source_md_path, output_docx_path):
    print(f"Reading source markdown: {source_md_path}")
    with open(source_md_path, 'r', encoding='utf-8') as f:
        full_text = f.read()

    # Determine whether it's pure markdown or a ChatGPT chat export
    if "## Response:" not in full_text and "## Prompt:" not in full_text:
        combined_md = full_text
    else:
        # Intelligently extract from ChatGPT export turns
        responses = full_text.split("## Response:")
        parts = []

        # Find Front Matter (usually in response 1 or 2)
        for r in responses[1:]:
            r_clean = r.split("## Prompt:")[0]
            if "# PAGE 1 - FRONT COVER" in r_clean:
                s_idx = r_clean.find("# PAGE 1 - FRONT COVER")
                e_idx = r_clean.find("Front Matter complete")
                if e_idx == -1: e_idx = r_clean.find("**Type `Proceed` for Lesson 3.1")
                if e_idx == -1: e_idx = len(r_clean)
                parts.append(r_clean[s_idx:e_idx].strip())
                break

        # Find Lessons 3.1 to 3.6
        for lesson_num in ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6"]:
            for r in responses[1:]:
                r_clean = r.split("## Prompt:")[0]
                m_start = re.search(r'\(Lesson ' + re.escape(lesson_num) + r'\)|# LESSON ' + re.escape(lesson_num), r_clean)
                if m_start:
                    s_idx = m_start.start()
                    m_end = re.search(r'\*\*Lesson ' + re.escape(lesson_num) + r' complete\*\*|\*\*All six Quarter 3 lessons complete\*\*', r_clean)
                    e_idx = m_end.start() if m_end else len(r_clean)
                    parts.append(r_clean[s_idx:e_idx].strip())
                    break

        # Find Back Matter
        for r in responses[1:]:
            r_clean = r.split("## Prompt:")[0]
            if "(Back Matter)" in r_clean or "# PAGE 47" in r_clean or "# QUARTER 3 - BACK MATTER" in r_clean:
                m_start = re.search(r'\(Back Matter\)|# PAGE 47|# QUARTER 3 - BACK MATTER', r_clean)
                s_idx = m_start.start() if m_start else 0
                m_end = re.search(r'\*\*Quarter 3 manuscript complete\*\*|\*\*END OF QUARTER 3 BACK MATTER\*\*', r_clean)
                e_idx = m_end.start() if m_end else len(r_clean)
                parts.append(r_clean[s_idx:e_idx].strip())
                break

        combined_md = "\n\n[PAGE BREAK]\n\n".join(parts)
    
    print(f"Assembled complete textbook text: {len(combined_md.split())} words, {len(combined_md)} chars.")

    # Initialize Document
    doc = Document()
    for s in doc.sections:
        s.page_width = Inches(8.5)
        s.page_height = Inches(11.0)
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)
        s.different_first_page_header_footer = True
        
        # Header on Pages 2+
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr = hp.add_run("DepEd MATATAG Curriculum • Mathematics 7 | Quarter 3")
        hr.font.name = 'Cambria'
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(0x77, 0x77, 0x77)
        
        # Footer on Pages 2+
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        fr = fp.add_run("DepEd MATATAG Curriculum • Public Edition • Grade 7 Mathematics")
        fr.font.name = 'Cambria'
        fr.font.size = Pt(8.5)
        fr.font.color.rgb = RGBColor(0x77, 0x77, 0x77)

    # Parsing Lines
    lines = combined_md.splitlines()
    i = 0
    total = len(lines)

    while i < total:
        line = lines[i]
        stripped = line.strip()

        # Empty lines
        if not stripped:
            i += 1
            continue

        # Page Breaks
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
            # If it's a page label like '# PAGE 1 - FRONT COVER', skip banner or render cleanly
            if re.match(r'^PAGE \d+ -', h_text, re.IGNORECASE):
                # Clean page label
                pass
            else:
                add_heading_1_banner(doc, h_text)
            i += 1
            continue

        # Heading 2 (## ...)
        if stripped.startswith('## '):
            h_text = stripped[3:].strip()
            add_heading_2_banner(doc, h_text)
            i += 1
            continue

        # Heading 3 (### ...)
        if stripped.startswith('### '):
            h_text = stripped[4:].strip()
            add_heading_3_text(doc, h_text)
            i += 1
            continue

        # Bulleted Lists (* or - or •)
        if re.match(r'^[\*\-•]\s+', stripped):
            b_text = re.sub(r'^[\*\-•]\s+', '', stripped)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
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
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            format_inline_runs(p, stripped, default_size=10.5)
            i += 1
            continue

        # Normal Paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3.5)
        p.paragraph_format.line_spacing = 1.15
        format_inline_runs(p, stripped, default_size=10.5)
        i += 1

    print(f"Saving compiled master document to {output_docx_path}...")
    doc.save(output_docx_path)
    print("Compilation completed successfully!")

if __name__ == '__main__':
    src = "ChatGPT-Grade 7 Math Lessons-20261024-0711.md"
    if not os.path.exists(src):
        src = "MATATAG_Mathematics_Quarter3_Full_Manuscript.md"
    out = "MATATAG_Mathematics_7_Quarter_3_UNABRIDGED_MASTERPIECE.docx"
    compile_math_quarter_3(src, out)
