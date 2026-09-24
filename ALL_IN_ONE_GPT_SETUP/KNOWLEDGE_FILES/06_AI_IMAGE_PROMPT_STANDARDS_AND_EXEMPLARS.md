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

# PART 3: THE 5 MANDATORY CINEMATOGRAPHIC PILLARS

Every single image prompt in the textbook MUST be built upon these **5 concrete physical layers**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      THE 5 VISUAL PROMPT PILLARS                       │
├────────────────────────────────────────────────────────────────────────┤
│ 1. SPECIFIC CHARACTERS & TANGIBLE ACTION                               │
│    Who is physically present? What exact action are their hands and    │
│    eyes performing right now?                                          │
├────────────────────────────────────────────────────────────────────────┤
│ 2. PHYSICAL ENVIRONMENT & ARCHITECTURAL SETTING                        │
│    Where is the scene? Room type, wall material, window style, floor.  │
├────────────────────────────────────────────────────────────────────────┤
│ 3. 3 TO 4 CONCRETE TANGIBLE PROPS / ARTIFACTS                          │
│    Name physical objects sitting on tables, held in hands, or mounted. │
├────────────────────────────────────────────────────────────────────────┤
│ 4. DIRECTIONAL LIGHTING, ATMOSPHERE & COLOR PALETTE                   │
│    Where does light enter? What shadows fall? What are the key tones?  │
├────────────────────────────────────────────────────────────────────────┤
│ 5. CAMERA FRAMING, DEPTH OF FIELD & ARTISTIC MEDIUM                    │
│    Shot type (medium shot, macro close-up), lens bokeh, art style      │
│    (museum archival photography, classical oil painting realism).      │
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

# PART 5: MULTI-SUBJECT GOLD-STANDARD EXEMPLARS

### EXEMPLAR 1: GRADE 8 FILIPINO (Panitikan sa Panahon ng Hapon)

#### Bad / Generic Prompt (DO NOT DO THIS):
`"A publication-grade Grade 8 Filipino infographic illustrating literature during the Japanese period with historical elements --ar 16:9"`

#### Good / Publication-Grade Prompt (DO THIS):
```text
[IMAGE PLACEHOLDER: Tagong Palimbagan ng Panitikan sa Panahon ng Hapon (1943)]
Layunin: Magbigay ng kongkretong historikal na konteksto sa lihim na pagsulat at paglilimbag ng mga maikling kuwento at tula sa gitna ng sensura noong 1943.

AI Prompt: An evocative, dramatic historical scene set in 1943 Manila during the Japanese occupation. Inside a dimly lit clandestine printing cellar, two Filipino writers—a young man in a rolled-up Barong Tagalog and an older editor wearing vintage round wire spectacles—quietly inspect newly inked mimeograph sheets of wartime Tagalog short stories. On the heavy weathered wooden table rests an antique hand-cranked mimeograph machine, dark ink bottles, stacks of rough brown Manila paper, and a pair of brass tweezers. In the background, wooden shelves stacked with hidden manuscripts, and faint moonlight filtering through a high, barred basement grate. Chiaroscuro lighting with warm amber lantern glow illuminating their focused faces, cinematic historical realism, rich atmospheric textures, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0
```

---

### EXEMPLAR 2: GRADE 8 FILIPINO (Pagsusuri sa Tanaga at Katutubong Tula)

#### Good / Publication-Grade Prompt:
```text
[IMAGE PLACEHOLDER: Pagsulat at Pagbigkas ng Tanaga sa Ilalim ng Katutubong Bahay]
Layunin: Ipakita ang tradisyong oral at nakalimbag na anyo ng Tanaga (7-7-7-7 pantig) bilang salamin ng katatagan at talinghaga ng mga karaniwang mamamayan.

AI Prompt: A warm, authentic rural scene in 1940s Bulacan, Philippines. On the wide bamboo-slatted floor of a traditional bahay kubo balcony, an elderly Filipina poet in a simple vintage floral kimona recites traditional 7-syllable Tanaga verses to two attentive teenage students (a 14-year-old Filipino boy and girl in neat cotton daily school attire). On a low wooden dulang table between them lie a handwritten ink diary with neatly lined stanzas, an opened clay palayok cup with native tea, and dried tobacco leaves. Soft tropical morning sunbeams stream through sliding capiz-shell window panels, casting gentle lattice shadows across the polished bamboo slats. Lush banana groves and mango foliage in the background. Masterful watercolor and gouache realism, fine line art, warm earthy tones, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0
```

---

### EXEMPLAR 3: GRADE 7 SCIENCE (Microscopy & Plant vs. Animal Cells)

#### Bad / Generic Prompt (DO NOT DO THIS):
`"An educational infographic showing cell biology and students analyzing cells --ar 16:9"`

