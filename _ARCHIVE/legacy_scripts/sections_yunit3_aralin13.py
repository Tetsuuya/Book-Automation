# -*- coding: utf-8 -*-
"""Aralin 13 Builder: Pages 4 to 15 (12 Full Pages)"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from generate_expanded_ebook import (
    format_paragraph, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_prompt_box, add_callout_box, add_custom_table,
    add_multimedia_box, set_cell_shading
)

def build_yunit3_aralin13(doc):
    # =========================================================================
    # PAHINA 4: PANIMULA, LAYUNIN, AT MULTIMEDIA CORNER #1
    # =========================================================================
    add_heading_1(doc, "ARALIN 13: Ang Panitikan sa Panahong Sakop ng Espanya ang Pilipinas")
    add_heading_2(doc, "MGA LAYUNIN AT BALANGKAS NG PAGKATUTO")
    add_body_p(
        doc,
        "Sa araling ito, bubuksan ang Yunit III sa pamamagitan ng masusing pagbasa at pagsusuri sa panitikan sa ilalim ng kolonyalismong Espanyol. "
        "Bibigyang-diin ang kaligirang pangkasaysayan bilang pangunahing salalayan ng pag-unawa sa mga akdang lumaganap sa panahong ito. "
        "Matututuhan ng mga mag-aaral na ang panitikan ay hindi nagsimula sa pagdating ng mga banyaga; bagkus, mayroon nang maunlad na tradisyong "
        "pasalita ang mga katutubong Pilipino na nakipagtagpo at nakipagtunggali sa mga bagong anyong ipinakilala ng mga mananakop. Tatalakayin din ang "
        "tekstong paglalahad, nailathalang balita, panghihiram at pagtutumbas ng salita, at ang representasyon ng etnisidad sa mga tekstong biswal at multimodal."
    )

    add_body_p(
        doc,
        "1. F7PN-IIIa-1: Nailalahad ang kaligirang pangkasaysayan ng mga tekstong pampanitikan sa Panahon ng Pananakop ng Espanya.\n"
        "2. F7PB-IIIa-2: Nasusuri ang mga elemento, detalye, mensahe, at konteksto ng tekstong paglalahad at nailathalang balita.\n"
        "3. F7PT-IIIa-3: Naipaliliwanag ang wastong paraan ng panghihiram at pagtutumbas ng mga salita ayon sa konteksto ng pangungusap.\n"
        "4. F7PD-IIIa-4: Nasusuri ang representasyon ng etnisidad at antas ng pamumuhay sa mga tekstong biswal at multimodal.\n"
        "5. F7PU-IIIa-5: Nakabubuo ng borador ng comic book brochure na nagpapakita ng makabuluhang tagpo nang may pananagutang historikal.",
        bold_prefix="Mga Kasanayang Pampagkatuto (MATATAG Competencies):\n"
    )

    add_body_p(
        doc,
        "• Paano binago ng pananakop ng Espanya ang anyo, daluyan, at layunin ng panitikan sa Pilipinas nang hindi ganap na nabubura ang katutubong kamalayan?\n"
        "• Bakit mahalagang suriin ang pinagmulan at layunin ng isang nailathalang balita bago ito tanggapin bilang obhetibong katotohanan?\n"
        "• Paano nakatutulong ang maingat na panghihiram at pagtutumbas ng salita sa pagpapanatili ng katumpakan ng kahulugan at dignidad ng kultura?",
        bold_prefix="Mga Susing Katanungan para sa Aralin:\n"
    )

    add_multimedia_box(
        doc,
        mod_title="Pagsusuri sa Unang Limbag na Aklat sa Pilipinas",
        vid_title="Doctrina Christiana (1593): Ang Pambansang Kayamanan at Unang Limbag sa Pilipinas",
        channel="National Historical Commission of the Philippines (NHCP) / Pambansang Aklatan",
        link="https://www.youtube.com/results?search_query=National+Historical+Commission+Doctrina+Christiana+1593",
        qr_code_text="",
        timestamps=[
            "01:15 - 04:30: Ang Tradisyong Pasalita bago ang 1565 at ang Pagdating ng Palimbagan sa Maynila.",
            "04:31 - 08:45: Pagsusuri sa Orihinal na Manuskrito ng Doctrina Christiana sa Library of Congress.",
            "08:46 - 12:50: Ang Paggamit ng Baybayin at Titik Latin sa mga Unang Nilimbag na Akda."
        ],
        questions=[
            "Ayon sa dokumentaryo, bakit napakahalaga ng preserbasyon ng orihinal na sipi ng Doctrina Christiana para sa kasaysayan ng literasi sa Pilipinas?",
            "Paano pinatutunayan ng aklat na mayroon nang maunlad na sistema ng pagsulat (Baybayin) ang mga katutubong Tagalog bago pa man dumating ang mga Espanyol?",
            "Magtala ng dalawang salitang hiram sa Espanyol na ginagamit mo araw-araw at ipaliwanag ang konteksto ng paggamit nito."
        ]
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 5: PAKSA 13.1 - PANITIKAN AT KALIGIRANG PANGKASAYSAYAN
    # =========================================================================
    add_heading_2(doc, "PAKSA 13.1: Panitikan at Kaligirang Pangkasaysayan sa Panahon ng Espanyol")
    
    prompt_13_1 = (
        "PROMPT: A detailed historical narrative illustration of a 16th-century Dominican xylographic woodblock printing workshop in Intramuros Manila, 1593. "
        "A skilled native Tagalog woodcarver and master printer working side-by-side with a Spanish Dominican friar, carefully inspecting a freshly inked page of "
        "Doctrina Christiana on handmade mulberry paper. Carved wooden printing blocks displaying Baybayin and Latin script, ink rollers, and candle lanterns in "
        "a rustic stone colonial workshop. Warm morning sunlight filtering through timber windows, authentic archival realism, 8k resolution --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "LARAWANG PANGKASAYSAYAN: ANG PALIMBAGAN AT DOCTRINA CHRISTIANA (1593)", prompt_13_1)
    
    add_body_p(
        doc,
        "Ang kaligirang pangkasaysayan ay tumutukoy sa kabuuan ng mga kondisyong panlipunan, pampolitika, pang-ekonomiya, at kultural na umiiral sa panahon "
        "ng paglikha at paglaganap ng isang akdang pampanitikan. Sa pagsusuri ng panitikan sa Panahon ng Pananakop ng Espanya (1565–1898), mahalagang kilalanin "
        "na ang kapuluan ay sumailalim sa isang masalimuot na sistema ng kolonyalismo. Sa pamamagitan ng patakarang reduccion, sapilitang pinagsama-sama ang "
        "mga kalat-kalat na pamayanang barangay patungo sa mga bayang nakasentro sa plaza complex—sa ilalim ng tunog ng kampana ng simbahan at pamahalaan."
    )

    add_body_p(
        doc,
        "Dahil sa sentralisasyong ito, ang panitikan ay naging pangunahing instrumento sa pagpapatatag ng kapangyarihang kolonyal. Ang mga tradisyonal na "
        "anyong pasalita tulad ng epiko, mitolohiya, at mga ritwal ng babaylan ay ipinagbawal o pinalitan ng mga akdang nakasentro sa pananampalatayang Katoliko. "
        "Ipinakilala ang palimbagan noong 1593 sa pamamagitan ng Doctrina Christiana. Sa unang pagkakataon, ang panitikang dating nakasalalay sa pagbigkas at "
        "kolektibong memorya ng pamayanan ay naging nakasulat at nakalimbag sa papel, na mahigpit na binabantayan ng sensor ng Simbahan."
    )

    add_body_p(
        doc,
        "Gayunpaman, isang pagkakamali na ipalagay na ganap na nawala ang katutubong identidad. Ang mga Pilipino ay hindi naging pasibong tagatanggap lamang "
        "ng banyagang kultura. Sa proseso ng inkulturasyon at sinkretismo, matalinong ginamit ng mga katutubo ang mga banyagang estruktura upang ipagpatuloy "
        "ang kanilang sariling damdamin at talinghaga. Ang sukat at tugma ng katutubong tula ay nanatili sa mga dalit at awit, at ang pagmamahal sa kalayaan "
        "ay lihim na ibinaon sa mga salaysay ng pagdurusa at pagtubos."
    )

    headers_13_1 = ["Panahon / Aspekto", "Kalagayang Panlipunan", "Pangunahing Anyo ng Panitikan", "Layunin at Gamit ng Akda"]
    data_13_1 = [
        ["Bago ang Pananakop (Katutubo)", "Malalayang barangay; ugnayan sa kalikasan; pamumuno ng datu at babaylan", "Pasalitang panitikan: Bugtong, Salawikain, Epiko, Awiting-bayan", "Pagkakakilanlan ng tribo; ritwal; edukasyong komunal"],
        ["Panimulang Kolonyalismo (Ika-16 - 17 Siglo)", "Reduccion; encomienda; pagpasok ng mga prayle at palimbagan", "Doctrina Christiana, katekismo, dasal, nobena, bokabularyo", "Kristiyanisasyon; pagpapalaganap ng doktrina; kolonyal na kontrol"],
        ["Lumalagong Kolonyalismo (Ika-18 - 19 Siglo)", "Plaza complex; pag-usbong ng uring mestizo at ilustrado; agrikulturang komersiyal", "Pasyon, Komedya/Moro-moro, Senakulo, Awit at Korido, Liham-aral", "Moralidad; libangan ng pamayanan; pagsisimula ng kamalayang panlipunan"]
    ]
    add_custom_table(doc, headers_13_1, data_13_1)

    add_body_p(
        doc,
        "Sa kontekstuwalisadong pagbasa, hindi natin hinahatulan ang mga lumang akda gamit lamang ang makabagong pananaw (iwasan ang presentismo). "
        "Sa halip, sinusuri natin kung ano ang kahulugan ng akda sa sarili nitong panahon, sino ang sumulat, para kanino ito isinulat, at paano ito naging "
        "patunay ng kakayahan ng mga Pilipinong magpatuloy at umangkop sa gitna ng matitinding pagsubok sa kanilang pagkatao at kalayaan."
    )

    add_callout_box(
        doc,
        "MUNTING PAGSASANAY 13.1 (Pagsusuri sa Konteksto):\n"
        "1. Bakit naging sentral ang plaza complex at palimbagan sa pagbabago ng panitikang Pilipino noong panahon ng Espanyol?\n"
        "2. Paano napanatili ng mga katutubo ang kanilang sariling talino at sensibilidad sa kabila ng mahigpit na sensura ng mga prayle?\n"
        "3. Ipaliwanag ang ibig sabihin ng presentismo at bakit dapat itong iwasan sa pag-aaral ng kasaysayan at panitikan."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 6: PAKSA 13.2 - NAILATHALANG BALITA AT PAGLALAHAD
    # =========================================================================
    add_heading_2(doc, "PAKSA 13.2: Nailathalang Balita at Panghihiram o Pagtutumbas ng Salita")
    
    prompt_13_plaza = (
        "PROMPT: A wide panoramic aerial illustration of an early 17th-century Philippine colonial town (Pueblo) laid out under the Reduccion system. "
        "In the center, an imposing stone church with a tall belfry and spacious plaza mayor surrounded by administrative convento, tribunal, and tiled-roof houses. "
        "Native farmers and river boatmen arriving at the market arcade under golden tropical afternoon light. Historically authentic architectural reconstruction --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "KULTURA AT LIPUNAN: ANG SISTEMANG REDUCCION AT PLAZA COMPLEX", prompt_13_plaza)
    
    add_body_p(
        doc,
        "Ang paglalahad ay isang diskursong naglalayong magpaliwanag, magbigay-linaw, at maghatid ng organisado at obhetibong impormasyon nang walang "
        "kinikilingang emosyon o opinyon. Sa ilalim ng MATATAG kurikulum, mahalagang kasanayan ang pagsusuri sa tekstong ekspositori at nailathalang balita. "
        "Noong Panahon ng Pananakop ng Espanya, ang paglabas ng mga unang pahayagan tulad ng Del Superior Govierno (1811) at La Esperanza (1846) ay nagbunsod "
        "ng bagong paraan ng komunikasyon na dati ay hindi nararanasan sa tradisyong pasalita."
    )

    add_body_p(
        doc,
        "Ang isang nailathalang balita ay sumasagot sa mga pangunahing tanong: Sino, Ano, Kailan, Saan, Bakit, at Paano. Gayunpaman, ang bawat balita ay "
        "isinusulat mula sa isang tiyak na pananaw at interes. Noong panahon ng kolonyalismo, karamihan sa mga pahayagan ay pag-aari ng pamahalaan o ng "
        "mga korporasyong relihiyoso. Dahil dito, ang mga ulat tungkol sa mga pagtitipon, kalakalan, at kaayusang pambayan ay sumasalamin sa interes ng mga "
        "namumuno. Ang mapanuring mambabasa ay kailangang matutong maghiwalay sa tuwirang datos (faktwal) laban sa interpretasyon at adyenda ng sumulat."
    )

    add_body_p(
        doc,
        "Kaagapay ng pag-usbong ng pamamahayag ang dinamikong transpormasyon ng wika sa pamamagitan ng panghihiram at pagtutumbas ng mga salita. "
        "Ang panghihiram ay ang natural na pag-aangkop ng salita mula sa banyagang wika (Espanyol) patungo sa Filipino upang punan ang kakulangan sa mga "
        "bagong konseptong administratibo, legal, teknolohikal, at panrelihiyon. Ang pagtutumbas naman ay ang maingat na paghahanap ng pinakamalapit at "
        "pinakaangkop na salita sa sariling wika na nagtataglay ng eksaktong kahulugan ng banyagang termino."
    )

    headers_13_2 = ["Konsepto sa Wika", "Kahulugan at Tuntunin", "Halimbawa mula sa Tekstong Kolonyal", "Modernong Gamit sa Filipino"]
    data_13_2 = [
        ["Tuwirang Panghihiram", "Pagkuha ng salita na may pagbabago sa baybay alinsunod sa ortograpiyang Filipino", "Alcalde → Alkalde; Gobernador → Gobernador; Iglesia → Simbahan / Iglesya", "Pangangasiwa ng pamahalaang lokal; legal na katawagan"],
        ["Pagtutumbas ng Termino", "Paggamit ng katutubong salita na katumbas ng banyagang kaisipan sa konteksto", "Ayuntamiento → Pamahalaang Lungsod; Justicia → Katarungan; Orden → Kaayusan", "Pormal na talumpati, balita, at akademikong sanaysay"],
        ["Saling Pahiwatig", "Paglikha ng tambalan o parirala upang maipaliwanag ang banyagang institusyon", "Tribunal → Bahay-pamahalaan; Casa Real → Maharlikang Tahanan", "Pagsulat ng historikal na komiks at modyul pampagkatuto"]
    ]
    add_custom_table(doc, headers_13_2, data_13_2)

    add_body_p(
        doc,
        "Sa pamamahayag, mapanganib ang padalus-dalos na panghihiram kung mayroon namang umiiral at mayamang katumbas sa Filipino. Ang labis na paggamit "
        "ng salitang banyaga nang walang malinaw na layunin ay maaaring magpalabo sa diwa ng balita at lumikha ng pader sa pagitan ng manunulat at ng mambabasa. "
        "Ang responsableng mamamahayag ay nagtitimbang: humihiram lamang kung kinakailangan para sa teknikal na katumpakan, at nagtutumbas upang mapanatili "
        "ang linaw, dalisay na kahulugan, at kasarinlan ng pambansang wika."
    )

    add_callout_box(
        doc,
        "MUNTING PAGSASANAY 13.2 (Pagsusuri sa Balita at Wika):\n"
        "1. Ano ang pagkakaiba ng faktwal na detalye sa interpretasyon sa loob ng isang nailathalang ulat noong panahong kolonyal?\n"
        "2. Bakit kinakailangang suriin ang motibo o pinagmulan ng isang pahayagan bago paniwalaan ang nilalaman nito?\n"
        "3. Ibigay ang angkop na katumbas sa Filipino ng mga sumusunod na salitang Espanyol batay sa konteksto ng pamahalaan: decreto, bando, cabildo."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 7: LUNSARANG TEKSTO - ANG ULAT SA LIWASAN AT ANG LIHAM NG KURA
    # =========================================================================
    add_heading_2(doc, "LUNSARANG TEKSTO: Ang Ulat sa Liwasan at ang Liham ng Kura")
    add_body_p(doc, "Orihinal na Tekstong Pangkasaysayan at Ekspositori para sa Masinsing Pagsusuri", italic_prefix="")

    add_body_p(
        doc,
        "Noong ika-14 ng Oktubre 1872, naglathala ang isang pahayagan sa Maynila ng maikling balita tungkol sa ginanap na pagtitipon sa liwasan ng bayan "
        "ng San Gabriel. Ayon sa nakalimbag na ulat, ang pagtitipon ay dinaluhan ng mga punong-bayan, mga kawani ng tribunal, at mga karaniwang mamamayan "
        "upang pakinggan ang bagong bando o kautusan mula sa pamahalaang sibil. Inilarawan ng mamamahayag ang okasyon bilang isang patunay ng 'ganap na "
        "katahimikan, masiglang pagsunod, at walang-maliw na katapatan ng mga indio sa kapangyarihan ng Inang Espanya.' Binanggit din sa ulat na masayang "
        "tinanggap ng mga magsasaka ang pagtatakda ng bagong buwis sa tabako at palay bilang ambag sa kaunlaran ng kolonya."
    )

    add_body_p(
        doc,
        "Gayunpaman, sa isang lihim na liham na natuklasan sa sinupan ng parokya makalipas ang maraming taon, iba ang naging ulat ng kura paroko sa kaniyang "
        "probinsiyal. Ayon sa kura: 'Ang mga tao sa liwasan ay nagtipon hindi dahil sa kagalakan kundi dahil sa takot sa mga sundalong nagbabantay sa bawat "
        "sulok ng plaza. Walang nagsalita nang basahin ang bando, ngunit ang kanilang katahimikan ay hindi tanda ng pagsang-ayon kundi ng nagbabantang poot. "
        "Ang mga katutubo ay nagbubulung-bulungan sa ilalim ng mga punong mangga, at marami sa mga pamilya ang nagbabalak na lumikas patungo sa kabundukan "
        "upang maiwasan ang paniningil ng hindi makatwirang tributo at polo y servicio.'"
    )

    add_body_p(
        doc,
        "Nang ihambing ng mga modernong mag-aaral ng kasaysayan ang dalawang dokumento, natuklasan nila ang malaking bangin sa pagitan ng nailathalang balita "
        "at ng aktuwal na kalagayang panlipunan. Ang opisyal na pahayagan ay gumamit ng mga piling salita tulad ng 'marangal,' 'mapayapa,' at 'tapat' upang "
        "lumikha ng ilusyon ng kaayusan para sa mga mambabasa sa kabisera at sa Espanya. Samantala, ang kumpidensiyal na liham ng prayle ay nagbunyag ng "
        "tunay na tensiyon, pangamba, at maramihang pagtutol ng mga mamamayang naipit sa marahas na sistema ng kolonyal na pamamahala."
    )

    add_body_p(
        doc,
        "Ipinakikita ng lunsarang tekstong ito na ang teksto ay laging may konteksto. Ang isang dokumento ay hindi kailanman ganap na hiwalay sa kapangyarihan "
        "ng nagpalimbag nito. Sa pag-aaral ng panitikan at kasaysayan, ang kritikal na mag-aaral ay hindi tumitigil sa pagbasa ng nakalimbag na salita; "
        "nagtatanong siya: Kaninong tinig ang narinig? Kaninong tinig ang pinatahimik? At anong mga ebidensiya ang kinakailangan upang matuklasan ang "
        "katotohanang nakakubli sa likod ng opisyal na pahayag?"
    )

    add_callout_box(
        doc,
        "MGA GABAY NA TANONG SA PAG-UNAWA SA LUNSARAN:\n"
        "1. Ano ang pangunahing pagkakaiba sa tono, mensahe, at layunin ng nailathalang balita kumpara sa liham ng kura paroko?\n"
        "2. Paano ginamit sa opisyal na ulat ang mga salitang 'mapayapa' at 'masiglang pagsunod' upang tabingan ang tunay na reaksiyon ng mga mamamayan?\n"
        "3. Ano ang panganib kung ang opisyal na balita lamang ang gagamiting batayan sa pagsulat ng kasaysayan ng bayan ng San Gabriel?\n"
        "4. Paano maiuugnay ang aral ng tekstong ito sa paraan ng ating pagsusuri sa mga balita at impormasyon sa social media sa kasalukuyan?"
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 8: SOCRATIC NA TALAKAYAN - KATOTOHANAN, PAGLALAHAD, AT BATIS
    # =========================================================================
    add_heading_2(doc, "SOCRATIC NA TALAKAYAN: Katotohanan, Paglalahad, at Kontekstuwal na Batis")
    add_body_p(doc, "Pilosopikal at Mapanuring Palitan ng Katuwiran sa Pagitan ng Guro at mga Mag-aaral", italic_prefix="")

    socratic_dialogue = [
        ("Guro", "Kung babasahin natin ang opisyal na balita sa pahayagan noong 1872, masasabi ba nating nagsinungaling ang mamamahayag, o naglahad lamang siya ayon sa kaniyang pananaw?"),
        ("Mag-aaral 1 (Mika)", "Para po sa akin, hindi lamang ito simpleng pagkakaiba ng pananaw; may sadya pong pagtatakip. Ginamit niya ang kaniyang posisyon upang paboran ang pamahalaan dahil kontrolado ng kolonyal na opisyal ang pahayagan."),
        ("Guro", "Napakahusay na obserbasyon, Mika. Ngunit paano kung sabihin ng mamamahayag na totoo namang tahimik ang mga tao sa liwasan at walang nagprotesta nang hayagan? Hindi ba totoo ang kaniyang nakita?"),
        ("Mag-aaral 2 (Paolo)", "Maaaring totoo po ang kaniyang 'obserbasyon' na walang sumisigaw, ngunit mali ang kaniyang 'interpretasyon' na ang katahimikan ay nangangahulugang pagsang-ayon. Hindi niya isinama ang takot ng mga tao sa mga sundalong may baril."),
        ("Guro", "Eksakto, Paolo! Iyan ang pinakabuod ng kritikal na literasi: ang paghihiwalay sa tuwirang datos laban sa interpretasyon. Ngayon, tingnan natin ang liham ng prayle. Dahil ba lihim ito at sumalungat sa balita, awtomatiko ba nating tatanggapin na 100% totoo ang lahat ng sinabi ng kura?"),
        ("Mag-aaral 3 (Lina)", "Hindi rin po dapat tanggapin agad nang walang pagsusuri. May sarili rin pong motibo ang kura—maaaring pinalalaki niya ang banta ng rebelyon upang humingi ng karagdagang guardia civil o proteksiyon para sa kaniyang kumbento."),
        ("Guro", "Napakatalas, Lina! Kung parehong may motibo ang pahayagan at ang liham, paano ngayon bubuo ng makatwirang kongklusyon ang isang mag-aaral ng panitikan at kasaysayan?"),
        ("Mag-aaral 4 (Joshua)", "Kailangan pong maghanap ng ikatlo o higit pang batis—tulad ng mga talaarawan ng mga katutubo, mga opisyal na tala ng buwis, o mga awiting-bayan sa panahong iyon. Ang katotohanan ay nabubuo sa pagtatagpi-tagpi ng maraming ebidensiya."),
        ("Guro", "Tumpak! Ang panitikan at kasaysayan ay hindi koleksiyon ng mga pinal na sagot, kundi patuloy na pagsisiyasat gamit ang matibay na ebidensiya at malalim na pag-unawa sa kalagayan ng tao.")
    ]

    for speaker, text in socratic_dialogue:
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
        "HAMONG SOCRATIC (Pagninilay at Pagpapalalim):\n"
        "Sumulat ng isang masinsing talata (5–7 pangungusap) bilang tugon sa tanong:\n"
        "\"Bakit ang katahimikan ng isang pamayanan sa ilalim ng pamumuno ay hindi kailanman sapat na patunay ng kanilang kaligayahan o pagsang-ayon?\"\n"
        "Gumamit ng hindi bababa sa dalawang konseptong tinalakay sa seminar: ebidensiya, interpretasyon, konteksto, o panlipunang kontrol."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 9: PAKSA 13.3 - ETNISIDAD, TEKSTONG BISWAL, AT MULTIMODAL
    # =========================================================================
    add_heading_2(doc, "PAKSA 13.3: Etnisidad, Tekstong Biswal, at Gawaing Multimodal")
    
    add_body_p(
        doc,
        "Ang etnisidad ay tumutukoy sa pagkakakilanlang kultural ng isang pangkat ng tao na pinagbubuklod ng magkakatulad na wika, kasaysayan, tradisyon, "
        "paniniwala, at pinagmulang pamayanan. Sa Panahon ng Pananakop ng Espanya, ang etnisidad ay ginamit ng pamahalaang kolonyal upang magtatag ng isang "
        "hirarkikal na kaayusang panlipunan. Sa sistemang ito, ang mga Espanyol na ipinanganak sa Espanya (peninsulares) at sa Pilipinas (insulares) ang nasa "
        "tuktok, kasunod ang mga mestizo, samantalang ang mga katutubong naninirahan sa kapatagan ay tinawag na indio, at ang mga pangkat sa kabundukan na hindi "
        "napasailalim sa binyag ay itinuring na infieles o remontados."
    )

    add_body_p(
        doc,
        "Sa pagsusuri ng mga tekstong biswal noong panahong kolonyal—tulad ng mga litograpo, dibuho sa mga aklat, at mga selyo—makikita kung paano "
        "naging kasangkapan ang imahen sa pagbuo ng stereotype. Ang mga katutubo ay madalas iguhit na nakayuko, payak ang kasuotan, at gumagawa ng mabibigat "
        "na gawaing-kamay, samantalang ang mga opisyal na kolonyal at prayle ay inilalarawan sa gitna ng komposisyon, nakatayo nang tuwid, at may hawak na "
        "aklat o kapangyarihan. Ang ganitong biswal na representasyon ay hindi aksidente; layunin nitong itanim sa isip ng mambabasa na natural ang paghahari "
        "ng dayuhan sa katutubo."
    )

    visual_prompt_13 = (
        "PROMPT: A detailed historical concept art illustration for an educational comic book panel depicting the diverse ethnicity and social strata "
        "in a 19th-century Philippine colonial plaza. In the center foreground, a Tagalog native clerk (principalia) dressed in a translucent embroidered barong tagalog "
        "and black trousers, holding an official document quill with an expression of quiet defiance. To his left, an indigenous Cordilleran Igorot warrior in authentic "
        "woven bahag and traditional tattoos observing from the market stalls. To the right, a Spanish alferez in military uniform standing haughtily near the stone fountain. "
        "In the background, bustling multi-ethnic trade with Chinese mestizo merchants and native market women selling textiles and produce under tile-roofed colonial arcades. "
        "Atmospheric warm daylight, cinematic depth of field, historically accurate architectural and costume details --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "KONSEPTONG BISWAL AT PROMPT SA PAGLIKHA NG COMIC PANEL (ETNISIDAD AT LIPUNAN)", visual_prompt_13)

    add_body_p(
        doc,
        "Sa pagbuo ng multimodal na teksto tulad ng comic book brochure, tungkulin ng mag-aaral na bawiin ang dignidad ng mga katutubong pangkat. "
        "Ang multimodal na teksto ay pinagsamang salita, larawan, kulay, espasyo, at layout upang makalikha ng isang buong kahulugan. Hindi dapat ilarawan "
        "ang mga katutubo bilang mga walang mukhang biktima o mga primitibong nilalang. Sa halip, kailangang ipakita ang kanilang mayamang kultura, sariling "
        "ahensiya (kakayahang magpasya at kumilos), at ang katatagan ng kanilang pagkatao sa harap ng panggigipit."
    )

    headers_13_3 = ["Elementong Biswal sa Komiks", "Kahulugan at Layunin sa Eksena", "Tanong sa Responsableng Pag-edit"]
    data_13_3 = [
        ["Panel at Framing", "Pagtatakda ng hangganan ng tagpo upang ituon ang pansin ng mambabasa", "Sino ang nasa gitna ng frame? Nabibigyan ba ng kaukulang diin ang katutubong tauhan?"],
        ["Foreground at Background", "Paghihiwalay ng pangunahing kilos sa kontekstong panlipunan at historikal", "Mayroon bang makabuluhang detalye sa likuran na nagpapakita ng tunay na kalagayan ng bayan?"],
        ["Speech Balloon at Diyalogo", "Pagbibigay ng sariling tinig at kaisipan sa mga tauhan", "Angkop ba ang pananalita sa antas ng tauhan nang hindi nagiging katawa-tawa o mapanghamak?"],
        ["Kasuotan at Kagamitan", "Biswal na pagpapakita ng kultura, hanapbuhay, at katayuan", "Nasaliksik ba nang tumpak ang kasuotan upang maiwasan ang mga maling stereotype?"]
    ]
    add_custom_table(doc, headers_13_3, data_13_3)

    add_callout_box(
        doc,
        "MUNTING PAGSASANAY 13.3 (Biswal at Multimodal na Pagsusuri):\n"
        "1. Bakit hindi neutral ang paraan ng pagguhit sa mga tauhan sa isang historikal na larawan o komiks?\n"
        "2. Paano makatutulong ang wastong pagsasaliksik sa kasuotan at kagamitan upang maiwasan ang stereotype sa mga katutubong Pilipino?\n"
        "3. Ano ang kahalagahan ng speech balloon sa pagbibigay ng kapangyarihan sa mga tauhang madalas pinatahimik sa kasaysayan?"
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 10: MGA GAWAING PAMPAGKATUTO 13.1 AT 13.2
    # =========================================================================
    add_heading_2(doc, "MGA GAWAING PAMPAGKATUTO SA ARALIN 13")
    add_heading_3(doc, "Gawain 13.1: Pagkilatis sa Katotohanan, Paglalahad, at Batis")
    add_body_p(
        doc,
        "Panuto: Basahing mabuti ang sumusunod na mga pahayag mula sa mga historikal na ulat noong panahon ng Espanyol. Tukuyin kung ang bawat aytem "
        "ay maituturing na (A) Tuwirang Faktwal na Datos, (B) May Pagkiling na Interpretasyon ng May-akda, o (C) Mapanlahatang Stereotype. "
        "Isulat ang titik ng iyong sagot sa patlang at magbigay ng maikling paliwanag sa iyong naging batayan."
    )

    drill_items_13 = [
        "1. ______ \"Nagsimula ang pagpapatupad ng bagong buwis sa tabako noong unang araw ng Enero 1782 sa ilalim ng kautusan ng Gobernador-Heneral.\"",
        "2. ______ \"Ang lahat ng mga katutubo sa lalawigan ay likas na tamad at ayaw magtrabaho kung hindi gagamitan ng latigo ng pamahalaan.\"",
        "3. ______ \"Pinasinayaan ang bagong tulay na bato sa ilog ng Pasig na pinondohan mula sa ambag ng mga mangangalakal sa Maynila.\"",
        "4. ______ \"Buong galak at pasasalamat na tinanggap ng mga mamamayan ang pagdating ng bagong kura paroko sa kanilang munisipyo.\"",
        "5. ______ \"Ayon sa opisyal na sensus ng parokya noong 1850, mayroong 4,230 binyagang mamamayan na naninirahan sa loob ng poblasyon.\""
    ]
    for itm in drill_items_13:
        add_body_p(doc, itm)

    add_heading_3(doc, "Gawain 13.2: Masinsing Matrix ng Konteksto at Panghihiram ng Salita")
    add_body_p(
        doc,
        "Panuto: Suriin ang mga sumusunod na salitang hiram mula sa Espanyol na malimit gamitin sa mga dokumento at panitikan noong panahong kolonyal. "
        "Punan ang talahanayan sa pamamagitan ng pagbibigay ng orihinal na kahulugan sa kontekstong Espanyol, ang katumbas nito sa sariling wika, "
        "at isang makabuluhang pangungusap na nagpapakita ng mapanuring paggamit nito sa kasalukuyang lipunang Pilipino."
    )

    headers_matrix_13 = ["Salitang Hiram", "Konteksto sa Panahong Espanyol", "Angkop na Katumbas sa Filipino", "Makabuluhang Pangungusap sa Kasalukuyan"]
    data_matrix_13 = [
        ["Tributo", "Buwis na sapilitang ibinabayad ng mga katutubo sa pamahalaan", "Buwis / Bayad-pananagutan", "Hal: Ang tapat na pagbabayad ng buwis ay dapat masuklian ng tapat na serbisyo."],
        ["Polo y Servicio", "Sapilitang paggawa ng mga kalalakihang katutubo sa loob ng 40 araw", "Sapilitang Paggawa / Paglilingkod", "Hal: __________________________________________________"],
        ["Principalia", "Uring panlipunan ng mga maykaya at dating maharlika sa bayan", "Uring Maykaya / Pamunuan", "Hal: __________________________________________________"],
        ["Bandala", "Sapilitang pagbebenta ng ani ng mga magsasaka sa pamahalaan", "Sapilitang Pagtatapyas ng Ani", "Hal: __________________________________________________"],
        ["Cedula Personal", "Dokumento ng pagkakakilanlan at patunay ng pagbabayad ng buwis", "Katibayan ng Pagkakakilanlan", "Hal: __________________________________________________"]
    ]
    add_custom_table(doc, headers_matrix_13, data_matrix_13)

    add_callout_box(
        doc,
        "GABAY SA PAGPUPUNO NG MATRIX:\n"
        "Tiyakin na ang binuong pangungusap ay hindi lamang naglalarawan ng kahulugan ng salita, kundi nag-uugnay sa kahalagahan ng katarungang panlipunan, "
        "karapatang pantao, at mapanuring pagkaunawa sa kasaysayan ng ating bansa."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 11: GAWAIN 13.3 - GAWAING PAGGANAP AT ANALITIKONG RUBRIK
    # =========================================================================
    add_heading_2(doc, "Gawain 13.3: Autentikong Gawaing Pagganap — Borador ng Comic Book Brochure")
    add_body_p(
        doc,
        "Sitwasyon: Ikaw ay naatasan ng Pambansang Komisyong Pangkasaysayan na maging punong manunulat at tagapagdisenyo ng isang pang-edukasyong "
        "comic book brochure na ipapamahagi sa mga mag-aaral sa Baitang 7. Ang layunin ng brochure ay ipakita ang isang makabuluhang tagpo sa isang "
        "karaniwang bayan noong ika-19 na siglo kung saan nagtagpo ang dalawang magkasalungat na pananaw: ang opisyal na ulat ng pamahalaang kolonyal "
        "at ang lihim na damdamin ng mga katutubong mamamayan."
    )

    add_body_p(
        doc,
        "Mga Bahaging Dapat Buuin sa Borador:\n"
        "1. Pamagat ng Comic Brochure: Makatawag-pansing pamagat na naglalaman ng pangunahing tema ng aralin.\n"
        "2. Balangkas ng Apat na Panel (Storyboard Framework):\n"
        "   • Panel 1 (Tagpuan at Konteksto): Ipakita ang plaza complex, simbahan, at ang pagdating ng opisyal na tagapagbalita ng bando.\n"
        "   • Panel 2 (Ang Opisyal na Pahayag): Ipakita ang pagbasa ng kautusan at ang reaksiyon ng mga maykapangyarihan.\n"
        "   • Panel 3 (Ang Lihim na Tinig): Ipakita ang pag-uusap ng dalawang katutubo sa gilid ng liwasan na nagpapahayag ng kanilang tunay na saloobin.\n"
        "   • Panel 4 (Pangwakas at Pag-asa): Ipakita ang kapasyahan ng mga mamamayan na magkaisa at ingatan ang kanilang sariling kultura at dignidad.\n"
        "3. Pagsulat ng Caption at Diyalogo: Tiyaking wasto ang gramatika, natural ang tono, at angkop sa kontekstong historikal nang walang stereotype."
    )

    headers_rubrik_13 = ["Pamantayan", "Napakahusay (4)", "Mahusay (3)", "Nalilinang (2)", "Nangangailangan ng Gabay (1)"]
    data_rubrik_13 = [
        ["Katumpakang Historikal at Konteksto (25%)", "Ganap na tumpak ang mga detalye ng tagpuan, patakaran, at panlipunang kalagayan; walang anachronism.", "Tumpak ang karamihan sa mga historikal na detalye; may isa o dalawang maliliit na kakulangan sa konteksto.", "May ilang maling impormasyon o hindi angkop na historikal na kaisipan sa tagpo.", "Maraming maling detalye sa kasaysayan; hindi maunawaan ang kontekstong kolonyal."],
        ["Diyalogo at Boses ng Tauhan (25%)", "Mapanuri, natural, at malinaw ang diyalogo; may natatanging boses ang bawat tauhan na angkop sa kaniyang uri at katayuan.", "Malinaw at maayos ang diyalogo; kadalasang angkop ang pananalita sa mga tauhan.", "Medyo artipisyal o pare-pareho ang paraan ng pananalita ng magkakaibang tauhan.", "Hindi angkop ang diyalogo; magulo ang pananalita at gumagamit ng mga modernong balbal."],
        ["Organisasyong Biswal at Multimodal (25%)", "Napakalinaw ng daloy ng mga panel; mahusay na nagpupunan ang larawan, caption, at speech balloons upang bumuo ng kahulugan.", "Maayos ang daloy ng kuwento; malinaw ang ugnayan ng teksto at deskripsiyon ng biswal.", "May ilang bahagi na nagiging paulit-ulit ang sinasabi ng teksto sa nakikita sa larawan.", "Magulo ang pagkakasunod-sunod ng mga panel; walang malinaw na ugnayan ang teksto at biswal."],
        ["Etikal na Representasyon (25%)", "Ganap na umiiwas sa stereotype; binibigyang-diin ang ahensiya, talino, at dignidad ng mga katutubong tauhan.", "Responsable ang paglalarawan; halos walang bahid ng mapanghamak na stereotype.", "May ilang simplistikong paglalarawan sa mga katutubo bilang mga walang magawang biktima.", "Malinaw na nagpapakita ng mapanghusga at mapanlahatang stereotype sa mga pangkat-etniko."]
    ]
    add_custom_table(doc, headers_rubrik_13, data_rubrik_13)

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 12: PAGNINILAY, EXIT TICKET, AT BUOD NG ARALIN 13
    # =========================================================================
    add_heading_2(doc, "PAGNINILAY, METAKOGNITIBONG EXIT TICKET, AT BUOD")
    add_heading_3(doc, "Metakognitibong Pagninilay ng Mag-aaral")
    add_body_p(
        doc,
        "Panuto: Matapos ang masusing pag-aaral sa Aralin 13, pagnilayan ang iyong naging paglalakbay sa pagkatuto. Kumpletuhin ang mga sumusunod "
        "na pahayag nang buong katapatan upang masuri ang pagbabago sa iyong pananaw bilang isang mapanuring mag-aaral ng panitikan."
    )

    reflection_prompts_13 = [
        "1. Bago ko pinag-aralan ang Aralin 13, ang akala ko sa panitikan noong panahon ng Espanyol ay __________________________________________________________________________________________________.",
        "2. Napagtanto ko na ang isang nailathalang balita mula sa nakaraan ay hindi dapat tanggapin agad bilang ganap na katotohanan dahil __________________________________________________________________________________________________.",
        "3. Ang pinakamahalagang kasanayan na natutuhan ko sa paghihiwalay ng tuwirang datos laban sa interpretasyon ay __________________________________________________________________________________________________.",
        "4. Bilang tagapagdisenyo ng multimodal na comic brochure, sisikapin kong iwasan ang stereotype sa pamamagitan ng __________________________________________________________________________________________________."
    ]
    for prm in reflection_prompts_13:
        add_body_p(doc, prm)

    add_heading_3(doc, "Exit Ticket: 3-2-1 ng Aralin 13")
    add_body_p(
        doc,
        "• 3 Mahahalagang Konsepto na Aking Natutuhan: (1) ________________________, (2) ________________________, (3) ________________________\n"
        "• 2 Kasanayang Aking Nalinang sa Pagsusuri ng Teksto: (1) ________________________, (2) ________________________\n"
        "• 1 Malaking Katanungan na Nais Ko Pang Masagot sa Susunod na Aralin: __________________________________________________________________"
    )

    add_callout_box(
        doc,
        "SINTESIS AT BUOD NG ARALIN 13:\n"
        "1. Ang panitikan sa Panahon ng Pananakop ng Espanya ay sumailalim sa matinding impluwensiya ng Simbahan at pamahalaang kolonyal sa pamamagitan "
        "ng reduccion at palimbagan, ngunit nagpatuloy ang katutubong kamalayan sa pamamagitan ng malikhaing pag-aangkop at sinkretismo.\n"
        "2. Ang tekstong paglalahad at nailathalang balita ay naghahatid ng impormasyon ngunit laging nagtataglay ng pananaw at kapangyarihan ng naglathala. "
        "Kailangang suriin ang motibo, pinagmulan, at nawawalang tinig sa bawat ulat.\n"
        "3. Ang panghihiram at pagtutumbas ng salita ay dapat isagawa nang may pananagutan upang mapanatili ang katumpakan at kasarinlan ng sariling wika.\n"
        "4. Ang representasyon ng etnisidad sa mga tekstong biswal ay nangangailangan ng etikal na pagsusuri upang maiwasan ang mapanirang stereotype at "
        "maitanghal ang tunay na dignidad ng pagkataong Pilipino."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 13: MABILISANG PAGTATAYA SA ARALIN 13 (BAHAGI I: AYTEM 1-8)
    # =========================================================================
    add_heading_2(doc, "MABILISANG PAGTATAYA SA ARALIN 13 (15 PUNTOS)")
    add_heading_3(doc, "Bahagi I: Mapanuring Pagpili (Aytem 1 hanggang 8)")
    add_body_p(doc, "Panuto: Piliin ang titik ng pinakatumpak na sagot. Isulat ang malaking titik sa patlang bago ang bawat bilang.")

    mcq_items_13_p1 = [
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
        ("3. Bakit itinuturing na may 'pananaw' o hindi ganap na neutral ang mga opisyal na balitang inilathala noong panahong kolonyal?",
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
          "D. Dahil mas mura ang magiging gastusin sa pagpapalimbag ng aklat."])
    ]

    for q_text, choices in mcq_items_13_p1:
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
    # PAHINA 14: MABILISANG PAGTATAYA (BAHAGI I KONT. AT BAHAGI II: PAGSUSURI)
    # =========================================================================
    add_heading_2(doc, "MABILISANG PAGTATAYA SA ARALIN 13 (PAGPAPATULOY)")
    add_heading_3(doc, "Bahagi I (Pagpapatuloy: Aytem 9 at 10)")

    mcq_items_13_p2 = [
        ("9. Sa pagbuo ng isang responsableng balita, ano ang unang dapat gawin kapag nakatanggap ng ulat na may magkasalungat na pahayag?",
         ["A. Beripikahin ang impormasyon sa iba pang mapagkakatiwalaang batis at ilahad ang magkakaibang panig nang patas.",
          "B. Piliin agad ang pahayag ng may pinakamataas na katungkulan at balewalain ang iba.",
          "C. Huwag nang isulat ang balita upang maiwasan ang gulo.",
          "D. Gumawa ng sariling kuwento na magugustuhan ng mga mambabasa."]),
        ("10. Alin sa mga sumusunod ang nagpapakita ng ahensiya at katatagan ng mga katutubong Pilipino sa kabila ng pananakop?",
         ["A. Ang ganap na pagtalikod sa lahat ng katutubong kaugalian nang walang pagtutol.",
          "B. Ang pagtanggap sa lahat ng banyagang batas nang hindi nagtatanong.",
          "C. Ang paglalangkap ng sariling ritmo, talinghaga, at damdamin sa loob ng mga ipinakilalang anyong banyaga.",
          "D. Ang paglimot sa sariling wika upang magsalita lamang ng Espanyol."])
    ]

    for q_text, choices in mcq_items_13_p2:
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

    open_items_13 = [
        "11. Ipaliwanag kung bakit hindi sapat na basahin lamang ang literal na teksto ng isang lumang dokumento upang maunawaan ang tunay na mensahe nito.",
        "12. Paano naiiba ang paraan ng pagpapahayag ng katotohanan sa tradisyong pasalita kumpara sa nakalimbag na pamamahayag noong panahon ng Espanyol?",
        "13. Magbigay ng isang kongkretong halimbawa kung paano maaaring magbunga ng maling interpretasyon ang padalus-dalos na panghihiram ng salitang banyaga.",
        "14. Sa paggawa ng comic book brochure, anong dalawang elemento ng visual framing ang gagamitin mo upang ipakita ang panloob na lakas ng isang katutubong tauhan?",
        "15. Bakit itinuturing na ang panitikan ay kapwa maaaring maging kasangkapan ng pananakop at tanglaw ng pagpapalaya sa sariling pagkatao?"
    ]

    for o_q in open_items_13:
        p_oq = doc.add_paragraph()
        format_paragraph(p_oq, space_before=3, space_after=2)
        r_oq = p_oq.add_run(o_q)
        r_oq.font.name = 'Cambria'
        r_oq.font.size = Pt(10)
        r_oq.font.bold = True

    add_callout_box(
        doc,
        "PAMANTAYAN SA PAGMAMARKA NG BAHAGI II:\n"
        "• 1.0 Puntos: Tumpak ang konsepto, malinaw ang pangangatwiran, at may suportang ebidensiya mula sa aralin.\n"
        "• 0.5 Puntos: May kaugnayan ang sagot ngunit kulang sa paliwanag o malabo ang ilang punto.\n"
        "• 0.0 Puntos: Walang kaugnayan o mali ang ibinigay na katuwiran."
    )

    # doc.add_page_break() [REMOVED TO PREVENT ORPHAN BLANK PAGES]

    # =========================================================================
    # PAHINA 15: ARALIN 13 TRANSITION & PAGHAHANDA SA ARALIN 14
    # =========================================================================
    add_heading_2(doc, "PAGLALAGOM AT TULAY PATUNGO SA ARALIN 14")
    
    add_body_p(
        doc,
        "Sa pagtatapos ng Aralin 13, napatunayan natin na ang panitikan sa Panahon ng Pananakop ng Espanya ay isang masalimuot na larangan ng pagtutunggali "
        "ng kapangyarihan at pagpapatuloy ng katutubong kamalayan. Natutuhan nating suriin ang kaligirang pangkasaysayan, kumilatis ng mga balitang kolonyal, "
        "magtimbang ng panghihiram at pagtutumbas ng salita, at bumuo ng responsableng representasyon sa multimodal na komiks nang walang stereotype."
    )

    add_body_p(
        doc,
        "Ang mga kasanayang ito sa kontekstuwalisadong pagsusuri ay magsisilbing matibay nating pundasyon sa pagtuntong sa Aralin 14. Kung sa araling ito ay "
        "tinalakay natin ang panitikan sa pangkalahatan at ang opisyal na pamamahayag, sa susunod na aralin ay sisisirin natin ang isa sa pinakamakapangyarihan "
        "at pinakamatagal na anyong pampanitikan na humubog sa kaluluwang Pilipino sa ilalim ng Espanya: ang Pasyon at ang mga akdang panrelihiyon."
    )

    add_callout_box(
        doc,
        "PASILIP SA ARALIN 14: PASYON AT MGA TEKSTONG PANRELIHIYON\n"
        "• Ano ang lihim na kapangyarihan ng Pasyon bakit ito inawit, isinapuso, at naging inspirasyon pa ng mga kilusang mapagpalaya tulad ng Katipunan?\n"
        "• Paano sumasalamin sa Pasyon ang antas ng pamumuhay at pakikipagkapuwa ng mga Pilipino sa panahong kolonyal?\n"
        "• Paano gagamitin ang mga elementong biswal ng comic book brochure upang isabuhay ang isang tagpong hango sa kulturang panrelihiyon nang may dangal?"
    )

    doc.add_page_break()
