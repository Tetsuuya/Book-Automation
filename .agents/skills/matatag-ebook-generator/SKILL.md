---
name: matatag-ebook-generator
description: >-
  Expert generator for DepEd MATATAG Curriculum interactive multimedia textbooks across ALL subjects
  (Science, Math, English, Filipino, AP, MAPEH, TLE/TVL, GMRC/EsP, Grades 1–10).
  Transforms any user Table of Contents (Talaan ng Nilalaman) and MATATAG curriculum competencies
  into a comprehensive 40+ page full-density textbook with a strict 70% lesson / 30% activity
  ratio, real YouTube multimedia search modules, zero-branding AI prompts with 3-tier title banners,
  solid Navy Blue header banners, and full-spectrum interactivity.
---

# MATATAG Universal Multi-Subject Textbook Generator Skill

This skill governs the end-to-end generation of publication-grade, interactive educational textbooks aligned with the Department of Education (DepEd) **MATATAG K-10 Curriculum** across **ALL SUBJECTS and GRADE LEVELS**.

The skill operates from **ONLY two required inputs**:
1. **Table of Contents (Talaan ng Nilalaman)**: The list of units, lessons (aralins), and specific subtopics.
2. **MATATAG Curriculum Guide / Competencies**: The competency codes, content standards, and performance standards.

---

## Universal Subject & Language Matrix

Adapt tone, language, and core discipline anchors based on the subject:

| Discipline / Subject | Medium of Instruction | Core Discipline Anchors | Competency Domains |
| :--- | :--- | :--- | :--- |
| **Science** | English | Full Laboratory Protocols, Hypothesis Testing, Controlled Data Tables, Scientific Laws | *Scientific Inquiry, Living Things & Environment, Matter, Force & Energy, Earth & Space* |
| **Mathematics** | English | Step-by-Step Proofs, Real-World Mathematical Modeling, Derivations, Problem Solving | *Number & Algebra, Measurement & Geometry, Statistics & Probability* |
| **English** | English | Unabridged Literary Selections (400-500 words), Rhetorical & Stylistic Devices, Speeches | *Literary & Informational Texts, Grammar & Syntax, Viewing & Multimodal, Oral Fluency* |
| **Filipino** | Filipino | Kumpletong Akdang Pampanitikan (400-500 salita), Pag-aaral sa Gramatika, Sintaks, at Reperensiya | *Pag-unawa sa Binasa, Pagsusuring Panlingguwistika, Tekstong Impormasyonal, Multimodal* |
| **Araling Panlipunan** | Filipino | Primaryang Sanggunian (Dekreto, Liham, Batas), Pagsusuring Pangkasaysayan, Heograpiya | *Tao, Kapaligiran at Lipunan; Panahon, Pagpapatuloy at Pagbabago; Kultura at Pagkabansa* |
| **MAPEH** | English / Filipino | Musical Organology, Biomechanical Kinesiology, Cultural Performance, Preventive Health | *Music (Analysis/Craft), Arts (Heritage/Design), PE (Fitness/Movement), Health (Community)* |
| **TLE / TVL** | English / Filipino | Technical Blueprints, Occupational Health & Safety (OHS), Tool Schematics, Standard SOPs | *Technical Competencies, Safety Protocols, Systems Troubleshooting, Enterprise Projects* |
| **GMRC / EsP** | Filipino | Moral Dilemmas, Ethical Case Studies, Character Reflections, Community Action Plans | *Pagpapahalaga sa Sarili, Pamilya, Kapuwa, Bansa, at Diyos; Mapanuring Pagpapasiya* |

---

## Golden Rules and Core Constraints

Every generated textbook **MUST strictly satisfy** these core constraints:

1. **Strict 70% Lesson / 30% Activity Ratio**:
   - **70% Masterclass Lesson Content**: Deep, substantive conceptual explanations, historical/scientific context, unabridged anchor reading/lab protocol, Socratic inquiry seminars (8-10 turns), and concept matrices. Minimum **3,500 words per Lesson** (~15,000+ words per 3-lesson unit).
   - **30% Activity & Assessment**: Guided practice recall drills, analytical matrices (5-6 rows), authentic performance tasks (GRASPS model) with complete 4x4 analytic rubrics (all 16 cells fully filled), 15-item formative quizzes with brackets `[  ]`, unit assessments (40 pts), and complete answer keys with rationales.

