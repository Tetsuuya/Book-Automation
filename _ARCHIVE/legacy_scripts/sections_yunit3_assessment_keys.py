# -*- coding: utf-8 -*-
"""Yunit III Assessment, Summary, Glossary, and Answer Keys: Pages 40 to 44+
Features:
- Bahagi I: 30-Item Comprehensive Multiple Choice Quiz (Items 1-30) with [ ] checkboxes
- Bahagi II: Authentic Performance Task (GRASPS Framework + 4x4 Analytic Rubric)
- Unit Summary & 25-term Glossary
- Structured Table Answer Keys (10-col grids for lessons + 15-col grids for 30-item Unit Assessment)
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from generate_expanded_ebook import (
    format_paragraph, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_callout_box, add_custom_table
)

def build_yunit3_assessment_and_keys(doc):
    # =========================================================================
    # PAHINA 40: PANGWAKAS NA PAGTATAYA SA YUNIT III (50 PUNTOS)
    # =========================================================================
    add_heading_1(doc, "PANGWAKAS NA PAGTATAYA SA YUNIT III (50 PUNTOS)")
    add_heading_2(doc, "Yunit III: Ako at ang Aking Pagkatao, Tanglaw ng Katatagan")
    add_body_p(
        doc,
        "Panimula: Ang komprehensibong pagtatayang ito ay sumusukat sa iyong kabuuang kasanayan at kritikal na pag-unawa sa buong Yunit III "
        "(Aralin 13 hanggang 15). Binubuo ito ng dalawang pangunahing bahagi: "
        "(I) Komprehensibong Pagsusulit na Maramihang Pagpipili (Aytem 1–30, 30 Puntos) na sumusuri sa kaligirang pangkasaysayan, Pasyon, "
        "kagandahang-asal, tekstong impormasyonal, wika, at disenyong multimodal; at "
        "(II) Autentikong Gawaing Pagganap (Performance Task, 20 Puntos) gamit ang GRASPS Model at Analitikong Rubrik."
    )

    add_heading_3(doc, "Bahagi I: Maramihang Pagpipili (Aytem 1 hanggang 30 — 30 Puntos)")
    add_body_p(
        doc,
        "Panuto: Basahing mabuti ang bawat katanungan. Piliin ang titik ng pinakatumpak na sagot at lagyan ng tsek [ ✓ ] ang kahon katabi ng iyong napiling titik. (1 puntos bawat aytem)"
    )

    p1_mcq_30 = [
        # --- ARALIN 13 ITEMS (1 - 10) ---
        ("1. Ano ang pangunahing layunin ng patakarang reduccion na ipinatupad ng mga mananakop na Espanyol kaugnay ng pamamahala at panitikan?",
         ["A. Hikayatin ang mga katutubong maglakbay sa ibang bansa upang mag-aral.",
          "B. Ihiwalay ang mga katutubo sa mga prayle upang mapanatili ang sinaunang kultura.",
          "C. Tipunin ang mga mamamayan sa ilalim ng tunog ng kampana upang mapadali ang kontrol at pagpapalaganap ng relihiyon.",
          "D. Pabagsakin ang ekonomiya ng mga lungsod upang palakasin ang mga baryo."]),
        ("2. Alin sa mga sumusunod ang PINAKATUMPANG paglalarawan sa kalagayan ng panitikan sa Pilipinas bago dumating ang mga Espanyol noong 1565?",
         ["A. Mayaman at maunlad na tradisyong pasalita tulad ng epiko, awiting-bayan, at karunungang-bayan.",
          "B. Pawang mga aklat sa wikang Espanyol lamang ang binabasa ng mga datu.",
          "C. Walang anumang panitikan dahil hindi pa marunong sumulat ang mga ninuno.",
          "D. Nakasalalay lamang sa mga pahayagang inililimbag sa Maynila at Cebu."]),
        ("3. Bakit itinuturing na may pagkiling o hindi ganap na neutral ang mga opisyal na balitang inilathala noong panahong kolonyal?",
         ["A. Dahil kulang sa papel at tinta ang mga palimbagan noong panahong iyon.",
          "B. Dahil puro tula lamang ang nilalaman ng mga kolonyal na pahayagan.",
          "C. Dahil hindi marunong magbasa ng balita ang mga karaniwang mamamayan.",
          "D. Dahil ang mga pahayagan ay kontrolado at sumasailalim sa mahigpit na sensura ng pamahalaan at simbahan."]),
        ("4. Sa pagsusuri ng lunsarang tekstong 'Ang Ulat sa Liwasan,' ano ang ibinubunyag ng lihim na liham ng kura na hindi makikita sa opisyal na balita?",
         ["A. Ang masayang pagsasayaw ng mga mamamayan sa harap ng munisipyo.",
          "B. Ang matinding takot, tensiyon, at lihim na pagtutol ng mga katutubo sa bagong buwis.",
          "C. Ang pagdating ng malaking barko mula sa Espanya na may dalang mga regalo.",
          "D. Ang pagkakasundo ng mga katutubo at guardia civil sa pagbuo ng bagong tulay."]),
        ("5. Alin sa mga sumusunod ang halimbawa ng pagtutumbas ng salita sa halip na tuwirang panghihiram?",
         ["A. Paggamit ng salitang 'alkalde' mula sa 'alcalde'.",
          "B. Paggamit ng salitang 'gobernador' para sa pinuno ng lalawigan.",
          "C. Paggamit ng salitang 'kumpisal' mula sa salitang 'confesar'.",
          "D. Paggamit ng salitang 'pamahalaang lungsod' para sa konseptong 'ayuntamiento'."]),
        ("6. Ano ang tinutukoy ng konseptong 'presentismo' na dapat iwasan sa pagsusuri ng mga lumang akda?",
         ["A. Ang paghuhusga sa mga pangyayari sa nakaraan gamit lamang ang makabagong pamantayan nang hindi inuunawa ang konteksto.",
          "B. Ang pagbibigay ng regalo sa mga guro tuwing araw ng pagsusulit.",
          "C. Ang pagiging huli sa pagpasok sa klase sa panahon ng talakayan.",
          "D. Ang labis na paggamit ng pandiwang pangkasalukuyan sa pagsulat ng balita."]),
        ("7. Paano nakatutulong ang caption sa isang comic book brochure upang mapalalim ang kahulugan ng larawan?",
         ["A. Inuulit lamang nito ang eksaktong nakikita na sa drowing upang humaba ang teksto.",
          "B. Tinatakpan nito ang mukha ng mga tauhan upang maging misteryoso ang tagpo.",
          "C. Nagbibigay ito ng kontekstong pangkasaysayan at damdamin na hindi kayang ipakita ng biswal lamang.",
          "D. Pinapalitan nito ang pangangailangan sa pagguhit ng background."]),
        ("8. Bakit mapanganib ang paggamit ng mapanlahatang stereotype sa paglalarawan ng mga pangkat-etniko sa komiks?",
         ["A. Dahil nagiging mas madaling basahin ang komiks para sa mga bata.",
          "B. Dahil binubura nito ang pagkakaiba-iba, talino, at tunay na dignidad ng mga katutubong pamayanan.",
          "C. Dahil magiging masyadong makulay ang mga pahina ng brochure.",
          "D. Dahil mas mura ang magiging gastusin sa pagpapalimbag ng aklat."]),
        ("9. Sa pagbuo ng isang responsableng balita, ano ang unang dapat gawin kapag nakatanggap ng ulat na may magkasalungat na pahayag?",
         ["A. Beripikahin ang impormasyon sa iba pang mapagkakatiwalaang batis at ilahad ang magkakaibang panig nang patas.",
          "B. Piliin agad ang pahayag ng may pinakamataas na katungkulan at balewalain ang iba.",
          "C. Huwag nang isulat ang balita upang maiwasan ang gulo.",
          "D. Gumawa ng sariling kuwento na magugustuhan ng mga mambabasa."]),
        ("10. Alin sa mga sumusunod ang nagpapakita ng ahensiya at katatagan ng mga katutubong Pilipino sa kabila ng pananakop?",
         ["A. Ang ganap na pagtalikod sa lahat ng katutubong kaugalian nang walang pagtutol.",
          "B. Ang pagtanggap sa lahat ng banyagang batas nang hindi nagtatanong.",
          "C. Ang paglalangkap ng sariling ritmo, talinghaga, at damdamin sa loob ng mga ipinakilalang anyong banyaga.",
          "D. Ang paglimot sa sariling wika upang magsalita lamang ng Espanyol."]),

        # --- ARALIN 14 ITEMS (11 - 20) ---
        ("11. Ano ang tawag sa tradisyonal na anyo ng saknong ng Pasyon na binubuo ng limang taludtod na may walong pantig bawat isa?",
         ["A. Dalit", "B. Quintilla", "C. Tanaga", "D. Diona"]),
        ("12. Paano naiiba ang layunin ng mga prayle sa layunin ng mga katutubong Pilipino sa pagpapalaganap ng Pasyon?",
         ["A. Nais ng mga prayle na maging makata ang lahat, samantalang nais ng mga katutubo na maging mang-aawit.",
          "B. Nais ng mga prayle na ibenta ang aklat, samantalang ipinamigay ito ng mga katutubo nang libre.",
          "C. Walang anumang pagkakaiba sa kanilang naging pagtanggap sa akda.",
          "D. Ginamit ito ng mga prayle upang ituro ang pagpapasakop, samantalang nakita ng mga katutubo ang pag-asa sa pagtatagumpay ng mga api."]),
        ("13. Bakit itinuturing na gawaing panlipunan (social practice) ang Pabasa sa kulturang Pilipino?",
         ["A. Dahil ito ay sama-samang isinasagawa sa mga tahanan kung saan nagtitipon, nag-uusap, at nagsasalu-salo ang pamayanan.",
          "B. Dahil binabayaran ng pamahalaan ang lahat ng nakikinig sa pag-awit.",
          "C. Dahil ipinagbabawal ang pag-awit nito sa loob ng mga pribadong silid.",
          "D. Dahil mga dayuhan lamang ang pinapayagang magbasa nito."]),
        ("14. Alin sa mga sumusunod ang unang pang-araw-araw na pahayagan sa Pilipinas na itinatag noong 1846?",
         ["A. Del Superior Govierno", "B. La Esperanza", "C. Diariong Tagalog", "D. La Solidaridad"]),
        ("15. Sa pagsusuri ng isang lumang dokumento na may salitang hindi na ginagamit ngayon, ano ang PINAKARESPONSABLENG unang hakbang?",
         ["A. Palitan agad ito ng pinakamalapit na modernong salitang maisip.",
          "B. Burahin ang salita upang hindi malito ang mga mambabasa.",
          "C. Basahin ang buong pangungusap upang matukoy ang kontekstuwal na pahiwatig bago sumangguni sa talatinigan.",
          "D. Ipagpalagay na mali ang baybay ng may-akda noong unang panahon."]),
        ("16. Ano ang pangunahing gampanin ng 'foreground' sa pagbuo ng isang makasaysayang comic panel?",
         ["A. Ipakita ang malalayong bundok at ulap sa likuran.",
          "B. Punuin ang espasyo ng mga dekorasyong walang kaugnayan sa kuwento.",
          "C. Takpan ang mga pagkakamali sa pagguhit ng mga gusali.",
          "D. Ituon ang pansin ng mambabasa sa pangunahing tauhan, kilos, at emosyon ng tagpo."]),
        ("17. Paano dapat magtulungan ang caption at ang larawan sa isang responsableng comic book brochure?",
         ["A. Dapat magbigay ang caption ng konteksto o impormasyong hindi kayang ipakita ng larawan lamang.",
          "B. Dapat ulitin ng caption ang bawat bagay na iginuhit sa larawan.",
          "C. Dapat magkasalungat ang sinasabi ng caption sa ipinapakita ng larawan.",
          "D. Dapat mas marami ang salita kaysa sa espasyo ng drowing."]),
        ("18. Bakit mapanganib na gumawa ng pangkalahatang kongklusyon tungkol sa buong lipunan mula lamang sa isang larawan ng marangyang bahay-na-bato?",
         ["A. Dahil baka nasunog na ang bahay sa kasalukuyan.",
          "B. Dahil laging peke ang mga lumang larawan.",
          "C. Dahil ang larawan ay kumakatawan lamang sa uring maykaya at hindi sumasalamin sa kalagayan ng mayoryang magsasaka.",
          "D. Dahil hindi mahalaga ang arkitektura sa pag-aaral ng panitikan."]),
        ("19. Ano ang ipinahihiwatig ng pag-uulat ng pahayagang 'El Comercio' (1875) tungkol sa mga lihim na pag-uusap ng mga katutubo sa panahon ng Kuwaresma?",
         ["A. Na walang pakialam ang pamahalaan sa mga gawaing panrelihiyon.",
          "B. Na naging lehitimong panakip ang relihiyosong pagtitipon upang mag-usap ang mga mamamayan tungkol sa kanilang mga hinaing.",
          "C. Na mas gusto ng mga magsasaka na magbasa ng diyaryo kaysa umawit ng Pasyon.",
          "D. Na ipinagbawal ng pamahalaan ang pagbebenta ng Pasyon sa buong kapuluan."]),
        ("20. Sa pagguhit ng mga tauhan sa isang historikal na komiks, paano maiiwasan ang stereotype sa mga mahihirap na mamamayan?",
         ["A. Huwag na silang isama sa alinmang panel ng komiks.",
          "B. Bihisan sila ng modernong kasuotan upang magmukhang mayaman.",
          "C. Gawin silang katawa-tawa upang maging masaya ang mambabasa.",
          "D. Ipakita sila na may sariling dignidad, talino, aktibong pagkilos, at kontekstuwal na katotohanan."]),

        # --- ARALIN 15 ITEMS (21 - 30) ---
        ("21. Ano ang tawag sa anyong pampanitikan ng 'Urbana at Feliza' na gumagamit ng palitan ng mga liham sa pagitan ng mga tauhan?",
         ["A. Epistolaryo", "B. Alegoriko", "C. Pikaresko", "D. Tulang Pasalaysay"]),
        ("22. Sino ang paring may-akda ng klasikong aklat na 'Pagsusulatan ng Dalawang Binibini na si Urbana at si Feliza' (1864)?",
         ["A. P. Gaspar Aquino de Belen", "B. P. Mariano Pilapil", "C. P. Modesto de Castro", "D. P. Pedro Pelaez"]),
        ("23. Ayon sa kaisipan ni Urbana kay Feliza, bakit dapat panatilihin ang kalinisan ng katawan at kaayusan sa pagkilos?",
         ["A. Upang magmukhang mayaman at makahingi ng pabor sa mga pinuno.",
          "B. Upang gayahin ang mga banyagang nakikita sa mga larawan.",
          "C. Dahil may parusang kulong ang sinumang marumi ang pananamit.",
          "D. Sapagkat ang kalinisan at kaayusan ay salamin ng kalinisan ng budhi at paggalang sa sarili at kapuwa."]),
        ("24. Alin sa mga sumusunod ang PINAKAMAHUSAY na halimbawa ng bukas at neutral na tanong sa isang panayam para sa balita?",
         ["A. \"Hindi ba't napakahusay ng inyong pamamalakad sa paaralan?\"",
          "B. \"Paano ninyo ilalarawan ang mga naging tagumpay at hamon sa pagpapatupad ng bagong patakaran?\"",
          "C. \"Kayo po ang may kasalanan kung bakit marumi ang liwasan, tama?\"",
          "D. \"Masaya ang lahat sa programa, hindi ba?\""]),
        ("25. Ano ang pangunahing layunin ng isang 'follow-up question' sa panayam?",
         ["A. Baguhin agad ang paksa kapag hindi nagustuhan ang sagot ng kinakapanayam.",
          "B. Pilitin ang kinakapanayam na sumang-ayon sa sariling pananaw ng tagapagbalita.",
          "C. Palalimin, linawin, o kumuha ng kongkretong ebidensiya batay sa naunang pahayag ng kinakapanayam.",
          "D. Tapusin nang mabilis ang panayam upang makauwi na."]),
        ("26. Bakit mapanganib ang paggamit ng 'leading question' (nangungunang tanong) sa pamamahayag?",
         ["A. Dahil idinidikte nito ang sagot at nawawala ang pagiging patas, obhetibo, at mapagkakatiwalaan ng balita.",
          "B. Dahil nagiging masyadong mahaba ang artikulo sa pahayagan.",
          "C. Dahil baka hindi maintindihan ng mambabasa ang mga salita.",
          "D. Dahil mas mahal ang bayad sa tagapanayam kapag ganoon ang tanong."]),
        ("27. Paano wawasakin ng isang responsableng manunulat ng komiks ang stereotype tungkol sa kababaihan noong panahon ng Espanyol?",
         ["A. Huwag nang maglagay ng babaeng tauhan sa alinmang kuwento.",
          "B. Ipakita silang laging umiiyak at naghihintay ng tulong sa bawat tagpo.",
          "C. Baguhin ang kanilang kasuotan patungo sa makabagong pananamit sa kasalukuyan.",
          "D. Ilarawan ang mga babae na may sariling ahensiya, talino, aktibong pagpapasya, at ambag sa pamayanan."]),
        ("28. Alin sa mga sumusunod ang tamang rebisyon ng linyang: \"Feliza maghugas ka ng kamay mo ngayon na para malinis ka!\"?",
         ["A. \"Feliza maghugas ka kamay ngayon na.\"",
          "B. \"Feliza, maghugas ka ng iyong mga kamay ngayon upang mapanatili ang kalinisan.\"",
          "C. \"Edi maghugas ka na lang Feliza para tapos na!\"",
          "D. \"Hugas kamay ka na Feliza dali!\""]),
        ("29. Ano ang ibig sabihin ng prinsipyo na ang 'kalinisan ay salamin ng kaluluwa' ayon sa didaktikong panitikan?",
         ["A. Na ang panlabas na kaayusan at disiplina sa katawan ay nagmumula sa dalisay na budhi at paggalang sa Diyos at kapuwa.",
          "B. Na ang taong may mamahaling sabon ay tiyak na maliligtas sa kabilang buhay.",
          "C. Na kailangang magsuot ng puting damit araw-araw nang walang patid.",
          "D. Na hindi na kailangang magdasal kung naligo na sa umaga."]),
        ("30. Sa pag-edit ng diyalogo sa isang speech balloon, bakit mahalagang maging matipid at maingat sa salita?",
         ["A. Upang makatipid sa tinta ng bolpen o printer.",
          "B. Dahil bawal ang mahahabang pangungusap sa wikang Filipino.",
          "C. Upang hindi matakpan ang mahalagang visual elements ng larawan at maging madaling basahin ang mensahe.",
          "D. Upang magmukhang misteryoso ang tauhan sa komiks."])
    ]

    for q_text, choices in p1_mcq_30:
        add_body_p(doc, q_text, bold_prefix="")
        for ch in choices:
            p_c = doc.add_paragraph()
            format_paragraph(p_c, space_before=1, space_after=1)
            p_c.paragraph_format.left_indent = Inches(0.2)
            r_c = p_c.add_run(f"[   ]  {ch}")
            r_c.font.name = 'Cambria'
            r_c.font.size = Pt(9.5)

    # =========================================================================
    # BAHAGI II: AUTENTIKONG GAWAING PAGGANAP (PERFORMANCE TASK — 20 PUNTOS)
    # =========================================================================
    add_heading_2(doc, "Bahagi II: Autentikong Gawaing Pagganap (Performance Task — 20 Puntos)")
    add_heading_3(doc, "Gawaing Multimodal gamit ang GRASPS Model: 6-Panel Comic Book Brochure")
    
    add_body_p(
        doc,
        "G (Goal / Layunin): Bumuo ng isang organisado, makabuluhan, at masining na 6-panel na pang-edukasyong comic book brochure "
        "na naglalarawan sa isang makasaysayang tagpo sa panahon ng Espanyol. Dapat itong magtanghal sa katatagan ng pagkataong Pilipino, "
        "pagkakaisa ng pamayanan sa kabila ng kolonyal na kontrol, at tunay na dignidad ng kababaihan at mga katutubo nang walang stereotype.\n\n"
        "R (Role / Papel): Ikaw ay Punong Manunulat, Historikal na Tagasuri, at Tagapagdisenyo ng Multimodal na Nilalaman para sa pampaaralang eksibit.\n\n"
        "A (Audience / Mambabasa): Mga mag-aaral sa Baitang 7, mga guro sa Filipino at Araling Panlipunan, at ang buong pamayanan ng paaralan.\n\n"
        "S (Situation / Sitwasyon): Bilang pagdiriwang ng Buwan ng Kasaysayan at Wika, maglulunsad ang paaralan ng isang eksibit ng mga likhang multimodal. "
        "Kailangang ipakita sa brochure kung paano naging 'tanglaw ng katatagan' ang mga karaniwang mamamayan sa pamamagitan ng kanilang pananampalataya, "
        "kultura, at sariling wika.\n\n"
        "P (Product / Produkto): Isang 6-panel Comic Book Brochure na naglalaman ng: (1) Makatawag-pansing Pamagat at Panimula, "
        "(2) 6 na Kompletong Panel na may malinaw na Foreground at Background, (3) Speech Balloons na may maingat at angkop na diyalogo, "
        "(4) Makabuluhang Captions na nagpapalalim sa konteksto, at (5) Maikling Tala sa Batis at Konteksto sa huling bahagi.\n\n"
        "S (Standards / Pamantayan): Mamarkahan ang iyong awtput batay sa sumusunod na analitikong rubrik na may kabuuang 20 puntos."
    )

    headers_grasps_rubrik = ["Pamantayan sa Pagmamarka", "Napakahusay (5)", "Mahusay (4)", "Nalilinang (3)", "Nangangailangan ng Gabay (2)"]
    data_grasps_rubrik = [
        ["Nilalaman at Kontekstong Pangkasaysayan (30%)", "Ganap na tumpak, malalim ang pagkakaugnay sa mga aralin ng Yunit III; malinaw ang kontekstong kolonyal nang walang anachronism.", "Tumpak ang karamihan sa mga detalye; angkop ang tagpo at mensahe sa kasaysayan.", "May ilang kakulangan o malabong historikal na ugnayan sa salaysay.", "Maraming maling impormasyon sa kasaysayan; hindi maunawaan ang konteksto."],
        ["Diyalogo, Wika, at Bantas (25%)", "Napakalinaw, wasto ang gramatika at bantas; natural at angkop ang boses ng bawat tauhan sa speech balloon.", "Wasto at malinaw ang karamihan sa mga diyalogo; may kaunting maliliit na pagkukulang.", "Medyo magulo o artipisyal ang pananalita; may mga kamalian sa bantas.", "Maraming mali sa gramatika at bantas na nakahahadlang sa mensahe."],
        ["Organisasyong Biswal at Multimodal (25%)", "Napakatalas ng ugnayan ng panel, foreground, background, at caption; kumpleto ang daloy ng visual narrative.", "Maayos ang daloy ng mga panel; malinaw ang ugnayan ng larawan at teksto.", "Medyo paulit-ulit ang sinasabi ng teksto sa larawan; kulang sa background.", "Magulo ang pagkakaayos ng mga panel; walang malinaw na ugnayan ang teksto at biswal."],
        ["Etikal na Representasyon at Dignidad (20%)", "Ganap na umiiwas sa stereotype; itinatanghal ang talino, ahensiya, at katatagan ng kababaihan at katutubo.", "Responsable at maingat ang paglalarawan sa mga tauhan.", "May kaunting kababawan o simplistikong paglalarawan sa kahirapan.", "Malinaw na gumagamit ng mapanlait o mapanghusgang stereotype."]
    ]
    add_custom_table(doc, headers_grasps_rubrik, data_grasps_rubrik)

    add_body_p(doc, "Pagmamarka sa Bahagi II: Kabuuang Puntos sa Rubrik (Pinakamataas: 20 Puntos). Kabuuang Marka sa Pangwakas na Pagtataya: Bahagi I (30 pts) + Bahagi II (20 pts) = 50 Puntos.", italic_prefix="")

    # =========================================================================
    # BUOD NG YUNIT III AT KOMPREHENSIBONG TALATINIGAN
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
    # PAHINA 44+: KOMPLETONG SUSI SA PAGWAWASTO AT GABAY SA GURO
    # =========================================================================
    add_heading_1(doc, "KOMPLETONG SUSI SA PAGWAWASTO AT GABAY SA GURO")
    add_heading_2(doc, "Susi sa mga Mabilisang Pagtataya at Pangwakas na Pagsusulit")

    # --- ARALIN 13 ANSWER KEY ---
    add_heading_3(doc, "1. Susi sa Mabilisang Pagtataya sa Aralin 13")
    add_body_p(doc, "Bahagi I: Maramihang Pagpipili (Aytem 1–10)", bold_prefix="")
    headers_mcq = ["Aytem", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    data_mcq13 = [["Sagot", "C", "A", "D", "B", "D", "A", "C", "B", "A", "C"]]
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
    data_mcq14 = [["Sagot", "B", "D", "A", "B", "C", "D", "A", "C", "B", "D"]]
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
    data_mcq15 = [["Sagot", "A", "C", "D", "B", "C", "A", "D", "B", "A", "C"]]
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

    # --- PANGWAKAS NA PAGTATAYA ANSWER KEY (30 ITEMS MCQ) ---
    add_heading_3(doc, "4. Susi sa Pangwakas na Pagtataya sa Yunit III (30 Aytem na Maramihang Pagpipili)")
    add_body_p(doc, "Susi sa Pagwawasto: Aytem 1 hanggang 15 (Talahanayan A)", bold_prefix="")
    headers_p1_15 = ["Aytem", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    data_p1_15 = [["Sagot", "C", "A", "D", "B", "D", "A", "C", "B", "A", "C", "B", "D", "A", "B", "C"]]
    add_custom_table(doc, headers_p1_15, data_p1_15)

    add_body_p(doc, "Susi sa Pagwawasto: Aytem 16 hanggang 30 (Talahanayan B)", bold_prefix="")
    headers_p16_30 = ["Aytem", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
    data_p16_30 = [["Sagot", "D", "A", "C", "B", "D", "A", "C", "D", "B", "C", "A", "D", "B", "A", "C"]]
    add_custom_table(doc, headers_p16_30, data_p16_30)

    add_body_p(doc, "Bahagi II: Autentikong Gawaing Pagganap (Performance Task): Gamitin ang analitikong rubrik sa itaas (20 Puntos kabuuan).", bold_prefix="")

    add_callout_box(
        doc,
        "TALA AT DIAGNOSTIC GUIDE PARA SA GURO:\n"
        "1. Pagsusuri ng Aytem 1-10 (Aralin 13): Kung mababa ang iskor ng mag-aaral, balikan ang kasanayan sa pagkilala sa kaligirang pangkasaysayan at pagsusuri ng pagkiling sa balita.\n"
        "2. Pagsusuri ng Aytem 11-20 (Aralin 14): Sumusukat sa lalim ng pagkaunawa sa Pasyon bilang gawaing panlipunan at paghihiwalay ng datos laban sa interpretasyon.\n"
        "3. Pagsusuri ng Aytem 21-30 (Aralin 15): Sumusukat sa etika ng panayam, kagandahang-asal bilang kapuwa-dangal, at tamang rebisyon ng diyalogo sa komiks.\n"
        "4. Sa Gawaing Pagganap (Comic Book Brochure): Bigyang-diin ang katumpakang historikal, natural na diyalogo, at etikal na representasyon ng kababaihan at katutubo."
    )
