# DEPED MATATAG AI IMAGE PROMPT ENGINEERING & VISUAL EXEMPLARS
## Zero-Abstract, Cinematographic Scene Architecture for Midjourney v6 & DALL-E 3

This document is the mandatory standard for generating **all AI image prompts** across all DepEd MATATAG subjects (Filipino, English, Science, Mathematics, Araling Panlipunan, MAPEH, TLE, and Values Education / GMRC) for Grades 1 through 10.

---

# PART 1: THE CORE PHILOSOPHY — PHYSICAL SCENES VS. ABSTRACT CONCEPTS

Image generation models (Midjourney v6, DALL-E 3) **do NOT understand abstract curriculum concepts**, "subtopics", "pedagogical competencies", or mental activities like "analyzing" or "source checking". 

When a prompt says *"illustrating the central concept of this subtopic"* or *"showing textual analysis"*, the AI generator hallucinates:
- Blurry floating circles and random meaningless arrows.
- Distorted gibberish charts with fake letters.
- Cluttered, generic stock-illustration clipart that looks amateurish and unpublishable.

### 🌟 THE GOLDEN RULE OF TEXTBOOK PROMPT ENGINEERING:
> **An image prompt must describe PHOTONS HITTING PHYSICAL SURFACES — concrete people, physical hand actions, tangible architecture, realistic historical/scientific props, directional lighting, and camera optics.**

---

# PART 2: THE "WALL OF SHAME" — STRICTLY BANNED LAZY PROMPTS

The following types of prompts are **STRICTLY PROHIBITED** and will fail the Quality Assurance Audit:

### ❌ BANNED PROMPT 1: The "Abstract Concept" Cop-Out
```text
BANNED: "A publication-grade Grade 8 Filipino educational infographic illustrating the central concept of this subtopic through historically respectful, non-branded visual elements, clear hierarchy, realistic Filipino context, no readable gibberish, no logos, no watermark, no branding --ar 16:9 --v 6.0"
```
**Why it Fails**:
- What is in the picture? Nobody knows!
- *"Illustrating the central concept"* is meta-instruction, not a physical scene.
- *"Historically respectful visual elements"* does not name a single actual object.
- Result in Midjourney: Floating meaningless blue shapes and unreadable pseudo-text.

### ❌ BANNED PROMPT 2: The "Mental Action" Storyboard
```text
BANNED: "A six-frame educational storyboard for Filipino Grade 8 showing source checking, textual analysis, historically respectful archival-style imagery, camera framing, caption review, and final narration recording. Clean pencil storyboard, no logos, no watermark, no branding --ar 16:9 --v 6.0"
```
**Why it Fails**:
- You cannot draw "source checking" or "textual analysis" — those are invisible cognitive processes.
- An AI generator cannot draw 6 micro-storyboard panels with readable pedagogical steps; it produces a messy collage of distorted scribbles.

### ❌ BANNED PROMPT 3: The Generic "Students Learning" Cliché
```text
BANNED: "Filipino students in a classroom learning about the lesson with happy faces and books on their desk --ar 16:9"
```
**Why it Fails**:
- Generic stock photo feel with zero subject-matter connection.

### ❌ BANNED PROMPT 4: The "Faking Real Historical Heroes / Specific Persons" Blunder
```text
BANNED: "A portrait of Dr. Jose Rizal writing Noli Me Tangere in Berlin --ar 16:9"
BANNED: "Andres Bonifacio shouting in the Cry of Pugad Lawin holding a bolo with angry face --ar 16:9"
```
**Why it Fails**:
- AI image models (Midjourney, DALL-E) **cannot** accurately reproduce the true facial likeness of real historical persons. They hallucinate distorted faces, alien-looking eyes, inaccurate Westernized features, or disrespectful caricatures.
- In national educational publishing, generating a fake AI face of a revered historical figure (Dr. Jose Rizal, Andres Bonifacio, Apolinario Mabini, Tandang Sora, Emilio Aguinaldo) is an unacceptable historical distortion and violates DepEd textbook standards.

