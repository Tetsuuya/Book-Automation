# -*- coding: utf-8 -*-
"""Aralin 8 Builder: Pages 16 to 27 (12 Full Pages)"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from generate_expanded_ebook import (
    format_paragraph, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_prompt_box, add_callout_box, add_custom_table,
    add_multimedia_box, set_cell_shading
)

def build_aralin8(doc):
    # =========================================================================
    # PAHINA 16: PANIMULA, LAYUNIN, AT MULTIMEDIA CORNER #3
    # =========================================================================
    add_heading_1(doc, "ARALIN 8: Kuwento ng Pinagmulan, Linaw ng Pagpapaliwanag")
    add_heading_2(doc, "MGA LAYUNIN AT BALANGKAS NG PAGKATUTO")
    add_body_p(
        doc,
        "Ang Aralin 8 ay nakatuon sa dalawang magkaiba ngunit magkaugnay na daigdig ng pagpapaliwanag: ang Alamat (bilang katutubong malikhaing paliwanag ng ating mga ninuno) at ang Tekstong Ekspositori (bilang siyentipiko at faktuwal na paraan ng pagpapaliwanag sa makabagong panahon). Sa araling ito, tutuklasin ng mag-aaral kung paano ginamit ng ating mga ninuno ang panitikan upang sagutin ang mga hiwaga ng kalikasan, at kung paano naman ginagamit ng modernong manunulat ang faktuwal na pagsusuri ng sanggunian upang puksain ang disimpormasyon o fake news. Lilinangin din ang kasanayan sa Kohesiyong Gramatikal—partikular ang Anapora at Katapora—upang maging malinaw, maayos, at walang kalituhan ang paghabi ng mga talata."
    )

    add_body_p(
        doc,
        "1. F7PN-IIb-4: Naipaliliwanag ang tema, motibo, at kultural na kahulugan ng mga alamat bilang salamin ng katutubong karunungan at ekolohikal na pamumuhay.\n"
        "2. F7PB-IIb-5: Nakikilatis ang kredibilidad, motibo, at faktuwal na batayan ng mga sangguniang ginagamit sa tekstong ekspositori laban sa mga gawa-gawang impormasyon.\n"
        "3. F7PT-IIb-6: Natutukoy ang kahulugan ng mga matatalinghagang salita at kultural na termino sa alamat.\n"
        "4. F7WG-IIb-7: Nagagamit nang wasto ang mga kohesiyong gramatikal (anapora at katapora) upang maiwasan ang paulit-ulit na pagbanggit sa mga pangngalan at mapanatili ang kaisahan ng talata.",
        bold_prefix="Mga Kasanayang Pampagkatuto (MATATAG Competencies):\n"
    )

    add_body_p(
        doc,
        "• Paano sumasalamin ang mga alamat sa paraan ng pakikipag-ugnayan ng ating mga ninuno sa kalikasan at sa Dakilang Lumikha?\n"
        "• Ano ang malaking pagkakaiba ng 'katutubong paniniwala' sa 'modernong disimpormasyon/fake news'?\n"
        "• Paano nakatutulong ang wastong paggamit ng anapora at katapora upang maiwasan ang nakasasawang pag-uulit sa pagsulat ng sanaysay?",
        bold_prefix="Mga Susing Katanungan para sa Aralin:\n"
    )

    add_multimedia_box(
        doc,
        mod_title="Alamat at Katutubong Karunungan ng Pilipinas",
        vid_title="Mga Alamat at Mito ng Pilipinas: Pagsusuri sa Sinaunang Pananaw ng Ating mga Ninuno",
        channel="National Commission for Culture and the Arts (NCCA) / DepEd TV",
        link="https://www.youtube.com/watch?v=MATATAG_Fil7_Aralin8_Alamat",
        qr_code_text="QR-FIL7-ARALIN8-MOD3",
        timestamps=[
            "01:00 - 04:15: Ang Alamat bilang Katutubong Agham at Teolohiya ng Sinaunang Pilipino.",
            "04:16 - 08:30: Ekolohikal na Kamalayan at Pagtatanggol sa Kalikasan sa mga Alamat.",
            "08:31 - 12:45: Paano Suriin ang Alamat gamit ang Modernong Lente ng Antropolohiya."
        ],
        questions=[
            "Ayon sa dokumentaryo, bakit hindi dapat ituring na 'kasinungalingan' ang mga alamat kundi isang anyo ng sinaunang katutubong karunungan?",
            "Anong mga elemento sa video ang nagpapatunay na ang ating mga ninuno ay may mataas na paggalang sa kabundukan, ilog, at kagubatan?",
            "Kung ikaw ay susulat ng isang bagong alamat tungkol sa pinagmulan ng isang modernong bagay (hal. smartphone o internet), anong pagpapahalagang moral ang iyong isasama?"
        ]
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 17: PAKSA 8.1 - ANG ALAMAT BILANG TULUYANG ETNOGRAPIKO
    # =========================================================================
    add_heading_2(doc, "Paksa 8.1: Ang Alamat Bilang Panitikang Tuluyan at Malikhaing Paliwanag")
    add_body_p(
        doc,
        "Bago pa man naging laganap ang mga aklat-pampaaralan sa agham at heolohiya, ang ating mga ninuno ay nagkaroon na ng masidhing pagnanais na ipaliwanag ang mundo sa kanilang paligid. Bakit pumuputok ang bulkang Mayon? Saan nanggaling ang tamis ng lansones? Bakit lumuluha ang langit sa anyo ng ulan? Ang sagot ng ating mga ninuno sa mga tanong na ito ay nasa anyo ng Alamat (Legend)."
    )
    add_body_p(
        doc,
        "Ang alamat ay isang uri ng panitikang tuluyan na nagsasalaysay sa pinagmulan ng mga bagay-bagay, lugar, hayop, halaman, o pangalan sa daigdig. Bagamat nagtataglay ito ng mga mahiwagang elemento, kababalaghan, at di-pangkaraniwang kapangyarihan, ang alamat ay hindi simpleng kuwentong pambata. Sa larangan ng etnograpiya at antropolohiya, ang alamat ay itinuturing na salamin ng 'katutubong epistemolohiya'—ang natatanging paraan ng isang kultura sa pagbuo ng kaalaman at pagpapaliwanag sa katotohanan."
    )
    add_body_p(
        doc,
        "1. May Elemento ng Hiwaga o Mahika: Naglalaman ng mga diwata, anito, engkanto, o kapangyarihang nagpapabago sa pisikal na kalagayan ng tao o kalikasan.\n"
        "2. Nakaangkla sa Moralidad at Kultural na Kodigo: Ang mga tauhan ay madalas na pinarurusahan dahil sa kasakiman, kataksilan, o paglapastangan sa kalikasan, o ginagantimpalaan dahil sa kababaang-loob at katapangan.\n"
        "3. Nag-iiwan ng Ekolohikal na Aral: Ang mga sinaunang alamat ng Pilipinas ay nagtuturo na ang tao ay hindi panginoon ng kalikasan kundi bahagi lamang nito.",
        bold_prefix="Tatlong Katangian ng Katutubong Alamat:\n"
    )

    prompt_p17 = (
        "PROMPT: A mystical and reverent editorial concept art of an indigenous Philippine mountain stream at dawn. "
        "A graceful, ethereal nature guardian spirit (diwata) shimmering with soft pearlescent bioluminescence, gently cupping "
        "crystal-clear water in her hands. Around her, sacred giant ferns, rare orchids, and ancient mossy boulders in an untouched "
        "Philippine rainforest. A vibrant kingfisher perches peacefully on a nearby bamboo branch. Golden sunbeams piercing through "
        "the dense canopy fog. High fantasy realism, studio ghibli-level emotional depth mixed with Unreal Engine 5 cinematic rendering, "
        "rich emerald and gold tones, authentic pre-colonial Philippine aesthetics --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "PROMPT SA PAGBUO NG LARAWAN: ANG DIWATA NG BATIS AT KALIKASAN", prompt_p17)

    add_body_p(
        doc,
        "Sa pag-aaral ng alamat sa ilalim ng MATATAG Kurikulum, mahalagang kilalanin ang mga arketipo (archetypes)—mga unibersal na huwaran ng tauhan at simbolo tulad ng 'Matiyagang Anak,' 'Mapanirang Dayo,' at 'Banal na Batis.' Sa pamamagitan ng pagsusuri sa mga ito, natututuhan nating pahalagahan ang karunungang-bayan ng ating mga ninuno na nagpapanatili ng balanse sa kalikasan bago pa man naimbento ang konsepto ng climate change."
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 18: ALAMAT-LUNSARAN - SI TALA SA TABI NG BATIS
    # =========================================================================
    add_heading_2(doc, "Akdang Pampanitikan para sa Aralin 8: Alamat-Lunsaran")
    add_heading_3(doc, "SI TALA AT ANG HIWAGA SA TABI NG BATIS (Alamat ng Nayon)")
    add_body_p(
        doc,
        "Noong unang panahon sa paanan ng Bundok Halcon, may isang munting pamayanan ng mga katutubong naninirahan nang payapa sa tabi ng Batis ng Liwayway. Ang batis na ito ang buhay ng buong nayon; doon sila umiinom, nangingisda ng maliliit na paitan, at nagdidilig ng kanilang mga tanim na palay at gabi. Pinaniniwalaan ng mga katutubo na ang batis ay binabantayan ng isang maamong diwata na siyang nagpapanatili ng linaw ng tubig hangga't may isang taong may busilak na puso na nag-aalaga rito.",
        italic_prefix="Panimula: "
    )
    add_body_p(
        doc,
        "Si Tala ay isang dalagitang kilala sa kaniyang pambihirang malasakit sa kalikasan. Araw-araw, bago sumikat ang araw, nagtutungo siya sa batis upang linisin ang mga nalaglag na dahon at kausapin ang mga ibon. May pambihira siyang tinig na kapag narinig ng mga hayop ay nagpapatigil maging sa mababangis na baboy-ramo. Ipinagbilin ng kaniyang ina na si Aling Dalia: 'Tala, ang tubig ay hindi pag-aari ng tao. Ito ay hiram lamang natin sa langit, kaya huwag mong hahayaang dungisan ito ng kasakiman.'"
    )
    add_body_p(
        doc,
        "Subalit dumating ang panahon ng tagtuyot sa buong kapuluan. Natuyo ang mga bukal sa kapatagan, at nagsimulang dagsain ng mga mangangalakal mula sa malalayong bayan ang Batis ng Liwayway. Sa pangunguna ng isang mayamang dayo na nagngangalang Don Saturnino, nagdala sila ng mga malalaking kariton at drum. Nais nilang bakuran ang batis at ibenta ang tubig sa mataas na halaga sa mga uhaw na mamamayan.",
        italic_prefix="Kasukdulan: "
    )
    add_body_p(
        doc,
        "Mariing humarang si Tala sa tabi ng tubig. 'Hindi ninyo maaaring ibenta ang buhay ng nayon! Ang tubig na ito ay biyaya para sa lahat!' Subalit pinagtawanan lamang siya ng mga tauhan ni Don Saturnino. Nang akmang itatapon ng mga mangangalakal ang kanilang mga kemikal upang palayasin ang mga isda at mas mabilis na maipon ang tubig, tumalon si Tala sa gitna ng batis at lumuhod sa lumot na bato habang umaawit ng sinaunang panalangin sa diwata."
    )
    add_body_p(
        doc,
        "Biglang kumulog sa kalawakan kahit walang ulap. Ang malinaw na tubig ng batis ay nagliwanag na parang natutunaw na pilak. Sa isang kisapmata, naglaho ang katawan ni Tala at sa kaniyang kinatatayuan ay sumibol ang isang pambihirang halamang-tubig na may puting bulaklak na kumikinang tuwing gabi—ang halamang 'Tala-Batis.' Ang mga sakim na mangangalakal ay nabulag sa liwanag at kumaripas ng takbo palayo sa nayon.",
        italic_prefix="Kakalasan at Wakas: "
    )
    add_body_p(
        doc,
        "Mula noon, hindi na muling natuyo ang batis. Tuwing dapit-hapon, ang mga bulaklak ng Tala-Batis ay naglalabas ng halimuyak na nagpapaalala sa mga taganayon sa sakripisyo ng isang dalagang nagtanggol sa kanilang pamana. Naging tradisyon na sa nayon na bago kumuha ng tubig ay mag-iwan ng bulaklak at magpasalamat kay Tala.",
        italic_prefix="Aral Kultural: "
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 19: MAPANURING PAGSUSURI AT SOCRATIC SEMINAR SA ALAMAT
    # =========================================================================
    add_heading_2(doc, "Mapanuring Pagsusuri at Socratic Seminar sa Alamat")
    add_body_p(
        doc,
        "Suriin ang transkripsiyon ng talakayan sa pagitan ng Guro at mga mag-aaral upang makita ang mas malalim na kahulugan ng Alamat ni Tala:"
    )

    add_body_p(
        doc,
        "Guro: Sa unang tingin, ang 'Alamat ni Tala' ay isang kuwentong puno ng hiwaga. Ngunit kung susuriin natin ito gamit ang kontekstong sosyo-kultural at ekolohikal, ano ang sinasabi nito tungkol sa ugnayan ng tao at likas-yaman?",
        bold_prefix="Guro: "
    )
    add_body_p(
        doc,
        "Bea (Mag-aaral): Ipinakikita po nito ang tunggalian sa pagitan ng 'komunal na pagmamay-ari' at 'komersyalisasyon.' Para sa mga katutubo, ang batis ay buhay na biyayang ibinabahagi sa lahat nang libre. Ngunit para kay Don Saturnino, ang krisis ng tagtuyot ay isang oportunidad upang magkamal ng salapi sa pamamagitan ng pagbebenta ng batayang pangangailangan.",
        bold_prefix="Bea (Mag-aaral): "
    )
    add_body_p(
        doc,
        "Guro: Napakahusay, Bea! Carlo, ano naman ang sinisimbolo ng pagbabagong-anyo (metamorphosis) ni Tala bilang isang kumikinang na bulaklak sa batis?",
        bold_prefix="Guro: "
    )
    add_body_p(
        doc,
        "Carlo (Mag-aaral): Ang pagbabagong-anyo po ay hindi literal na kamatayan kundi imortalidad sa kamalayan ng nayon. Ipinahihiwatig nito na ang sinumang nagtatanggol sa kalikasan ay nagiging bahagi ng mismong kalikasan. Ang kaniyang alaala ay nagiging moral na paalala sa mga susunod na henerasyon na huwag maging sakim.",
        bold_prefix="Carlo (Mag-aaral): "
    )
    add_body_p(
        doc,
        "Guro: Napakagandang interpretasyon. Ngayon, ilapat natin ito sa ating kasalukuyang panahon: Paano natin maiuugnay si Tala sa mga modernong environmental defenders at indigenous youth leaders ngayon?",
        bold_prefix="Guro: "
    )
    add_body_p(
        doc,
        "Bea: Tulad po ni Tala, marami tayong mga kababayang katutubo ngayon na buong-tapang na humaharang sa mga ilegal na pagmimina, deforestation, at mapanirang dam upang mapanatili ang kalinisan ng ating mga kabundukan at ilog.",
        bold_prefix="Bea: "
    )

    add_callout_box(
        doc,
        title="BOKABULARYONG PAMPANITIKAN AT KULTURAL (TALASALITAAN)",
        body_lines=[
            "• Epistemolohiya: Ang sangay ng pilosopiya na nag-aaral sa pinagmulan, kalikasan, at limitasyon ng kaalaman ng tao.",
            "• Arketipo (Archetype): Isang pangkalahatang modelo ng tauhan, simbolo, o tema na paulit-ulit na lumilitaw sa mga panitikan ng iba't ibang kultura sa daigdig.",
            "• Metamorphosis: Ang hiwaga ng pagbabago ng pisikal na anyo (hal. mula sa tao patungo sa halaman o hayop) sa mga mitolohiya at alamat bilang simbolismo ng espiritwal na paglipat."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 20: PAKSA 8.2 (BAHAGI 1) - TEKSTONG EKSPOSITORI AT FAKTUWAL NA PALIWANAG
    # =========================================================================
    add_heading_2(doc, "Paksa 8.2: Tekstong Ekspositori at Faktuwal na Paliwanag (Bahagi 1)")
    add_body_p(
        doc,
        "Kung ang alamat ay gumagamit ng imahinasyon at hiwaga upang magpaliwanag, ang Tekstong Ekspositori naman ay gumagamit ng katotohanan, lohika, at siyentipikong ebidensiya. Ang tekstong ekspositori ay isang anyo ng diskursong naglalayong magpaliwanag at maglahad ng mga impormasyon, konsepto, at proseso sa paraang malinaw, tumpak, at walang kinikilingan."
    )

    add_body_p(
        doc,
        "1. Kahulugan at Klasipikasyon (Definition and Classification): Ipinapaliwanag ang kahulugan ng isang termino at hinahati ito sa mga kategorya o grupo batay sa tiyak na katangian.\n"
        "2. Sanhi at Bunga (Cause and Effect): Sinusuri ang mga dahilan kung bakit naganap ang isang pangyayari at ang mga naging direktang epekto nito sa tao o kapaligiran.\n"
        "3. Paghahambing at Pagkakaiba (Comparison and Contrast): Inilalatag ang mga pagkakatulad at pagkakaiba ng dalawa o higit pang ideya o konsepto upang makabuo ng mas matalinong pagsusuri.\n"
        "4. Proseso o Hakbang-hakbang na Pagpapaliwanag (Sequential / Process): Isinasaad ang sunod-sunod na yugto kung paano ginagawa ang isang bagay o paano nagaganap ang isang natural na penomenon.",
        bold_prefix="Apat na Karaniwang Huwaran ng Tekstong Ekspositori:\n"
    )

    expo_headers = ["Elemento ng Tekstong Ekspositori", "Pangunahing Pamantayan", "Layunin sa Pagkatuto ng Mag-aaral"]
    expo_data = [
        ["Tono at Pananaw", "Obhetibo, impersonal, pormal, at walang bahid ng emosyonal na bias.", "Masubaybayan ang purong datos nang walang manipulasyon."],
        ["Estruktura ng Talata", "May malinaw na introduksiyon, paksang pangungusap, katawan, at konklusyon.", "Maihatid ang komplikadong ideya sa madaling maunawaang anyo."],
        ["Batayang Datos", "Nakasandig sa napatunayang pananaliksik, eksperimento, o opisyal na ulat.", "Matiyak ang kredibilidad at kaligtasan ng impormasyon."]
    ]
    add_custom_table(doc, expo_headers, expo_data, col_widths=[2.0, 2.5, 2.0])

    add_body_p(
        doc,
        "Sa pagsulat ng faktuwal na paliwanag, hindi maaaring sabihin ng manunulat na 'marami ang nagsasabi' o 'narinig ko sa kapitbahay.' Kinakailangang tiyak ang pinagmulan ng impormasyon. Dito pumapasok ang kasanayan sa Media and Information Literacy (MIL) na ating tatalakayin sa susunod na bahagi."
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 21: PAKSA 8.2 (BAHAGI 2) - MEDIA AND INFORMATION LITERACY (MIL)
    # =========================================================================
    add_heading_2(doc, "Paksa 8.2: Media & Information Literacy: Pagsusuri ng Sanggunian (Bahagi 2)")
    add_body_p(
        doc,
        "Sa kasalukuyang digital na panahon, ang pinakamalaking hamon sa mga mag-aaral ay hindi ang kakulangan ng impormasyon, kundi ang labis-labis na pagbaha ng impormasyon (infodemic). Maraming kumakalat na 'disinformation' (sinasadyang maling impormasyon upang manlinlang) at 'misinformation' (maling impormasyon na ipinapasa nang walang masamang intensiyon)."
    )

    add_body_p(
        doc,
        "Upang maging matatag at mapanuri, ginagamit natin ang 'CRAAP Test' (isina-Filipino bilang Pagsusuring KOPAL: Kasariwaan, Otoridad, Paninindigan, Katumpakan, Layunin):",
        bold_prefix="Ang Pamantayang KOPAL sa Pagkilatis ng Sanggunian:\n"
    )

    craap_headers = ["Pamantayan", "Kritikal na Tanong na Dapat Sagutin", "Indikasyon ng Maaasahang Sanggunian"]
    craap_data = [
        [
            "Kasariwaan\n(Currency)",
            "Kailan inilathala o huling binago ang impormasyon? Napapanahon pa ba ito para sa paksa?",
            "May malinaw na petsa ng publikasyon; gumagamit ng pinakabagong estadistika."
        ],
        [
            "Otoridad\n(Authority)",
            "Sino ang sumulat o naglathala? May sapat ba siyang kredensiyal, edukasyon, o karanasan?",
            "May pangalan ng lehitimong may-akda, institusyon (DepEd, DOST, UP), o peer-reviewed journal."
        ],
        [
            "Paninindigan at Layunin\n(Purpose / Bias)",
            "Ano ang motibo ng teksto? Ito ba ay magturo, magbenta ng produkto, o mang-impluwensiya sa eleksiyon?",
            "Walang agresibong pop-up ads; hindi nagtatangkang maghasik ng galit o takot."
        ],
        [
            "Katumpakan\n(Accuracy)",
            "Saan kinuha ang mga datos? May binanggit bang sanggunian? Mave-verify ba ito sa ibang lehitimong website?",
            "May talaan ng talasanggunian (references), gumagamit ng opisyal na `.gov` o `.edu` domain."
        ]
    ]
    add_custom_table(doc, craap_headers, craap_data, col_widths=[1.8, 2.5, 2.2])

    add_callout_box(
        doc,
        title="PAALALA LABAN SA DISIMPORMASYON (RED FLAGS)",
        body_lines=[
            "🚩 Clickbait na Titulo: 'HINDI MO PAPANIWALAAN ANG GINAWA NI...' (Kadalasan ay gawa-gawa lamang).",
            "🚩 Walang Pangalan ng Awtor: Kung walang nangangahas umako ng pananagutan sa artikulo, magduda kaagad.",
            "🚩 Emosyonal at Mapanindak na Wika: Ang faktuwal na artikulo ay mahinahon at naglalahad ng datos, hindi nanggagalaiti."
        ],
        color_fill="FFF5F5",
        border_color="CC0000"
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 22: MULTIMEDIA CORNER #4 AT CASE STUDY SA MIL
    # =========================================================================
    add_heading_2(doc, "Multimedia Corner #4: Mapanuring Pagkilatis sa Sanggunian")
    
    add_multimedia_box(
        doc,
        mod_title="Fact-Checking at Pagsugpo sa Fake News sa Pilipinas",
        vid_title="Mapanuring Netizen: Paano Kumilatis ng Katotohanan laban sa Disimpormasyon Online",
        channel="DepEd Information and Communications Technology / PTV Special",
        link="https://www.youtube.com/watch?v=MATATAG_Fil7_Aralin8_FactCheck",
        qr_code_text="QR-FIL7-ARALIN8-MOD4",
        timestamps=[
            "00:50 - 03:30: Ang Anatomya ng isang Fake News Post sa Facebook at TikTok.",
            "03:31 - 07:15: Paggamit ng Reverse Image Search at Pag-verify sa Opisyal na Website ng Gobyerno.",
            "07:16 - 11:00: Responsableng Pagbabahagi: 'Think Before You Click' bilang Tungkulin ng Kabataan."
        ],
        questions=[
            "Ano ang tatlong pangunahing teknik na itinuro sa bidyo upang malaman kung ang isang litrato ay recycled o gawa-gawa lamang?",
            "Bakit sinabi ng tagapagsalita na ang 'mabilisang pag-like at pag-share' ang nagpapakalat ng kasinungalingan?",
            "Pumili ng isang viral post kamakailan sa inyong komunidad at suriin ito gamit ang pamantayang KOPAL."
        ]
    )

    add_heading_3(doc, "Kaso ng Pagsusuri (Case Study): Ang Viral na Post tungkol sa Batis")
    add_body_p(
        doc,
        "Senaryo: Isang viral post sa isang hindi beripikadong Facebook Page ang nag-post ng larawan ng isang tuyong ilog na may sumusunod na caption: 'NAKU PO! ANG BATIS NG LIWAYWAY AY SINIRA NA RAW NG MGA TAGA-MAY-AKDA NG DAM! UBOS NA ANG TUBIG! MAG-REPOST NGAYON DIN KUNG MAHAL MO ANG BAYAN!'"
    )
    add_body_p(
        doc,
        "Mapanuring Pagsusuri gamit ang KOPAL:\n"
        "1. Pagsusuri sa Larawan (Reverse Image Search): Napatunayan na ang larawan ng tuyong ilog ay kinuha sa ibang bansa noong 2018 at hindi sa Batis ng Liwayway.\n"
        "2. Pagsusuri sa Otoridad: Ang Facebook Page ay walang opisyal na contact number, walang rehistro sa DTI o SEC, at puro online games ang mga dating post.\n"
        "3. Pagsusuri sa Katotohanan: Ayon sa pinakahuling ulat ng Municipal Environment and Natural Resources Office (MENRO) kahapon, normal at ligtas ang lebel ng tubig sa batis.\n"
        "Konklusyon: Ang viral post ay isang malinaw na kaso ng Disimpormasyon na naglalayong maghasik ng takot at maghakot ng likes at shares (engagement farming)."
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 23: PAKSA 8.3 (BAHAGI 1) - KOHESIYONG GRAMATIKAL: ANAPORA AT KATAPORA
    # =========================================================================
    add_heading_2(doc, "Paksa 8.3: Kohesiyong Gramatikal: Anapora at Katapora (Bahagi 1)")
    add_body_p(
        doc,
        "Ang isang mabisang manunulat ay marunong maghabi ng mga pangungusap nang hindi paulit-ulit ang mga salita. Upang maiwasan ang nakasasawang pagbanggit sa mga pangngalan (noun repetition) at gawing makinis ang daloy ng diskurso, ginagamit natin ang 'Kohesiyong Gramatikal' sa anyo ng 'Reperensiya' (Reference)."
    )

    add_body_p(
        doc,
        "Sa Filipino, may dalawang pangunahing uri ng reperensiya batay sa posisyon ng panghalip (pronoun) at ng pangngalang kinakatawan nito:",
        bold_prefix="Dalawang Uri ng Reperensiya:\n"
    )

    add_body_p(
        doc,
        "Ito ang reperensiya kung saan ang pangngalan (referent) ay nauunang binanggit sa pangungusap o talata, bago sundan ng panghalip na kumakatawan dito. Ang salitang 'ana' ay nagmula sa Griyego na nangangahulugang 'pabalik' (looking backward).\n"
        "• Pormula: Pangngalan (Nauuna) ➔ Panghalip (Sumusunod pabalik)\n"
        "• Halimbawa 1: Si Tala ay huwarang dalaga sa nayon; siya ang nagtanggol sa kalinisan ng batis.\n"
        "  (Paliwanag: Ang pangngalang 'Si Tala' ang nauna, at kinatawan ito ng panghalip na 'siya' sa kabilang sugnay).\n"
        "• Halimbawa 2: Ang Batis ng Liwayway ay pinagmumulan ng inuming tubig; ito ay pinangangalagaan ng buong pamayanan.",
        bold_prefix="1. Anapora (Anaphoric Reference):\n"
    )

    add_body_p(
        doc,
        "Ito ang reperensiya kung saan ang panghalip ay nauunang ginamit sa simula ng pangungusap o talata bilang pahiwatig, bago tuluyang banggitin ang tiyak na pangngalan sa dakong huli. Ang salitang 'kata' ay nangangahulugang 'pasulong' (looking forward). Ginagamit ito sa retorika upang lumikha ng pananabik o pagbibigay-diin.\n"
        "• Pormula: Panghalip (Nauuna pasulong) ➔ Pangngalan (Sumusunod na tinutukoy)\n"
        "• Halimbawa 1: Buong-tapang siyang humarap sa mga dambuhalang bulldozer; si Sinta ay hindi natinag sa kaniyang paninindigan.\n"
        "  (Paliwanag: Ang panghalip na 'siyang' ang unang lumitaw, bago ipinahayag ang pangngalang 'si Sinta').\n"
        "• Halimbawa 2: Kahit luma na ito, ang liwasan ng bayan ay nananatiling puso ng ating kasaysayan.",
        bold_prefix="2. Katapora (Cataphoric Reference):\n"
    )

    kohesyon_headers = ["Uri ng Reperensiya", "Direksiyon ng Pagtukoy", "Halimbawang Retorikal sa Talata"]
    kohesyon_data = [
        [
            "Anapora",
            "Pabalik (Backward-looking)\n[Pangngalan ➔ Panghalip]",
            "Ang mga katutubong Dumagat ay may malalim na karunungan; nararapat lamang silang pakinggan ng pamahalaan."
        ],
        [
            "Katapora",
            "Pasulong (Forward-looking)\n[Panghalip ➔ Pangngalan]",
            "Dahil sa kanilang malasakit, ang mga nakatatanda sa nayon ay pinarangalan ng komunidad."
        ]
    ]
    add_custom_table(doc, kohesyon_headers, kohesyon_data, col_widths=[1.8, 2.2, 2.5])

    doc.add_page_break()

    # =========================================================================
    # PAHINA 24: PAKSA 8.3 (BAHAGI 2) - ESTILO AT PAG-IWAS SA REDUNDANCY
    # =========================================================================
    add_heading_2(doc, "Paksa 8.3: Estilo ng Pagsulat at Pag-iwas sa Redundancy (Bahagi 2)")
    add_body_p(
        doc,
        "Bakit napakahalaga ng anapora at katapora sa pagsulat ng tekstong ekspositori? Isa sa pinakakaraniwang kahinaan ng mga baguhang manunulat ay ang tinatawag na 'redundancy' o ang paulit-ulit na pagbanggit sa iisang pangngalan sa bawat pangungusap. Nagdudulot ito ng kabagutan sa mambabasa at nagpapakita ng limitadong bokabularyo."
    )

    add_body_p(
        doc,
        "Paghambingin ang dalawang bersiyon ng talata sa ibaba:",
        bold_prefix="Pagsusuri sa Dalawang Estilo ng Pagsulat:\n"
    )

    add_callout_box(
        doc,
        title="BERSINON A: MAY REDUNDANCY (WALANG KOHESIYONG GRAMATIKAL)",
        body_lines=[
            "Si Lolo Tasio ay nagtungo sa liwasan. Si Lolo Tasio ay may dalang lumang kasulatan. Kinausap ni Lolo Tasio ang mga manggagawa. Sinabi ni Lolo Tasio sa mga manggagawa na ang puno ay sagrado. Nagalit ang mga manggagawa kay Lolo Tasio."
        ],
        color_fill="FFF5F5",
        border_color="CC0000"
    )

    add_callout_box(
        doc,
        title="BERSINON B: MAHUSAY NA PAGKAKAHABI (MAY ANAPORA AT KATAPORA)",
        body_lines=[
            "Nang magtungo si Lolo Tasio sa liwasan, may dala siyang isang lumang kasulatan ng bayan (Anapora). Kinausap niya ang mga manggagawa at buong-hinahong ipinaliwanag na ang punong iyon ay buhay na bantayog ng kasaysayan. Bagamat nagulat sila sa kaniyang paninindigan, ang mga obrero ay napilitang makinig sa kaniyang tinig (Katapora at Anapora)."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    add_heading_3(doc, "Iba Pang Uri ng Kohesiyong Gramatikal:")
    add_body_p(
        doc,
        "1. Substitusyon (Substitution): Paggamit ng ibang salita na may parehong kahulugan upang palitan ang isang sugnay o salita (hal. 'Nawala ang lumang gusali; pinalitan ito ng bagong estruktura').\n"
        "2. Elipsis (Ellipsis): Pagbabawas o pag-aalis ng ilang salita sa pangungusap dahil naiintindihan na ito mula sa konteksto (hal. 'Bumili si Carlo ng libro tungkol sa alamat, at si Sinta naman ay ng magasin' - inalis ang 'bumili').\n"
        "3. Kohesiyong Leksikal (Lexical Cohesion): Paggamit ng magkakaugnay na salita tulad ng kasingkahulugan, kasalungat, o bahagi ng isang kabuuan (hal. puno, ugat, sanga, dahon)."
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 25: GAWAIN 8.1 AT GAWAIN 8.2 (30% ACTIVITY)
    # =========================================================================
    add_heading_2(doc, "Bahaging Gawain at Paglalapat para sa Aralin 8 (30% Activity)")
    
    add_callout_box(
        doc,
        title="Gawain 8.1: Etnograpikong Pagsusuri sa Elementong Alamat",
        body_lines=[
            "Panuto: Balikan ang akdang 'Si Tala at ang Hiwaga sa Tabi ng Batis.' Suriin ang mga elemento nito gamit ang grapikong pantulong sa ibaba. Ipaliwanag kung paano ipinakita sa akda ang katutubong karunungan ng ating mga ninuno.",
            "Pamantayan: Lalim ng Pagsusuri (5 pts), Katumpakan ng Ebidensiya sa Akda (5 pts), Kaayusan ng Wika (5 pts) = 15 Puntos."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    act8_1_headers = ["Bahagi ng Alamat", "Pangyayari sa Akda", "Kultural at Moral na Kahulugan"]
    act8_1_data = [
        ["Tagpuan at Simbolo", "Batis ng Liwayway at Bundok Halcon", "Sinasalamin ang pagsalig ng buhay ng tao sa kalikasan."],
        ["Pangunahing Tauhan", "Si Tala (dalagang may busilak na puso)", "Arketipo ng tagapangalaga ng likas-yaman."],
        ["Tunggalian", "Pagdating ni Don Saturnino at mga drum", "Tunggalian ng komersyalisasyon vs. pamanang pangkomunidad."],
        ["Metamorphosis / Wakas", "Pagiging kumikinang na bulaklak", "Imortalidad ng kabayanihan at ekolohikal na alaala."]
    ]
    add_custom_table(doc, act8_1_headers, act8_1_data, col_widths=[2.0, 2.3, 2.2])

    add_callout_box(
        doc,
        title="Gawain 8.2: Fact-Checking Matrix (Pagkilatis sa Sanggunian)",
        body_lines=[
            "Panuto: Suriin ang tatlong pinagmulang balita sa ibaba tungkol sa isang bagong proyektong pangkalikasan. Gamit ang Pamantayang KOPAL (Kasariwaan, Otoridad, Paninindigan, Katumpakan, Layunin), tukuyin kung Maaasahan (Credible) o Hindi Maaasahan (Suspicious) ang bawat isa. Pangatwiranan ang iyong sagot.",
            "Sanggunian 1: Ulat mula sa opisyal na website ng Department of Environment and Natural Resources (denr.gov.ph) na may petsang kahapon at nilagdaan ng Regional Director.",
            "Sanggunian 2: Isang anonymous blog sa Blogspot na may pamagat na 'MGA LIHIM NA HINDI SINASABI NG GOBYERNO' na puno ng mga babalang 'I-share bago mabura!'",
            "Sanggunian 3: Pananaliksik mula sa isang peer-reviewed journal sa siyensiya na inilathala ng Unibersidad ng Pilipinas noong 2024 na may kumpletong methodology at citations."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 26: GAWAIN 8.3 AT PAGSULAT NG FAKTUWAL NA FACT SHEET
    # =========================================================================
    add_heading_2(doc, "Bahaging Pagsasanay at Paglalapat para sa Aralin 8")
    
    add_callout_box(
        doc,
        title="Gawain 8.3: Siyasat-Panghalip (Pagsasanay sa Anapora at Katapora)",
        body_lines=[
            "Panuto: Tukuyin kung ang sumusunod na mga pangungusap ay nagtataglay ng ANAPORA o KATAPORA. Isulat ang tamang sagot sa patlang, at bilugan ang panghalip at salungguhitan ang pangngalang kinakatawan nito.",
            "1. Si Bb. Santos ay masigasig na nagtuturo ng panitikan; siya ang nagbukas ng isip ng mga mag-aaral sa alamat. (Sagot: ____________)",
            "2. Sa kabila ng kaniyang kahirapan, buong-tapang na nag-aral si Tala upang maipagtanggol ang kaniyang nayon. (Sagot: ____________)",
            "3. Ang Batis ng Liwayway ay patuloy na umaagos; ito ang nagsisilbing saksi sa kadakilaan ng dalaga. (Sagot: ____________)",
            "4. Habang sila ay nagpupulong, ang mga lider-katutubo ay nagkasundo na ipagbawal ang pagpuputol ng kahoy. (Sagot: ____________)",
            "5. Ipinakita ni Juan ang kaniyang galing sa debate; dahil dito, siya ay hinirang na kinatawan ng klase. (Sagot: ____________)"
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    add_heading_3(doc, "Mapanuring Paglalapat: Pagbuo ng Isang 'Environmental Fact-Sheet'")
    add_body_p(
        doc,
        "Magsaliksik tungkol sa isang tunay na ilog, lawa, o kabundukan sa Pilipinas na kasalukuyang nanganganib dahil sa polusyon o iresponsableng pag-unlad (hal. Ilog Pasig, Lawa ng Laguna, o kabundukan ng Sierra Madre). Gumawa ng isang 'One-Page Expository Fact-Sheet' na sumusunod sa sumusunod na balangkas:"
    )
    add_body_p(
        doc,
        "• Pamagat: Faktuwal at Nakapupukaw ng Kamalayan\n"
        "• Bahagi 1: Kahulugan at Kasalukuyang Kalagayan (Sanhi at Bunga gamit ang mga lehitimong datos mula sa gobyerno o unibersidad).\n"
        "• Bahagi 2: Pagsugpo sa Maling Impormasyon (Isang maling paniniwala o tsismis tungkol sa lugar na pinabulaanan ng siyensiya).\n"
        "• Bahagi 3: Panawagan sa Pagkilos (Gamit ang hindi bababa sa tatlong anapora at dalawang katapora)."
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 27: MABILISANG PAGTATAYA SA ARALIN 8 (FORMATIVE ASSESSMENT)
    # =========================================================================
    add_heading_2(doc, "Mabilisang Pagtataya sa Aralin 8 (Formative Assessment)")
    add_body_p(
        doc,
        "Panuto: Basahing mabuti ang bawat tanong. Piliin ang titik ng tamang sagot at isulat ito sa patlang bago ang bilang.",
        bold_prefix="Pangkalahatang Panuto: "
    )

    quiz8_items = [
        ("1. Ano ang pangunahing pagkakaiba ng alamat sa tekstong ekspositori?\n"
         "A. Ang alamat ay purong katotohanan samantalang ang ekspositori ay gawa-gawa.\n"
         "B. Ang alamat ay gumagamit ng hiwaga at naratibo sa pagpapaliwanag samantalang ang ekspositori ay gumagamit ng faktuwal na datos at lohika.\n"
         "C. Walang moral na aral ang alamat samantalang ang ekspositori ay mayroon.\n"
         "D. Ang alamat ay para lamang sa mga bata samantalang ang ekspositori ay para sa matatanda."),

        ("2. Sa pagsusuri ng sinaunang alamat, ano ang ibinubunyag ng konsepto ng 'diwata na nagpaparusa sa sakim'?\n"
         "A. Ang kawalan ng kaalaman ng mga ninuno sa batas trapiko.\n"
         "B. Ang katutubong paniniwala na may pananagutan ang tao sa pagpapanatili ng balanse ng kalikasan.\n"
         "C. Ang pagiging tamad ng mga katutubong magsasaka.\n"
         "D. Ang impluwensiya ng mga pelikula mula sa Hollywood."),

        ("3. Alin sa mga sumusunod ang halimbawa ng Anapora?\n"
         "A. Dahil sa kaniyang sipag, si Tala ay hinangaan ng lahat.\n"
         "B. Si Tala ay masipag na mag-aaral; siya ay palaging nangunguna sa klase.\n"
         "C. Bago pa man dumating ang mga dayuhan, sila ay nagtipon na sa bundok.\n"
         "D. Masarap ang mangga kapag ito ay hinog na sa puno."),

        ("4. Alin sa mga sumusunod ang halimbawa ng Katapora?\n"
         "A. Ang ilog ay malinis; ito ay pinagpapala ng kalikasan.\n"
         "B. Patuloy silang nagtatanim ng bakawan; ang mga kabataan ng nayon ay modelo ng malasakit.\n"
         "C. Si Carlo ay bumili ng bagong aklat tungkol sa kasaysayan.\n"
         "D. Ang Bulkang Mayon ay may perpektong hugis ng apa; hinahangaan ito ng mga dayuhan."),

        ("5. Sa ilalim ng pamantayang KOPAL sa pagsusuri ng balita, ano ang sinusukat ng 'Otoridad'?\n"
         "A. Kung gaano karami ang likes at shares ng isang post.\n"
         "B. Ang kredensiyal, kadalubhasaan, at lehitimong pagkakakilanlan ng sumulat ng artikulo.\n"
         "C. Kung maganda ang kulay ng website at mga larawan nito.\n"
         "D. Kung libreng mabubuksan ang artikulo nang walang internet connection."),

        ("6. Bakit mapanganib ang tinatawag na 'Clickbait Headlines'?\n"
         "A. Dahil nakasisira ito sa screen ng cellphone.\n"
         "B. Dahil madalas itong nagpapalaki o nagbabaluktot ng katotohanan upang makahakot ng clicks lamang.\n"
         "C. Dahil magastos ito sa kuryente.\n"
         "D. Dahil labag ito sa batas ng heograpiya."),

        ("7. Ano ang ibig sabihin ng 'Redundancy' sa pagsulat ng talata?\n"
         "A. Ang paggamit ng iba't ibang bantas sa bawat pangungusap.\n"
         "B. Ang nakasasawang pag-uulit ng iisang pangngalan o ideya nang walang pagbabago.\n"
         "C. Ang pagsulat ng napakagandang pamagat.\n"
         "D. Ang paglalagay ng mga larawan sa gilid ng pahina."),

        ("8. Aling uri ng kohesyon ang nagaganap kapag sadyang inalis ang isang salita dahil madali na itong maunawaan sa daloy ng pangungusap?\n"
         "A. Anapora   B. Katapora   C. Elipsis   D. Substitusyon"),

        ("9. Ano ang naging motibasyon ni Don Saturnino sa kuwentong 'Si Tala sa Tabi ng Batis'?\n"
         "A. Nais niyang magtayo ng libreng paaralan para sa mga bata.\n"
         "B. Nais niyang pagsamantalahan ang tagtuyot upang magbenta ng tubig at magkamal ng tubo.\n"
         "C. Nais niyang sumulat ng aklat tungkol sa mga halaman sa gubat.\n"
         "D. Nais niyang linisin ang batis mula sa mga plastic waste."),

        ("10. Paano nakatutulong ang pagsusuri ng sanggunian sa pagiging responsableng mamamayan?\n"
         "A. Nagiging immune tayo sa lahat ng uri ng sakit.\n"
         "B. Naiiwasan nating maging tagapagpakalat ng kasinungalingan at nagiging matibay ang ating mga desisyong panlipunan.\n"
         "C. Nagiging mas sikat tayo sa mga kaklase.\n"
         "D. Hindi na natin kailangang pumasok sa klase.")
    ]

    for item in quiz8_items:
        add_body_p(doc, item)

    add_callout_box(
        doc,
        title="EXIT TICKET / PAGNINILAY SA ARALIN 8",
        body_lines=[
            "1. Ang pinakamahalagang aral na natutuhan ko tungkol sa pagsusuri ng fake news ay: __________________________",
            "2. Paano ko gagamitin ang anapora at katapora sa aking susunod na sanaysay? _________________________________"
        ],
        color_fill="FAFAFA",
        border_color="CCCCCC"
    )

    doc.add_page_break()
