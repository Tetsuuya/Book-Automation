# 🚀 ALL-IN-ONE DEPED MATATAG E-BOOK CREATOR SETUP GUIDE

This setup consolidates everything into **ONE single powerful Custom GPT** that generates 45 to 70 page publication-grade quarterly interactive textbooks across ALL subjects matching the MATATAG curriculum without hitting the 8,000-character prompt limit.

---

## 📁 WHAT IS IN THIS FOLDER

1. **`INSTRUCTIONS_FOR_CHATGPT.txt`** (~7,990 characters — strictly under the 8,000-character prompt ceiling)
   - Paste this directly into your Custom GPT's **Instructions** box.
   - Enforces Turn 0 handshake confirmation, turn-by-turn pacing, strict 45-70 page ceiling (2,200-2,600 words/lesson for 5-6 lesson quarters; 4,000-4,500 words/lesson for 3-lesson units), solid Navy blue headers, natural continuous flow (NO internal page breaks), zero branding in prompts, 1 quarterly GRASPS performance task (Back Matter), structured table answer keys, zero-hallucinations fact audit, and auto-compilation via Code Interpreter.

2. **`KNOWLEDGE_FILES/`** (Upload all 7 files into your Custom GPT's **Knowledge** section):
   - **`00_REFERENCE_TEXTBOOK_BENCHMARK.docx`**: The physical benchmark `.docx` file demonstrating blue header blocks, rubrics, structured table answer keys, and natural continuous flow.
   - **`01_PEDAGOGICAL_FRAMEWORK_AND_EXEMPLAR.md`**: Universal 70/30 model, 45-70 page pacing standards, 10-section blueprint, and subject adaptations across ALL 8 DepEd disciplines.
   - **`02_VISUAL_AND_MULTIMEDIA_STANDARDS.md`**: Zero-branding AI prompts with 3-tier title banners and real YouTube video standards.
   - **`docx_builder.py`** (or **`03_DOCX_BUILDER_SCRIPT.py`**): The complete Python `python-docx` compilation engine that Code Interpreter runs to generate the final `.docx` file.
   - **`04_FRONT_MATTER_AND_ANSWER_KEYS_STANDARDS.md`**: Dedicated architectural blueprint for Page 1 (Cover) and Structured Table Answer Keys.
   - **`05_QUALITY_ASSURANCE_AND_CURRICULUM_AUDIT.md`**: Zero-hallucination fact checking (history, science, math, literature), grade-level readiness (DOK 1-4), and the 100-point DepEd MATATAG QA Audit Scorecard calibrated to 45-70 pages.
   - **`06_AI_IMAGE_PROMPT_STANDARDS_AND_EXEMPLARS.md`**: Zero-abstract physical scene architecture, 5 Cinematographic Pillars, Ghibli style, and problem-tied STEM figures.

---

## ⚙️ 2-MINUTE SETUP IN CHATGPT

1. Open ChatGPT ➔ Click on your profile / **Explore GPTs** ➔ **Create a GPT** (or edit your existing one).
2. Go to the **Configure** tab:
   - **Name**: `DepEd MATATAG Master Textbook Creator`
   - **Description**: `Generates publication-grade, 45-70 page interactive textbook units (70% lessons / 30% activities) across all subjects matching the MATATAG curriculum.`
3. **Instructions**:
   - Open [`INSTRUCTIONS_FOR_CHATGPT.txt`](file:///c:/Users/Rhenel%20Jhon%20Sajol/Documents/CERE_BOOK/ALL_IN_ONE_GPT_SETUP/INSTRUCTIONS_FOR_CHATGPT.txt), copy everything, and paste it into the **Instructions** box.
4. **Knowledge**:
   - Click **Upload files** and upload all 7 files inside the [`KNOWLEDGE_FILES/`](file:///c:/Users/Rhenel%20Jhon%20Sajol/Documents/CERE_BOOK/ALL_IN_ONE_GPT_SETUP/KNOWLEDGE_FILES) folder. (Make sure to replace existing `01_PEDAGOGICAL_FRAMEWORK_AND_EXEMPLAR.md` and `05_QUALITY_ASSURANCE_AND_CURRICULUM_AUDIT.md`).
5. **Capabilities**:
   - Check **Code Interpreter & Data Analysis** (required for compiling `.docx` files).
   - Check **Web Search** (optional, for curating real YouTube links).
6. Click **Save** / **Update** in the top-right corner.

---

## 🎯 HOW TO USE IT

1. In the chat, upload your **Table of Contents (TOC)** and **Curriculum Guide (CG)** (PDF or Markdown).
2. Tell it: *"Gawin natin ang Quarter 3, Lessons 3.1–3.6."*
3. **Turn 1**: The GPT outputs the clean 3-page Front Matter (Cover, Preface, non-table TOC), initializes `/mnt/data/manuscript.md`, and pauses.
4. Type **`Proceed`** at each step:
   - It outputs each lesson one turn at a time, strictly calibrated to land between 45 and 70 pages:
     * For 5–6 lesson quarters (Math/Science): ~2,200–2,600 words per lesson.
     * For 3-lesson units (Filipino/Values): ~4,000–4,500 words per lesson.
   - It appends each lesson directly into `/mnt/data/manuscript.md`.
5. After all lessons are complete, type **`Proceed for Back Matter`**:
   - It outputs the 50-pt Comprehensive Assessment, Culminating GRASPS Task (4x4 Rubric), Synthesis, Glossary, Structured Keys, and QA Stamp.
6. Type **`Compile`**:
   - Code Interpreter runs `docx_builder.compile_markdown_to_docx('/mnt/data/manuscript.md', 'MATATAG_[Subject]_[Quarter]_Textbook.docx')`.
   - Your publication-grade `.docx` is produced verbatim with zero summaries, landing squarely in the **45 to 70 page target**!
