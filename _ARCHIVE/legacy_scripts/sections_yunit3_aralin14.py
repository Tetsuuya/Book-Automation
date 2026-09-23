# -*- coding: utf-8 -*-
"""Aralin 14 Builder: Pages 16 to 27 (12 Full Pages)"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from generate_expanded_ebook import (
    format_paragraph, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_prompt_box, add_callout_box, add_custom_table,
    add_multimedia_box, set_cell_shading
)

def build_yunit3_aralin14(doc):
    # =========================================================================
    # PAHINA 16: PANIMULA, LAYUNIN, AT MULTIMEDIA CORNER #2
    # =========================================================================
    add_heading_1(doc, "ARALIN 14: Pasyon at mga Tekstong Panrelihiyon sa Panahong Kolonyal")
    add_heading_2(doc, "MGA LAYUNIN AT BALANGKAS NG PAGKATUTO")
    add_body_p(
        doc,
        "Sa Aralin 14, itutuon ang ating mapanuring pag-aaral sa Pasyon bilang pinakatanyag at pinakamaimpluwensiyang akdang panrelihiyon sa Panahon ng "
        "Pananakop ng Espanya. Sisiyasatin natin kung paano ang isang tekstong dinala ng mga banyaga upang magturo ng pananampalataya at pagpapakumbaba "
        "ay inangkin at binigyan ng bagong kahulugan ng mga katutubong Pilipino. Tatalakayin din ang anyo, mensahe, at konteksto ng mga akdang panrelihiyon, "
        "ang mga unang pahayagan sa bansa, ang wikang matatagpuan sa matatandang dokumento, ang antas ng pamumuhay sa ilalim ng pamahalaang kolonyal, "
        "at ang mga masining na elementong biswal na gagamitin sa pagbuo ng isang komprehensibong comic book brochure."
    )

    add_body_p(
        doc,
        "1. F7PN-IIIb-1: Nasusuri ang anyo, paksa, mensahe, at kontekstong kultural ng Pasyon at iba pang akdang panrelihiyon.\n"
        "2. F7PB-IIIb-2: Naiisa-isa ang mahahalagang impormasyon mula sa mga lumang pahayagan noong panahon ng Espanyol gamit ang mapanuring pagbasa.\n"
        "3. F7PT-IIIb-3: Natutukoy ang kahulugan ng mga lumang salitang ginamit sa mga tekstong kolonyal sa pamamagitan ng kontekstuwal na pahiwatig.\n"
        "4. F7PD-IIIb-4: Nasusuri ang ugnayan ng antas ng pamumuhay at mga elementong biswal (panel, foreground, background, caption) sa komiks.\n"
        "5. F7PU-IIIb-5: Nakalilikha ng organisadong storyboard para sa comic book brochure na nagtatanghal ng tagpong panrelihiyon nang may dignidad.",
        bold_prefix="Mga Kasanayang Pampagkatuto (MATATAG Competencies):\n"
    )

    add_body_p(
        doc,
        "• Paano naging daluyan ang pag-awit ng Pasyon (pabasa) ng kolektibong damdamin, pakikipagkapuwa, at pagtutol ng mga Pilipino sa kaapihan?\n"
        "• Ano ang maitutulong ng pagsusuri sa wikang matatagpuan sa matatandang teksto sa pag-unawa sa pamumuhay noong panahong kolonyal?\n"
        "• Paano nagtutulungan ang biswal na diin (foreground/background) at teksto sa paghahatid ng makatarungang representasyon ng lipunan?",
        bold_prefix="Mga Susing Katanungan para sa Aralin:\n"
    )

    add_multimedia_box(
        doc,
        mod_title="Buhay na Tradisyon ng Pabasa ng Pasyon",
        vid_title="Tradisyong Pabasa ng Pasyon Tuwing Mahal na Araw sa Bulacan",
        channel="GMA Public Affairs / i-Witness / News5 Documentaries",
        link="https://www.youtube.com/results?search_query=GMA+Public+Affairs+Pabasa+ng+Pasyon+Tradisyon",
        qr_code_text="",
        timestamps=[
            "01:20 - 05:10: Ang Tradisyonal na Punto at Tono ng Pabasa sa mga Tahanan sa Lalawigan.",
            "05:11 - 09:30: Paghahanda ng Pamilya sa Altar at Pag-awit nang Salit-salitang 24-Oras.",
            "09:31 - 13:45: Pagsusuri ni Dr. Reynaldo Ileto: Paano naging Sandata ng Pagkakaisa ang Pasyon."
        ],
        questions=[
            "Ayon sa ulat pantelebisyon, paano naipapasa ng mga nakatatanda sa kabataan ang tamang 'punto' o himig ng pag-awit ng Pasyon?",
            "Bakit itinuturing ng komunidad na panata at pagpapasalamat ang Pabasa kaysa isang simpleng palabas?",
            "Anong katangian ng wikang ginamit sa Pasyon ang nagbibigay-daan upang madali itong maisaulo ng mga karaniwang mamamayan?"
        ]
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 17: PAKSA 14.1 - PASYON BILANG AKDANG PANRELIHIYON
    # =========================================================================
    add_heading_2(doc, "PAKSA 14.1: Ang Pasyon bilang Akdang Panrelihiyon: Anyo, Mensahe, at Konteksto")
    
    prompt_14_1 = (
        "PROMPT: An intimate, atmospheric cultural scene of a traditional Filipino Pabasa ng Pasyon inside a warm wooden provincial ancestral home during Holy Week. "
        "A multi-generational family seated respectfully around an ornate wooden altar adorned with white sampaguita flowers, yellow candles, and the Santo Entierro icon. "
        "Chanters solemnly singing from vintage cloth-bound Pasyon books, while neighborhood visitors listen quietly in the background. Warm nostalgic lighting, documentary realism, 8k resolution --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "TRADISYONG KULTURAL: ANG PABASA SA ISANG TAHANANG TAGALOG", prompt_14_1)
    
    add_body_p(
        doc,
        "Ang Pasyon ang maituturing na pinakamakapangyarihang akdang patula sa Panahon ng Pananakop ng Espanya. Ito ay isang naratibong tula na naglalahad "
        "ng buhay, mga aral, pagpapakasakit, kamatayan, at muling pagkabuhay ni Hesukristo, na karaniwang nagsisimula sa paglikha sa daigdig (Henesis) hanggang "
        "sa paghuhukom. Ang pinakatanyag na bersiyon nito sa Tagalog ay ang Pasyon ni Gaspar Aquino de Belen (1704) at ang Pasyong Genesis o Pasyon Pilapil "
        "(1814) na naging pangunahing aklat ng pananampalataya sa mga tahanang Pilipino sa loob ng mahigit dalawang siglo."
    )

    add_body_p(
        doc,
        "Sa estruktura at anyo, ang Pasyon ay binubuo ng mga saknong na may limang taludtod (quintilla), kung saan ang bawat taludtod ay may walong "
        "pantig (octosyllabic) na may isahang tugma (aaaaa). Ang ganitong estruktura ay sadyang idinisenyo upang magkaroon ng indayog at madaling kantahin. "
        "Dito sumibol ang tradisyon ng Pabasa—ang sama-samang pag-awit ng buong teksto tuwing Mahal na Araw. Sa pamamagitan ng pag-awit, ang panitikan ay "
        "lumalampas sa pahina; ito ay nagiging gawaing pandinig, performatibo, at panlipunan kung saan nagtitipon ang buong pamayanan upang makinig at magsalu-salo."
    )

    add_body_p(
        doc,
        "Sa pagsusuri ng mensahe at konteksto, mahalagang makilala ang dalawahang mukha ng Pasyon. Sa pananaw ng mga prayleng Espanyol, ang Pasyon ay "
        "kasangkapan upang ituro ang pagpapakumbaba, pagiging masunurin, at pagtitiis sa hirap ng buhay upang makamit ang kaligtasan sa kabilang buhay. "
        "Subalit sa pananaw ng mga katutubong Pilipino, ang salaysay ni Kristo ay naging salamin ng kanilang sariling kalagayan sa ilalim ng kolonyalismo. "
        "Nakita nila ang kanilang sarili kay Kristo na inusig, nilapastangan, at pinahirapan ng mga maykapangyarihang pinuno (mga Pariseo at sundalong Romano), "
        "ngunit sa huli ay nagtagumpay laban sa kamatayan."
    )

    headers_14_1 = ["Lente sa Pagsusuri", "Kahulugan at Katangian sa Pasyon", "Halimbawa / Ebidensiya sa Teksto", "Kabuluhan sa Mapanuring Mambabasa"]
    data_14_1 = [
        ["Anyo at Estruktura", "Quintilla: 5 taludtod bawat saknong, 8 pantig bawat taludtod, isahang tugma", "Hal: 'O Diyos sa kalangitan / Hari ng sangkalupaan / Mabait, maalam, banal...'", "Nagpapakita ng ritmo at musikalidad na angkop sa tradisyong pasalita"],
        ["Paksa at Salaysay", "Buhay, pagpapakasakit, kamatayan, at tagumpay ni Kristo", "Mula sa kasalanan nina Adan at Eba hanggang sa muling pagkabuhay", "Nagsilbing bibliya at aklat-pangkasaysayan ng karaniwang mamamayan"],
        ["Mensahe ng Simbahan", "Pagtitiis, pagpapakumbaba, pagiging masunurin sa mga maykapangyarihan", "Pangangaral na tanggapin ang hirap bilang kaloob ng langit", "Mekanismo ng panlipunang kontrol at kapayapaang kolonyal"],
        ["Katutubong Pahiwatig", "Pag-asa sa paglaya, pagtatagumpay ng api, at pagpapanibago ng loob", "Pasyon at Rebolusyon: inspirasyon sa kilusan nina Hermano Pule at Bonifacio", "Pagpapatunay na ang kahulugan ng teksto ay binubuo rin ng mambabasa"]
    ]
    add_custom_table(doc, headers_14_1, data_14_1)

    add_body_p(
        doc,
        "Dahil dito, ang pagsusuri sa akdang panrelihiyon ay hindi simpleng usapin ng teolohiya o pananampalataya. Ito ay pagsusuri sa kapangyarihan ng wika "
        "at talinghaga. Napatunayan ng mga Pilipino na kahit ang tekstong ipinakilala ng mananakop ay maaaring maging kasangkapan sa paglinang ng katatagan ng "
        "pagkatao, pagkakaisa ng pamayanan, at paggising sa damdaming makabayan."
    )

    add_callout_box(
        doc,
        "MUNTING PAGSASANAY 14.1 (Pagsusuri sa Anyo at Mensahe):\n"
        "1. Ano ang katangian ng anyong quintilla sa Pasyon at bakit napakahalaga nito sa tradisyon ng Pabasa tuwing Mahal na Araw?\n"
        "2. Paano nagkaiba ang layunin ng mga prayle sa layunin ng mga katutubong Pilipino sa pagbabasa at pag-awit ng Pasyon?\n"
        "3. Bakit sinasabing ang pag-awit ng Pasyon ay gawaing panlipunan at hindi pansariling pagdarasal lamang?"
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 18: PAKSA 14.2 - MGA PAHAYAGAN AT WIKANG NASUSULAT
    # =========================================================================
    add_heading_2(doc, "PAKSA 14.2: Mga Pahayagan at Wikang Nasusulat noong Panahon ng Espanyol")
    
    prompt_14_senakulo = (
        "PROMPT: A dramatic, wide-angle depiction of an outdoor community Senakulo passion play staged in a Philippine town plaza. "
        "A local actor portraying the suffering Christ carrying the heavy wooden cross, escorted by costumed Roman soldiers wearing handcrafted tin armor "
        "and red cloaks, surrounded by an emotional crowd of townspeople. Late afternoon dust illuminated by golden sunlight, authentic Philippine folk theater aesthetic --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "DULAANG PANGKASAYSAYAN: ANG SENAKULO SA PLAZA NG BAYAN", prompt_14_senakulo)
    
    add_body_p(
        doc,
        "Kasabay ng mga akdang panrelihiyon, mahalagang bahagi ng tekstong impormasyonal sa panahong kolonyal ang pag-unlad ng mga pahayagan at ng wikang "
        "nasusulat. Bago ang ika-19 na siglo, ang limbagan sa Pilipinas ay halos nakalaan lamang sa mga aklat-dasalan at gramatika ng mga prayle. Subalit "
        "nang pumasok ang ika-19 na siglo, bunsod ng pagbubukas ng Maynila sa pandaigdigang kalakalan noong 1834, sumibol ang pangangailangan sa mabilis "
        "na impormasyon tungkol sa kalakalan, barko, presyo ng bilihin, at mga opisyal na dekreto ng pamahalaan."
    )

    add_body_p(
        doc,
        "Kabilang sa mga naunang pahayagan ang Del Superior Govierno (1811) na pinamatnugutan mismo ng Gobernador-Heneral upang maghatid ng mga balita mula "
        "sa digmaan sa Europa. Sumunod dito ang La Esperanza (1846) bilang unang pang-araw-araw na pahayagan, ang El Comercio, at ang Diariong Tagalog (1882) "
        "na itinatag ni Marcelo H. del Pilar bilang unang pahayagang bilingguwal (Tagalog at Espanyol) na nagtangkang maghatid ng makabayang kamalayan sa mga masa."
    )

    add_body_p(
        doc,
        "Sa pagsusuri ng mga lumang tekstong pampahayagan at pampanitikan, madalas tayong makatagpo ng mga salitang nagbago na ang baybay o hindi na "
        "karaniwang ginagamit ngayon. Halimbawa, ang paggamit ng letrang 'c' at 'qu' sa halip na 'k' (tulad ng 'catotohanan' o 'aquing'), ang pagpapalitan ng "
        "'u' at 'o', at ang mga sinaunang ekspresyon ng paggalang. Sa halip na palitan agad ang mga salitang ito, tungkulin ng mapanuring mag-aaral na "
        "kilalanin ang mga ito bilang mahalagang ebidensiya ng ebolusyon ng ating wika at ortograpiya."
    )

    headers_14_2 = ["Pahayagan / Dokumento", "Taon ng Pagkakatatag", "Wika at Katangian", "Kabuluhang Pangkasaysayan"]
    data_14_2 = [
        ["Del Superior Govierno", "1811", "Espanyol; pormal at opisyal na tono", "Unang pahayagan sa Pilipinas; naglathala ng mga balitang kolonyal at digmaan sa Europa"],
        ["La Esperanza", "1846", "Espanyol; nakatuon sa komersiyo, batas, at panitikan", "Unang pang-araw-araw na pahayagan; nagbukas ng espasyo para sa sanaysay at pagsusuri"],
        ["Ilustracion Filipina", "1859", "Espanyol; may mga kasamang litograpo at dibuho", "Unang pahayagang nagtataglay ng masaganang tekstong biswal at etnograpikong sining"],
        ["Diariong Tagalog", "1882", "Bilingguwal: Tagalog at Espanyol (itinatag ni M.H. del Pilar)", "Unang pahayagang naglathala ng makabayang artikulo sa sariling wika (El Amor Patrio)"]
    ]
    add_custom_table(doc, headers_14_2, data_14_2)

    add_body_p(
        doc,
        "Upang maunawaan ang lumang salita sa isang teksto, ipinapatupad ang apat na hakbang na proseso: (1) Konteksto: basahin ang buong pangungusap; "
        "(2) Pahiwatig: tingnan ang mga katabing salita; (3) Beripikasyon: sumangguni sa talatinigan o batis pangkasaysayan; at (4) Pagpapakahulugan: "
        "ipaliwanag ang kahulugan ayon sa kaisipan ng panahong iyon. Sa pamamagitan ng prosesong ito, naiiwasan ang maling pag-unawa sa diwa ng akda."
    )

    add_callout_box(
        doc,
        "MUNTING PAGSASANAY 14.2 (Pagsusuri sa Pahayagan at Ortograpiya):\n"
        "1. Bakit naging mahalagang hakbang sa kasaysayan ng pamamahayag ang pagkakatatag ng Diariong Tagalog noong 1882?\n"
        "2. Paano nakatutulong ang pagsusuri sa lumang baybay ng mga salita sa pagtukoy ng kapanahunan ng isang makasaysayang dokumento?\n"
        "3. Gamit ang apat na hakbang na proseso, ano ang ibig sabihin ng pariralang 'walang liwag na pagsunod' sa isang ika-19 na siglong dekreto?"
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 19: LUNSARANG TEKSTO - SIPI MULA SA PASYON AT PAHAYAGAN
    # =========================================================================
    add_heading_2(doc, "LUNSARANG TEKSTO: Sipi mula sa Pasyon at Pagbasa sa Pahayagan")
    
    prompt_14_belen = (
        "PROMPT: A dignified historical portrait of Filipino master poet and printer Gaspar Aquino de Belen in 1704 Manila. "
        "Standing beside the historic printing press of the Jesuits, holding a freshly bound copy of his groundbreaking 1704 Mahal na Passion. "
        "Early 18th-century colonial attire, intellectual gravitas, warm studio lighting, classical oil painting portrait style --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "PAMPANITIKANG KASAYSAYAN: SI GASPAR AQUINO DE BELEN (1704)", prompt_14_belen)
    add_body_p(doc, "Pagkakatabi ng Tradisyong Panrelihiyon at Tekstong Impormasyonal para sa Masinsing Paghahambing", italic_prefix="")

    add_heading_3(doc, "Bahagi A: Sipi mula sa Pasyong Henesis (Panawagan sa Mambabasa)")
    add_body_p(
        doc,
        "\"O Diyos sa kalangitan,\n"
        "Hari ng sangkalupaan,\n"
        "Mabait, maalam, banal,\n"
        "Ikaw ang pinagmulan\n"
        "Ng tanang kabutihan.\n\n"
        "Ikaw ang nagpuno't may-ari\n"
        "Sa langit na maluwalhati,\n"
        "Ang mga anghel na marami,\n"
        "May ligayang walang sawi,\n"
        "Puri't pasasalamat lagi.\n\n"
        "At noong lalangin mo\n"
        "Itong bilog na mundo,\n"
        "Gubat, bundok, at damo,\n"
        "Ginawa mo ngang totoo\n"
        "Sa kapurihan ng ngalan mo.\n\n"
        "Tao ay iyong nilikha,\n"
        "Hinubog mula sa lupa,\n"
        "Binigyan ng kaluluwa,\n"
        "Nang maglingkod sa tuwina\n"
        "Sa Maykapal na dakila.\""
    )

    add_heading_3(doc, "Bahagi B: Ulat mula sa Pahayagang 'El Comercio' (1875)")
    add_body_p(
        doc,
        "\"Sa pagdating ng Kuwaresma sa lalawigan ng Bulacan, napansin ng pamunuan ang pambihirang sigla ng mga katutubo sa pagtatayo ng mga kubol para sa "
        "pabasa. Gabi-gabi, ang mga lansangan ay napupuno ng awitan at panalangin. Gayunman, naglabas ng paalaala ang pamahalaang sibil na huwag gawing "
        "dahilan ang pagtitipong panrelihiyon upang magdaos ng mga pag-uusap na walang kinalaman sa simbahan, lalo na't nagbabala ang mga ulat ng guardia civil "
        "laban sa mga tagong pagpupulong ng mga magsasaka sa mga liblib na pook pagkatapos ng pag-awit.\""
    )

    add_body_p(
        doc,
        "Sa pagtatabi ng dalawang tekstong ito, makikita ang kamangha-manghang ugnayan ng panitikan at lipunan. Sa Bahagi A, ipinapakita ang pormal at taimtim "
        "na anyo ng Pasyon na nagpupuri sa kapangyarihan ng Diyos at nagpapaalala sa tungkulin ng tao bilang nilikha. Sa Bahagi B naman, mababasa sa opisyal "
        "na pahayagan ang pangamba ng kolonyal na pamahalaan sa mismong gawaing kanilang ipinakilala. Ang pabasa, na orihinal na nilikha para sa debosyon, "
        "ay naging espasyo kung saan ang mga mamamayan ay nagkakatipon nang legal, nag-uusap tungkol sa kanilang mga hinaing, at nagpapalitan ng mga balita "
        "na mahigpit na ipinagbabawal sa ilalim ng kolonyal na pamamahala."
    )

    add_callout_box(
        doc,
        "MGA GABAY NA TANONG SA PAG-UNAWA SA LUNSARAN:\n"
        "1. Suriin ang estruktura ng saknong sa Bahagi A: Ilang taludtod mayroon ang bawat saknong at ano ang napapansin mo sa tugma ng mga huling salita?\n"
        "2. Bakit nangangamba ang pamahalaang sibil sa ulat ng 'El Comercio' (Bahagi B) sa kabila ng pagiging gawaing panrelihiyon ng pabasa?\n"
        "3. Paano naging daluyan ng lihim na komunikasyon at pagkakaisa ng mga mamamayan ang mga relihiyosong pagtitipon noong panahong kolonyal?"
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 20: SOCRATIC NA TALAKAYAN - ORALIDAD, KULTURA, AT AWIT
    # =========================================================================
    add_heading_2(doc, "SOCRATIC NA TALAKAYAN: Oralidad, Pag-awit, at Kamalayang Panlipunan")
    add_body_p(doc, "Masusing Pagsisiyasat sa Ugnayan ng Musika, Panitikan, at Kapangyarihan", italic_prefix="")

    socratic_dialogue_14 = [
        ("Guro", "Bakit sa tingin ninyo mas piniling awitin (pabasa) ng mga katutubo ang Pasyon kaysa basta basahin lamang ito nang tahimik sa sariling silid?"),
        ("Mag-aaral 1 (Lina)", "Dahil po bago pa dumating ang mga Espanyol, sanay na ang ating mga ninuno sa tradisyong pasalita tulad ng pag-awit ng epiko at awiting-bayan sa tuwing may pagtitipon."),
        ("Guro", "Napakagaling, Lina! Ibig sabihin, ginamit ng mga Pilipino ang kanilang sinaunang pamamaraan ng pakikipagtalastasan upang tanggapin ang bagong relihiyon. Ngayon, ano ang nangyayari sa kahulugan ng isang teksto kapag ito ay inawit nang sabay-sabay ng isang komunidad?"),
        ("Mag-aaral 2 (Joshua)", "Hindi na po ito pagmamay-ari ng sumulat lamang. Nagiging pag-aari na ito ng buong pamayanan. Ang damdamin ng nag-aawit at nakikinig ay nagiging iisa."),
        ("Guro", "Eksakto, Joshua. At kapag naging iisa ang damdamin ng pamayanan sa ilalim ng paghihirap, ano ang nagiging panganib nito para sa isang mananakop?"),
        ("Mag-aaral 3 (Mika)", "Nagiging panganib po ito dahil ang pagkakaisa ng damdamin ang simula ng pagtutol. Nakita ng mga tao na kung si Kristo ay nagtiis ngunit nagtagumpay sa huli, maaari rin silang magtagumpay laban sa mga umaapi sa kanila."),
        ("Guro", "Napakatalas na kaisipan, Mika! Iyan ang tinatawag ng historyador na si Reynaldo Ileto na 'Pasyon and Revolution.' Ngunit paano naman natin mapatutunayan ang interpretasyong ito gamit ang ebidensiya?"),
        ("Mag-aaral 4 (Paolo)", "Makikita po sa mga ulat ng guardia civil na ang mga kilusang tulad ng Cofradia de San Jose ni Hermano Pule at maging ang Katipunan ay gumamit ng mga talinghaga ng liwanag, dilim, kalinisan ng loob, at pagpapakasakit na matatagpuan din sa Pasyon."),
        ("Guro", "Tumpak, Paolo! Ipinakikita nito na ang panitikan ay hindi nakakulong sa pahina ng aklat. Ang panitikan ay may buhay, humihinga sa tinig ng tao, at may kakayahang bumago sa takbo ng kasaysayan.")
    ]

    for speaker, text in socratic_dialogue_14:
        p = doc.add_paragraph()
        format_paragraph(p, space_before=2, space_after=3)
        r_spk = p.add_run(f"{speaker}: ")
        r_spk.font.name = 'Cambria'
        r_spk.font.size = Pt(10)
        r_spk.font.bold = True
        r_spk.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D) if "Guro" in speaker else RGBColor(0x8B, 0x1A, 0x1A)
        r_txt = p.add_run(f"\"{text}\"")
        r_txt.font.name = 'Cambria'
        r_txt.font.size = Pt(10)

    add_callout_box(
        doc,
        "HAMONG SOCRATIC (Pagsusuri sa Salita at Kapangyarihan):\n"
        "Sumulat ng isang masinsing talata (5–7 pangungusap) na sumasagot sa hamon:\n"
        "\"Paano napatunayan sa kasaysayan ng Pilipinas na ang isang akdang nilikha upang magpasunod ay naging mitsa ng paglaya ng kaisipan?\"\n"
        "Gamitin sa iyong paliwanag ang mga konseptong: tradisyong pasalita, talinghaga ng pagpapakasakit, pagkakaisa ng pamayanan, at pagpapanibago ng loob."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 21: PAKSA 14.3 - ANTAS NG PAMUMUHAY AT ELEMENTONG BISWAL
    # =========================================================================
    add_heading_2(doc, "PAKSA 14.3: Antas ng Pamumuhay at Elementong Biswal ng Comic Book Brochure")
    
    add_body_p(
        doc,
        "Ang antas ng pamumuhay sa lipunang kolonyal noong panahon ng Espanyol ay mahigpit na nakatali sa lahi, yaman, lupa, at ugnayan sa Simbahan. "
        "Sa pisikal na anyo ng bayan, makikita ang antas na ito sa layo ng tirahan mula sa plaza. Ang mga pamilyang kabilang sa principalia at mayayamang "
        "mestizo ay naninirahan sa mga bahay-na-bato na nakapaligid mismo sa liwasan, samantalang ang mga karaniwang magsasaka at manggagawa ay nakatira "
        "sa mga bahay-kubo sa mga liblib na baryo o sakahan. Ang agwat na ito ay masasalamin din sa uri ng kasuotan, edukasyon, at akses sa mga kalakal."
    )

    add_body_p(
        doc,
        "Sa pagbuo ng isang makasaysayang comic book brochure, napakahalagang maunawaan kung paano isinasalin ang mga panlipunang katotohanang ito sa mga "
        "elementong biswal. Ang komiks ay hindi lamang drowing; ito ay isang masalimuot na gramatika ng mga panel, espasyo, framing, at visual emphasis. "
        "Kapag naglalarawan ng isang eksena sa liwasan o sa loob ng simbahan, ang posisyon ng mga tauhan sa foreground (unahan) at background (likuran) "
        "ay nagtatakda kung kaninong pananaw ang binibigyang-diin ng kuwento."
    )

    visual_prompt_14 = (
        "PROMPT: A poignant historical comic book panel illustration depicting a nighttime pabasa ritual in an authentic 19th-century Philippine village. "
        "In the center foreground, a warm glowing lantern illuminates a wooden table where an open weathered manuscript of the Pasyon rests. "
        "A multi-generational native family—an elderly grandmother in a traditional baro't saya, a young mother holding an infant, and a teenage boy singing intently— "
        "surrounds the table with solemn devotion. In the midground, neighbors gathered on bamboo benches sharing rice cakes (kakanin) under the nipa eaves. "
        "In the shadowy background outside the illuminated hut, the faint silhouette of two Spanish guardia civil patrolling on horseback in the misty moonlit night, "
        "creating a tense atmospheric contrast between community warmth and colonial surveillance. High-contrast chiaroscuro lighting, emotional realism --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "KONSEPTONG BISWAL AT PROMPT SA COMIC PANEL (PABASA AT LIPUNAN)", visual_prompt_14)

    add_body_p(
        doc,
        "Ang ugnayan ng teksto at larawan sa komiks ay dapat komplementaryo—nagpupunan at hindi nag-uulit. Kung malinaw na sa drowing na ang tauhan ay "
        "naghihirap dahil sa kaniyang payat na pangangatawan at sirang damit, hindi na kailangang sabihin sa caption na 'Siya ay mahirap.' Sa halip, "
        "dapat gamitin ang caption upang ilahad ang konteksto: 'Ang paniningil ng labis na buwis sa ilalim ng bandala ang nag-iwan sa kaniyang pamilya "
        "nang walang aning pambuhay.' Sa ganitong paraan, nagiging matalino, siksik, at makabuluhan ang bawat panel ng brochure."
    )

    headers_14_3 = ["Elementong Biswal", "Gampanin sa Komiks", "Halimbawa sa Tagpong Kolonyal", "Mapanuring Tuntunin sa Pagdisenyo"]
    data_14_3 = [
        ["Panel Layout", "Nagtatakda ng bilis at daloy ng salaysay", "Paggamit ng pahalang na panel para sa malawak na liwasan; patayong panel para sa mataas na kampanaryo", "Iwasan ang sobrang sikip na pagkakaayos upang maging maginhawa ang pagbasa."],
        ["Foreground (Unahan)", "Nagbibigay ng pangunahing pokus at emosyonal na diin", "Mukha ng mang-aawit ng pasyon na may pumatak na luha habang nagdarasal", "Dapat malinaw ang detalye ng ekspresyon upang maiparating ang damdamin."],
        ["Background (Likuran)", "Nagbibigay ng kontekstong historikal, espasyo, at panlipunang kalagayan", "Ang marangyang kumbento sa likod ng mga naghihirap na magsasaka sa pilapil", "Huwag iwang blangko; ang background ay nagpapatunay ng historikal na tagpuan."],
        ["Speech Balloon", "Naglalaman ng buhay na tinig at diyalogo ng tauhan", "Diyalogo ng pagtutol o panalangin ng mga katutubong tauhan", "Dapat matipid at natural; hindi dapat takpan ang mukha o mahalagang bahagi ng drowing."]
    ]
    add_custom_table(doc, headers_14_3, data_14_3)

    add_callout_box(
        doc,
        "MUNTING PAGSASANAY 14.3 (Pagsusuri sa Disenyong Multimodal):\n"
        "1. Paano nakatutulong ang contrast sa pagitan ng foreground at background sa pagpapakita ng hindi pagkakapantay-pantay sa lipunang kolonyal?\n"
        "2. Bakit sinasabing ang caption ay dapat magdagdag ng konteksto at hindi mag-ulit ng nakikita na sa larawan?\n"
        "3. Paano mo gagamitin ang panel layout upang ipakita ang pagkakaiba ng marangyang buhay sa poblasyon laban sa payak na buhay sa kabukiran?"
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 22: MGA GAWAING PAMPAGKATUTO 14.1 AT 14.2
    # =========================================================================
    add_heading_2(doc, "MGA GAWAING PAMPAGKATUTO SA ARALIN 14")
    add_heading_3(doc, "Gawain 14.1: Mula Paksa tungo sa Mensahe ng Akdang Panrelihiyon")
    add_body_p(
        doc,
        "Panuto: Gamit ang lunsarang sipi ng Pasyon sa pahina 19, punan ang sumusunod na analytical matrix. Tiyakin na ang bawat sagot ay sinusuportahan "
        "ng tiyak na linya o saknong mula sa binasang teksto bilang matibay na ebidensiya."
    )

    headers_g14_1 = ["Elemento ng Akda", "Pagsusuri sa Nilalaman ng Pasyon", "Tiyak na Ebidensiya mula sa Saknong", "Interpretasyon at Konteksto"]
    data_g14_1 = [
        ["Paksa (Tungkol saan?)", "Ang kapangyarihan ng Diyos sa paglikha sa daigdig at sa tao", "\"At noong lalangin mo / Itong bilog na mundo...\"", "Ipinakikita ang Diyos bilang tanging may-ari ng lahat ng likas na yaman."],
        ["Mensahe (Anong kaisipan?)", "Ang tao ay may dakilang pananagutan na maglingkod sa Maykapal nang may kalinisan ng loob", "\"Tao ay iyong nilikha / Hinubog mula sa lupa...\"", "Ang paglilingkod ay dapat bukal sa loob at hindi dahil sa takot sa parusa."],
        ["Anyo at Tugma", "Quintilla: 5 taludtod bawat saknong na may isahang tugma", "\"Diyos sa kalangitan / sangkalupaan / pinagmulan / kabutihan\"", "Ang ritmo ay nagpapadali sa pagsasaulo ng mga mamamayang hindi marunong bumasa."],
        ["Katutubong Pananaw", "Pagkilala sa kabanalan ng kapaligiran at pagkakapantay-pantay ng tao", "\"Gubat, bundok, at damo / Ginawa mo ngang totoo...\"", "Ugnayan ng sinaunang animismo sa paggalang sa kalikasan bilang likha ng Diyos."]
    ]
    add_custom_table(doc, headers_g14_1, data_g14_1)

    add_heading_3(doc, "Gawain 14.2: Imbestigador ng Lumang Pahayagan at Pagbabago ng Wika")
    add_body_p(
        doc,
        "Sitwasyon: Isipin na nakatuklas ka ng isang lumang pahina ng ulat noong 1885 ngunit napunit ang itaas na bahagi kung saan nakasulat ang petsa "
        "at pangalan ng sumulat. Mababasa sa natitirang talata: \"Ipinag-utos ng alcaldia mayor na ang lahat ng mga cabeza de barangay ay magtipon sa tribunal "
        "upang isulit ang natipong tributo at ilista ang mga polistang gagawa sa bagong kalsada.\""
    )

    add_body_p(
        doc,
        "Hakbang 1: Pangkatin ang impormasyon sa tatlong kategorya:\n"
        "• Tiyak na Makikita sa Teksto: ___________________________________________________________________________________________\n"
        "• Posibleng Hinuha / Interpretasyon: _____________________________________________________________________________________\n"
        "• Hindi Pa Matitiyak (Kailangan ng Batis): _______________________________________________________________________________\n\n"
        "Hakbang 2: Sumulat ng 4–6 na pangungusap na nagpapaliwanag kung bakit mapanganib na hulaan agad ang petsa o motibo ng dokumento nang walang karagdagang batis."
    )

    add_callout_box(
        doc,
        "DISIPLINA SA PANANALIKSIK:\n"
        "Ang isang tunay na iskolar at mapanuring mambabasa ay may lakas ng loob na sabihing 'Hindi pa ito matitiyak' sa halip na gumawa ng haka-haka. "
        "Ang pagkilala sa limitasyon ng datos ay tanda ng mataas na antas ng katapatang intelektuwal."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 23: GAWAIN 14.3 - STORYBOARD AT ANALITIKONG RUBRIK
    # =========================================================================
    add_heading_2(doc, "Gawain 14.3: Biswal na Rekonstruksiyon — Storyboard ng Kolonyal na Pamayanan")
    add_body_p(
        doc,
        "Gawain: Bumuo ng isang 4-panel storyboard para sa comic book brochure na nagpapakita ng tagpo ng tradisyong Pabasa sa isang baryo noong panahong "
        "kolonyal. Ipakita ang ugnayan ng debosyon, antas ng pamumuhay, at ang lihim na hangarin ng pamayanan para sa katarungan at kapayapaan."
    )

    add_body_p(
        doc,
        "Mga Detalyeng Dapat Ilahad sa Bawat Panel ng Storyboard:\n"
        "• Panel 1 (Tagpuan at Atmospera): Deskripsiyon ng liwasan o looban ng nayon sa dapithapon; mga lampara at kubol; background ng simbahan.\n"
        "• Panel 2 (Pangunahing Kilos): Ang pamilya at kapitbahay na nag-aawit ng Pasyon sa harap ng altar; caption na nagpapaliwanag sa kahulugan ng awit.\n"
        "• Panel 3 (Tensiyon at Panlipunang Kalagayan): Pagdaan ng mga sundalo o guardia civil sa labas ng kubol; palitan ng makahulugang tingin ng mga mamamayan.\n"
        "• Panel 4 (Pangwakas na Kaisipan): Pagsasalu-salo ng pamayanan at pagpapatibay ng kanilang loob sa pamamagitan ng pagkakaisa at pananampalataya."
    )

    headers_rubrik_14 = ["Pamantayan", "Napakahusay (4)", "Mahusay (3)", "Nalilinang (2)", "Nangangailangan ng Gabay (1)"]
    data_rubrik_14 = [
        ["Lalim ng Konteksto at Salaysay (25%)", "Napakalinaw at makatotohanan ang pagkakaugnay ng Pasyon sa antas ng pamumuhay at kalagayang kolonyal.", "Malinaw ang karamihan sa mga historikal na ugnayan; angkop ang tagpo ng pabasa sa panahon.", "Mababaw ang pagkakaugnay; parang modernong pagtitipon lamang ang inilarawan.", "Walang kaugnayan sa aralin; hindi maipakita ang historikal na konteksto."],
        ["Organisasyong Biswal (Panel at Diin) (25%)", "Napakatalas ng pagkakagamit sa foreground, background, at framing upang lumikha ng damdamin at tensiyon.", "Maayos ang pagkakabalanse ng mga elemento sa bawat panel; malinaw ang pokus ng eksena.", "Medyo magulo ang komposisyon; hindi malinaw kung ano ang pangunahing binibigyang-diin.", "Walang kaayusan ang mga panel; walang pagkakaiba ang unahan sa likuran."],
        ["Caption at Diyalogo (25%)", "Makabuluhan at matipid ang mga salita; nagbibigay ng malalim na konteksto nang hindi inuulit ang larawan.", "Malinaw at angkop ang mga caption at diyalogo sa sitwasyon ng mga tauhan.", "Medyo mahaba o inuulit lamang ang eksaktong nakikita na sa drowing.", "Magulo ang wika; maraming mali sa gramatika at hindi angkop sa tauhan."],
        ["Dignidad at Representasyon (25%)", "Ganap na magalang, makatarungan, at walang bahid ng stereotype ang paglalarawan sa mga katutubong tauhan.", "Responsable at maingat ang paglalarawan sa pamayanang Pilipino.", "May ilang bahagi na nagpapakita ng mapanghusgang paglalarawan sa kahirapan.", "Malinaw na gumagamit ng mapanirang stereotype sa mga karaniwang mamamayan."]
    ]
    add_custom_table(doc, headers_rubrik_14, data_rubrik_14)

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 24: PAGNINILAY, EXIT TICKET, AT BUOD NG ARALIN 14
    # =========================================================================
    add_heading_2(doc, "PAGNINILAY, EXIT TICKET, AT BUOD NG ARALIN 14")
    add_heading_3(doc, "Metakognitibong Pagninilay sa Aralin 14")
    add_body_p(
        doc,
        "Panuto: Matapos himayin ang Pasyon, mga lumang pahayagan, at ang disenyong multimodal, kumpletuhin ang mga sumusunod na pahayag upang "
        "ipakita ang paglalim ng iyong pagsusuri sa kapangyarihan ng panitikan at wika."
    )

    reflection_prompts_14 = [
        "1. Ang pinakamahalagang pagbabago sa aking pagkaunawa sa Pasyon ay __________________________________________________________________________________________________.",
        "2. Sa pagbasa ng mga lumang dokumento, natutuhan kong maging maingat sa mga salitang hindi ko pamilyar sa pamamagitan ng __________________________________________________________________________________________________.",
        "3. Kapag nagdidisenyo ako ng comic panel, gagamitin ko ang background upang __________________________________________________________________________________________________.",
        "4. Napatunayan ko na ang wika at musika ay naging sandata ng mga Pilipino sa pagharap sa kahirapan dahil __________________________________________________________________________________________________."
    ]
    for prm in reflection_prompts_14:
        add_body_p(doc, prm)

    add_heading_3(doc, "Exit Ticket: Pasyon, Pahayagan, at Panel")
    add_body_p(
        doc,
        "• PASYON: Isang talinghaga mula sa Pasyon na nagpapakita ng katatagan ng loob: ___________________________________________________\n"
        "• PAHAYAGAN: Isang katanungang dapat laging itanong sa pagsusuri ng lumang balita: _________________________________________________\n"
        "• PANEL: Isang prinsipyong biswal na gagamitin ko upang maiwasan ang stereotype sa komiks: ________________________________________"
    )

    add_callout_box(
        doc,
        "SINTESIS AT BUOD NG ARALIN 14:\n"
        "1. Ang Pasyon ay hindi lamang tekstong panrelihiyon kundi salamin ng kolektibong kamalayan at pakikipagkapuwa ng mga Pilipino. Sa pamamagitan "
        "ng Pabasa, naging espasyo ito ng pagkakaisa, pag-asa, at lihim na pagtutol sa kolonyal na kaapihan.\n"
        "2. Ang pag-usbong ng mga pahayagan noong ika-19 na siglo ay nagdulot ng bagong paraan ng pagpapalaganap ng impormasyon na sumasalamin sa interes "
        "ng mga namumuno, na nagbunsod naman ng pangangailangan sa kritikal na beripikasyon ng mga datos.\n"
        "3. Ang ebolusyon ng wika at ortograpiya ay nagpapakita ng dinamikong kasaysayan ng pambansang wika; ang mga lumang salita ay dapat suriin ayon "
        "sa konteksto at hindi basta palitan ng modernong termino nang walang pagsisiyasat.\n"
        "4. Sa disenyong multimodal ng komiks, ang panel, foreground, background, at caption ay nagtutulungan upang lumikha ng makabuluhan, responsable, "
        "at makatarungang representasyon ng lipunan at kasaysayang Pilipino."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 25: MABILISANG PAGTATAYA SA ARALIN 14 (BAHAGI I: AYTEM 1-8)
    # =========================================================================
    add_heading_2(doc, "MABILISANG PAGTATAYA SA ARALIN 14 (15 PUNTOS)")
    add_heading_3(doc, "Bahagi I: Mapanuring Pagpili (Aytem 1 hanggang 8)")
    add_body_p(doc, "Panuto: Piliin ang titik ng pinakatumpak na sagot. Isulat ang malaking titik sa patlang bago ang bawat bilang.")

    mcq_items_14_p1 = [
        ("1. Ano ang tawag sa tradisyonal na anyo ng saknong ng Pasyon na binubuo ng limang taludtod na may walong pantig bawat isa?",
         ["A. Dalit", "B. Quintilla", "C. Tanaga", "D. Diona"]),
        ("2. Paano naiiba ang layunin ng mga prayle sa layunin ng mga katutubong Pilipino sa pagpapalaganap ng Pasyon?",
         ["A. Nais ng mga prayle na maging makata ang lahat, samantalang nais ng mga katutubo na maging mang-aawit.",
          "B. Ginamit ito ng mga prayle upang ituro ang pagpapasakop, samantalang nakita ng mga katutubo ang pag-asa sa pagtatagumpay ng mga api.",
          "C. Nais ng mga prayle na ibenta ang aklat, samantalang ipinamigay ito ng mga katutubo nang libre.",
          "D. Walang anumang pagkakaiba sa kanilang naging pagtanggap sa akda."]),
        ("3. Bakit itinuturing na gawaing panlipunan (social practice) ang Pabasa sa kulturang Pilipino?",
         ["A. Dahil binabayaran ng pamahalaan ang lahat ng nakikinig sa pag-awit.",
          "B. Dahil ito ay sama-samang isinasagawa sa mga tahanan kung saan nagtitipon, nag-uusap, at nagsasalu-salo ang pamayanan.",
          "C. Dahil ipinagbabawal ang pag-awit nito sa loob ng mga pribadong silid.",
          "D. Dahil mga dayuhan lamang ang pinapayagang magbasa nito."]),
        ("4. Alin sa mga sumusunod ang unang pang-araw-araw na pahayagan sa Pilipinas na itinatag noong 1846?",
         ["A. Del Superior Govierno", "B. La Esperanza", "C. Diariong Tagalog", "D. La Solidaridad"]),
        ("5. Sa pagsusuri ng isang lumang dokumento na may salitang hindi na ginagamit ngayon, ano ang PINAKARESPONSABLENG unang hakbang?",
         ["A. Palitan agad ito ng pinakamalapit na modernong salitang maisip.",
          "B. Basahin ang buong pangungusap upang matukoy ang kontekstuwal na pahiwatig bago sumangguni sa talatinigan.",
          "C. Burahin ang salita upang hindi malito ang mga mambabasa.",
          "D. Ipagpalagay na mali ang baybay ng may-akda noong unang panahon."]),
        ("6. Ano ang pangunahing gampanin ng 'foreground' sa pagbuo ng isang makasaysayang comic panel?",
         ["A. Ipakita ang malalayong bundok at ulap sa likuran.",
          "B. Ituon ang pansin ng mambabasa sa pangunahing tauhan, kilos, at emosyon ng tagpo.",
          "C. Punuin ang espasyo ng mga dekorasyong walang kaugnayan sa kuwento.",
          "D. Takpan ang mga pagkakamali sa pagguhit ng mga gusali."]),
        ("7. Paano dapat magtulungan ang caption at ang larawan sa isang responsableng comic book brochure?",
         ["A. Dapat ulitin ng caption ang bawat bagay na iginuhit sa larawan.",
          "B. Dapat magbigay ang caption ng konteksto o impormasyong hindi kayang ipakita ng larawan lamang.",
          "C. Dapat magkasalungat ang sinasabi ng caption sa ipinapakita ng larawan.",
          "D. Dapat mas marami ang salita kaysa sa espasyo ng drowing."]),
        ("8. Bakit mapanganib na gumawa ng pangkalahatang kongklusyon tungkol sa buong lipunan mula lamang sa isang larawan ng marangyang bahay-na-bato?",
         ["A. Dahil baka nasunog na ang bahay sa kasalukuyan.",
          "B. Dahil ang larawan ay kumakatawan lamang sa uring maykaya at hindi sumasalamin sa kalagayan ng mayoryang magsasaka.",
          "C. Dahil laging peke ang mga lumang larawan.",
          "D. Dahil hindi mahalaga ang arkitektura sa pag-aaral ng panitikan."])
    ]

    for q_text, choices in mcq_items_14_p1:
        add_body_p(doc, q_text, bold_prefix="")
        for ch in choices:
            p_c = doc.add_paragraph()
            format_paragraph(p_c, space_before=1, space_after=1)
            p_c.paragraph_format.left_indent = Inches(0.2)
            r_c = p_c.add_run(ch)
            r_c.font.name = 'Cambria'
            r_c.font.size = Pt(9.5)

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 26: MABILISANG PAGTATAYA (BAHAGI I KONT. AT BAHAGI II: PAGSUSURI)
    # =========================================================================
    add_heading_2(doc, "MABILISANG PAGTATAYA SA ARALIN 14 (PAGPAPATULOY)")
    add_heading_3(doc, "Bahagi I (Pagpapatuloy: Aytem 9 at 10)")

    mcq_items_14_p2 = [
        ("9. Ano ang ipinahihiwatig ng pag-uulat ng pahayagang 'El Comercio' (1875) tungkol sa mga lihim na pag-uusap ng mga katutubo sa panahon ng Kuwaresma?",
         ["A. Na walang pakialam ang pamahalaan sa mga gawaing panrelihiyon.",
          "B. Na naging lehitimong panakip ang relihiyosong pagtitipon upang mag-usap ang mga mamamayan tungkol sa kanilang mga hinaing.",
          "C. Na mas gusto ng mga magsasaka na magbasa ng diyaryo kaysa umawit ng Pasyon.",
          "D. Na ipinagbawal ng pamahalaan ang pagbebenta ng Pasyon sa buong kapuluan."]),
        ("10. Sa pagguhit ng mga tauhan sa isang historikal na komiks, paano maiiwasan ang stereotype sa mga mahihirap na mamamayan?",
         ["A. Huwag na silang isama sa alinmang panel ng komiks.",
          "B. Ipakita sila na may sariling dignidad, talino, aktibong pagkilos, at kontekstuwal na katotohanan.",
          "C. Bihisan sila ng modernong kasuotan upang magmukhang mayaman.",
          "D. Gawin silang katawa-tawa upang maging masaya ang mambabasa."])
    ]

    for q_text, choices in mcq_items_14_p2:
        add_body_p(doc, q_text, bold_prefix="")
        for ch in choices:
            p_c = doc.add_paragraph()
            format_paragraph(p_c, space_before=1, space_after=1)
            p_c.paragraph_format.left_indent = Inches(0.2)
            r_c = p_c.add_run(ch)
            r_c.font.name = 'Cambria'
            r_c.font.size = Pt(9.5)

    add_heading_3(doc, "Bahagi II: Masinsing Pagsusuri at Pagbibigay-Katwiran (Aytem 11 hanggang 15)")
    add_body_p(doc, "Panuto: Sagutin ang bawat katanungan sa 3 hanggang 5 masinsing pangungusap. (1 puntos bawat aytem)")

    open_items_14 = [
        "11. Ipaliwanag ang dalawang dahilan kung bakit napakahalaga ng ritmo, sukat, at tugma sa mabilis na paglaganap ng Pasyon sa kapuluan.",
        "12. Ano ang pagkakaiba ng ebidensiya at interpretasyon sa pagsusuri ng isang sipi mula sa lumang pahayagan? Magbigay ng kongkretong halimbawa.",
        "13. Paano nakatutulong ang pahayagan sa pag-aaral ng isang tiyak na panahon, at ano ang isang pangunahing limitasyon nito bilang sanggunian?",
        "14. Sa pagbuo ng comic panel, paano magagamit ang kaibahan ng laki at posisyon ng tauhan upang ipahiwatig ang kapangyarihang panlipunan?",
        "15. Sa iyong sariling pananaw, paano naging daan ang Pasyon upang maipamalas ng mga Pilipino ang katatagan ng kanilang pagkatao sa gitna ng dusa?"
    ]

    for o_q in open_items_14:
        p_oq = doc.add_paragraph()
        format_paragraph(p_oq, space_before=3, space_after=2)
        r_oq = p_oq.add_run(o_q)
        r_oq.font.name = 'Cambria'
        r_oq.font.size = Pt(10)
        r_oq.font.bold = True

    add_callout_box(
        doc,
        "PAMANTAYAN SA PAGMAMARKA NG BAHAGI II:\n"
        "• 1.0 Puntos: Tumpak at malalim ang paliwanag, may maayos na lohika, at nagtataglay ng tiyak na ebidensiya mula sa aralin.\n"
        "• 0.5 Puntos: Bahagyang wasto ngunit kulang sa pagpapalalim o walang halimbawang sumusuporta.\n"
        "• 0.0 Puntos: Hindi tumutugon sa katanungan o mali ang ibinigay na katuwiran."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 27: ARALIN 14 TRANSITION & PAGHAHANDA SA ARALIN 15
    # =========================================================================
    add_heading_2(doc, "PAGLALAGOM AT TULAY PATUNGO SA ARALIN 15")
    
    add_body_p(
        doc,
        "Sa Aralin 14, nasilip natin ang lalim ng kaluluwang Pilipino sa pamamagitan ng Pasyon at mga tekstong panrelihiyon. Napatunayan natin na ang "
        "panitikan ay hindi lamang pasibong sumasalamin sa buhay kundi aktibong humuhubog sa damdamin at nagbibigay ng lakas sa pamayanan upang harapin "
        "ang mga unos ng kasaysayan. Natutuhan din nating suriin ang mga lumang pahayagan nang may kritikal na pag-iingat at gamitin ang mga elementong "
        "biswal upang lumikha ng makabuluhang komiks."
    )

    add_body_p(
        doc,
        "Kung sa Pasyon ay tiningnan natin ang ugnayan ng tao sa Diyos at sa kaniyang pamayanan sa pamamagitan ng pananampalataya, sa Aralin 15 naman ay "
        "haharapin natin ang isa pang mahalagang anyo ng panitikang kolonyal: ang akdang pangkagandahang-asal. Sa pamamagitan ng klasikong liham ni "
        "Urbana kay Feliza, sisisirin natin kung paano hinubog ng kolonyalismo ang pamantayan ng wastong kilos, kalinisan, pakikipagkapuwa, at ang "
        "tungkulin ng kababaihan sa lipunan."
    )

    add_callout_box(
        doc,
        "PASILIP SA ARALIN 15: URBANA AT FELIZA AT WIKANG PANG-KOMIK BROCHURE\n"
        "• Bakit naging batayan ng magandang asal sa buong kapuluan ang mga liham nina Urbana at Feliza noong ika-19 na siglo?\n"
        "• Paano natin susuriin ang mga payo tungkol sa kalinisan at kagandahang-asal nang hindi nahuhulog sa bitag ng presentismo?\n"
        "• Paano nakatutulong ang mahusay na panayam at wastong gramatika ng mga diyalogo upang makalikha ng de-kalidad na multimodal na teksto?"
    )

    doc.add_page_break()
