import re

files_to_clean = [
    r'c:\Users\Rhenel Jhon Sajol\Documents\CERE_BOOK\sections_yunit3_aralin13.py',
    r'c:\Users\Rhenel Jhon Sajol\Documents\CERE_BOOK\sections_yunit3_aralin14.py',
    r'c:\Users\Rhenel Jhon Sajol\Documents\CERE_BOOK\sections_yunit3_aralin15.py',
    r'c:\Users\Rhenel Jhon Sajol\Documents\CERE_BOOK\sections_yunit3_assessment_keys.py'
]

for filepath in files_to_clean:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Keep only the very last page break in the function (the lesson boundary break)
    # Remove all intermediate doc.add_page_break()
    lines = content.split('\n')
    new_lines = []
    
    # Find all line indices with doc.add_page_break()
    break_indices = [i for i, line in enumerate(lines) if 'doc.add_page_break()' in line]
    
    # We only keep the LAST break index (at the end of the lesson/section)
    last_break = break_indices[-1] if break_indices else -1
    
    for i, line in enumerate(lines):
        if 'doc.add_page_break()' in line and i != last_break:
            # Comment it out or remove
            new_lines.append("    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]")
        else:
            new_lines.append(line)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
        
    print(f"Cleaned {filepath}: removed {len(break_indices)-1} internal page breaks.")