### 🏛️ THE NATIONAL HERO INTEGRITY RULE (ZERO EXTRA WORK PROTOCOL):
> **NEVER generate AI faces of specific historical persons, and AVOID assigning manual photo-hunting homework to the user!**
> Asking authors or teachers to manually search government archives for historical photos creates unnecessary extra work.
> 
> **The Turnkey Golden Standard**: Always generate a 100% ready-to-run AI prompt using the **Primary Source Artifact / Historic Setting / POV Technique** (desks, manuscripts, flags, ships, trade goods):
> - **Studying Rizal & Literature?** ➔ Prompt the 1887 Berlin writing desk, handwritten draft manuscript of *Noli Me Tangere*, steel dip-pen, dark inkwell, vintage wire spectacles, and brass lamp.
> - **Studying the Katipunan & Revolution?** ➔ Prompt the rustic table with the red Katipunan flag (white KKK sun), oil lamp, goose feather quill, oath ledger, and bolo scabbard in candlelit shadows.
> - **Studying Pre-Colonial Society?** ➔ Prompt the ancient wooden balangay boat docked on a pristine shore with woven baskets of spices, native gold ornaments, and porcelain jars at golden sunrise.
> - **Studying Maritime Trade?** ➔ Prompt the 17th-century Spanish galleon cargo deck loaded with silk bolts and spice crates in Manila Bay.
> 
> **Result**: Generates breathtaking, dignified, historically rich visuals in Midjourney/DALL-E with **ZERO distorted hero faces** and **ZERO extra manual search work** for the user!

---

# PART 2.5: THE 3-STEP DYNAMIC TRANSLATION PIPELINE
### (How to Turn ANY Subtopic into a Concrete Physical Scene)

When generating an image prompt for a subtopic, the AI must NEVER summarize the syllabus or copy placeholder words like `"illustrating the central concept"`. Instead, execute this 3-step pipeline:

```text
┌────────────────────────────────────────────────────────────────────────────┐
│                    THE 3-STEP DYNAMIC TRANSLATION PIPELINE                 │
├────────────────────────────────────────────────────────────────────────────┤
│ STEP 1: SCAN THE SUBTOPIC PARAGRAPHS JUST WRITTEN                          │
│ Extract the specific real-world anchor:                                    │
│ • History/Literature: The author, character, date, town, or artifact.     │
│ • Science: The laboratory apparatus, specimen, cell, or chemical reaction. │
│ • Math: The physical structure (bridge arch, satellite dish, blueprint).   │
│ • Values/MAPEH/TLE: The physical craft, instrument, or human interaction.  │
├────────────────────────────────────────────────────────────────────────────┤
│ STEP 2: APPLY THE "HOLLYWOOD VIEWFINDER" TEST                              │
│ Ask: "If a camera were placed in front of this event, WHAT DOES THE LENS  │
│ ACTUALLY RECORD?"                                                          │
│ • A lens CANNOT see "textual analysis" or "central concept".               │
│ • A lens CAN see: A 19th-century writer dipping a steel quill into black   │
│   ink, leaning over rough abaca paper under amber lantern light.           │
├────────────────────────────────────────────────────────────────────────────┤
│ STEP 3: ASSEMBLE THE 5 PHYSICAL PILLARS                                    │
│ Assemble Characters + Setting + 3-4 Props + Lighting + Camera Optics.      │
│ Terminate with: no text, no logos, no watermark, no branding --ar 16:9     │
└────────────────────────────────────────────────────────────────────────────┘
```

---

# PART 3: THE SUBJECT-CALIBRATED ARTISTIC MEDIUM & VISUAL MATRIX