2. **40+ Full Pages Target (Strictly for Student Content, Excluding Answer Keys)**:
   - **40-Page Minimum Floor for Student Lessons**: The 40-page minimum applies **strictly to the student instructional core** (Front Matter, Lessons 1–3 at 11–12 pages each, 40-pt Unit Assessment, Synthesis, and Glossary).
   - **Answer Keys and Teacher Guides are EXCLUDED from the 40-page minimum**: Susi sa Pagwawasto and Teacher's Diagnostic Guide begin on **Page 44+**, bringing the total publication to **50 to 54+ full pages**.
   - **NO INTERNAL PAGE BREAKS**: Content must flow naturally and continuously. Never insert page breaks between topics, after callouts, or before tasks. Hard page breaks are strictly reserved for major structural boundaries:
     1. After Cover (Page 1)
     2. After Preface (Page 2)
     3. After Table of Contents (Page 3)
     4. At the end of each Lesson
     5. After Unit Assessment
     6. After Summary & Glossary (Page 43)
     7. Before Susi sa Pagwawasto (Page 44)
     8. Before QA Audit Certificate (Page 54)

3. **Page 1: Dedicated Front Cover (100% Zero Branding in Prompts)**:
   - Contains institutional header, large 24pt unit title, formal subtitle, and a dedicated **Front Cover AI Image Generation Prompt Box**.
   - **STRICT ZERO BRANDING IN PROMPTS**: Never include `"DepEd"`, `"MATATAG"`, or publisher names inside AI image prompts (to prevent Midjourney/DALL-E from hallucinating fake logos, badges, or watermarks).
   - **3-Tier Title Hierarchy in Quotes**: The cover prompt must specify:
     * Primary Title in quotes: `"[BOOK TITLE] [SUBJECT] [GRADE]"` (e.g., `"GABAY PAMPAGKATUTO SA FILIPINO 8"`, `"VALUES EDUCATION 7"`, or `"LEARNING GUIDE IN SCIENCE 8"`)
     * Secondary Title in quotes: `"UNIT [X]: [UNIT THEME]"`
     * Scope Sub-text in quotes: `"[Topic 1] • [Topic 2] • [Topic 3]"`
     * Typography instruction: Specify a sleek deep navy banner at the top featuring clean, crisp capital letters. Append: `clean graphic layout, perfectly centered professional typography, ultra-high resolution, no gibberish text, no watermarks, no logos --ar 8.5:11 --v 6.0`.
   - **MULTI-SUBJECT NEUTRALITY**: Never default or bias toward Grade 7 Filipino. When the user requests Grade 8 Filipino, Values Education 7, Science 8, Math 9, or Araling Panlipunan, dynamically adapt all titles, cover prompts, terminology, and mediums of instruction accordingly.

4. **Strict 10-Prompt Quota & Concrete Scene Architecture**:
   - Exactly 1 Full-Page Front Cover Prompt on Page 1 (`--ar 8.5:11`, 3-tier title banner in quotes).
   - Exactly 3 Image Prompt Frames per Lesson (Subtopic 1, Subtopic 2, Applied / Multimodal Task, `--ar 16:9`).
   - Zero image prompts in Back Matter.
   - Total Unit Quota: Exactly **10 Image Prompts Total** ($1 + 3 \times 3 = 10$).
   - **STRICT BAN ON ABSTRACT META-PROMPTS**: Follow `06_AI_IMAGE_PROMPT_STANDARDS_AND_EXEMPLARS.md`. NEVER output words like `"illustrating the central concept of this subtopic"`, `"showing source checking"`, or `"educational infographic"`. Every prompt MUST describe concrete photons hitting physical surfaces via the 5 Pillars: (1) Specific characters and physical hand actions, (2) Tangible architectural environment, (3) 3 to 4 concrete props, (4) Directional lighting/atmosphere, and (5) Camera framing and artistic medium.

5. **Bulletproof Interactive YouTube Modules (Zero QR Codes, Zero 404s)**:
   - NO QR code boxes (eliminates broken ASCII codes and non-functional print elements).
   - Feature REAL sample footage, performance traditions, or official documentaries from trusted channels (DepEd TV, Knowledge Channel, DOST-SEI, CrashCourse, Khan Academy, NHCP, NCCA).
   - Use direct search URLs: `https://www.youtube.com/results?search_query=[URL_ENCODED_KEYWORDS]`.

