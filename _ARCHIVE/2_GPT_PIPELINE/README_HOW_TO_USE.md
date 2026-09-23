# 🚀 MASTER GUIDE: 2-GPT MATATAG E-BOOK PRODUCTION PIPELINE

Ang sistemang ito ay gumagamit ng **Dalawang Dalubhasang GPT (Two-Agent Pipeline)** upang makabuo ng perpektong aklat sa kahit anong asignatura (Science, Math, MAPEH, TLE, Filipino, AP, English) nang hindi nagkakaroon ng cognitive overload ang AI!

```mermaid
graph LR
    A["TOC + MATATAG Curriculum"] --> B["GPT 1: Content Author"]
    B -->|"Drafted Textbook (70% Lessons / 30% Activities)"| C["GPT 2: Visual & Media Director"]
    C -->|"Final Textbook with Diagrams, Prompts & YouTube"| D["Final Publication-Grade E-Book"]
```

---

## 🛠️ HAKBANG SA PAG-SETUP NG IYONG DALAWANG GPTS

### 1. I-configure ang GPT 1 (Ang Kasalukuyan Mong GPT)
* **Pangalan ng GPT**: `MATATAG Master Textbook Author`
* **Description**: `Nagsusulat ng 40+ pahinang malalim na aralin (70% lesson / 30% activities) batay sa TOC at MATATAG Curriculum nang walang prompt distractions.`
* **Instructions**: Kopyahin ang buong laman ng:
  👉 [**`2_GPT_PIPELINE/GPT1_CONTENT_AUTHOR/INSTRUCTIONS_GPT1.txt`**](file:///c:/Users/Rhenel%20Jhon%20Sajol/Documents/CERE_BOOK/2_GPT_PIPELINE/GPT1_CONTENT_AUTHOR/INSTRUCTIONS_GPT1.txt)
* **Knowledge**: I-upload ang [`g7-filipino-matatag-curriculum-v10 (2).docx`](file:///c:/Users/Rhenel%20Jhon%20Sajol/Documents/CERE_BOOK/g7-filipino-matatag-curriculum-v10%20(2).docx) bilang visual style reference.
* **I-click**: **Save / Update**.

---

### 2. Gumawa ng Bagong GPT para sa GPT 2
* Pumunta sa ChatGPT ➔ **Explore GPTs** ➔ **Create a GPT** ➔ pumunta sa **Configure** tab.
* **Pangalan ng GPT**: `MATATAG Visual & Media Director`
* **Description**: `Eksperto sa paglalagay ng mga AI image prompts, scientific/math diagrams, at interactive YouTube multimedia modules sa kahit anong textbook.`
* **Instructions**: Kopyahin ang buong laman ng:
  👉 [**`2_GPT_PIPELINE/GPT2_VISUAL_MEDIA_DIRECTOR/INSTRUCTIONS_GPT2.txt`**](file:///c:/Users/Rhenel%20Jhon%20Sajol/Documents/CERE_BOOK/2_GPT_PIPELINE/GPT2_VISUAL_MEDIA_DIRECTOR/INSTRUCTIONS_GPT2.txt)
* **I-click**: **Save / Create**.

---

## 🔄 ARAW-ARAW NA DALOY NG TRABAHO (DAILY WORKFLOW)

### Yugto 1: Nilalaman Mula kay GPT 1
1. Buksan si **GPT 1 (Content Author)**.
2. I-upload ang iyong **Table of Contents** at **MATATAG Curriculum Guide** (Science man, Math, MAPEH, TLE, o Filipino).
3. Kapag nagtanong siya kung anong Unit at Aralin, sabihin mo ang nais mong gawin (hal. *"Unit III, Lessons 13 to 16"*).
4. Awtomatikong isusulat ni GPT 1 ang **buo, mahaba, at siksik na 70% aralin at 30% gawain** na may mga malinis na tag tulad ng `[VISUAL PLACEHOLDER]` at `[MULTIMEDIA PLACEHOLDER]`.

### Yugto 2: Pagpapaganda at Multimedia Mula kay GPT 2
1. Kopyahin ang naisulat ni GPT 1.
2. I-paste ito kay **GPT 2 (Visual & Media Director)** at sabihin:
   > *"Narito ang aralin mula kay GPT 1. Lagyan mo ito ng mga detalyadong AI Image/Diagram prompts at interactive YouTube multimedia modules batay sa ating standards."*
3. **Ang Gagawin ni GPT 2**:
   - Maglalagay siya ng **Cover AI Image Prompt** sa Pahina 1.
   - Maglalagay siya ng **Subject-Specific Diagrams** (Cellular/microscopic para sa Science, 3D coordinate graphs para sa Math, technical schematics para sa TLE, traditional instruments para sa MAPEH, o historical scenes para sa Panitikan/AP).
   - Maglalagay siya ng **Curated YouTube Modules** na may maikling video description, timestamps, QR code placeholder, at 2-3 gabay-tanong sa panonood!

---

### Yugto 3: Pinal na Dokumento
I-copy-paste mo lang ang resulta mula kay GPT 2 diretso sa iyong Microsoft Word document (`.docx`). Dahil may mga dashed boxes na ang bawat prompt, **madali mo na lang kopyahin ang mga prompt para i-render sa Midjourney/DALL-E at i-paste pabalik ang mga larawan bago i-print o isumite!**