Image generation in an educational textbook must **never look like generic AI plastic or eerie uncanny-valley stock photography**. Furthermore, different subjects demand fundamentally different visual languages:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   SUBJECT-CALIBRATED VISUAL ART MATRIX & MEDIUM                        │
├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│ DISCIPLINE / SUBJECT     │ MANDATORY VISUAL STYLE      │ KEY AESTHETIC MARKERS         │
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ • FILIPINO               │ Studio Ghibli-Inspired      │ Hand-painted lush watercolor  │
│ • ENGLISH                │ Pastoral Anime &            │ background art, warm Hayao    │
│ • VALUES ED / GMRC       │ High-Detail Storybook       │ Miyazaki lighting, soft       │
│ • TEXTBOOK FRONT COVERS  │ Illustration Aesthetic      │ expressive linework, nostalgic│
│                          │                             │ atmospheric skies, tropical   │
│                          │ (NOT hyper-real stock CGI!) │ flora, cultural warmth.       │
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ • TLE / TVL              │ Real Object Sample /        │ Authentic workshop product    │
│   (Technical-Vocational) │ Technical Engineering       │ photography, crisp isometric  │
│                          │ Photography & Blueprints    │ drafting, real hand tools,    │
│                          │                             │ clean workbench schematics,   │
│                          │ (STRICT: NO GHIBLI/CARTOON!)│ OHS safety gear in action.    │
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ • ARALING PANLIPUNAN     │ ZERO EXTRA WORK PROTOCOL:   │ Primary Source Still-Life &   │
│   (Philippine History &  │ NO AI HERO FACES &          │ Tangible Period Settings:     │
│    Historical Events)    │ NO MANUAL SEARCH HOMEWORK!  │ Historic desks, draft         │
│                          │                             │ manuscripts, flags, ships,    │
│                          │ 100% turnkey generatable    │ artifacts. Ready to generate; │
│                          │ still-life / POV scenes.    │ zero fake faces, zero hunting!│
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ • MAPEH                  │ Museum Cultural Artifact    │ Authentic cultural organology │
│   (Music, Arts, PE,      │ Documentation & Precise     │ (Kulintang, Okir carvings),   │
│    Health)               │ Biomechanical Kinesiology   │ museum-grade folk art, real   │
│                          │                             │ athletic human kinesiology.   │
├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ • SCIENCE & MATHEMATICS  │ Real Laboratory Photography,│ Crisp compound optical slides,│
│                          │ 3D Anatomical Cross-Section,│ specimen wet-mounts, clean    │
│                          │ Vector Blueprint Geometry   │ apparatus, Cartesian grids.   │
└──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

---

# PART 3.5: THE 5 MANDATORY CINEMATOGRAPHIC PILLARS

