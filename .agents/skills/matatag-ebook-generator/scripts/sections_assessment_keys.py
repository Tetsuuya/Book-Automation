# -*- coding: utf-8 -*-
"""Assessment and Answer Keys Builder: Pages 40 to 44 (5 Full Pages)"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from generate_expanded_ebook import (
    format_paragraph, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_prompt_box, add_callout_box, add_custom_table,
    set_cell_shading
)

def build_assessment_and_keys(doc):
    # =========================================================================
    # PAHINA 40: PANGWAKAS NA PAGTATAYA SA YUNIT II (BAHAGI I AT II)
    # =========================================================================
    add_heading_1(doc, "PANGWAKAS NA PAGTATAYA SA YUNIT II (Unit Assessment)")
    add_heading_2(doc, "Bahagi I: Mapanuring Pagbasa sa Bagong Akdang Tuluyan (10 Puntos)")
    add_body_p(
        doc,
        "Panuto: Basahin ang maikling sanaysay sa ibaba tungkol sa 'Bayanihan sa Nayon' at sagutin ang mga sumusunod na tanong batay sa konteksto at kaisipan nito.",
        bold_prefix="Panuto sa Bahagi I: "
    )

    add_callout_box(
        doc,
        title="TEKSTONG BABASAHIN: ANG HULING PANDAY NG SAN ROQUE",
        body_lines=[
            "   Sa isang liblib na sulok ng San Roque, nananatiling buhay ang lagablab ng apoy sa pagawaan ni Mang Ambo, ang huling panday ng nayon. Sa gitna ng pagdagsa ng mga imported na kagamitan mula sa mga pabrika sa Tsina, patuloy siyang humahampas ng bakal upang humubog ng mga itak at araro para sa mga lokal na magsasaka.",
            "   Para sa mga kabataang nahuhumaling sa e-commerce, itinuturing nilang lipas na sa panahon ang ganitong hanapbuhay. Subalit para kay Mang Ambo, ang bawat ararong kaniyang nililikha ay may taglay na kaluluwa—isinusukat niya ito ayon sa taas ng magsasaka at sa uri ng lupa sa kanilang bukirin. Ito ang tinatawag na katutubong teknolohiya na nag-uugnay sa tao at sa lupaing kaniyang binubungkal."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    p1_items = [
        "1. Ano ang pangunahing kontekstong pangkasaysayan at sosyo-kultural na makikita sa akda tungkol sa panday?",
        "2. Paano ipinagkaiba ng may-akda ang kagamitang gawa sa pabrika kumpara sa tradisyunal na araro ni Mang Ambo?",
        "3. Ano ang panganib na kahaharapin ng komunidad kung tuluyang maglalaho ang mga tradisyunal na panday?",
        "4. Tukuyin ang dalawang magkasalungat na pananaw na ipinahiwatig sa pagitan ng kabataan at ng matandang panday.",
        "5. Kung bibigyan mo ng bagong multimodal campaign ang pagawaan ni Mang Ambo, ano ang iyong magiging mensahe?"
    ]
    for it in p1_items:
        add_body_p(doc, it)

    add_heading_2(doc, "Bahagi II: Pagkilatis sa Balarila, Transisyon, at Kohesyon (10 Puntos)")
    p2_items = [
        "6. (Anapora o Katapora) 'Dahil sa kaniyang dedikasyon sa sining ng pagpapanday, si Mang Ambo ay pinarangalan ng National Museum.' Tukuyin kung anong uri ng kohesyon ang ginamit at ipaliwanag kung bakit.",
        "7. (Transisyong Gramatikal) Punan ang patlang: 'Mura ang mga kagamitang imported; __________, madali itong masira kumpara sa gawang-kamay ng lokal na panday.' (Piliin: bukod dito / datapwat / dahil dito).",
        "8. (Pagsusuri ng Pananaw) Alin sa mga sumusunod ang 'Mapanuring Pananaw' at alin ang 'Walang Suportang Opinyon'?\n"
        "   A. 'Wala nang kuwenta ang maging panday sa panahon ng artificial intelligence.'\n"
        "   B. 'Dapat suportahan ng gobyerno ang lokal na panday dahil pinoprotektahan nito ang food security at kultura ng pagsasaka.'",
        "9. (Pagkilatis sa Sanggunian) Nais mong saliksikin ang kasaysayan ng pagpapanday sa Pilipinas. Alin ang mas maaasahang sanggunian: isang anonymous TikTok video o isang monograph mula sa Pambansang Museo ng Pilipinas? Pangatwiranan.",
        "10. (Multimodalidad) Paano magagamit ang tamang lighting at angle upang maipakita ang dangal at kahusayan ng isang manggagawa sa isang advocacy poster?"
    ]
    for it in p2_items:
        add_body_p(doc, it)

    doc.add_page_break()

    # =========================================================================
    # PAHINA 41: PANGWAKAS NA PAGTATAYA (BAHAGI III AT IV - PERFORMANCE TASK)
    # =========================================================================
    add_heading_2(doc, "Bahagi III: Pagsulat ng Organisadong Mapanuring Sanaysay (10 Puntos)")
    add_body_p(
        doc,
        "Panuto: Pumili ng ISA sa mga sumusunod na paksa. Sumulat ng isang sanaysay na may tatlong organisadong talata (Introduksiyon, Katawan na may Apat na Haligi ng Pananaw, at Konklusyon). Siguraduhing gumamit ng hindi bababa sa tatlong transisyong gramatikal at dalawang kohesiyong gramatikal (anapora/katapora). Salungguhitan ang mga ito.",
        bold_prefix="Panuto sa Pagsulat: "
    )

    add_body_p(
        doc,
        "• Paksa 1: Ang Pagpapanatili ng Tradisyunal na Wikang Katutubo sa Gitna ng Laganap na Paggamit ng Ingles sa Social Media.\n"
        "• Paksa 2: Ang Papel ng Kabataan sa Paglaban sa Disimpormasyon at Fake News sa Panahon ng Eleksiyon sa Barangay.\n"
        "• Paksa 3: Makatarungang Representasyon ng mga Magsasaka at Mangingisda sa mga Patalastas at Balita."
    )

    add_heading_2(doc, "Bahagi IV: Performance Task ng Yunit II (10 Puntos)")
    add_body_p(
        doc,
        "Ikaw ay bubuo ng isang 'Multimodal Advocacy Plan' para sa iyong komunidad. Maaari itong isang storyboard para sa 1-minutong video, layout para sa isang infographic poster, o script para sa isang community radio broadcast. Tiyaking sumusunod ito sa Anti-Stereotype Guidelines at nagpapakita ng makatarungang representasyon."
    )

    rubric_unit_headers = ["Pamantayan sa Unit Performance", "Natatangi (4)", "Mahusay (3)", "Katamtaman (2)", "Nangangailangan (1)"]
    rubric_unit_data = [
        ["Nilalaman at Konteksto", "Malalim, tumpak ang historikal at kultural na batayan", "May sapat na nilalaman at konteksto", "Mababaw at may ilang maling detalye", "Walang kaugnayan sa konteksto ng nayon"],
        ["Estruktura at Balarila", "Perpekto ang gamit ng transisyon, anapora/katapora", "May 1-2 bahagyang kamalian sa kohesyon", "Maraming sirang pangungusap at walang transisyon", "Hindi organisado at magulo ang mga talata"],
        ["Makatarungang Representasyon", "Ganap na walang stereotype; nagbibigay-dangal", "May paggalang ngunit may kaunting karaniwang pananaw", "May bahid ng panlalahat o cultural insensitivity", "Hayagang nagpapakita ng diskriminasyon"],
        ["Kalinawan at Hikayat", "Lubhang nakahihikayat, propesyonal ang dating", "Malinaw at kapani-paniwala ang mensahe", "Kulang sa sigla at hindi nakapupukaw", "Walang malinaw na mensahe o layunin"]
    ]
    add_custom_table(doc, rubric_unit_headers, rubric_unit_data, col_widths=[1.8, 1.3, 1.3, 1.3, 1.3])

    doc.add_page_break()

    # =========================================================================
    # PAHINA 42: PANGKALAHATANG BUOD AT GLOSARYO NG YUNIT II
    # =========================================================================
    add_heading_1(doc, "PANGKALAHATANG BUOD AT GLOSARYO NG YUNIT II")
    add_heading_2(doc, "Konseptwal na Sintesis ng mga Natutuhan")
    
    add_body_p(
        doc,
        "Sa kabuuan ng Yunit II, ating napatunayan na ang wika at panitikan ay hindi mga patay na bagay na nakakulong sa mga lumang pahina ng aklat. Ang mga ito ay buhay na kapangyarihang humuhubog sa ating pagkatao, paninindigan, at kinabukasan bilang isang bansa:",
        bold_prefix="Sintesis ng Pagkatuto: "
    )

    add_body_p(
        doc,
        "1. Sa Aralin 7, natutuhan natin na ang Tuluyang Panitikan ay dapat basahin gamit ang pormulang 'Teksto + Konteksto.' Sa pamamagitan ng kontekstong pangkasaysayan, sosyo-kultural, biograpikal, at pampanitikan, natutuklasan natin ang tunay na kaluluwa ng komunidad. Natutuhan din natin na ang 'Mapanuring Pananaw' ay nangangailangan ng Apat na Haligi (Dahilan, Paliwanag, Halimbawa, at Ebidensiya) upang maiwaksi ang walang batayang opinyon, kalakip ang mga transisyong gramatikal para sa lohikal na daloy.\n"
        "2. Sa Aralin 8, sinuri natin ang Alamat bilang salamin ng katutubong karunungan at ekolohikal na pamumuhay, katambal ang Tekstong Ekspositori na gumagamit ng siyentipikong datos. Sinanay tayo sa Media and Information Literacy (MIL) gamit ang pamantayang KOPAL upang hindi mabiktima ng fake news, kasabay ng paggamit ng Kohesiyong Gramatikal (Anapora at Katapora) upang maiwasan ang redundancy sa pagsulat.\n"
        "3. Sa Aralin 9, ipinakita ng Kuwentong-Bayan ang kahalagahan ng mabuting pamamahala, katapatan, at transparency sa Kaban ng Bayan. Sa larangan ng makabagong komunikasyon, tinalakay ang limang semiotic modes ng Multimodal Texts at ang dakilang tungkulin ng bawat mag-aaral na magtaguyod ng Makatarungang Representasyon at buwagin ang anumang uri ng stereotyping sa media."
    )

    add_heading_2(doc, "Glosaryo ng mga Terminolohiyang Panretorika at Pampanitikan")
    glossary_headers = ["Termino", "Kahulugan sa Pagkatuto"]
    glossary_data = [
        ["Anapora", "Reperensiyang gramatikal kung saan nauuna ang pangngalan bago ang panghalip na tumutukoy pabalik dito."],
        ["Katapora", "Reperensiyang gramatikal kung saan nauuna ang panghalip bago ang pangngalang kinakatawan nito sa dakong huli."],
        ["Kontekstwalisasyon", "Ang pagsusuri sa isang teksto batay sa pangkasaysayan, kultural, at panlipunang kapaligiran nito."],
        ["CRAAP / KOPAL Test", "Pamantayan sa pagsusuri ng sanggunian: Kasariwaan, Otoridad, Paninindigan, Katumpakan, at Layunin."],
        ["Transisyong Gramatikal", "Mga salita o pariralang nag-uugnay sa mga sugnay at talata upang magpakita ng lohika (sanhi, bunga, pagsalungat)."],
        ["Makatarungang Representasyon", "Ang patas, may dignidad, at walang kinikilingang paglalarawan sa lahat ng pangkat sa lipunan sa media."],
        ["Multimodal Text", "Tekstong gumagamit ng dalawa o higit pang semiotic modes (teksto, biswal, audio, kilos, espasyal)."],
        ["Stereotyping", "Pangkalahatan at labis na pinasimpleng paniniwala o paghusga sa isang buong grupo ng tao."]
    ]
    add_custom_table(doc, glossary_headers, glossary_data, col_widths=[2.2, 4.3])

    doc.add_page_break()

    # =========================================================================
    # PAHINA 43: KOMPLETONG SUSI SA PAGWAWASTO (ARALIN 7 AT ARALIN 8)
    # =========================================================================
    add_heading_1(doc, "KOMPLETONG SUSI SA PAGWAWASTO (Answer Key)")
    add_heading_2(doc, "Susi sa Pagwawasto para sa Aralin 7")
    add_body_p(
        doc,
        "1. B - Binubuo ito ng mga pangungusap at talatang sumusunod sa natural na daloy ng wika (hindi tulad ng tula na may sukat at tugma).\n"
        "2. C - Kontekstong Pangkasaysayan (ang pananakop ng Hapon ang nagdikta sa pagbabawal ng Ingles at paggamit ng maikling Tagalog).\n"
        "3. A - Kontekstong Sosyo-Kultural (paniniwala at espiritwal na ugnayan ng nayon sa kalikasan).\n"
        "4. B - Dahil maipapataw ang modernong pananaw sa isang panahong may ibang kalagayan at pangangailangan.\n"
        "5. B - 'Tamad ang lahat ng kabataan ngayon...' (Ito ay isang mapanlahat at walang batayang emosyonal na opinyon).\n"
        "6. D - Ebidensiya (Datos, opisyal na ulat, o patunay).\n"
        "7. B - subalit (nagpapahayag ng pagsasalungat sa pagitan ng mabilis na internet at pangangalaga sa liwasan).\n"
        "8. A - Sa kabuuan (nagpapahiwatig ng lagom o konklusyon).\n"
        "9. B - Siya ang nagbukas sa kultural at pangkasaysayang konteksto ng puno para sa kabataan.\n"
        "10. B - Sinasanay tayo nitong suriin ang pinagmulan, motibo, at panahon bago maniwala sa impormasyon.",
        bold_prefix="Mabilisang Pagtataya sa Aralin 7 (Mga Tamang Sagot at Rationale):\n"
    )

    add_heading_2(doc, "Susi sa Pagwawasto para sa Aralin 8")
    add_body_p(
        doc,
        "1. B - Ang alamat ay gumagamit ng hiwaga sa pagpapaliwanag samantalang ang ekspositori ay gumagamit ng faktuwal na datos.\n"
        "2. B - Katutubong paniniwala na may pananagutan ang tao sa pagpapanatili ng balanse ng kalikasan.\n"
        "3. B - 'Si Tala ay masipag... siya ay palaging nangunguna...' (Nauuna ang pangngalang Tala bago ang panghalip na siya).\n"
        "4. B - 'Patuloy silang nagtatanim... ang mga kabataan...' (Nauuna ang panghalip na silang bago ang pangngalang mga kabataan).\n"
        "5. B - Ang kredensiyal, kadalubhasaan, at lehitimong pagkakakilanlan ng sumulat.\n"
        "6. B - Nagpapalaki o nagbabaluktot ng katotohanan upang makahakot ng clicks lamang.\n"
        "7. B - Ang nakasasawang pag-uulit ng iisang pangngalan nang walang pagbabago.\n"
        "8. C - Elipsis (sadyaing pag-aalis ng salita dahil naiintindihan na sa konteksto).\n"
        "9. B - Pagsamantalahan ang tagtuyot upang magbenta ng tubig at magkamal ng tubo.\n"
        "10. B - Naiiwasan nating maging tagapagpakalat ng kasinungalingan at nagiging matibay ang ating mga desisyon.",
        bold_prefix="Mabilisang Pagtataya sa Aralin 8 (Mga Tamang Sagot at Rationale):\n"
    )

    add_body_p(
        doc,
        "1. Anapora (Bb. Santos ➔ siya)  |  2. Katapora (kaniyang ➔ Tala)  |  3. Anapora (Batis ng Liwayway ➔ ito)  |  4. Katapora (sila ➔ mga lider-katutubo)  |  5. Anapora (Juan ➔ siya)",
        bold_prefix="Gawain 8.3 Susi sa Pagwawasto (Anapora at Katapora Drills):\n"
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 44: KOMPLETONG SUSI SA PAGWAWASTO (ARALIN 9 AT YUNIT ASSESSMENT)
    # =========================================================================
    add_heading_2(doc, "Susi sa Pagwawasto para sa Aralin 9")
    add_body_p(
        doc,
        "1. B - Magsilbing salamin ng kultura, tradisyon, at mga kodigo ng pamumuhay at hustisya sa nayon.\n"
        "2. B - Ninakaw niya ang butil sa kaban at pinalitan ito ng buhangin upang linlangin ang taumbayan.\n"
        "3. B - Paksang Pangungusap (Topic Sentence).\n"
        "4. B - Multimodal Text (kombinasyon ng teksto, audio, biswal, at layout).\n"
        "5. A - Ang laki at kulay ng font, pati ang liwanag at anggulo ng larawan.\n"
        "6. B - Ang paglalapat ng pangkalahatan at madalas ay maling katangian sa isang buong pangkat ng tao.\n"
        "7. B - Upang mabigyan ng pantay na dignidad, boses, at paggalang ang lahat ng sektor nang walang diskriminasyon.\n"
        "8. B - Ang maayos, madulas, at lohikal na pagdurugtong ng mga talata gamit ang mga transisyonal na kaisipan.\n"
        "9. A - Ang pamamahala ay hindi dapat ipinauubaya sa iisang tao lamang kundi ibinabahagi sa iba't ibang sektor.\n"
        "10. B - Nagiging mapanuri silang konsyumer at responsableng tagalikha ng media sa modernong lipunan.",
        bold_prefix="Mabilisang Pagtataya sa Aralin 9 (Mga Tamang Sagot at Rationale):\n"
    )

    add_body_p(
        doc,
        "Tamang Pagkakasunod-sunod: B ➔ D ➔ A ➔ C (2 - 1 - 4 - 3)\n"
        "Paliwanag: Ang B ang Paksang Pangungusap ('Ang pagkakaroon ng bukas na pamamahala...'); sinusundan ng D bilang unang paliwanag ('Ito ay sapagkat...'); sinusundan ng A bilang kongkretong halimbawa ('Halimbawa, napatunayan...'); at nagtatapos sa C bilang pangwakas na transisyon ('Samakatuwid...').",
        bold_prefix="Gawain 9.2 Susi sa Pagwawasto (Pagsasaayos ng Talata):\n"
    )

    add_heading_2(doc, "Gabay sa Pagwawasto para sa Pangwakas na Pagtataya (Yunit II)")
    add_body_p(
        doc,
        "• Aytem 1-5 (Mapanuring Pagbasa sa Panday): Tanggapin ang mga sagot na nagbibigay-diin sa ugnayan ng katutubong teknolohiya at pamayanan, at ang pagpapahalaga sa lokal na industriya laban sa pagbaha ng dayuhang imported goods nang may kaukulang ebidensiya mula sa teksto.\n"
        "• Aytem 6: Katapora (nauna ang panghalip na 'kaniyang' bago ang pangngalang 'Mang Ambo').\n"
        "• Aytem 7: 'datapwat' o 'subalit' (nagpapakita ng pagsalungat sa pagitan ng presyo at tibay).\n"
        "• Aytem 8: Ang A ay Walang Suportang Opinyon (emosyonal at mapanlahat); ang B ay Mapanuring Pananaw (may dahilan at panlipunang katwiran).\n"
        "• Aytem 9: Ang monograph ng Pambansang Museo dahil pumapasa ito sa Pamantayang KOPAL (may Otoridad, peer-reviewed, at faktuwal).\n"
        "• Aytem 10: Paggamit ng mainit na liwanag (warm lighting) na nakapokus sa masisipag na kamay ng manggagawa, at eye-level o low-angle shot upang ipakita ang kaniyang dangal at lakas sa halip na gawin siyang kaawa-awa.",
        bold_prefix="Gabay sa Pagmamarka ng Guro:\n"
    )

    add_callout_box(
        doc,
        title="PAALALA SA GURO UKOL SA PAGTATAYA SA MATATAG KURIKULUM",
        body_lines=[
            "Ang rubrik na ibinigay sa bawat aralin ay kagamitang diagnostic at formative.",
            "Hikayatin ang mga mag-aaral na mag-self-assess at mag-peer review bago isumite ang pinal na sulatin.",
            "Tandaan: Ang sukatan ng tagumpay ay hindi lamang ang matataas na marka kundi ang paghubog ng isang mapanuri, makabayan, at makatarungang mamamayang Pilipino."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )
