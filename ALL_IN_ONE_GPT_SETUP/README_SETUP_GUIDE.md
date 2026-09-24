# 🚀 ALL-IN-ONE DEPED MATATAG E-BOOK CREATOR SETUP GUIDE

This setup consolidates everything into **ONE single powerful Custom GPT** that generates 40+ page publication-grade textbooks identical to the benchmark `MATATAG_Filipino7_Yunit_III_NaturalFlow.docx` without hitting the 8,000-character prompt limit.

---

## 📁 WHAT IS IN THIS FOLDER

1. **`INSTRUCTIONS_FOR_CHATGPT.txt`** (7,878 characters — strictly under the 8,000-character prompt ceiling)
   - Paste this directly into your Custom GPT's **Instructions** box.
   - Enforces Turn 0 handshake confirmation, turn-by-turn pacing, blue background headers, natural continuous flow (NO internal page breaks), zero branding in prompts, strict 10-prompt quota, 30-item MCQ unit assessment, structured table answer keys with dynamic anti-pattern randomization, zero-hallucinations fact audit, and commands the GPT to read the uploaded Knowledge files.

2. **`KNOWLEDGE_FILES/`** (Upload all 7 files into your Custom GPT's **Knowledge** section):
   - **`00_REFERENCE_TEXTBOOK_BENCHMARK.docx`**: The physical 20,300+ word benchmark `.docx` file demonstrating 123 blue header blocks, 4x4 rubrics, structured table answer keys, 30-item MCQ quiz, and natural continuous flow.
   - **`01_PEDAGOGICAL_FRAMEWORK_AND_EXEMPLAR.md`**: Universal 70/30 model, 10-section blueprint, 7 interactivity protocols, and subject adaptations across ALL 8 DepEd disciplines (Science, Math, English, Filipino, AP, MAPEH, TLE, GMRC).
   - **`02_VISUAL_AND_MULTIMEDIA_STANDARDS.md`**: Zero-branding AI prompts with 3-tier title banners and real YouTube video standards (no QR codes, guaranteed search query URLs).
   - **`03_DOCX_BUILDER_SCRIPT.py`**: The complete Python `python-docx` compilation engine that Code Interpreter runs to generate the final `.docx` file.
   - **`04_FRONT_MATTER_AND_ANSWER_KEYS_STANDARDS.md`**: Dedicated architectural blueprint for Page 1 (3-tier Cover title banners across all subjects) and Page 44 (Structured Table Answer Keys with strict ban on paragraph blobs).
   - **`05_QUALITY_ASSURANCE_AND_CURRICULUM_AUDIT.md`**: Zero-hallucination fact checking (history, science, math, literature), grade-level readiness (DOK 1-4), and the 100-point DepEd MATATAG QA Audit Scorecard.
   - **`06_AI_IMAGE_PROMPT_STANDARDS_AND_EXEMPLARS.md`**: Zero-abstract physical scene architecture, "Wall of Shame" banning meta-prompts, the 5 Cinematographic Pillars, strict 10-prompt unit quota, and gold-standard exemplars for Filipino, Science, Math, and Values Ed.

---

## ⚙️ 2-MINUTE SETUP IN CHATGPT

1. Open ChatGPT ➔ Click on your profile / **Explore GPTs** ➔ **Create a GPT** (or edit your existing one).
2. Go to the **Configure** tab:
   - **Name**: `DepEd MATATAG Master Textbook Creator`
   - **Description**: `Generates publication-grade, 40+ page interactive textbook units (70% lessons / 30% activities) across all subjects matching the MATATAG curriculum.`
3. **Instructions**:
   - Open [`INSTRUCTIONS_FOR_CHATGPT.txt`](file:///c:/Users/Rhenel%20Jhon%20Sajol/Documents/CERE_BOOK/ALL_IN_ONE_GPT_SETUP/INSTRUCTIONS_FOR_CHATGPT.txt), copy everything, and paste it into the **Instructions** box.
4. **Knowledge**:
   - Click **Upload files** and upload all 7 files inside the [`KNOWLEDGE_FILES/`](file:///c:/Users/Rhenel%20Jhon%20Sajol/Documents/CERE_BOOK/ALL_IN_ONE_GPT_SETUP/KNOWLEDGE_FILES) folder.
5. **Capabilities**:
   - Check **Code Interpreter & Data Analysis** (required for compiling `.docx` files).
   - Check **Web Search** (optional, for curating real YouTube links).
6. Click **Save** / **Update** in the top-right corner.

---

## 🎯 HOW TO USE IT

1. In the chat, upload your **Table of Contents (TOC)** and **Curriculum Guide (CG)** (PDF or Markdown).
2. Tell it: *"Gawin natin ang Unit III, Aralin 13-15."*
3. **Turn 1**: The GPT outputs the clean 3-page Front Matter (Cover, Preface, TOC) and pauses.
4. Type **`Proceed`** at each step:
   - It outputs Lesson 1 (3,500+ words, full 10 sections, no internal breaks).
   - It outputs Lesson 2 (3,500+ words).
   - It outputs Lesson 3 (3,500+ words).
   - It outputs the 40-pt Unit Assessment, Summary, Glossary, and Complete Answer Key.
5. It then runs its Python Code Interpreter engine to give you the direct download link to your `.docx` file!
