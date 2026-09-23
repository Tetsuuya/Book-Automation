import docx

doc = docx.Document(r'C:\Users\Rhenel Jhon Sajol\Downloads\MATATAG_Filipino7_Yunit_III_Masterclass_Textbook_v2.docx')
pages = [[]]
for p in doc.paragraphs:
    pages[-1].append(p.text)
    for r in p.runs:
        if 'type="page"' in r._r.xml:
            pages.append([])

print(f"Total pages: {len(pages)}")
for i, page in enumerate(pages):
    words = sum(len(txt.split()) for txt in page)
    first_line = page[0] if page else "EMPTY"
    print(f"P{i+1}: {words}w | {first_line[:60]}")