Every single image prompt in the textbook MUST be built upon these **5 concrete physical layers**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      THE 5 VISUAL PROMPT PILLARS                       │
├────────────────────────────────────────────────────────────────────────┤
│ 1. SPECIFIC CHARACTERS & TANGIBLE ACTION                               │
│    Who is physically present? What exact action are their hands and    │
│    eyes performing right now? (Filipino students, craftsmen, writers). │
├────────────────────────────────────────────────────────────────────────┤
│ 2. PHYSICAL ENVIRONMENT & ARCHITECTURAL SETTING                        │
│    Where is the scene? Room type, wall material, window style, floor.  │
│    (Capiz-shell windows, bamboo dulang, science lab, workshop).        │
├────────────────────────────────────────────────────────────────────────┤
│ 3. 3 TO 4 CONCRETE TANGIBLE PROPS / ARTIFACTS                          │
│    Name physical objects sitting on tables, held in hands, or mounted. │
│    (Mimeograph, mortar and tenon joint, sliding calipers, slides).     │
├────────────────────────────────────────────────────────────────────────┤
│ 4. DIRECTIONAL LIGHTING, ATMOSPHERE & COLOR PALETTE                   │
│    Where does light enter? (Warm golden hour, dappled acacia leaves,   │
│    nostalgic Studio Ghibli amber lantern glow, cool fluorescent lab).  │
├────────────────────────────────────────────────────────────────────────┤
│ 5. DISCIPLINE-CALIBRATED ARTISTIC MEDIUM & CAMERA OPTICS               │
│    - Filipino / English / Values / Covers: Studio Ghibli anime style,  │
│      hand-painted lush watercolor background, soft expressive lines.   │
│    - TLE: Real object sample photography, crisp macro detail, studio.  │
│    - History (AP): Classical museum historical painting, archival oil. │
│    - Science/Math: Macro lab photography, 3D anatomical render.        │
└────────────────────────────────────────────────────────────────────────┘
```

### Parameter Suffix:
Always end with clean negative prompts and aspect ratio:
- **Interior Lesson Prompts**: `no text, no logos, no watermarks, no branding --ar 16:9 --v 6.0`
- **Front Cover Prompts**: `no text, no logos, no watermarks, no branding --ar 8.5:11 --v 6.0`

---

# PART 4: STRICT 10-PROMPT UNIT ALLOCATION QUOTA

To prevent visual clutter and maintain high editorial density:
- **Page 1 (Front Cover)**: Exactly 1 Full-Page Cover AI Prompt Box (`--ar 8.5:11`).
- **Lesson 1**: Exactly 3 Image Prompt Boxes (Subtopic 1, Subtopic 2, Applied Task, `--ar 16:9`).
- **Lesson 2**: Exactly 3 Image Prompt Boxes (Subtopic 1, Subtopic 2, Applied Task, `--ar 16:9`).
- **Lesson 3**: Exactly 3 Image Prompt Boxes (Subtopic 1, Subtopic 2, Applied Task, `--ar 16:9`).
- **Unit Assessment & Back Matter**: Exactly 0 prompts (focused purely on 1–30 MCQ quiz, Performance Task, and Answer Keys).
- **TOTAL UNIT QUOTA**: **EXACTLY 10 IMAGE PROMPTS PER 40+ PAGE UNIT**.

---

# PART 5: MULTI-SUBJECT GOLD-STANDARD BOXED EXEMPLARS

> **CRITICAL PRODUCTION DIRECTIVE:**  
> 1. **BAN DRAFT LABELS:** NEVER write `"Visual Prompt 1"`, `"Visual Prompt 2"`, or `"Prompt 1"`! Use ONLY clean production titles: `🖼️ Larawan: [Mapanuring Pamagat]` or `🖼️ Figure: [Descriptive Title]`.  
> 2. **MANDATORY SINGLE CONTAINER BOX:** The title, pedagogical purpose, AI prompt, and replacement note MUST ALL be enclosed inside ONE single container box (Markdown callout `> ...` or shaded 1-cell table). Never leave loose or unboxed lines outside!

### EXEMPLAR 1: GRADE 8 FILIPINO — GHIBLI / STORYBOOK STYLE
#### (Panitikan sa Panahon ng Hapon: Tagong Palimbagan)

> ### 🖼️ Larawan: Tagong Palimbagan ng Panitikan sa Panahon ng Hapon (1943)
> **Pedagohikal na Layunin:** Magbigay ng madamdaming historikal na konteksto sa lihim na pagsulat ng panitikan sa ilalim ng sensura noong 1943 sa estilong Studio Ghibli.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A warm, evocative, beautifully hand-painted Studio Ghibli anime aesthetic scene set in 1943 Manila during the Japanese occupation. Inside a dimly lit clandestine wooden attic, two Filipino writers—a young man with rolled-up white cotton sleeves and an elder editor wearing round wire spectacles—quietly inspect newly inked mimeograph sheets of wartime Tagalog short stories. On the heavy weathered acacia wood table rests a vintage hand-cranked mimeograph machine, dark ink bottles, stacks of warm brown paper, and a brass kerosene lantern casting a soft golden glow over their determined faces. In the background, wooden shelves stacked with hidden manuscripts, and a window opening to twilight rooftop silhouettes under a deep indigo sky. Lush hand-painted watercolor background art, Hayao Miyazaki pastoral warmth, gentle line art, rich nostalgic atmosphere, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

---

### EXEMPLAR 2: GRADE 7 FILIPINO / ENGLISH — GHIBLI / STORYBOOK STYLE
#### (Pagbigkas ng Tanaga sa Ilalim ng Katutubong Bahay)

> ### 🖼️ Larawan: Pagbigkas ng Katutubong Tula sa Balkonahe ng Bahay Kubo
> **Pedagohikal na Layunin:** Ipakita ang tradisyong oral at kultural na init ng pagpapasa ng panitikan sa nakababatang henerasyon.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A breathtaking Studio Ghibli inspired anime illustration of a peaceful rural afternoon in Bulacan, Philippines. On the polished bamboo-slatted balcony of a traditional bahay kubo, a gentle elderly Filipina grandmother in a floral vintage kimona recites traditional 7-syllable Tanaga verses to two attentive teenage students (a 13-year-old Filipino boy and girl in neat school uniforms). On a low wooden dulang table between them sit a clay tea pot with steaming cups and an open handwritten journal. Golden tropical sunlight filters through sliding capiz-shell window panels, casting intricate diamond light patterns across the floor. In the lush background, wind gently sways emerald banana groves, tall mango trees, and billowy painted cumulus clouds in an azure summer sky. Masterful watercolor anime scenery, Makoto Shinkai and Hayao Miyazaki aesthetic, warm heartfelt emotions, fine hand-drawn details, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

---

### EXEMPLAR 3: GRADE 7 VALUES EDUCATION / GMRC — GHIBLI / STORYBOOK STYLE
#### (Pagpapatawad at Pagkakasundo sa Hardin ng Paaralan)

> ### 🖼️ Larawan: Taos-Pusong Pagkakasundo ng Magkaibigan sa Ilalim ng Puno ng Acacia
> **Pedagohikal na Layunin:** Magbigay ng positibo, makatao, at emosyonal na representasyon ng pagpapatawad at pagtutulungan ng mga kabataan.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A heartwarming, emotionally resonant Studio Ghibli style anime illustration capturing sincere reconciliation between two 13-year-old Filipino Grade 7 students. Seated side-by-side on a rustic wooden bench under a sprawling, canopy-rich acacia tree in a quiet school courtyard, one boy smiles gently while placing a reassuring hand on his friend's shoulder, who looks up with humble relief. Between them, an open sketchbook with colorful drawings rests on their knees. Dappled golden morning sunlight dances through leaves, illuminating floating pollen and warm gentle breezes. Surrounding the courtyard are vibrant potted tropical flowers, blooming yellow kalachuchi, and retro school hallways. Soft hand-painted watercolor textures, heartfelt anime aesthetic, warm nostalgic color palette, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

---

### EXEMPLAR 4: TLE / TVL — STRICT REAL OBJECT SAMPLE EXCEPTION
#### (Woodworking Mortise and Tenon Joint & Workshop Tools)

> ### 🖼️ Figure: Actual Wooden Mortise and Tenon Joint Sample & Hand Tools
> **Pedagogical Purpose:** Ipakita ang aktuwal na estruktura at precision craftsmanship ng mortise and tenon joint para sa gawaing-kahoy.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A crisp, professional real-object product sample photograph of a finely crafted wooden mortise and tenon joint on a heavy carpenter's workbench. The joint is shown partially disassembled, revealing the precise rectangular tenon tongue fitting perfectly into the clean chiseled mortise hole in solid Narra hardwood with rich natural wood grain. Lying neatly beside the wooden joint are real authentic carpentry tools: a vintage steel marking gauge, an oiled hand-chisel with polished wooden handle, a brass sliding caliper, and fresh curly wood shavings scattered on the scarred wooden tabletop. Bright natural daylight from an overhead workshop window, macro commercial tool photography, sharp focus across wood fibers, authentic technical craftsmanship, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

---

### EXEMPLAR 5A: ARALING PANLIPUNAN — REAL HISTORICAL HERO (ARCHIVAL PHOTO FRAME)
#### (Method 1: Authentic Historical Portrait — STRICTLY NO AI GENERATION!)

> ### 🏛️ Larawang Pangkasaysayan: Dr. Jose Rizal (1896 Archival Collection)
> **Pedagohikal na Layunin:** Magpakita ng tunay at hindi gawa-gawang (authentic, non-AI) historikal na larawan ng pambansang bayani bilang paggalang sa kanyang tunay na mukha at kasaysayan.  
> *Paunawa sa Guro/Editor: HUWAG gamitin ang AI para iguhit o gawin ang mukha ni Rizal! I-insert sa Microsoft Word ang opisyal na public-domain archival photograph mula sa Pambansang Komisyong Pangkasaysayan ng Pilipinas (NHCP) o Pambansang Aklatan ng Pilipinas.*  
> **Sanggunian:** National Historical Commission of the Philippines (NHCP) Digital Archival Collection.

---

### EXEMPLAR 5B: ARALING PANLIPUNAN — PRIMARY SOURCE STILL LIFE / POV
#### (Method 2: Atmospheric Historical Reconstruction — Desk, Artifacts, Zero Hero Faces!)

> ### 🖼️ Larawan: Pagsulat ng Noli Me Tangere: Ang Mesa ng Manunulat sa Berlin (1887)
> **Pedagohikal na Layunin:** Ilarawan ang kongkretong atmospera at mga kagamitan sa pagsulat ng Noli Me Tangere sa Berlin nang hindi gumagawa ng pekeng mukha ng bayani.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `An authentic 1887 historical still life and point-of-view scene inside a cold, modest attic room in Berlin, Germany. Focus on a heavy oak writing desk: open handwritten draft manuscripts of "Noli Me Tangere" with neat Spanish cursive script in sepia ink, a dark glass ink bottle, a slender steel dip pen resting on an inkstand, and vintage round wire-rimmed reading spectacles lying beside an unfolded letter addressed to Ferdinand Blumentritt. On the corner of the table sits an antique brass kerosene lamp casting a warm amber pool of light over the paper, alongside a small, half-eaten loaf of dark rye bread. In the background, tall wooden windowpanes with frost patterns overlooking dim European cobblestone streets under a snowy twilight sky. Classical museum oil painting realism, rich canvas textures, dignified historical atmosphere, NO human faces, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

