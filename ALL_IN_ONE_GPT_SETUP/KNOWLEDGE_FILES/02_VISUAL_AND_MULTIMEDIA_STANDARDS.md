# DEPED MATATAG VISUAL MEDIA & INTERACTIVE MULTIMEDIA STANDARDS

This document specifies the exact format and styling for all visual placeholders, AI generation prompts, and interactive YouTube video modules across ALL DepEd MATATAG subjects (Science, Math, English, Filipino, AP, MAPEH, TLE).

---

## 1. VISUAL CONCEPT ART & AI PROMPT SPECIFICATION (BOXED CONTAINER)

Whenever a visual placeholder is embedded into the textbook, it must be structured as a dedicated, fully self-contained visual prompt callout frame:

### 🛑 MANDATORY "PROMPTS ONLY (PLACEHOLDER FRAME)" LAW:
The AI generator must **NEVER** generate, scrape, fetch, or embed actual image files or external web URLs! Output **ONLY** the text prompt inside the styled boxed container as a placeholder frame so that the author can generate the image in Midjourney v6 / DALL-E 3 and manually insert it into the Word document via `Insert > Pictures`.

### Strict Production Rules (No Draft Labels & Mandatory Box):
- **NO DRAFT LABELS (BAN "Visual Prompt 1", "Prompt 2")**: This is a publication-ready textbook. Never output draft labels like `"Visual Prompt 1:"` or `"Prompt 1:"`! Use ONLY clean production titles: `🖼️ Larawan: [Mapanuring Pamagat ng Larawan]` or `🖼️ Figure: [Descriptive Image Title]`.
- **100% INSIDE A DEDICATED CONTAINER BOX**: The Title, Pedagogical Purpose, AI Prompt, and Replacement Note MUST ALL BE ENCLOSED INSIDE ONE SINGLE CONTAINER BOX (using Markdown callouts `> ...` or a 1-cell shaded table in DOCX). Never let titles or purpose statements float outside as loose text!
- **Box Shading**: Soft Gray-Blue (`#F4F7FA` or `#FAFAFA`).
- **Border**: Navy Blue (`#1B365D`, 4.5pt solid left border) or subtle dashed border (`#CCCCCC`).
- **Header**: `🖼️ Larawan: [Mapanuring Pamagat]` (or `🖼️ Figure: [Descriptive Title]`) in 10.5pt Bold Navy Blue (`#1B365D`).
- **Pedagogical Purpose (Layunin)**: 1–2 sentences explaining how this visual supports the learning competency.
- **Reference**: Follow [`06_AI_IMAGE_PROMPT_STANDARDS_AND_EXEMPLARS.md`](file:///c:/Users/Rhenel%20Jhon%20Sajol/Documents/CERE_BOOK/ALL_IN_ONE_GPT_SETUP/KNOWLEDGE_FILES/06_AI_IMAGE_PROMPT_STANDARDS_AND_EXEMPLARS.md) for the 5 Physical Cinematographic Pillars, banned abstract prompts, and the Subject-Calibrated Visual Art Matrix:
  * **Filipino, English, Values Ed / GMRC, and Book Covers**: Mandatory **Studio Ghibli-inspired warm pastoral anime watercolor illustration** (hand-painted lush watercolor background art, Hayao Miyazaki lighting, expressive warmth, gentle linework, nostalgic atmospheric skies; NEVER hyper-real plastic stock CGI).
  * **Mathematics & Science (STEM)**: **TECHNICAL 2D VECTOR DIAGRAMS & SCHEMATICS** (horizontal number lines, 2-color integer discs, coordinate Cartesian grids, geometric figures, balance scales, laboratory cross-sections). Rendered in crisp **flat 2D vector educational textbook schematic style** on pure white or subtle grid. Straight-on orthographic view. STRICT BANS FOR STEM: NO wooden desks, NO pencils/rulers, NO hands/people, NO room windows/sunlight beams, NO 3D perspective clutter!
  * **TLE / TVL**: Mandatory **real object sample photography** and technical isometric blueprints (strict NO Ghibli/cartoon).
  * **Araling Panlipunan**: **ZERO EXTRA WORK PROTOCOL (NO AI HERO FACES & NO MANUAL PHOTO HUNTING)**: To save authors from manual photo-hunting work, always prompt **Primary Source Still-Life / POV & Historic Settings** (historic desks, draft manuscripts, flags, ships, trade goods). 100% turnkey generatable in Midjourney/DALL-E with zero fake faces!
  * **MAPEH**: Museum-grade cultural artifacts (organology) & authentic biomechanical sports kinesiology.
- **Strict Zero-Branding Rule for Prompts**:
  * **NEVER** include publisher names, brand names, or government acronyms (`DepEd`, `MATATAG`, `CERE`) inside ANY AI image prompt.
  * AI image generators (Midjourney, DALL-E) try to render acronyms as distorted text, fake badges, or watermark artifacts.
  * Always describe pure visual elements (scene, lighting, subjects, uniforms without badges, historical context, colors).
  * Always append negative styling: `no text, no logos, no watermark, no branding --ar 16:9 --v 6.0` (or `--ar 8.5:11` for covers).
- **Teacher / Student Instruction**: *"Paunawa: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures)."*

### Standard Boxed Markdown Format:
```markdown
> ### 🖼️ Larawan: [Mapanuring Pamagat ng Larawan]
> **Pedagohikal na Layunin:** [1-2 pangungusap kung paano sinusuportahan ng biswal ang aralin]  
> **AI Generation Prompt (DALL-E 3 / Midjourney v6):**  
> `[Concrete 5-Pillar Scene: Characters + Action + Setting + 3-4 Props + Lighting + Medium, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0]`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng aktuwal na nabuong larawan sa Microsoft Word (Insert > Pictures).*
```

### Mandatory Image-Prompt Quota (Scales with Lesson Count):
To maintain clean typography and prevent visual clutter, every generated textbook follows a fixed per-lesson quota:
- **Page 1 (Front Cover)**: Exactly 1 Full-Page Cover AI Prompt Box (3-tier title banner, `--ar 8.5:11`).
- **Every Lesson**: Exactly 3 Image Prompt Boxes (Subtopic 1, Subtopic 2, Applied / Multimodal Task, `--ar 16:9`).
- **Unit Assessment & Back Matter**: Zero image prompts (focused purely on 1-30 MCQ quiz, Performance Task, Synthesis, and Answer Keys).
- **Total Quota = 1 + (3 × number of lessons)**: 3-lesson unit = **10 prompts**; 5-lesson quarter = **16 prompts**; 6-lesson quarter = **19 prompts**.
- **Mathematics exception**: lesson figures are drawn by code per `07_MATHEMATICS_TEXTBOOK_STANDARDS.md` (no AI prompt boxes inside Math lessons); only the cover uses an AI prompt.

---

## 2. INTERACTIVE YOUTUBE MULTIMEDIA MODULES (DIRECT REAL VIDEO LINKS)

### ⚠️ MANDATORY DIRECT VIDEO LINK POLICY (NO SEARCH LINKS, REAL VIDEOS ONLY):
Teachers and students must have an immediate, direct click to the actual video. To ensure maximum usability, authenticity, and professionalism:

1. **LESSON- & ACTIVITY-SPECIFIC DIRECT VIDEO LINK (NO GENERAL COMPILATIONS)**:
   - Provide an authentic direct YouTube video link: `https://www.youtube.com/watch?v=[REAL_VIDEO_ID]`.
   - **MUST BE TOPIC-SPECIFIC**: The video MUST directly match the specific topic, concept, or learning activity of THAT lesson (e.g., if the lesson is about *Developing Talents & Purpose*, use a video specifically on talents and purpose; if *Forgiveness*, on forgiveness; if *Photosynthesis*, on photosynthesis).
   - **STRICT BAN ON GENERAL FULL-COURSE COMPILATIONS**: NEVER link to a 2-hour "Values Education 7 Full Course" or general grade-level compilation! The video must be a focused, targeted 5–15 minute educational lesson or case study.
   - **DO NOT USE SEARCH LINKS** (e.g., do not use `results?search_query=...`).
   - The video MUST legit exist and be actively hosted on YouTube by verified educational channels (*DepEd TV Official, Knowledge Channel, CrashCourse, Khan Academy, TED-Ed, SoulPancake, DOSTv, GMA Public Affairs*).

2. **🚫 ZERO AI DISCLAIMERS OR NOTES (STRICT PUBLICATION STANDARD)**:
   - **NEVER** output apologies, meta-disclaimers, or editorial excuses like:
     * ❌ *"The multimedia box intentionally does not invent a direct video address..."*
     * ❌ *"A real, verified link should be inserted during final publication verification."*
     * ❌ *"A direct video is intentionally not fabricated here..."*
   - In a publication textbook, disclaimers and excuses are unacceptable defects.
   - **MANDATORY WORKING LINK PROTOCOL**:
     * If the generator does not know an exact video ID by heart, it MUST immediately pull the verified topic match from the **Curated Topic-Specific Video Bank** below.
     * All elements MUST be 100% inside the single container box. **ZERO text or notes below the box.**

3. **ZERO FAKE TIMESTAMPS**:
   - Never invent fake minutes and seconds (e.g., do not write `02:10 - 05:30`).
   - Instead, provide 2–3 **Key Concepts & Themes to Observe** that focus students' attention on what the lesson covers.

4. **Zero QR Codes**: Banned to eliminate broken ASCII boxes.

5. **100% Inside a Dedicated Container Box**: Title, Channel, Direct Video Link, Key Concepts to Observe, and 3 Socratic Viewing Questions MUST all be enclosed inside ONE single box (`> ...` with solid YouTube Red `#CC0000` left border in Markdown, or a 1-cell table in DOCX).

---

### 📚 CURATED TOPIC-SPECIFIC VIDEO BANK (100% REAL, TESTED, ACTIVE EDUCATIONAL VIDEOS):
Use these permanent, active, high-authority educational videos tailored specifically per lesson topic:

| Subject & Grade | Specific Lesson / Activity Topic | Official Channel | Verified Working Direct Link |
| :--- | :--- | :--- | :--- |
| **Values Ed 7 (Unit III Lesson 1)** | Developing Talents, Abilities & Purpose | SoulPancake / Kid President | `https://www.youtube.com/watch?v=1Evwgu369Jw` |
| **Values Ed 7 (Unit III Lesson 2)** | Forgiving, Reconciling & Healing Kapuwa | SoulPancake / Science of Forgiveness | `https://www.youtube.com/watch?v=EpclyrcMMHs` |
| **Values Ed 7 (Unit III Lesson 3)** | Honest Friendship, Empathy & Trust | TED-Ed / Social Well-being | `https://www.youtube.com/watch?v=W3I3kAg2J7w` |
| **Filipino 7/8 (Aralin 1)** | Doctrina Christiana & Panitikang Kolonyal | Knowledge Channel | `https://www.youtube.com/watch?v=kS6Y2L0hO08` |
| **Filipino 7/8 (Aralin 2)** | Kuwentong-Bayan, Alamat, at Pabula | Knowledge Channel | `https://www.youtube.com/watch?v=R9R3t2dF9m0` |
| **Science 8 (Lesson 1)** | Cellular Transport & Cell Membranes | CrashCourse Biology | `https://www.youtube.com/watch?v=dPKvHrD1eS4` |
| **Science 8 (Lesson 2)** | Photosynthesis & Cellular Respiration | Amoeba Sisters | `https://www.youtube.com/watch?v=qBCGGnuuUwk` |
| **Science 8 (Lesson 3)** | Earth's Orbit, Seasons & Climate | CrashCourse Kids | `https://www.youtube.com/watch?v=jgPE3O24jv8` |
| **Math 7/8 (Lesson 1)** | Introduction to Algebraic Expressions | Khan Academy | `https://www.youtube.com/watch?v=NybHckSEQBI` |
| **Math 8/9 (Lesson 2)** | Geometric Patterns, Symmetry & Tessellations | Numberphile | `https://www.youtube.com/watch?v=302eJ3TzJQU` |
| **Araling Panlipunan 7/8** | Kolonyalismo at Kasaysayan ng Pilipinas | GMA Public Affairs | `https://www.youtube.com/watch?v=s1Q4f7mYh1o` |
| **Araling Panlipunan 7/8** | Katipunan, Rebolusyon at Pambansang Kamalayan | National Historical Commission (NHCP) | `https://www.youtube.com/watch?v=KzK8d_j2iNk` |
| **English 7/8 (Lesson 1)** | Why We Read Literature & Narrative Themes | CrashCourse Literature | `https://www.youtube.com/watch?v=MSYw502dJNY` |
| **English 8/9 (Lesson 2)** | Dystopian Literature & Social Critical Thinking | TED-Ed | `https://www.youtube.com/watch?v=7h84HqP1Uf0` |
| **MAPEH (PE & Health)** | Physical Activity, Nutrition & Mental Health | TED-Ed | `https://www.youtube.com/watch?v=gT_qLp6r6_8` |
| **MAPEH (Music & Arts)** | Katutubong Musika, Instrumento at Kulintang | Knowledge Channel | `https://www.youtube.com/watch?v=aG38K50qS_M` |
| **TLE / TVL (Agri-Crop)** | Agricultural Innovation & Food Technology | DOSTv | `https://www.youtube.com/watch?v=2TzF3K1xYyA` |

### Required Module Layout & Styling (100% Boxed, Direct Video Link):
- **Box Shading**: Soft Red (`#FFF5F5`)
- **Left Border**: Solid YouTube Red (`#CC0000`, 4.5pt / `sz="36"`)
- **Title (match the book's language of instruction)**: `🎥 INTERACTIVE MULTIMEDIA: [MODULE TITLE]` for English-medium subjects (Math, Science, English, MAPEH, TLE); `🎥 INTERAKTIBONG MULTIMEDIA: [MODULE TITLE]` for Filipino-medium subjects (Filipino, AP, Values Ed). 10.5pt Bold YouTube Red.
- **Verified Channels**: Must cite recognized channels (*DepEd TV Official, Knowledge Channel, CrashCourse, Khan Academy, DOST-SEI, GMA Public Affairs*).
- **Direct Video Link**: `https://www.youtube.com/watch?v=[REAL_VIDEO_ID]` (Must be a real, working video!).
- **Key Concepts to Observe**: 2–3 conceptual bullet points on what to look for.
- **Socratic Viewing Questions (3 Items)**:
  1. *Recall / Direct Observation*: What specific evidence, event, or phenomenon was shown?
  2. *Concept Connection*: How does this explain the principle in the lesson?
  3. *Real-World Critical Thinking*: What are the societal, ethical, or practical implications?

### YouTube Module Boxed Exemplar (Filipino-Medium):
```markdown
> ### 🎥 INTERAKTIBONG MULTIMEDIA: Paglalayag sa Panitikan ng Panahong Kolonyal
> **Opisyal na Tsanel:** Knowledge Channel  
> **Direktang Link sa Video:** [Panoorin sa YouTube: Panitikang Pilipino](https://www.youtube.com/watch?v=kS6Y2L0hO08)  
>  
> **🎯 Mga Tampok na Konseptong Dapat Obserbahan:**  
> • Ang pagdating ng imprenta at Doctrina Christiana sa Maynila noong 1593 at ang epekto nito sa panitikan.  
> • Paggamit ng Pasyon at Senakulo bilang multimodal na pagpapahayag ng pananampalataya at damdaming bayan.  
>  
> **❓ Mga Gabay na Tanong sa Panonood:**  
> 1. *Direct Observation:* Batay sa video, anong teknikal na pamamaraan ang ginamit ng mga manlilimbag sa unang aklat?  
> 2. *Concept Connection:* Paano ipinakita sa dokumentaryo ang paggamit ng Pasyon sa pagpapahayag ng damdaming bayan?  
> 3. *Real-World Application:* Bakit naging napakalakas ng biswal at pasalitang anyo ng panitikan sa panahong iyon?  
```

### YouTube Module Boxed Exemplar (English-Medium / Science):
```markdown
> ### 🎥 INTERACTIVE MULTIMEDIA: Cellular Transport in Living Organisms
> **Official Channel:** CrashCourse  
> **Direct Video Link:** [Watch on YouTube: In Da Club - Membranes & Transport: Crash Course Biology #5](https://www.youtube.com/watch?v=dPKvHrD1eS4)  
>  
> **🎯 Key Concepts & Themes to Observe:**  
> • Phospholipid bilayer fluid mosaic structure and the nature of selective permeability.  
> • Passive vs. active transport mechanisms across cellular membrane gradients.  
>  
> **❓ Socratic Viewing Questions:**  
> 1. *Direct Observation:* What molecular properties determine whether a particle can diffuse directly through the lipid bilayer?  
> 2. *Concept Connection:* How does the documentary illustrate the role of ATP energy in active transport pumps?  
> 3. *Real-World Application:* Relate cellular osmotic regulation to how plant root systems absorb water from hypertonic or hypotonic soil.  
```

---

## 3. SUBJECT-SPECIFIC COVER & VISUAL PROMPT EXEMPLARS

### Cover Art Exemplar 1: Filipino-Medium (Grade 7 Filipino — Studio Ghibli Aesthetic)
```text
[PROMPT SA PAGBUO NG LARAWAN SA PABALAT / FRONT COVER AI IMAGE PROMPT]
PAMAGAT NG AKLAT: Gabay Pampagkatuto sa Filipino 7
BAITANG AT YUNIT: Filipino Baitang 7 • Yunit III: "Ako at ang Aking Pagkatao, Tanglaw ng Katatagan"
PAKSA: Panitikan sa Panahon ng Espanya • Tekstong Pampahayagan • Wika at Multimodal

PROMPT: A prestigious, high-end educational textbook cover layout. At the top of the cover, a sleek deep navy blue graphic banner featuring clean, crisp, perfectly rendered typography. The primary headline in bold white capital letters reads: "GABAY PAMPAGKATUTO SA FILIPINO 7". Below it, a secondary title in elegant warm gold letters reads: "YUNIT III: AKO AT ANG AKING PAGKATAO, TANGLAW NG KATATAGAN". Beneath in subtle light silver text: "Panitikan sa Panahon ng Espanya • Tekstong Pampahayagan • Wika at Multimodal". In the lower two-thirds illustration, a breathtaking Studio Ghibli-inspired anime watercolor scene of two Filipino Grade 7 students (a 13-year-old boy and girl in neat school uniforms) reading together at an open-air wooden veranda under warm morning sunbeams. Beside them on the wooden table rests a stack of books and a small potted calamansi plant. In the background, rolling verdant hills, ancient capiz-window heritage houses, and billowy painted cumulus clouds across an azure tropical sky. Hand-painted watercolor anime aesthetic, Hayao Miyazaki warmth, rich pastoral beauty, clean textbook graphic design, perfectly centered professional typography, ultra-high resolution, no gibberish text, no watermarks, no logos --ar 8.5:11 --v 6.0
```

### Cover Art Exemplar 2: English-Medium (Grade 8 Science)
```text
[FRONT COVER AI IMAGE PROMPT / COVER ART SPECIFICATION]
BOOK TITLE: Learning Guide in Science 8
GRADE & UNIT: Science Grade 8 • Unit II: "Force, Motion, and Energy Transformations"
SCOPE: Newtonian Mechanics • Work and Power • Energy Flow in Living Ecosystems

PROMPT: A prestigious, high-end educational textbook cover layout. At the top of the cover, a sleek deep navy blue graphic banner featuring clean, crisp, perfectly rendered typography. The primary headline in bold white capital letters reads: "SCIENCE 8: LEARNING GUIDE". Below it, a secondary title in elegant warm gold letters reads: "UNIT II: FORCE, MOTION, AND ENERGY". Beneath in subtle light silver text: "Newtonian Mechanics • Work and Power • Energy Transformations". In the lower two-thirds illustration, two Filipino junior high school students (a 14-year-old boy and girl wearing protective laboratory goggles and modern school uniforms) actively conducting a physics mechanics experiment with dynamic tracks and photogate timers in a modern, well-lit school laboratory. In the background, illuminated chalkboard blueprints of physics vectors and dynamic energy conversion models. Clean textbook graphic design, perfectly centered professional typography, ultra-high resolution, no gibberish text, no watermarks, no logos --ar 8.5:11 --v 6.0
```

### Filipino & English (Literature, Poetry, Humanist Themes — Studio Ghibli Style):
> ### 🖼️ Larawan: Pagbasa at Pagsusuri ng Akda sa Lilim ng Punong Mangga
> **Pedagohikal na Layunin:** Magbigay ng mainit, madamdaming visual connection sa panitikan at kulturang Pilipino sa estilong Studio Ghibli.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A warm, enchanting Studio Ghibli anime style illustration of two Filipino junior high students seated on a weathered wooden bamboo bench beneath a majestic flowering mango tree. One student points with wonder to a page of an open illustrated poetry anthology, while gentle tropical breezes carry green leaves into the air. Golden afternoon sunbeams break through the foliage, casting dappled light across their school uniforms and textbooks. In the background, quiet provincial rice paddies and distant blue mountain ridges under soft watercolor clouds. Hand-painted anime background art, Hayao Miyazaki nostalgic aesthetic, emotional warmth, fine hand-drawn outlines, no text, no logos, no watermark --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

### Values Education / GMRC (Empathy, Friendship, Ethical Dilemmas — Studio Ghibli Style):
> ### 🖼️ Larawan: Pagtutulungan at Pagkakaibigan sa Komunidad
> **Pedagohikal na Layunin:** Magbigay ng makatao at positibong huwaran ng pagmamalasakit at kapuwa sa kabataan.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A heartwarming Studio Ghibli anime style illustration of Filipino teenage students helping an elder community neighbor carry handmade woven baskets filled with fresh vegetables in a clean, sunlit barangay pathway. Warm, sincere facial expressions, hand-drawn character details, rustic wooden houses with potted orchids, soft golden morning light, and lush tropical greenery. Emotionally resonant storybook art, watercolor painterly textures, nostalgic warmth, no text, no logos, no watermark --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

### TLE / TVL (Technical & Industrial — STRICT REAL OBJECT SAMPLE EXCEPTION):
> ### 🖼️ Figure: Real Wooden Mortise and Tenon Joint & Workshop Tool Setup
> **Pedagogical Purpose:** Ipakita ang aktuwal na estruktura at precision craftsmanship ng gawaing-kahoy para sa technical education.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A crisp, professional commercial product sample photograph of an authentic wooden mortise and tenon joint on a heavy carpenter's workbench. The joint is shown partially disassembled, revealing the precise rectangular tenon tongue fitting perfectly into the clean chiseled mortise hole in solid Narra hardwood with rich natural wood grain. Lying neatly beside the wooden joint are real authentic carpentry tools: a vintage steel marking gauge, an oiled hand-chisel with polished wooden handle, a brass sliding caliper, and fresh curly wood shavings. Bright natural workshop window lighting, macro tool photography, razor-sharp focus across wood fibers, authentic craftsmanship, no text, no logos, no watermark --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

### Araling Panlipunan (History & Heroes — STRICT HERO INTEGRITY RULE: NO FAKE AI HERO FACES):

#### Method 1: Authentic Archival Photograph Frame (For Real Historical Figures):
> ### 🏛️ Larawang Pangkasaysayan: Dr. Jose Rizal (1896 Archival Collection)
> **Pedagohikal na Layunin:** Magpakita ng tunay at hindi gawa-gawang (authentic, non-AI) larawan ng pambansang bayani bilang paggalang sa kanyang tunay na mukha.  
> *Paunawa sa Guro/Editor: HUWAG gamitin ang AI para iguhit o buuin ang mukha ni Rizal! I-insert sa Word ang opisyal na public-domain archival photo mula sa National Historical Commission of the Philippines (NHCP) o Pambansang Aklatan.*

#### Method 2: Primary Source Still-Life / POV (Historical Artifacts, Desks, Zero Hero Faces):
> ### 🖼️ Larawan: Pagsulat ng Noli Me Tangere: Ang Mesa ng Manunulat sa Berlin (1887)
> **Pedagohikal na Layunin:** Ilarawan ang kongkretong atmospera at mga kagamitan sa pagsulat ng Noli Me Tangere sa Berlin nang walang pekeng mukha ng bayani.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `An authentic 1887 historical still life and point-of-view scene inside a cold, modest attic room in Berlin, Germany. Focus on a heavy oak writing desk: open handwritten draft manuscripts of "Noli Me Tangere" with neat Spanish cursive script in sepia ink, a dark glass ink bottle, a slender steel dip pen resting on an inkstand, and vintage round wire-rimmed reading spectacles lying beside an unfolded letter addressed to Ferdinand Blumentritt. On the corner of the table sits an antique brass kerosene lamp casting a warm amber pool of light over the paper, alongside a small, half-eaten loaf of dark rye bread. In the background, tall wooden windowpanes with frost patterns overlooking dim European cobblestone streets under a snowy twilight sky. Classical museum oil painting realism, rich canvas textures, dignified historical atmosphere, NO human faces, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

### MAPEH (Music, Arts, PE, Health — Cultural Organology & Kinesiology):
> ### 🖼️ Figure: Traditional Mindanaoan Kulintang Gong Ensemble
> **Pedagogical Purpose:** Preserves indigenous cultural organology and traditional performance crafts.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A culturally authentic, highly detailed still-life illustration of a complete traditional Mindanaoan Kulintang ensemble set. Ornate, intricately hand-carved okir wooden frame (antangan) holding a row of eight bossed bronze gongs with glowing metallic sheen. Beside it, agung gongs and dabakan drum. Warm dramatic lighting, museum quality, cultural dignity, no text, no logos, no watermark --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

### Science (Cellular & Laboratory — Real Laboratory / 3D Specimen):
> ### 🖼️ Figure: High-Resolution 3D Cross-Section of Plant Cell Organelles
> **Pedagogical Purpose:** Demonstrates the structural relationship between rigid cellulose cell wall, large central vacuole, and emerald chloroplasts during photosynthesis.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A highly detailed, photorealistic 3D anatomical cross-section diagram of a eukaryotic plant cell (Allium cepa) on an ultra-clean scientific laboratory background. Clear distinct visualization of the cell wall, central vacuole, bright emerald green chloroplasts, and translucent nucleus. Vibrant color-coded educational palette, studio lighting, volumetric glow, high scientific accuracy, 8k resolution, documentary science textbook quality, no text, no logos, no watermark --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

### Mathematics (Vector & 3D Geometry — Clean Blueprint Vector):
> ### 🖼️ Figure: 2D Cartesian Coordinate Plane with Linear Functions
> **Pedagogical Purpose:** Visualizes linear slope intercept equations and coordinate intersection points.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A clean, high-precision mathematical diagram of a 2D Cartesian coordinate plane on subtle blueprint grid paper. Crisp, dark navy x-axis and y-axis clearly labeled from -10 to +10. A bold royal blue linear function line intersecting the y-axis with distinct labeled coordinate points (0,2) and (3,8). Minimalist, high contrast, clean vector style, textbook mathematical illustration, no text, no logos, no watermark --ar 16:9 --style raw`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

