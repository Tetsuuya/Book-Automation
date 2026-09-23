with open(r'c:\Users\Rhenel Jhon Sajol\Documents\CERE_BOOK\2_GPT_PIPELINE\GPT1_CONTENT_AUTHOR\INSTRUCTIONS_GPT1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('ZERO EMPTY SPACE & 350-500 WORDS PER PAGE: Every page boundary ends with "[PAGE BREAK]". Each page MUST contain 350-500 words, or 250 words plus a complete multi-row data matrix or rubric. NEVER write brief 2-line activities or short dialogues. Every page must be fully packed from top to bottom.',
     'ZERO EMPTY SPACE (350-500 WORDS/PAGE): Every page boundary ends with "[PAGE BREAK]". Each page MUST contain 350-500 words, or 250 words plus a full data matrix or 4x4 rubric. NEVER write 2-line activities or short dialogues. Pages must be fully packed top to bottom.'),
    ('Single-cell callout box with thick Navy Blue (#1B365D, 4.5pt) left border stripe and #FAFAFA background listing EVERY lesson, subtopic, task, session, and page number so the box fills the entire page:',
     'Callout box (Navy #1B365D 4.5pt left border, #FAFAFA fill) listing EVERY lesson, subtopic, task, session, and page so the box fills the entire page:'),
    ('PART 2: LESSON CORES (LESSONS 1, 2, 3...) - 10-12 PAGES PER LESSON (~3,500 words per lesson):',
     'PART 2: LESSON CORES (10-12 PAGES PER LESSON, ~3,500 words/lesson):'),
    ('Page 1 of Lesson: Lesson Title, MATATAG codes, 3 Essential Questions, [MULTIMEDIA: Video intro], Context Background (350+ words). [PAGE BREAK]',
     'Page 1: Lesson Title, MATATAG codes, 3 Essential Questions, [MULTIMEDIA: Video intro], Context Background (350+ words). [PAGE BREAK]'),
    ('Page 7: Learning Task X.1 (recall drill) & Task X.2 (analytical matrix with 5-6 items to complete) (350+ words). [PAGE BREAK]',
     'Page 7: Learning Task X.1 (recall drill) & Task X.2 (analytical matrix with 5-6 items) (350+ words). [PAGE BREAK]'),
    ('Page 8: Learning Task X.3 (authentic performance task) + FULL 4x4 Analytic Rubric Table with descriptions in all cells. [PAGE BREAK]',
     'Page 8: Learning Task X.3 (authentic task) + FULL 4x4 Analytic Rubric Table (detailed descriptors in all cells). [PAGE BREAK]'),
    ('Page 10: Formative Assessment (15 rigorous items: 10 MCQs with A-B-C-D options + 5 analytical justification questions). [PAGE BREAK]',
     'Page 10: Formative Assessment (15 items: 10 MCQs with A-B-C-D options + 5 analytical justification questions). [PAGE BREAK]'),
    ('PART 3: COMPREHENSIVE UNIT ASSESSMENT (4 PAGES - 40 POINTS)',
     'PART 3: COMPREHENSIVE UNIT ASSESSMENT (4 PAGES, 40 PTS)'),
    ('STRICT LESSON-BY-LESSON PACING & DOCX COMPILATION:',
     'STRICT PACING & COMPILATION:'),
    ('To prevent truncation and ensure full 40+ page publication depth, NEVER generate the whole textbook in a single response! Follow this exact pacing:',
     'To prevent truncation and ensure full 40+ page depth, NEVER generate all lessons at once! Follow this exact pacing:'),
    ('Turn 1 (Front Matter): Output exact 3-page Front Matter (Cover, Preface, Table of Contents). STOP and ask: "Ready to generate Lesson 1 in full V10 depth? (Type \'Proceed\' or specify instructions)."',
     'Turn 1 (Front Matter): Output 3-page Front Matter (Cover, Preface, TOC). STOP & ask: "Ready to generate Lesson 1? (Type \'Proceed\')."'),
    ('Turn 2 (Lesson 1): Upon \'Proceed\', output Lesson 1 in full 10-12 page depth (~3,500 words with all [PAGE BREAK] markers). STOP and ask: "Ready to generate Lesson 2? (Type \'Proceed\')."',
     'Turn 2 (Lesson 1): Upon \'Proceed\', output Lesson 1 in full depth (~3,500 words with [PAGE BREAK]). STOP & ask: "Ready for Lesson 2? (Type \'Proceed\')."'),
    ('Turn 3 (Lesson 2): Output Lesson 2 in full depth (~3,500 words). STOP and ask: "Ready to generate Lesson 3? (Type \'Proceed\')."',
     'Turn 3 (Lesson 2): Output Lesson 2 in full depth (~3,500 words). STOP & ask: "Ready for Lesson 3? (Type \'Proceed\')."'),
    ('Turn 4 (Lesson 3): Output Lesson 3 in full depth (~3,500 words). STOP and ask: "Ready to generate Unit Assessment and Answer Key? (Type \'Proceed\')."',
     'Turn 4 (Lesson 3): Output Lesson 3 in full depth (~3,500 words). STOP & ask: "Ready for Unit Assessment & Keys? (Type \'Proceed\')."')
]

for old, new in replacements:
    text = text.replace(old, new)

with open(r'c:\Users\Rhenel Jhon Sajol\Documents\CERE_BOOK\2_GPT_PIPELINE\GPT1_CONTENT_AUTHOR\INSTRUCTIONS_GPT1.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print('Final character count:', len(text))