---

### EXEMPLAR 6: GRADE 7 SCIENCE — REAL LABORATORY & MACRO SPECIMEN EXCEPTION
#### (Compound Optical Microscope & Plant Cell Wet-Mount)

> ### 🖼️ Figure: Real Laboratory Microscope & Wet-Mount Slide Examination
> **Pedagogical Purpose:** Ilarawan ang aktuwal na proseso ng paghahanda ng wet-mount slide at paghahambing sa estruktura ng plant cell.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A crisp, professional laboratory scene in a modern Philippine school science laboratory. In the foreground, an authentic compound optical light microscope stands on a clean black chemical-resistant lab counter. Resting beside it on a white ceramic tray are prepared glass slides: one clearly showing a translucent purple-stained Allium cepa (onion epidermal) wet mount with a thin square coverslip, alongside a blue methylene-stained human cheek epithelial smear. A stainless steel dissection needle, a plastic dropper with iodine reagent bottle, and an open student laboratory observation notebook with clean hand-drawn pencil diagrams of hexagonal plant cell walls. Soft directional LED laboratory lighting, macro photography aesthetic, crisp glass reflections, shallow depth of field with blurred classroom background, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

---

### EXEMPLAR 7: GRADE 9 MATHEMATICS — GEOMETRIC & ARCHITECTURAL CURVE EXCEPTION
#### (Parabolic Bridge Cable Suspension Architecture)