6. **Blue Background Header System & UI/UX Styling**:
   - **Page Size**: Letter (8.5" x 11.0"), 1.0-inch margins all around.
   - **Heading 1 / Major Titles**: Solid Navy Blue (`#1B365D`) background banner table cell with bold white text.
   - **Heading 2 / Subtopics**: Soft blue (`#EBF3FA`) block with 4.5pt solid Navy Blue (`#1B365D`) left border stripe.
   - **Table Headers**: Solid Navy Blue (`#1B365D`) with bold white text.
   - **Activity & Assessment Boxes**: Cool soft blue (`#F4F7FA`) with solid Navy left border.
   - **Interactive YouTube Modules**: Soft red (`#FFF5F5`) with solid YouTube Red (`#CC0000`) left border.
   - **AI Image Prompts**: Soft gray (`#FAFAFA`) with dashed border (`#CCCCCC`).

7. **Unit Assessment Architecture, Structured Keys & Psychometric Balance**:
   - **Comprehensive Unit Assessment (50 Pts)**: 30-Item Multiple Choice Quiz (Items 1–30 with `[  ]` checkboxes, balanced A–D spread) followed immediately by the Authentic Performance Task (GRASPS Model + Complete 4x4 Analytic Rubric, 20 pts).
   - **Structured Table Answer Keys**: Rendered in clean table grids (10-col for lessons, two 15-col grids for 30-item Unit Assessment, plus 2-col rationale tables). **ZERO paragraph blobs!**
   - **ANTI-"MOSTLY B" / BALANCED CHOICES**: Correct answers MUST be evenly distributed across options `A`, `B`, `C`, and `D` (~25% each; 7-8 per 30 items). Never repeat any letter >2 times consecutively. Distractors must be parallel in length and complexity.

8. **Zero-Hallucination & Factual Integrity Standards**:
   - The AI must NEVER fabricate data, dates, laws, historical figures, or mathematical derivations.
   - *History / AP*: Real dates, primary sources, and verified Republic Acts (e.g., R.A. 10533, R.A. 11476).
   - *Literature / Filipino*: Authentic recognized selections and exact syllable counts for poetic forms (Tanaga: 7-7-7-7; Haiku: 5-7-5; Awit: 12 pantig).
   - *Science & Math*: Standard SI units, IUPAC chemical formulas, sound physical laws, and calculation concordance between quiz items and answer keys.

9. **Grade-Level Cognitive & Developmental Readiness**:
   - Cognitive demand calibrated to grade level (DOK 1-2 for G7; DOK 2-3 for G8; DOK 3-4 for G9; DOK 4 for G10).
   - Socio-emotional suitability: Authentic adolescent dilemmas without moralizing or dogmatism.
   - Inclusivity & Gender Fairness: Gender-fair language (DepEd Order No. 32, s. 2017) and positive Indigenous Peoples representation (IPED).

---

## 4-Step Interactive Execution Pacing

To prevent LLM output token cutoffs and guarantee 3,500+ words per lesson:
- **Turn 0 (Handshake)**: Acknowledge uploaded TOC/Curriculum Guide and ask teacher to confirm: (1) Subject & Grade Level, (2) Unit Number & Lesson range.
- **Turn 1 (Front Matter)**: Output 3-page Front Matter (Cover with 3-tier prompt, Preface, TOC). STOP & ask to proceed.
- **Turn 2 to 4 (Lessons 1 to 3)**: Output each lesson one at a time in full 3,500+ word depth with exactly 3 visual prompt boxes and 7 interactive protocols. STOP & ask to proceed.
- **Turn 5 (Back Matter & QA Audit)**: Output 30-Item MCQ Unit Assessment (Items 1–30), Performance Task with 4x4 rubric, Unit Synthesis, Glossary (20-25 terms), Complete Structured Answer Key (with 30-item grid), and the 100-Point QA Audit Certificate Stamp.
- **Turn 6 (Compilation)**: Execute `03_DOCX_BUILDER_SCRIPT.py` to compile the `.docx` textbook with zero orphan pages and provide direct download.
