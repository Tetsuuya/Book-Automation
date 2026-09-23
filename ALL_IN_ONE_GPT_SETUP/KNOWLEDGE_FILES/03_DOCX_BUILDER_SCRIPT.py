# -*- coding: utf-8 -*-
"""
DEPED MATATAG PUBLICATION-GRADE DOCX BUILDER ENGINE
Use this Python script in Code Interpreter or local environment to compile
the complete 40+ page interactive textbook (.docx) matching the benchmark V10 styling.
"""

import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# --- XML STYLING UTILITIES ---

def set_cell_shading(cell, color_hex):
    """Set background color fill for a table cell."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    """Set internal cell padding (in dxa)."""
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
    """Set a bold solid left border stripe for callout boxes (4.5pt)."""
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
    """Set dashed border around image placeholder frames."""
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
    """Set crisp light gray grid borders for tables."""
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

# --- TYPOGRAPHY & HEADING HELPERS ---

def format_paragraph(p, space_before=0, space_after=4, line_spacing=1.15, align=WD_ALIGN_PARAGRAPH.LEFT):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    p.alignment = align

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

def add_heading_1(doc, text):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, "1B365D")
    set_cell_margins(c, top=100, bottom=100, left=150, right=150)
    set_table_no_borders(t)
    p = c.paragraphs[0]
    format_paragraph(p, space_before=2, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
    run = p.add_run(text)
    run.font.name = 'Cambria'
    run.font.size = Pt(13.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return p

def add_heading_2(doc, text):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, "EBF3FA")
    set_callout_border(c, color_hex="1B365D", sz="36")
    set_cell_margins(c, top=80, bottom=80, left=150, right=150)
    p = c.paragraphs[0]
    format_paragraph(p, space_before=2, space_after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
    run = p.add_run(text)
    run.font.name = 'Cambria'
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    doc.add_paragraph().paragraph_format.space_after = Pt(3)
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=6, space_after=2)
    run = p.add_run(text)
    run.font.name = 'Cambria'
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x2A, 0x4B, 0x7C)
    return p

def add_body_p(doc, text, bold_prefix="", italic_prefix=""):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=0, space_after=4, line_spacing=1.15)
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Cambria'
        r_b.font.size = Pt(10.5)
        r_b.font.bold = True
        r_b.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    if italic_prefix:
        r_i = p.add_run(italic_prefix)
        r_i.font.name = 'Cambria'
        r_i.font.size = Pt(10.5)
        r_i.font.italic = True
    run = p.add_run(text)
    run.font.name = 'Cambria'
    run.font.size = Pt(10.5)
    run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

# --- RICH VISUAL & CALLOUT COMPONENTS ---

def add_callout_box(doc, title, items, bg_color="FAFAFA", border_color="1B365D"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, bg_color)
    set_callout_border(cell, border_color, "36")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p = cell.paragraphs[0]
    format_paragraph(p, space_before=2, space_after=4)
    run = p.add_run(title)
    run.font.name = 'Cambria'
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    for item in items:
        pi = cell.add_paragraph()
        format_paragraph(pi, space_before=1, space_after=2)
        ri = pi.add_run(item)
        ri.font.name = 'Cambria'
        ri.font.size = Pt(9.5)
        ri.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    doc.add_paragraph()

def add_prompt_box(doc, title, role, prompt, aspect_ratio="16:9"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, "F4F7FA")
    set_dashed_border(cell, "CCCCCC", "12")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p = cell.paragraphs[0]
    format_paragraph(p, space_before=2, space_after=2)
    r1 = p.add_run(f"🖼️ [IMAGE PLACEHOLDER: {title}]")
    r1.font.name = 'Cambria'
    r1.font.size = Pt(10.5)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    p2 = cell.add_paragraph()
    format_paragraph(p2, space_before=1, space_after=2)
    r2 = p2.add_run(f"Layunin: {role}")
    r2.font.name = 'Cambria'
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    
    p3 = cell.add_paragraph()
    format_paragraph(p3, space_before=1, space_after=2)
    r3 = p3.add_run(f"AI Prompt: {prompt} --ar {aspect_ratio} --v 6.0")
    r3.font.name = 'Cambria'
    r3.font.size = Pt(9.0)
    r3.font.italic = True
    r3.font.color.rgb = RGBColor(0x2A, 0x4B, 0x7C)
    
    p4 = cell.add_paragraph()
    format_paragraph(p4, space_before=1, space_after=2)
    r4 = p4.add_run("Paunawa: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).")
    r4.font.name = 'Cambria'
    r4.font.size = Pt(8.5)
    r4.font.color.rgb = RGBColor(0x77, 0x77, 0x77)
    doc.add_paragraph()

def add_youtube_module(doc, title, channel, timestamps, questions, search_url="", search_keywords=""):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, "FFF5F5")
    set_callout_border(cell, "CC0000", "36")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    p = cell.paragraphs[0]
    format_paragraph(p, space_before=2, space_after=2)
    r = p.add_run(f"🎥 INTERAKTIBONG MULTIMEDIA: {title}")
    r.font.name = 'Cambria'
    r.font.size = Pt(10.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0xCC, 0x00, 0x00)
    
    pm = cell.add_paragraph()
    format_paragraph(pm, space_before=1, space_after=2)
    rm = pm.add_run(f"Opisyal na Channel: {channel} | [📱 QR Code Box: Scan to Watch]")
    rm.font.name = 'Cambria'
    rm.font.size = Pt(9.5)
    rm.font.bold = True
    rm.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    if search_url:
        pu = cell.add_paragraph()
        format_paragraph(pu, space_before=1, space_after=1)
        ru = pu.add_run(f"Direct Search Link: {search_url}")
        ru.font.name = 'Cambria'
        ru.font.size = Pt(9.0)
        ru.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        
    if search_keywords:
        pk = cell.add_paragraph()
        format_paragraph(pk, space_before=1, space_after=2)
        rk = pk.add_run(f'YouTube Search Keywords: "{search_keywords}"')
        rk.font.name = 'Cambria'
        rk.font.size = Pt(9.0)
        rk.font.italic = True
        rk.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    
    for ts in timestamps:
        pts = cell.add_paragraph()
        format_paragraph(pts, space_before=1, space_after=1)
        rts = pts.add_run(f"⏱️ {ts}")
        rts.font.name = 'Cambria'
        rts.font.size = Pt(9.0)
        rts.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
        
    pq_h = cell.add_paragraph()
    format_paragraph(pq_h, space_before=3, space_after=1)
    rq_h = pq_h.add_run("Mga Gabay na Tanong sa Panonood:")
    rq_h.font.name = 'Cambria'
    rq_h.font.size = Pt(9.5)
    rq_h.font.bold = True
    rq_h.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    for q in questions:
        pq = cell.add_paragraph()
        format_paragraph(pq, space_before=1, space_after=1)
        rq = pq.add_run(f"• {q}")
        rq.font.name = 'Cambria'
        rq.font.size = Pt(9.0)
        rq.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    doc.add_paragraph()

def initialize_document(subject="Filipino", grade="7", unit="III"):
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    section.different_first_page_header_footer = True
    
    # Running Header on Pages 2+
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hr = hp.add_run(f"DepEd MATATAG Curriculum • {subject} {grade} | Unit {unit}")
    hr.font.name = 'Cambria'
    hr.font.size = Pt(8.5)
    hr.font.color.rgb = RGBColor(0x77, 0x77, 0x77)
    
    # Running Footer on Pages 2+
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    fr = fp.add_run("DepEd MATATAG Curriculum • Public Edition / Edisyong Pampubliko")
    fr.font.name = 'Cambria'
    fr.font.size = Pt(8.5)
    fr.font.color.rgb = RGBColor(0x77, 0x77, 0x77)
    
    return doc