> ### 🖼️ Figure: Real-World Parabolic Arch Engineering of Marcelo Fernan Bridge
> **Pedagogical Purpose:** Ipakita ang kongkretong aplikasyon ng quadratic equation at vertex form sa estruktura ng suspension bridge cables.  
> **AI Prompt (Midjourney v6 / DALL-E 3):**  
> `A breathtaking architectural and civil engineering photograph of a major Philippine modern cable-stayed bridge spanning across a calm coastal strait at sunset. The massive steel-reinforced parabolic suspension cables sweep downward in a mathematically perfect quadratic curve, tethered to tall concrete pylons against a luminous twilight sky of amber, violet, and deep indigo. In the foreground, an engineering blueprint clipboard with clean white line drawings of a coordinate Cartesian plane overlaid along the bridge curve, marking the vertex (h, k) and axis of symmetry. Golden hour directional lighting reflecting on the water below, ultra-wide 24mm architectural photography, razor-sharp structural steel details, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0`  
>  
> *Paunawa sa Guro at Mag-aaral: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures).*

---

# PART 6: PRE-GENERATION AUDIT CHECKLIST FOR IMAGE PROMPTS

Before outputting ANY image prompt frame in the textbook, verify that it passes all 8 checkpoints:

- [ ] **Check 1: Clean Production Title Only (BAN "Visual Prompt 1")**: Does it use ONLY `🖼️ Larawan: [Title]` or `🖼️ Figure: [Title]`? Is `"Visual Prompt 1"` or any draft number strictly banned?
- [ ] **Check 2: 100% Inside Dedicated Container Box**: Are the title, purpose, prompt, and note ALL completely enclosed inside the container box (`> ...` in Markdown or 1-cell shaded table in DOCX) with NO loose text outside?
- [ ] **Check 3: Style Calibration**: 
      - Is it **English, Filipino, Values Ed / GMRC, or Book Cover**? -> Must be **Studio Ghibli-inspired warm pastoral anime watercolor illustration**!
      - Is it **TLE / TVL**? -> Must be **real object sample photography / engineering schematics**!
      - Is it **History / AP (real heroes/events)**? -> **STRICT BAN on AI-generating hero faces!** Use Archival Photo Frame (NHCP) OR Primary Source Still-Life / POV (desks, manuscripts, artifacts; NO fake hero faces)!
      - Is it **Science / Math**? -> Must be **macro lab photography, 3D anatomical render, or vector geometry**!
- [ ] **Check 4: Zero Meta-Words**: Does it completely avoid words like *"infographic"*, *"illustrating the concept"*, *"showing textual analysis"*, or *"central concept"*?
- [ ] **Check 5: Physical People & Action**: Are the subjects physically described with specific postures, hands, or eye focus?
- [ ] **Check 6: Concrete Physical Setting**: Is the room, building, landscape, or environment explicitly named?
- [ ] **Check 7: 3 to 4 Tangible Artifacts/Props**: Are there real physical objects mentioned (mimeograph, dulang, joint, tools, microscope, slides)?
- [ ] **Check 8: Strict Zero Branding & Proper Parameters**: Are all brand acronyms (`DepEd`, `MATATAG`) completely omitted, and does it end with `--ar 16:9 --v 6.0` (or `--ar 8.5:11` for covers)?
