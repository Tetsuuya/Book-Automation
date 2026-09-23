# -*- coding: utf-8 -*-
"""Yunit III Assessment, Summary, Glossary, and Answer Keys: Pages 40 to 44 (5 Full Pages)"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from generate_expanded_ebook import (
    format_paragraph, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_callout_box, add_custom_table
)

def build_yunit3_assessment_and_keys(doc):
    # =========================================================================
    # PAHINA 40: PANGWAKAS NA PAGTATAYA SA YUNIT III (BAHAGI I: 10 PUNTOS)
    # =========================================================================
    add_heading_1(doc, "PANGWAKAS NA PAGTATAYA SA YUNIT III (40 PUNTOS)")
    add_heading_2(doc, "Yunit III: Ako at ang Aking Pagkatao, Tanglaw ng Katatagan")
    add_body_p(
        doc,
        "Panimula: Ang komprehensibong pagtatayang ito ay sumusukat sa iyong kritikal na pag-unawa at kasanayan sa pagsusuri ng panitikan sa Panahon ng "
        "Pananakop ng Espanya, tekstong ekspositori at pampahayagan, panghihiram at pagtutumbas ng wika, etika ng panayam, at pagbuo ng multimodal na teksto. "
        "Binubuo ito ng apat na bahagi: (I) Kritikal na Pagsusuri ng Bagong Teksto, (II) Konsepto at Aplikasyon, (III) Estrukturadong Sanaysay, at (IV) Gawaing Pagganap."
    )

    add_heading_3(doc, "Bahagi I: Kritikal na Pagsusuri ng Bagong Teksto / Datos (10 Puntos)")
    add_body_p(doc, "Basahing mabuti ang sumusunod na bagong sipi ng historikal na dokumento at sagutin ang mga sumusunod na katanungan (2 puntos bawat aytem):", italic_prefix="")

    add_callout_box(
        doc,
        "ANG TALA SA SINUPAN NG PAROKYA NG SANTO TOMAS (1888):\n"
        "\"Noong ika-20 ng Nobyembre 1888, dumating sa aming bayan ang isang tanyag na manggagamot mula sa Maynila kasama ang dalawang madre ng kawanggawa. "
        "Ayon sa ulat ng pahayagang kolonyal, ang layunin ng kanilang pagbisita ay upang 'turuan ang mga ignorante at maruruming katutubo ng wastong "
        "pamumuhay upang maiwasan ang sakit na kolera.' Gayunman, sa aktuwal na talaan ng parokya, mababasa na bago pa dumating ang mga taga-Maynila, "
        "ang mga katutubong kababaihan na pinamumunuan ni Kapitana Juana ay nakapagtayo na ng kubol-pagamutan sa tabi ng ilog, nagpapakulo na ng inuming "
        "tubig, at gumagamit ng mga halamang-gamot tulad ng sambong at lagundi upang mapigilan ang pagkalat ng epidemya sa kanilang pamayanan.\""
    )

    p1_items = [
        ("1. Pagkilatis sa Pagkiling: Paano ginamit sa ulat ng pahayagang kolonyal ang mga salitang 'ignorante at marurumi' upang lumikha ng isang may pagkiling na pananaw tungkol sa mga katutubo? (2 pts)",
         "Inaasahang Pagsusuri: Ipinapakita nito ang pananaw ng mananakop na nagpapalagay na walang sariling kaalaman ang mga katutubo at kailangan silang 'iligtas' ng banyagang sibilisasyon."),
        ("2. Pagtatabi ng Datos laban sa Pahayag: Ano ang tiyak na ebidensiya sa talaan ng parokya na sumasalungat sa sinabi ng pahayagang kolonyal? (2 pts)",
         "Inaasahang Pagsusuri: Ang ebidensiya na bago pa dumating ang mga madre ay nakapagtayo na si Kapitana Juana ng kubol-pagamutan at nagpapakulo na ng tubig."),
        ("3. Ahensiya at Katatagan ng Kababaihan: Paano binabasag ng tauhang si Kapitana Juana ang stereotype ng mahina at walang kibo na kababaihan noong panahon ng Espanyol? (2 pts)",
         "Inaasahang Pagsusuri: Ipinamalas niya ang pamumuno, maagap na pagpapasya, kaalamang medikal, at malasakit sa kalusugan ng kaniyang bayan."),
        ("4. Pagsusuri sa Konteksto ng Kalinisan: Iugnay ang ginawa ng mga katutubo sa kaisipan ni Urbana tungkol sa kalinisan bilang paggalang sa kapuwa at kaligtasan ng katawan. (2 pts)",
         "Inaasahang Pagsusuri: Ang pagpapanatili ng kalinisan ay hindi lamang panlabas kundi panlipunang pananagutan upang mapangalagaan ang buhay ng pamayanan."),
        ("5. Mapanuring Katanungan: Kung ikaw ay mamamahayag na kakapanayamin si Kapitana Juana, sumulat ng isang bukas at neutral na tanong na maglalantad sa kaniyang naging karanasan nang walang paghuhusga. (2 pts)",
         "Inaasahang Pagsusuri: Halimbawa: 'Paano po ninyo pinangunahan ang pamayanan sa pagharap sa epidemya bago dumating ang tulong mula sa Maynila?'")
    ]

    for q, ans in p1_items:
        add_body_p(doc, q, bold_prefix="")

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 41: BAHAGI II (KONSEPTO AT WIKA) AT BAHAGI III (SANAYSAY)
    # =========================================================================
    add_heading_2(doc, "PANGWAKAS NA PAGTATAYA: BAHAGI II AT BAHAGI III")
    add_heading_3(doc, "Bahagi II: Konsepto, Wika, at Aplikasyon (10 Puntos)")
    add_body_p(doc, "Panuto: Piliin ang titik ng pinakatumpak na sagot para sa bawat bilang. (1 puntos bawat aytem)")

    p2_mcq = [
        ("1. Ang proseso kung saan ang katutubong talinghaga at damdamin ay patagong isinama sa banyagang anyo ng Pasyon ay tinatawag na—",
         ["A. Reduccion", "B. Sinkretismo at Inkulturasyon", "C. Kolonyal na Sensura", "D. Presentismo"]),
        ("2. Alin ang pinakatamang pagtutumbas sa Filipino ng konseptong administratibo na 'Gobernadorcillo' batay sa konteksto ng bayan?",
         ["A. Munting Gobernador", "B. Punong-bayan / Kapitan del Barrio", "C. Tagasingil ng Buwis", "D. Sundalo ng Pamahalaan"]),
        ("3. Sa panayam para sa balita, bakit itinuturing na depektibo ang tanong na: 'Hindi ba't pabaya ang mga kawani sa paglilinis?'",
         ["A. Dahil masyadong maikli ang tanong.", "B. Dahil nangunguna ito at nagpapataw ng paghusga sa halip na maging neutral.", "C. Dahil bawal magtanong sa kawani.", "D. Dahil gumagamit ng wikang Filipino."]),
        ("4. Alin sa mga sumusunod ang nagpapakita ng responsableng paggamit ng speech balloon sa comic book brochure?",
         ["A. Paglalagay ng buong sanaysay sa loob ng iisang lobo ng diyalogo.", "B. Paggamit ng matipid, wasto sa bantas, at natural na pananalita na angkop sa tauhan.", "C. Pagtakip sa mukha ng tauhan upang makatipid sa espasyo.", "D. Paggamit ng mga modernong balbal sa historikal na tagpo."]),
        ("5. Ang pangunahing aral sa lunsarang 'Urbana at Feliza' tungkol sa kalinisan ay—",
         ["A. Ang kalinisan ay para lamang sa mga maykaya.", "B. Ang kalinisan ng katawan at kaayusan sa pagkilos ay salamin ng kalinisan ng budhi at dangal.", "C. Hindi kailangang mag-aral kung malinis ang kasuotan.", "D. Ang pananamit ang tanging batayan ng kabutihan ng tao."])
    ]

    for q, chs in p2_mcq:
        add_body_p(doc, q, bold_prefix="")
        for c in chs:
            p_c = doc.add_paragraph()
            format_paragraph(p_c, space_before=1, space_after=1)
            p_c.paragraph_format.left_indent = Inches(0.2)
            r_c = p_c.add_run(c)
            r_c.font.name = 'Cambria'
            r_c.font.size = Pt(9.5)

    add_heading_3(doc, "Bahagi III: Estrukturadong Sanaysay at Pagpapalalim (10 Puntos)")
    add_body_p(
        doc,
        "Paksa ng Sanaysay: \"Ang Panitikan bilang Salamin ng Katatagan: Paano Napanatili ng mga Pilipino ang Kanilang Kaakuhan at Dignidad sa Gitna ng Pananakop ng Espanya?\"\n\n"
        "Panuto: Sumulat ng isang organisado, malalim, at makabuluhang sanaysay na binubuo ng 3 talata (200–250 salita). "
        "Dapat gamitin at iugnay sa iyong paliwanag ang hindi bababa sa apat sa sumusunod na mga konsepto:\n"
        "• Kaligirang Pangkasaysayan\n"
        "• Pasyon at Tradisyong Pabasa\n"
        "• Urbana at Feliza (Kagandahang-asal)\n"
        "• Mapanuring Pagsusuri sa Balita at Batis\n"
        "• Etnisidad at Representasyon sa Multimodal na Komiks\n"
        "• Pagtutumbas at Kasarinlan ng Wika"
    )

    headers_rubrik_essay = ["Pamantayan sa Pagmamarka ng Sanaysay", "Laang Puntos", "Deskripsiyon ng Kahusayan"]
    data_rubrik_essay = [
        ["Lalim ng Pagsusuri at Konsepto", "4 Puntos", "Matalas na naipaliwanag ang apat o higit pang konsepto nang may matibay na historikal na batayan."],
        ["Lohika, Organisasyon, at Transisyon", "3 Puntos", "Napakalinaw ng simula, gitna, at wakas; mahusay ang daloy gamit ang mga retorikal na pang-ugnay."],
        ["Wika, Gramatika, at Bantas", "3 Puntos", "Wasto ang baybay, bantas, at pormalidad ng akademikong Filipino nang walang balbal o kamalian."]
    ]
    add_custom_table(doc, headers_rubrik_essay, data_rubrik_essay)

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 42: BAHAGI IV - GAWAING PAGGANAP (GRASPS MODEL AT RUBRIK)
    # =========================================================================
    add_heading_2(doc, "PANGWAKAS NA PAGTATAYA: BAHAGI IV — GAWAING PAGGANAP (10 PUNTOS)")
    add_heading_3(doc, "Autentikong Pagganap: Pinal na Comic Book Brochure gamit ang GRASPS Model")
    
    add_body_p(
        doc,
        "G (Goal / Layunin): Bumuo ng isang 6-panel na pang-edukasyong comic book brochure na naglalarawan sa isang makasaysayang tagpo sa panahon ng "
        "Espanyol na nagtatanghal sa katatagan ng pagkataong Pilipino, pagkakaisa ng komunidad sa kabila ng kolonyal na kontrol, at dignidad ng kababaihan at katutubo.\n\n"
        "R (Role / Papel): Ikaw ay Punong Manunulat, Historikal na Tagasuri, at Tagapagdisenyo ng Multimodal na Nilalaman para sa pampaaralang eksibit.\n\n"
        "A (Audience / Mambabasa): Mga mag-aaral sa Baitang 7, mga guro sa Filipino at Araling Panlipunan, at ang buong pamayanan ng paaralan.\n\n"
        "S (Situation / Sitwasyon): Bilang pagdiriwang ng Buwan ng Kasaysayan at Wika, maglulunsad ang paaralan ng isang eksibit ng mga likhang multimodal. "
        "Kailangang ipakita sa brochure kung paano naging 'tanglaw ng katatagan' ang mga karaniwang mamamayan sa pamamagitan ng kanilang pananampalataya, "
        "kultura, at sariling wika.\n\n"
        "P (Product / Produkto): Isang organisado, malinis, at masining na 6-panel Comic Book Brochure na may: (1) Pamagat at Introduksiyon, "
        "(2) 6 na Kompletong Panel na may Foreground/Background, (3) Speech Balloons na wasto ang diyalogo at bantas, (4) Makabuluhang Caption, at "
        "(5) Maikling Tala sa Batis at Konteksto sa huling bahagi.\n\n"
        "S (Standards / Pamantayan): Mamarkahan ang iyong produkto batay sa sumusunod na analitikong rubrik na may kabuuang 10 puntos."
    )

    headers_grasps_rubrik = ["Pamantayan", "Napakahusay (4)", "Mahusay (3)", "Nalilinang (2)", "Nangangailangan ng Gabay (1)"]
    data_grasps_rubrik = [
        ["Nilalaman at Kontekstong Pangkasaysayan (30%)", "Ganap na tumpak, malalim ang pagkakaugnay sa mga aralin ng Yunit III; malinaw ang kontekstong kolonyal nang walang anachronism.", "Tumpak ang karamihan sa mga detalye; angkop ang tagpo at mensahe sa kasaysayan.", "May ilang kakulangan o malabong historikal na ugnayan sa salaysay.", "Maraming maling impormasyon sa kasaysayan; hindi maunawaan ang konteksto."],
        ["Diyalogo, Wika, at Bantas (25%)", "Napakalinaw, wasto ang gramatika at bantas; natural at angkop ang boses ng bawat tauhan sa speech balloon.", "Wasto at malinaw ang karamihan sa mga diyalogo; may kaunting maliliit na pagkukulang.", "Medyo magulo o artipisyal ang pananalita; may mga kamalian sa bantas.", "Maraming mali sa gramatika at bantas na nakahahadlang sa mensahe."],
        ["Organisasyong Biswal at Multimodal (25%)", "Napakatalas ng ugnayan ng panel, foreground, background, at caption; kumpleto ang daloy ng visual narrative.", "Maayos ang daloy ng mga panel; malinaw ang ugnayan ng larawan at teksto.", "Medyo paulit-ulit ang sinasabi ng teksto sa larawan; kulang sa background.", "Magulo ang pagkakaayos ng mga panel; walang malinaw na ugnayan ang teksto at biswal."],
        ["Etikal na Representasyon at Dignidad (20%)", "Ganap na umiiwas sa stereotype; itinatanghal ang talino, ahensiya, at katatagan ng kababaihan at katutubo.", "Responsable at maingat ang paglalarawan sa mga tauhan.", "May kaunting kababawan o simplistikong paglalarawan sa kahirapan.", "Malinaw na gumagamit ng mapanlait o mapanghusgang stereotype."]
    ]
    add_custom_table(doc, headers_grasps_rubrik, data_grasps_rubrik)

    add_body_p(doc, "Pagmamarka sa Bahagi IV: (Kabuuang Iskor sa Rubrik ÷ 16) × 10 = Puntos sa Bahagi IV", italic_prefix="")

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 43: BUOD NG YUNIT III AT KOMPREHENSIBONG TALATINIGAN
    # =========================================================================
    add_heading_1(doc, "BUOD NG YUNIT III AT KOMPREHENSIBONG TALATINIGAN")
    add_heading_2(doc, "Sintesis ng Pagkatuto: Ako at ang Aking Pagkatao, Tanglaw ng Katatagan")
    add_body_p(
        doc,
        "Ang Yunit III ay nagbigay sa atin ng isang malalim at mapanuring paglalakbay sa panitikan at lipunan noong Panahon ng Pananakop ng Espanya. "
        "Napatunayan natin na ang panitikan ay hindi isang tahimik na saksi lamang ng kasaysayan, kundi isang buháy na larangan kung saan nagtagpo, "
        "nakipagtunggali, at nagtagumpay ang diwa ng mga Pilipino. Sa pamamagitan ng Aralin 13 hanggang 15, naipakita na ang ating wika, pananampalataya, "
        "at kagandahang-asal ay nag-ugat sa isang masalimuot na proseso ng pakikibagay at paninindigan para sa sariling dignidad."
    )

    add_heading_3(doc, "Komprehensibong Talatinigan ng Yunit III (25 Susing Konsepto)")
    
    headers_glossary = ["Termino / Konsepto", "Gumaganang Kahulugan sa Konteksto ng Yunit III"]
    data_glossary = [
        ["Ahensiya (Agency)", "Ang kakayahan ng isang tao o pangkat na magpasya, kumilos, at magkaroon ng impluwensiya sa sariling kapalaran."],
        ["Akdang Pangkagandahang-asal", "Didaktikong panitikan na nagtuturo ng moralidad, wastong kilos, at pakikipagkapuwa (hal. Urbana at Feliza)."],
        ["Akdang Panrelihiyon", "Mga akdang nakasentro sa pananampalatayang Katoliko tulad ng Pasyon, dasal, nobena, at senakulo."],
        ["Anachronism", "Pagkakamali sa paglalagay ng isang bagay, salita, o kaisipan sa panahong hindi pa ito umiiral."],
        ["Balita", "Tekstong impormasyonal at pampahayagan na naglalahad ng mga faktuwal na pangyayari nang patas at tapat."],
        ["Beripikasyon", "Proseso ng pagpapatunay sa katotohanan ng datos gamit ang mapagkakatiwalaang ebidensiya at batis."],
        ["Bukas na Tanong", "Tanong sa panayam na nagbibigay-laya sa kinakapanayam na magpaliwanag at maglahad ng sariling karanasan."],
        ["Comic Book Brochure", "Tekstong multimodal na gumagamit ng mga panel, speech balloon, caption, at biswal para sa tiyak na layunin."],
        ["Doctrina Christiana (1593)", "Ang kauna-unahang aklat na nalimbag sa Pilipinas gamit ang xylographic printing sa Maynila."],
        ["Epistolaryo", "Anyong pampanitikan na binubuo ng palitan ng mga liham sa pagitan ng mga tauhan."],
        ["Etnisidad", "Kultural na pagkakakilanlan ng isang pangkat batay sa wika, tradisyon, pinagmulan, at paniniwala."],
        ["Follow-up Question", "Tanong na sumusunod sa naging sagot ng kinakapanayam upang magpalalim o maglinaw ng impormasyon."],
        ["Foreground", "Ang unahang bahagi ng isang larawan o panel na karaniwang nagbibigay ng pangunahing diin sa tagpo."],
        ["Kaligirang Pangkasaysayan", "Ang kabuuan ng mga kondisyong panlipunan at pampolitika sa panahon ng paglikha ng isang akda."],
        ["Nangungunang Tanong (Leading Question)", "Depektibong tanong sa panayam na naglalaman na ng inaasahang sagot o paghusga ng nagtatanong."],
        ["Pabasa", "Tradisyong panlipunan at panrelihiyon ng sama-samang pag-awit ng Pasyon tuwing Kuwaresma."],
        ["Paglalahad", "Diskurso na naglalayong magpaliwanag at maghatid ng organisado at malinaw na impormasyon."],
        ["Panghihiram", "Pagkuha at pag-aangkop ng salita mula sa banyagang wika alinsunod sa ortograpiyang Filipino."],
        ["Pagtutumbas", "Pagpili ng pinakaangkop na katutubong salita na nagtataglay ng eksaktong kahulugan ng banyagang termino."],
        ["Pasyon", "Naratibong tula tungkol sa buhay, pagpapakasakit, at muling pagkabuhay ni Hesukristo (anyong quintilla)."],
        ["Presentismo", "Mapanirang gawi ng paghuhusga sa nakaraan gamit lamang ang makabagong pamantayan nang walang konteksto."],
        ["Quintilla", "Anyo ng saknong na may 5 taludtod, 8 pantig bawat taludtod, at isahang tugma (aaaaa)."],
        ["Reduccion", "Patakarang kolonyal na nagtipon sa mga kalat-kalat na barangay patungo sa plaza complex sa ilalim ng kampana."],
        ["Sinkretismo", "Pagsasama at paglalangkap ng magkaibang paniniwala o kultural na tradisyon tungo sa isang bagong anyo."],
        ["Stereotype", "Mapanlahat, pinasimpleng, at madalas mapanghusgang palagay tungkol sa isang pangkat ng tao."]
    ]
    add_custom_table(doc, headers_glossary, data_glossary)

    doc.add_page_break()

    # =========================================================================
    # PAHINA 44: KOMPLETONG SUSI SA PAGWAWASTO AT GABAY SA GURO
    # =========================================================================
    # =========================================================================
    # PAHINA 44: KOMPLETONG SUSI SA PAGWAWASTO AT GABAY SA GURO
    # =========================================================================
    add_heading_1(doc, "KOMPLETONG SUSI SA PAGWAWASTO AT GABAY SA GURO")
    add_heading_2(doc, "Susi sa mga Mabilisang Pagtataya at Pangwakas na Pagsusulit")

    # --- ARALIN 13 ANSWER KEY ---
    add_heading_3(doc, "1. Susi sa Mabilisang Pagtataya sa Aralin 13")
    add_body_p(doc, "Bahagi I: Maramihang Pagpipili (Aytem 1–10)", bold_prefix="")
    headers_mcq = ["Aytem", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    data_mcq13 = [["Sagot", "B", "C", "B", "B", "B", "B", "B", "B", "B", "B"]]
    add_custom_table(doc, headers_mcq, data_mcq13)

    add_body_p(doc, "Bahagi II: Mapanuring Pagsusuri at Pagpapaliwanag (Aytem 11–15)", bold_prefix="")
    headers_open = ["Aytem", "Inaasahang Sagot, Batayan, at Rubrik sa Pagmamarka"]
    data_open13 = [
        ["11", "Kontekstong Historikal: Dahil ang teksto ay may kontekstong pangkasaysayan at boses ng kapangyarihang nagpalimbag nito."],
        ["12", "Pasalita vs. Nakalimbag: Ang tradisyong pasalita ay nakasalalay sa kolektibong memorya ng bayan, samantalang ang nakalimbag na balita ay sumailalim sa sensura ng kolonya."],
        ["13", "Pagtutumbas: Halimbawa ang maling pag-aakala na ang 'justicia' ay nangangahulugang katarungan para sa lahat, gayong para sa mananakop ito ay pagsunod sa kolonyal na batas."],
        ["14", "Biswal na Semiotika: Paggamit ng foreground para sa matatag na tindig ng tauhan at background na nagpapakita ng kaniyang ugnayan sa lupang sinilangan."],
        ["15", "Talinghaga ng Pagdurusa: Ginamit ito ng Espanya upang magpasunod, ngunit ginamit ng mga Pilipino ang talinghaga ng pagdurusa upang magkaisa at lumaban."]
    ]
    add_custom_table(doc, headers_open, data_open13)

    # --- ARALIN 14 ANSWER KEY ---
    add_heading_3(doc, "2. Susi sa Mabilisang Pagtataya sa Aralin 14")
    add_body_p(doc, "Bahagi I: Maramihang Pagpipili (Aytem 1–10)", bold_prefix="")
    data_mcq14 = [["Sagot", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]
    add_custom_table(doc, headers_mcq, data_mcq14)

    add_body_p(doc, "Bahagi II: Mapanuring Pagsusuri at Pagpapaliwanag (Aytem 11–15)", bold_prefix="")
    data_open14 = [
        ["11", "Estruktura ng Quintilla: Ang quintilla (8 pantig, isahang tugma) ay may likas na musikalidad na madaling maawit at maisaulo ng mga mamamayan."],
        ["12", "Ebidensiya vs. Interpretasyon: Ang ebidensiya ay ang nakalimbag na datos (hal. petsa at bilang ng dumalo); ang interpretasyon ay ang paghuhusga kung matagumpay ba ito o hindi."],
        ["13", "Kahalagahan ng Batis: Nakapagbibigay ito ng opisyal na rekord ng panahon, ngunit ang limitasyon nito ay ang kawalan ng tinig ng mga karaniwang mamamayan."],
        ["14", "Biswal na Herarkiya: Ang mas malaking tauhan sa foreground ay nagpapahiwatig ng biswal na kapangyarihan kumpara sa maliliit na pigura sa likuran."],
        ["15", "Pag-aangkin sa Pasyon: Sa pamamagitan ng pag-aangkin sa salaysay ni Kristo bilang simbolo ng kanilang sariling pagpapakasakit tungo sa pambansang pagtubos."]
    ]
    add_custom_table(doc, headers_open, data_open14)

    # --- ARALIN 15 ANSWER KEY ---
    add_heading_3(doc, "3. Susi sa Mabilisang Pagtataya sa Aralin 15")
    add_body_p(doc, "Bahagi I: Maramihang Pagpipili (Aytem 1–10)", bold_prefix="")
    data_mcq15 = [["Sagot", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]
    add_custom_table(doc, headers_mcq, data_mcq15)

    add_body_p(doc, "Bahagi II: Mapanuring Pagsusuri at Pagpapaliwanag (Aytem 11–15)", bold_prefix="")
    data_open15 = [
        ["11", "Konteksto vs. Pagtanggap: Ang pag-unawa sa konteksto ay pagkilala sa pinagmulan ng akda; ang pagtanggap naman ay sariling pagpapasiya batay sa modernong etika."],
        ["12", "Neutral na Panayam: Halimbawa: 'Paano po ninyo pinangangasiwaan ang pagtatapon ng basura sa inyong purok?' Neutral ito dahil hindi nagpapataw ng paghusga."],
        ["13", "Etika sa Batis: Upang hindi mabaluktot ang katotohanan at mapanatili ang integridad at karapatan ng kinapanayam."],
        ["14", "Kababaihan sa Kasaysayan: Ang pamumuno nina Gabriela Silang sa labanan at ang pamamahala ng mga kababaihan sa negosyo at pamilihan sa Paombong at Maynila."],
        ["15", "Kuwit sa Pantawag: Ang kuwit pagkatapos ng pantawag (hal. 'Feliza,') ay nagtatakda ng natural na paghinto sa pagbasa na katulad ng tunay na pagbigkas."]
    ]
    add_custom_table(doc, headers_open, data_open15)

    # --- PANGWAKAS NA PAGTATAYA ANSWER KEY ---
    add_heading_3(doc, "4. Susi sa Pangwakas na Pagtataya sa Yunit III")
    add_body_p(doc, "Bahagi I: Pagsusuri sa Dokumentong Pangkasaysayan (Aytem 1–5)", bold_prefix="")
    headers_p1 = ["Aytem", "Inaasahang Pagsusuri at Batayan"]
    data_p1 = [
        ["1", "Kolonyal na Pananaw: Nilikha ito ng kolonyal na pahayagan upang magmukhang sila ang tagapagligtas."],
        ["2", "Lokal na Batis: Ang talaan ng parokya na nagpatunay na nauna nang kumilos si Kapitana Juana."],
        ["3", "Katatagan at Liderato: Nagpamalas siya ng liderato, agham, at pagkukusa sa harap ng epidemya."],
        ["4", "Pagpapahalaga sa Kapuwa: Ang kalinisan at pag-iingat sa tubig ay paggalang sa kalusugan at buhay ng kapuwa."],
        ["5", "Etikal na Tanong: 'Ano po ang inyong naging pamamaraan sa pagpapakulo ng tubig upang mahikayat ang mga mamamayan?'"]
    ]
    add_custom_table(doc, headers_p1, data_p1)

    add_body_p(doc, "Bahagi II: Konsepto, Wika, at Aplikasyon (Aytem 1–5)", bold_prefix="")
    headers_mcq_p2 = ["Aytem", "1", "2", "3", "4", "5"]
    data_mcq_p2 = [["Sagot", "B", "B", "B", "B", "B"]]
    add_custom_table(doc, headers_mcq_p2, data_mcq_p2)

    add_body_p(doc, "Bahagi III (Sanaysay) at Bahagi IV (GRASPS Performance Task): Gamitin ang nakalaang 4x4 analitikong rubrik sa Pahina 41 at 42.", bold_prefix="")

    add_callout_box(
        doc,
        "TALA AT DIAGNOSTIC GUIDE PARA SA GURO:\n"
        "1. Gamitin ang mga maling sagot sa pagsusuri ng ebidensiya upang matukoy kung nahihirapan pa ang mag-aaral sa paghihiwalay ng katotohanan laban sa opinyon.\n"
        "2. Sa pagmamarka ng sanaysay, bigyang-diin ang kakayahan ng mag-aaral na magtagpi-tagpi ng mga konsepto mula sa iba't ibang aralin.\n"
        "3. Sa Comic Book Brochure, huwag sukatin ang galing sa pagguhit; sukatin ang linaw ng komunikasyon, katumpakan ng konteksto, at etikal na representasyon."
    )