#### Good / Publication-Grade Prompt (DO THIS):
```text
[IMAGE PLACEHOLDER: Comparative Laboratory Examination of Onion and Cheek Cells]
Layunin: Ilarawan ang aktuwal na proseso ng paghahanda ng wet-mount slide at paghahambing sa estruktura ng plant cell (may cell wall) laban sa animal cell.

AI Prompt: A crisp, professional laboratory scene in a modern Philippine school science laboratory. In the foreground, an authentic compound optical light microscope stands on a clean black lab counter. Resting beside it on a white ceramic tray are prepared glass slides: one clearly showing a translucent purple-stained Allium cepa (onion epidermal) wet mount with a thin square coverslip, alongside a blue methylene-stained human cheek epithelial smear. A stainless steel dissection needle, a plastic dropper with iodine reagent bottle, and an open student laboratory observation notebook with clean hand-drawn pencil diagrams of hexagonal plant cell walls. Soft directional LED laboratory lighting, macro photography aesthetic, crisp glass reflections, shallow depth of field with blurred classroom background, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0
```

---

### EXEMPLAR 4: GRADE 9 MATHEMATICS (Quadratic Functions & Parabolic Bridge Architecture)

#### Bad / Generic Prompt (DO NOT DO THIS):
`"A mathematical diagram illustrating quadratic functions with real-world context --ar 16:9"`

#### Good / Publication-Grade Prompt (DO THIS):
```text
[IMAGE PLACEHOLDER: Real-World Parabolic Arch Engineering of Marcelo Fernan Bridge]
Layunin: Ipakita ang kongkretong aplikasyon ng quadratic equation at vertex form sa estruktura ng suspension bridge cables at parabolic arch geometry.

AI Prompt: A breathtaking architectural and civil engineering photograph of a major Philippine modern cable-stayed bridge spanning across a calm coastal strait at sunset. The massive steel-reinforced parabolic suspension cables sweep downward in a mathematically perfect quadratic curve, tethered to tall concrete pylons against a luminous twilight sky of amber, violet, and deep indigo. In the foreground, an engineering blueprint clipboard with clean white line drawings of a coordinate Cartesian plane overlaid along the bridge curve, marking the vertex (h, k) and axis of symmetry. Golden hour directional lighting reflecting on the water below, ultra-wide 24mm architectural photography, razor-sharp structural steel details, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0
```

---

### EXEMPLAR 5: GRADE 7 VALUES EDUCATION (Forgiveness & Kapuwa Reconciliation)

#### Bad / Generic Prompt (DO NOT DO THIS):
`"An infographic showing values education and reconciliation concept among teenagers --ar 16:9"`

#### Good / Publication-Grade Prompt (DO THIS):
```text
[IMAGE PLACEHOLDER: Sincere Peer Reconciliation in a School Courtyard]
Layunin: Magbigay ng positibo at makataong representasyon sa pagpapatawad, pagpapakumbaba, at panunumbalik ng tiwala sa pagitan ng magkaibigan.

AI Prompt: A heartwarming, emotionally authentic interaction between two 13-year-old Filipino Grade 7 students (two boys wearing clean, badge-free navy blue and white school uniforms) seated side-by-side on a rustic wooden bench in a quiet school courtyard garden. One student looks down with an expression of honest sincerity and humility, while the other places a reassuring hand on his shoulder with an open, forgiving smile, holding a shared school sketchbook between them. Surrounding them are potted native tropical plants, blooming yellow calachuchi blossoms, and gentle dappled morning sunlight filtering through broad acacia tree branches. Natural candid portrait photography, 85mm portrait lens, creamy soft-focus background bokeh, warm uplifting natural tones, no text, no logos, no watermark, no branding --ar 16:9 --v 6.0
```

---

# PART 6: PRE-GENERATION AUDIT CHECKLIST FOR IMAGE PROMPTS

Before outputting ANY image prompt frame in the textbook, verify that it passes all 5 checkpoints:

- [ ] **Check 1: Zero Meta-Words**: Does it completely avoid words like *"infographic"*, *"illustrating the concept"*, *"showing textual analysis"*, or *"central concept"*?
- [ ] **Check 2: Physical People & Action**: Are the subjects physically described with specific postures, hands, or eye focus?
- [ ] **Check 3: Concrete Physical Setting**: Is the room, building, landscape, or environment explicitly named?
- [ ] **Check 4: 3 to 4 Tangible Artifacts/Props**: Are there real physical objects mentioned (mimeograph, quill, slide, microscope, cables, bench)?
- [ ] **Check 5: Strict Zero Branding & Proper Parameters**: Are all brand acronyms (`DepEd`, `MATATAG`) completely omitted, and does it end with `--ar 16:9 --v 6.0` (or `--ar 8.5:11` for covers)?
