# -*- coding: utf-8 -*-
"""
Generator script for the expanded 44-page MATATAG Interactive Multimedia E-Book.
Strictly implements:
- 70% Lesson / 30% Activity ratio
- 40+ pages (44 full pages) with zero empty space (Page 1 = Cover with prompt)
- Embedded YouTube Multimedia Modules with QR code boxes & reflection questions
- AI Image Generation Prompts (dashed callouts)
- UI/UX: Deep Navy (#1B365D), Soft Blue (#F4F7FA), Neutral (#FAFAFA), YouTube Red (#CC0000)
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

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

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
    r_t = p.add_run(text)
    r_t.font.name = 'Cambria'
    r_t.font.size = Pt(10.5)
    r_t.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

def add_multimedia_box(doc, mod_title, vid_title, channel, link, qr_code_text, timestamps, questions):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, "FFF5F5")
    set_callout_border(c, color_hex="CC0000", sz="36")
    set_cell_margins(c, top=140, bottom=140, left=180, right=180)
    
    p0 = c.paragraphs[0]
    format_paragraph(p0, space_after=2)
    r0 = p0.add_run(f"🎥 INTERAKTIBONG MULTIMEDIA: {mod_title.upper()}")
    r0.font.name = 'Arial'
    r0.font.size = Pt(10.5)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(0xCC, 0x00, 0x00)
    
    p1 = c.add_paragraph()
    format_paragraph(p1, space_after=2)
    r1 = p1.add_run(f"Pamagat ng Panoorin: \"{vid_title}\"  |  Opisyal na Tsanel: {channel}")
    r1.font.name = 'Cambria'
    r1.font.size = Pt(10)
    r1.font.bold = True
    
    p2 = c.add_paragraph()
    format_paragraph(p2, space_after=2)
    r2a = p2.add_run("Direktang Link: ")
    r2a.font.name = 'Cambria'
    r2a.font.size = Pt(9.5)
    r2a.font.bold = True
    r2b = p2.add_run(link)
    r2b.font.name = 'Cambria'
    r2b.font.size = Pt(9.5)
    r2b.font.color.rgb = RGBColor(0x00, 0x44, 0xCC)
    r2b.font.underline = True
    
    p3 = c.add_paragraph()
    format_paragraph(p3, space_after=2)
    r3 = p3.add_run("Mahahalagang Bahagi at Timestamps na Pag-aaralan:")
    r3.font.name = 'Arial'
    r3.font.size = Pt(9.5)
    r3.font.bold = True
    
    for ts in timestamps:
        pts = c.add_paragraph()
        format_paragraph(pts, space_after=1)
        r_ts = pts.add_run(f"• {ts}")
        r_ts.font.name = 'Cambria'
        r_ts.font.size = Pt(9.5)
        
    p4 = c.add_paragraph()
    format_paragraph(p4, space_before=3, space_after=2)
    r4 = p4.add_run("Panonood at Mapanuring Pagsusuri (Gabay sa Mapanuring Pag-iisip):")
    r4.font.name = 'Arial'
    r4.font.size = Pt(9.5)
    r4.font.bold = True
    
    for i, q in enumerate(questions, 1):
        pq = c.add_paragraph()
        format_paragraph(pq, space_after=1)
        rq = pq.add_run(f"{i}. {q}")
        rq.font.name = 'Cambria'
        rq.font.size = Pt(9.5)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_prompt_box(doc, title, prompt_text):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, "FAFAFA")
    set_dashed_border(c, color_hex="CCCCCC", sz="12")
    set_cell_margins(c, top=120, bottom=120, left=160, right=160)
    
    p0 = c.paragraphs[0]
    format_paragraph(p0, space_after=2)
    r0 = p0.add_run(f"📷 [{title.upper()}]  Detailed Image Generation Prompt")
    r0.font.name = 'Arial'
    r0.font.size = Pt(10)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    
    p1 = c.add_paragraph()
    format_paragraph(p1, space_after=0)
    r1 = p1.add_run(prompt_text)
    r1.font.name = 'Cambria'
    r1.font.size = Pt(9.5)
    r1.font.italic = True
    r1.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_callout_box(doc, title, body_lines=None, color_fill="F4F7FA", border_color="1B365D"):
    if body_lines is None:
        lines = [l for l in title.split("\n") if l.strip()]
        title = lines[0] if lines else ""
        body_lines = lines[1:] if len(lines) > 1 else []
    elif isinstance(body_lines, str):
        body_lines = [l for l in body_lines.split("\n") if l.strip()]

    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    set_cell_shading(c, color_fill)
    set_callout_border(c, color_hex=border_color, sz="36")
    set_cell_margins(c, top=140, bottom=140, left=180, right=180)
    
    p0 = c.paragraphs[0]
    format_paragraph(p0, space_after=2)
    r0 = p0.add_run(title)
    r0.font.name = 'Arial'
    r0.font.size = Pt(10.5)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    for line in body_lines:
        p = c.add_paragraph()
        format_paragraph(p, space_after=2)
        r = p.add_run(line)
        r.font.name = 'Cambria'
        r.font.size = Pt(10)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_custom_table(doc, headers, data_rows, col_widths=None):
    table = doc.add_table(rows=len(data_rows)+1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_grid_borders(table, color_hex="D0D7DE", sz="4")
    
    # Header Row
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_shading(hdr_cells[i], "1B365D")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        p = hdr_cells[i].paragraphs[0]
        format_paragraph(p, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        p.runs[0].font.name = 'Arial'
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    for r_idx, row_data in enumerate(data_rows):
        row_cells = table.rows[r_idx+1].cells
        bg_fill = "F9FBFD" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, cell_value in enumerate(row_data):
            row_cells[c_idx].text = cell_value
            set_cell_shading(row_cells[c_idx], bg_fill)
            set_cell_margins(row_cells[c_idx], top=90, bottom=90, left=120, right=120)
            p = row_cells[c_idx].paragraphs[0]
            format_paragraph(p, space_after=0, align=WD_ALIGN_PARAGRAPH.LEFT)
            p.runs[0].font.name = 'Cambria'
            p.runs[0].font.size = Pt(9.5)
            p.runs[0].font.color.rgb = RGBColor(0x22, 0x22, 0x22)
            
    if col_widths:
        for row in table.rows:
            for idx, w in enumerate(col_widths):
                row.cells[idx].width = Inches(w)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

print("Base setup functions compiled.")


def create_base_document():
    doc = Document()
    for section in doc.sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
    
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Cambria'
    style_normal.font.size = Pt(11)
    style_normal.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(4)
    style_normal.paragraph_format.space_before = Pt(0)
    
    return doc
