# -*- coding: utf-8 -*-
"""Aralin 7 Builder: Pages 4 to 15 (12 Full Pages)"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from generate_expanded_ebook import (
    format_paragraph, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_prompt_box, add_callout_box, add_custom_table,
    add_multimedia_box, set_cell_shading
)

def build_aralin7(doc):
    # =========================================================================
    # PAHINA 4: PANIMULA, LAYUNIN, AT MULTIMEDIA CORNER #1
    # =========================================================================
    add_heading_1(doc, "ARALIN 7: Pagbasa sa Panitikan at Pananaw ng Pamayanan")
    add_heading_2(doc, "MGA LAYUNIN AT BALANGKAS NG PAGKATUTO")
    add_body_p(
        doc,
        "Sa araling ito, bibigyang-tuon ang masusing pagbasa at pagsusuri sa panitikang tuluyan (prose) bilang salamin ng kasaysayan, kultura, at kolektibong kamalayan ng pamayanang Pilipino. Hindi sapat na malaman lamang ang banghay o mga tauhan ng isang akda; kailangang siyasatin ang mga panlipunang puwersa at pangkulturang konteksto na nagluwal dito. Matututuhan din ang masusing pagkilatis sa pagkakaiba ng walang batayang opinyon laban sa mapanuring pananaw, at ang wastong paggamit ng mga transisyong gramatikal at retorikal na pang-ugnay upang maging lohikal, kapani-paniwala, at mabisa ang pagpapahayag."
    )

    add_body_p(
        doc,
        "1. F7PN-IIa-1: Nailalahad ang sariling pananaw tungkol sa mga motibasyon, desisyon, at tunggalian ng mga tauhan sa binasang akdang tuluyan batay sa kontekstong pangkasaysayan at kultural.\n"
        "2. F7PB-IIa-2: Nasusuri ang mga elemento at apat na uri ng konteksto (pangkasaysayan, sosyo-kultural, biograpikal, pampanitikan) sa pagbibigay-kahulugan sa akda.\n"
        "3. F7PT-IIa-3: Naipaliliwanag ang kahulugan ng mga salitang ginamit sa akda batay sa kontekstwal na pahiwatig at kultural na pagpapakahulugan.\n"
        "4. F7WG-IIa-4: Nagagamit ang angkop na mga transisyong gramatikal at pang-ugnay na retorikal sa pagbuo ng organisado at makatwirang pananaw.",
        bold_prefix="Mga Kasanayang Pampagkatuto (MATATAG Competencies):\n"
    )

    add_body_p(
        doc,
        "• Paano naiiba ang panitikang tuluyan sa patula sa aspekto ng estruktura, layon, at panlipunang gampanin?\n"
        "• Bakit itinuturing na mapanganib ang paghusga sa isang akda o gawi ng pamayanan nang walang pag-unawa sa konteksto?\n"
        "• Paano nagiging sandata ang apat na haligi ng pananaw (dahilan, paliwanag, halimbawa, ebidensiya) sa pagbuwag ng mga maling opinyon sa modernong lipunan?",
        bold_prefix="Mga Susing Katanungan para sa Aralin:\n"
    )

    add_multimedia_box(
        doc,
        mod_title="Pagsusuri sa Konteksto ng Panitikan sa Pilipinas",
        vid_title="Kasaysayan at Kultura sa Likod ng mga Tuluyang Akda sa Pilipinas",
        channel="DepEd TV / Knowledge Channel Official",
        link="https://www.youtube.com/watch?v=MATATAG_Fil7_Aralin7_Intro",
        qr_code_text="QR-FIL7-ARALIN7-MOD1",
        timestamps=[
            "00:45 - 03:20: Ang Pag-usbong ng Tuluyang Panitikan sa Tradisyong Pasalita ng mga Katutubo.",
            "03:21 - 07:15: Impluwensiya ng Panahong Kolonyal sa Pagbabago ng Estilo ng Pagsulat.",
            "07:16 - 11:30: Pagsusuri sa Kontekstong Sosyo-Kultural sa mga Modernong Kuwentong-Bayan."
        ],
        questions=[
            "Paano inilarawan sa video ang pagbabago sa paraan ng pagkukuwento mula sa sinaunang 'kuwentuhan sa silong' patungo sa nakalimbag na prosa?",
            "Bakit binigyang-diin ng tagapagsalita na ang heograpiya ng isang komunidad ang nagdidikta sa mga simbolo ng kanilang panitikan?",
            "Magtala ng isang tradisyon sa inyong lugar na may malalim na kontekstong pangkasaysayan ngunit madalas hindi naiintindihan ng mga taga-ibang bayan."
        ]
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 5: PAKSA 7.1 (BAHAGI 1) - ANG PANITIKANG TULUYAN AT KASAYSAYAN NITO
    # =========================================================================
    add_heading_2(doc, "Paksa 7.1: Ang Panitikang Tuluyan at Kahalagahan ng Konteksto (Bahagi 1)")
    add_body_p(
        doc,
        "Ang panitikang tuluyan (prose) ay anumang anyo ng sulatin na binubuo ng mga malayang pangungusap at talata na sumusunod sa natural na daloy ng pakikipagtalastasan. Hindi tulad ng panitikang patula na may mahigpit na pagkakatugma, sukat, at taludturan, ang tuluyan ay nagbibigay ng kaluwagan sa manunulat upang magpaliwanag, maglarawan, maglahad ng argumento, at magsalaysay ng masalimuot na karanasan ng tao. Sa kasaysayan ng panitikang Pilipino, ang tuluyan ay nagmula sa ating mayamang tradisyong pasalita (oral tradition)—mga kuwentong isinasalaysay ng mga katutubong pantas at matatanda sa paligid ng siga o liwasan ng nayon."
    )
    add_body_p(
        doc,
        "Nang dumating ang sistema ng pagsulat at ang impluwensiyang kolonyal, ang mga kuwentong ito ay naitala sa anyo ng mga maikling katha, nobela, sanaysay, talaarawan, at anekdota. Sa ilalim ng MATATAG Kurikulum, kinikilala natin na ang tuluyan ay hindi lamang libangan o malikhaing imbensiyon; ito ay isang 'kultural na dokumento' na naglalaman ng mga pilosopiya, hinanakit, pakikibaka, at pangarap ng mga ordinaryong mamamayan sa isang partikular na yugto ng panahon."
    )
    add_body_p(
        doc,
        "• Estruktura: Gumagamit ng gramatikal na talata na may malinaw na bantas, paksang pangungusap, at mga sumusuportang kaisipan.\n"
        "• Wika: Natural, malapit sa pang-araw-araw na salitaan, ngunit may antas ng pormalidad depende sa layunin ng manunulat.\n"
        "• Saklaw ng Pagtalakay: May kakayahang maglaman ng masalimuot na detalye ng sosyolohikal na kalagayan, sikolohiya ng tauhan, at lohikal na pangangatwiran.",
        bold_prefix="Pangunahing Katangian ng Panitikang Tuluyan:\n"
    )

    prompt_p5 = (
        "PROMPT: A cinematic, historically grounded wide-angle illustration of an ancient pre-colonial Philippine village gathering "
        "at dusk. An indigenous female elder (babaylan/storyteller) with weathered, wise features, wearing traditional woven garments "
        "adorned with authentic shell necklaces, is narrating a sacred prose tale to captivated villagers gathered around a glowing "
        "hearth. Children and young warriors listening in profound rapt attention under towering mahogany and coconut palms. Warm golden firelight "
        "contrasting against the deep indigo twilight sky. Masterful digital painting style, photorealistic textures, atmospheric smoke and sparks, "
        "authentic Philippine indigenous anthropology --ar 16:9 --style raw --v 6.0"
    )
    add_prompt_box(doc, "PROMPT SA PAGBUO NG LARAWAN: ANG TRADISYONG PASALITA NG TULUYAN", prompt_p5)

    add_body_p(
        doc,
        "Mahalagang maunawaan na sa bawat panahon, nagbabago ang anyo at paksa ng tuluyan. Sa panahon ng mga Espanyol, ginamit ang tuluyan sa mga tekstong panrelihiyon at moralistiko, ngunit kalaunan ay naging sandata sa propaganda tulad ng mga sanaysay nina Marcelo H. del Pilar at Jose Rizal. Sa panahon ng Amerikano at Hapon, sumibol ang modernong maikling kuwento na sumusuri sa kalagayan ng uring manggagawa at pesante. Sa kasalukuyang digital na panahon, ang tuluyan ay nag-anyong mga blog, micro-fiction, at online expository essays na mababasa sa iba't ibang multimodal na plataporma."
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 6: PAKSA 7.1 (BAHAGI 2) - ANG APAT NA URI NG KONTEKSTO
    # =========================================================================
    add_heading_2(doc, "Paksa 7.1: Ang Apat na Dimensiyon ng Konteksto (Bahagi 2)")
    add_body_p(
        doc,
        "Upang maging ganap ang ating pag-unawa sa isang akdang tuluyan, kinakailangan nating gamitin ang lente ng 'konteksto.' Ang konteksto ay tumutukoy sa kabuuan ng mga panloob at panlabas na kalagayan, ugnayan, at kapaligirang nakapalibot sa akda noong ito ay nilikha. Ayon sa teoryang hermenyutika, ang kahulugan ng isang teksto ay hindi nakahiwalay sa daigdig ng may-akda at ng mambabasa."
    )

    context_headers = ["Uri ng Konteksto", "Kahulugan at Katangian", "Mapanuring Halimbawa sa Pagbasa"]
    context_data = [
        [
            "1. Kontekstong Pangkasaysayan\n(Historical Context)",
            "Tumutukoy sa tiyak na panahon, mga kaganapang politikal, digmaan, batas, at panlipunang krisis kung kailan isinulat ang akda.",
            "Ang isang kuwento tungkol sa lihim na pagtitipon sa kagubatan ay maaaring sumasalamin sa panahon ng batas militar o himagsikan laban sa mga dayuhan."
        ],
        [
            "2. Kontekstong Sosyo-Kultural\n(Socio-Cultural Context)",
            "Sumasaklaw sa mga tradisyon, pamahiin, panlipunang uri, relihiyon, at kultural na gawi ng pamayanang pinangyarihan ng kuwento.",
            "Ang ritwal ng paghingi ng tawad sa 'nuno sa punso' bago magputol ng puno ay nagpapakita ng katutubong paggalang sa kalikasan at espiritwalidad."
        ],
        [
            "3. Kontekstong Biograpikal\n(Biographical Context)",
            "Naglalaman ng personal na talambuhay ng may-akda: kaniyang edukasyon, pamilya, hilig, mga kasawian, at ideolohiyang pinanghahawakan.",
            "Kung ang manunulat ay lumaki sa isang baybaying nayon ng mga mangingisda, ang kaniyang mga talinghaga ay madalas na hango sa dagat at bagyo."
        ],
        [
            "4. Kontekstong Pampanitikan\n(Literary Context)",
            "Ang ugnayan ng teksto sa iba pang naunang akda, sa kasaysayan ng genre, at sa mga umiiral na kumbensiyon at teoryang pampanitikan sa panahong iyon.",
            "Pagsusuri kung ang isang maikling katha ay sumusunod sa realismong panlipunan o sa tradisyon ng mahiwagang realismo (magical realism)."
        ]
    ]
    add_custom_table(doc, context_headers, context_data, col_widths=[2.0, 2.5, 2.0])

    add_body_p(
        doc,
        "TEKSTO + KONTEKSTO = MAS MALALIM AT MAKATARUNGANG PAG-UNAWA",
        bold_prefix="Ang Gintong Pormula ng Pagpapakahulugan:\n",
        italic_prefix=""
    )
    add_body_p(
        doc,
        "Bakit napakahalaga ng pormulang ito? Kung babasahin natin ang isang sinaunang kuwentong-bayan nang walang konteksto, madali nating maipapataw ang ating makabagong pamantayan at husgahan ang mga tauhan bilang 'mangmang' o 'mapamahiin.' Subalit kung gagamitin natin ang kontekstong sosyo-kultural at pangkasaysayan, mauunawaan natin na ang kanilang mga paniniwala ay naging mekanismo ng kaligtasan, pagkakabuklod, at pagpapanatili ng ekolohikal na balanse sa kanilang pamayanan noong panahong wala pang modernong agham."
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 7: KUWENTONG-LUNSARAN - ANG PUNO SA LIWASAN
    # =========================================================================
    add_heading_2(doc, "Akdang Pampanitikan para sa Aralin 7: Kuwentong-Lunsaran")
    add_heading_3(doc, "ANG PUNO SA LIWASAN (Maikling Kuwento ng Pamayanan)")
    add_body_p(
        doc,
        "Sa gitna ng lumang liwasan ng Bayan ng San Jose ay nakatindig ang isang dambuhalang puno ng balete. Ayon sa mga tala ng parokya at sa salindila ng mga matatanda, ang punong ito ay naroroon na bago pa man dumaong ang mga unang barko ng mga Kastila sa look. May malalapad itong rami na wari'y mga bisig na kumakandili sa buong liwasan, at ang mga baging nito ay sumasayad sa lupa na parang mga kurtina ng sinaunang panahon.",
        italic_prefix="Panimula: "
    )
    add_body_p(
        doc,
        "Para sa bagong henerasyon ng kabataan sa nayon, sa pangunguna ni Sinta—isang masipag na mag-aaral sa ikapitong baitang at lider ng youth council—ang puno ay isang magandang tagpuan lamang para sa kuwentuhan matapos ang klase at pagkuha ng mga aesthetic na larawan para sa kanilang social media. Sa paningin ng mga kabataan at ng ilang lokal na negosyante, ang malaking balete ay naging sagabal sa modernong plano ng munisipyo na magtayo ng isang apat na linyang highway na mag-uugnay sa San Jose sa kabisera, kasama ang paglalagay ng mga modernong commercial strip at cell towers para sa mas mabilis na koneksiyon sa internet."
    )
    add_body_p(
        doc,
        "Subalit isang umaga, nagbago ang karaniwang katahimikan nang dumating ang mga dambuhalang bulldozer ng kontraktor. Bago pa man maibaba ang lagari upang simulan ang pagputol, isang hanay ng mga nakatatanda sa nayon ang humarang sa liwasan sa pamumuno ni Lolo Tasio, isang retiradong guro sa kasaysayan at apo ng isang beterano ng rebolusyon. Nagkapit-bisig sila sa paligid ng dambuhalang puno.",
        italic_prefix="Tunggalian: "
    )
    add_body_p(
        doc,
        "'Bakit po ninyo hinahadlangan ang progreso, Lolo Tasio?' ang naguguluhang tanong ni Sinta. 'Ang kalsadang ito ang magdadala ng mga mamumuhunan at magbibigay ng trabaho sa aming mga kabataan. Hindi po ba't makaluma na ang maniwala sa mga pamahiin tungkol sa engkanto ng balete?'"
    )
    add_body_p(
        doc,
        "Tumingin si Lolo Tasio kay Sinta nang may malalim na pagmamahal at pag-unawa. 'Apo, hindi ito tungkol sa pamahiin ng engkanto. Ito ay tungkol sa ating kasaysayan at kaluluwa bilang pamayanan. Noong panahon ng Himagsikang 1896, sa ilalim ng mga ugat ng punong ito lumagda sa kasunduan ang mga katutubong Dumagat at mga Katipunero upang ipagtanggol ang ating lambak. Noong Ikalawang Digmaang Pandaigdig, ang mga sanga nito ang naging kublihan ng ating mga kababayan laban sa mga bomba. Ang bawat ugat nito ay nakabaon sa dugo at sakripisyo ng inyong mga ninuno. Kung puputulin natin ito para lamang sa aspalto, buburahin natin ang kaisa-isang buhay na saksi ng ating pagkabansa sa bayang ito.'"
    )

    prompt_p7 = (
        "PROMPT: A dramatic, emotionally powerful narrative scene set in a historic Philippine town plaza (liwasan). In the center, "
        "a towering ancient Balete tree with majestic curtain-like aerial roots. In front of the tree, an elderly Filipino man (Lolo Tasio) "
        "with silver hair and a proud Barong Tagalog stands hand-in-hand with fellow town elders, peacefully confronting modern construction "
        "bulldozers. A smart Grade 7 Filipina schoolgirl (Sinta) holding a notebook stands between them, listening intently with a transformative "
        "look of realization and respect in her eyes. Golden hour light illuminating the historic plaza facade and ancient stone church in the background. "
        "High realism, emotional storytelling, cinematic depth of field, 8k resolution --ar 16:9 --v 6.0"
    )
    add_prompt_box(doc, "PROMPT SA PAGBUO NG LARAWAN: ANG DIWATA NG KASAYSAYAN SA LIWASAN", prompt_p7)

    add_body_p(
        doc,
        "Natigilan si Sinta. Sa unang pagkakataon, nakita niya ang balete hindi bilang isang pisikal na kahoy na humahadlang sa trapiko, kundi bilang isang buhay na monumento. Sa tulong ng kaniyang impluwensiya sa kapuwa kabataan, nagpatawag sila ng isang pambihirang diyalogo sa pagitan ng munisipyo, mga inhinyero, at mga nakatatanda. Sa halip na magmatigas, nagpanukala ang mga kabataan ng isang bagong disenyo: ang 'San Jose Heritage Park Loop'—kung saan ang bagong kalsada ay gagawing pabilog sa liwasan upang manatiling buo ang puno at maging sentro ng edukasyon at turismo.",
        italic_prefix="Kakalasan at Wakas: "
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 8: MAPANURING TALAKAYAN SA KLASE (SOCRATIC SEMINAR)
    # =========================================================================
    add_heading_2(doc, "Mapanuring Talakayan sa Klase (Socratic Seminar sa Aralin 7)")
    add_body_p(
        doc,
        "Ang sumusunod na transkripsiyon ng talakayan sa silid-aralan ay nagpapakita kung paano ginagamit ang mga pamamaraang Socratic upang malalimang suriin ang binasang akda gamit ang mga kasanayan sa MATATAG Filipino 7:"
    )

    add_body_p(
        doc,
        "Guro: Magandang araw sa inyo! Matapos basahin ang kuwentong 'Ang Puno sa Liwasan,' nais kong itanong kay Sinta: Ano ang naging dahilan kung bakit tinawag ng mga kabataan na 'makaluma' ang mga matatanda noong una?",
        bold_prefix="Guro: "
    )
    add_body_p(
        doc,
        "Sinta: Noong una po, tiningnan lamang ng mga kabataan ang sitwasyon gamit ang praktikal na pananaw ng modernong teknolohiya at komersiyo. Para sa kanila, ang progreso ay nasusukat lamang sa bilis ng internet, bagong kalsada, at mga gusali. Dahil hindi nila alam ang pangkasaysayang konteksto ng balete, inakala nilang pamahiin lamang ang dahilan ng pagtatanggol ng mga matatanda.",
        bold_prefix="Sinta (Mag-aaral): "
    )
    add_body_p(
        doc,
        "Guro: Napakahusay ng iyong obserbasyon. Juan, kung ikaw naman ang tatanungin, paano ipinamalas ni Lolo Tasio ang kapangyarihan ng kontekstong pangkasaysayan at sosyo-kultural sa kaniyang pangangatwiran?",
        bold_prefix="Guro: "
    )
    add_body_p(
        doc,
        "Juan (Mag-aaral): Hindi po nakipagsigawan si Lolo Tasio. Sa halip, binuksan niya ang 'kultural na alaala' ng nayon. Ipinunto niya na ang balete ay naging saksi sa Kasunduan ng mga Katipunero at Dumagat, at naging tagapagligtas sa panahon ng digmaan. Nang marinig ito ng mga kabataan, nagbago ang kahulugan ng puno mula sa pagiging 'hadlang sa kalsada' patungo sa pagiging 'monumento ng kalayaan.' Dito po napatunayan na ang Teksto + Konteksto ay nagbubunga ng mas mataas na antas ng respeto at pag-unawa.",
        bold_prefix="Juan (Mag-aaral): "
    )
    add_body_p(
        doc,
        "Guro: Tumpak! Mark, ano naman ang mahalagang aral sa naging tugon ng mga kabataan matapos marinig ang paliwanag? Bakit mahalaga ang diyalogo sa paglutas ng tunggalian?",
        bold_prefix="Guro: "
    )
    add_body_p(
        doc,
        "Mark (Mag-aaral): Ipinakita po ng mga kabataan na hindi kailangang maging magkaaway ang tradisyon at modernisasyon. Sa pamamagitan ng diyalogo, nakabuo sila ng malikhaing solusyon—ang Heritage Loop. Naipakita rito na ang tunay na edukado at mapanuring kabataan ay marunong makinig sa nakaraan bago magdisenyo ng kinabukasan.",
        bold_prefix="Mark (Mag-aaral): "
    )
    add_body_p(
        doc,
        "Guro: Napakagandang paglalagom. Tandaan natin: Ang panitikan ay hindi simpleng kuwento; ito ay buhay na salamin ng ating pamayanan na nagtuturo sa atin na ang pag-unlad na walang paggalang sa kultura ay isang hungkag na progreso.",
        bold_prefix="Guro (Paglalagom): "
    )

    add_callout_box(
        doc,
        title="PAGSUSURING PANG-ISIPAN: KONTEKSTO AT PAGPILI NG TAO",
        body_lines=[
            "1. Sa iyong sariling komunidad, mayroon bang mga lumang gusali, puno, o tradisyon na nanganganib mawala dahil sa mga modernong proyekto?",
            "2. Kung ikaw ang magiging tagapayo ng alkalde o kapitan, anong mga hakbang ang iyong imumungkahi upang mapanatili ang kultura nang hindi napipigilan ang kaunlarang pang-ekonomiya?",
            "3. Paano nakatutulong ang pag-aaral ng panitikan upang hindi maging padalus-dalos ang desisyon ng isang pamayanan?"
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 9: PAKSA 7.2 (BAHAGI 1) - PAGLALAHAD, OPINYON, AT PANANAW
    # =========================================================================
    add_heading_2(doc, "Paksa 7.2: Paglalahad, Katotohanan, Opinyon, at Pananaw (Bahagi 1)")
    add_body_p(
        doc,
        "Sa pang-araw-araw na komunikasyon—lalo na sa social media tulad ng Facebook, TikTok, at X—napakaraming impormasyon at pahayag ang ating nababasa at naririnig. Bilang mag-aaral ng MATATAG Kurikulum, napakahalagang matutuhan mo ang kritikal na pagkakaiba ng Katotohanan (Fact), Opinyon (Baseless Opinion), at Mapanuring Pananaw (Substantiated Perspective)."
    )

    add_body_p(
        doc,
        "Ang paglalahad ay isang anyo ng diskurso na naglalayong magpaliwanag, magbigay-linaw, magbigay-kaalaman, o magturo nang walang halong panlilinlang. Sa pagsulat ng tekstong ekspositori, ang paglalahad ang pangunahing kasangkapang ginagamit ng manunulat upang maiparating ang kaniyang mensahe sa isang organisado, obhetibo, at lohikal na pamamaraan.",
        bold_prefix="Kikilalanin Natin ang Tatlong Antas ng Pagpapahayag:\n\n1. Katotohanan (Fact): "
    )
    add_body_p(
        doc,
        "Ito ay isang pahayag na mapatutunayan ng mga kongkretong ebidensiya, siyentipikong datos, opisyal na rekord, o pangkalahatang obserbasyon na hindi nakadepende sa personal na damdamin. Halimbawa: 'Ang puno ng balete sa San Jose ay itinanim bago pa man dumating ang mga Kastila ayon sa dokumento ng parokya noong 1890.'"
    )
    add_body_p(
        doc,
        "Ito ay personal na paniniwala, damdamin, kagustuhan, o agarang paghuhusga ng isang indibidwal na madalas ay walang matibay na batayan o patunay. Madalas itong nagsisimula sa mga pariralang 'Sa tingin ko,' 'Para sa akin,' o 'Pakiramdam ko.' Halimbawa: 'Masyadong makaluma at mabagal mag-isip ang lahat ng matatanda sa nayon.' Mapapansin na ito ay isang mapanlahat (sweeping generalization) at emosyonal na pahayag.",
        bold_prefix="2. Walang Suportang Opinyon (Baseless Opinion): "
    )
    add_body_p(
        doc,
        "Ito ay isang maingat na binuong tindig o posisyon tungkol sa isang isyu na nakasandig sa lohikal na pangangatwiran, pagsusuri ng konteksto, at mga sumusuportang patunay. Hindi ito basta emosyon; ito ay bunga ng pagninilay at pagsusuri ng magkabilang panig bago magbitiw ng konklusyon. Halimbawa: 'Bagamat mahalaga ang pagpapalawak ng kalsada para sa ekonomiya, nararapat lamang na ibahin ang ruta nito upang mapangalagaan ang makasaysayang liwasan, sapagkat ang pamanang pangkultura ay hindi na mapapalitan kapag nawasak.'",
        bold_prefix="3. Mapanuring Pananaw (Substantiated Perspective): "
    )

    add_callout_box(
        doc,
        title="TANDAAN: ANG PANGANIB NG 'OPINYON LANG NAMAN YAN'",
        body_lines=[
            "Sa modernong lipunan, madalas gamitin ng ilang tao ang katwirang 'Opinyon ko naman ito kaya may karapatan akong sabihin kahit ano.'",
            "Tandaan: Bagamat malaya tayong magpahayag, ang isang opinyon na nagkakalat ng maling impormasyon (misinformation) o naninira sa kapuwa ay walang halagang akademiko at moral.",
            "Ang layunin ng MATATAG Kurikulum ay iangat ang iyong pahayag mula sa pagiging 'simpleng opinyon' tungo sa pagiging 'mapanuring pananaw.'"
        ],
        color_fill="FFF5F5",
        border_color="CC0000"
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 10: PAKSA 7.2 (BAHAGI 2) - ANG 4 NA HALIGI NG PANANAW AT MULTIMEDIA
    # =========================================================================
    add_heading_2(doc, "Paksa 7.2: Ang Apat na Haligi ng Mapanuring Pananaw (Bahagi 2)")
    add_body_p(
        doc,
        "Upang matiyak na ang iyong isusulat o bibigkasing pananaw ay matatag, kapani-paniwala, at may mataas na antas ng kredibilidad, dapat itong magtaglay ng Apat na Haligi ng Mapanuring Pananaw:"
    )

    pillars_headers = ["Haligi ng Pananaw", "Pangunahing Tanong", "Papel sa Pagsulat ng Sanaysay"]
    pillars_data = [
        [
            "1. Dahilan (Reasoning)",
            "Bakit mo ito nasabi?",
            "Ito ang lohikal na premise o pangunahing saligan kung bakit pinanghahawakan ng manunulat ang kaniyang posisyon."
        ],
        [
            "2. Paliwanag (Elaboration)",
            "Paano ito nagaganap?",
            "Ang pagpapalalim at pagpapaliwanag sa ugnayan ng sanhi at bunga upang lubos na maintindihan ng mambabasa ang kaisipan."
        ],
        [
            "3. Halimbawa (Illustration)",
            "Ano ang kongkretong sitwasyon?",
            "Isang partikular na karanasan, sitwasyon sa totoong buhay, o senaryo na nagpapatunay na totoo ang iyong paliwanag."
        ],
        [
            "4. Ebidensiya (Evidence)",
            "Ano ang patunay o dokumento?",
            "Datos, estadistika, sipi mula sa mga eksperto, batas, o opisyal na kasulatan mula sa mapagkakatiwalaang sanggunian."
        ]
    ]
    add_custom_table(doc, pillars_headers, pillars_data, col_widths=[2.0, 2.0, 2.5])

    add_body_p(
        doc,
        "Suriin ang malaking kaibahan sa sumusunod na talahanayan:"
    )

    compare_headers = ["Walang Suportang Opinyon (Payak / Emosyonal)", "Mapanuring Pananaw (May Apat na Haligi)"]
    compare_data = [
        [
            "Walang kuwenta ang mga lumang puno at gusali sa bayan, dapat gibain lahat para maging parang Makati ang San Jose.",
            "Nararapat na isulong ang 'adaptive reuse' sa mga makasaysayang pook ng San Jose (Dahilan) sapagkat pinagdurugtong nito ang pamanang kultural at makabagong komersiyo (Paliwanag). Tulad ng ginawa sa Heritage Loop ng Iloilo City kung saan napanatili ang mga lumang gusali habang dumarami ang mga turista (Halimbawa), napatunayan ng UNESCO na ang mga bayang may mayamang kultural na identidad ay 30% mas mabilis makaakit ng lokal na pamumuhunan (Ebidensiya)."
        ]
    ]
    add_custom_table(doc, compare_headers, compare_data, col_widths=[3.0, 3.5])

    add_multimedia_box(
        doc,
        mod_title="Mapanuring Pagsusuri: Katotohanan vs. Opinyon sa Media",
        vid_title="Fact-Checking at Pagsusuri ng Argumento sa Digital Age",
        channel="DepEd Media Literacy / Rappler Fact Check Guide",
        link="https://www.youtube.com/watch?v=MATATAG_Fil7_Aralin7_Media",
        qr_code_text="QR-FIL7-ARALIN7-MOD2",
        timestamps=[
            "01:10 - 03:45: Paano Kumakalat ang mga Walang Suportang Opinyon bilang 'Katotohanan'.",
            "03:46 - 06:30: Ang Apat na Hakbang sa Pag-verify ng Datos at Pahayag ng mga Resource Speaker.",
            "06:31 - 10:15: Pagsulat ng Mapanuring Posisyong Papel sa Silid-Aralan."
        ],
        questions=[
            "Bakit madaling mapaniwala ang mga tao sa mga emosyonal na pahayag sa social media ayon sa video?",
            "Paano mo magagamit ang Apat na Haligi ng Pananaw sa pagsusuri ng mga komentaryo sa balita?",
            "Pumili ng isang kontrobersiyal na isyu sa inyong paaralan at bumuo ng isang mapanuring pananaw gamit ang dahilan, paliwanag, halimbawa, at ebidensiya."
        ]
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 11: PAKSA 7.3 (BAHAGI 1) - TRANSISYONG GRAMATIKAL AT RETORIKAL
    # =========================================================================
    add_heading_2(doc, "Paksa 7.3: Transisyong Gramatikal at Pang-ugnay na Retorikal (Bahagi 1)")
    add_body_p(
        doc,
        "Ang isang magandang ideya ay mawawalan ng bisa kung hindi ito maayos na maipahahayag. Upang maging magkakaugnay, madulas, at lohikal ang paglipat ng mga kaisipan sa loob at pagitan ng mga talata, gumagamit tayo ng mga 'Transisyong Gramatikal' at 'Pang-ugnay na Retorikal.' Ang mga ito ay nagsisilbing mga tulay at ilaw-trapiko ng diskurso na gumagabay sa mambabasa kung paano dapat unawain ang relasyon ng bawat pangungusap."
    )

    trans_headers = ["Relasyon ng Kaisipan", "Mga Transisyon / Pang-ugnay", "Halimbawa sa Mapanuring Pangungusap"]
    trans_data = [
        [
            "Pagdaragdag at Pagpapalawig\n(Addition)",
            "bukod dito, higit pa rito, gayundin, kalakip nito, sa kabilang banda",
            "Nais ng munisipyo na palawakin ang kalsada; bukod dito, target din nilang magtayo ng mga modernong commercial center sa tabi nito."
        ],
        [
            "Pagsalungat at Pagkakaiba\n(Contrast / Concession)",
            "subalit, ngunit, datapwat, sa kabilang dako, bagaman, sa kabaligtaran",
            "Nais ng mga negosyante na gibain ang liwasan; subalit, nanindigan ang mga matatanda na mahalaga ang puno sa kasaysayan ng bayan."
        ],
        [
            "Sanhi at Bunga\n(Cause and Effect)",
            "dahil dito, bunga nito, sapagkat, kung kaya't, samakatuwid, sa gayon",
            "Nakinig ang mga kabataan sa pangkasaysayang konteksto; dahil dito, nagbago ang kanilang saloobin at nakiisa sila sa pangangalaga."
        ],
        [
            "Pagbibigay-diin at Pagpapatibay\n(Emphasis / Reinforcement)",
            "sa katunayan, sa totoo lamang, walang dudang, tunay ngang, higit sa lahat",
            "Sa katunayan, napatunayan ng mga arkitekto na kayang iwasan ng kalsada ang puno nang hindi naaantala ang trapiko."
        ],
        [
            "Paglalahat at Pagwawakas\n(Summary / Conclusion)",
            "sa kabuuan, bilang pagtatapos, sa madaling salita, anupa't, kung tutuusin",
            "Sa kabuuan, pinatunayan ng San Jose na ang tunay na kaunlaran ay yaong nagbibigay-pugay sa nakaraan habang sumusulong sa hinaharap."
        ]
    ]
    add_custom_table(doc, trans_headers, trans_data, col_widths=[1.8, 2.2, 2.5])

    add_body_p(
        doc,
        "Ang Tungkulin ng Pang-ugnay sa Retorika:",
        bold_prefix="Bakit Mahalaga ang Transisyon sa Retorikal na Diskurso?\n"
    )
    add_body_p(
        doc,
        "1. Nagbibigay ng Direksiyon: Nililinaw nito kung ang kasunod na pangungusap ay sumasang-ayon, sumasalungat, o nagbibigay ng karagdagang patunay sa naunang punto.\n"
        "2. Nag-aalis ng Kalituhan (Ambiguity): Kung walang transisyon, ang mga pangungusap ay magmumukhang mga hiwa-hiwalay na pulo na walang ugnayan (choppy sentences).\n"
        "3. Nagpapalutang ng Tono ng Awtor: Ang paggamit ng mga pormal na pang-ugnay tulad ng 'datapwat' at 'samakatuwid' ay nagpapahiwatig ng seryoso at mapanuring tono sa akademikong pagsulat."
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 12: PAKSA 7.3 (BAHAGI 2) - PAGLALAPAT SA TALATA AT MGA KAMALIAN
    # =========================================================================
    add_heading_2(doc, "Paksa 7.3: Paglalapat ng Transisyon at Pag-iwas sa Kamalian (Bahagi 2)")
    add_body_p(
        doc,
        "Sa pagsulat ng isang buong sanaysay, hindi lamang sa loob ng iisang pangungusap ginagamit ang transisyon. Ginagamit din ito bilang 'transisyonal na talata' o panimulang sugnay sa bawat bagong talata upang mapanatili ang kaisahan (unity) at koherensiya (coherence) ng buong akda."
    )

    add_body_p(
        doc,
        "Suriin ang modelong talata sa ibaba kung paano hinabi ang mga transisyon upang maging buo ang argumento:",
        bold_prefix="Pagsusuri sa Huwarang Talata:\n"
    )

    add_callout_box(
        doc,
        title="HUWARANG TALATANG NAGLALAHAD NA MAY RETORIKAL NA PANG-UGNAY",
        body_lines=[
            "   Sa pagpasok ng modernisasyon sa Bayan ng San Jose, naging mabilis ang panawagan para sa modernong imprastruktura. Bukod sa pangakong mas mabilis na transportasyon, inasahan din ng marami na daragsa ang mga negosyo. Subalit, sa likod ng mga pangakong ito ay may malaking panganib sa ating kultural na pamana.",
            "   Dahil dito, mahalagang kilatisin kung ano nga ba ang tunay na kahulugan ng pag-unlad. Kung mawawala ang ating mga makasaysayang liwasan, mawawalan ng kaluluwa ang bayan. Sa katunayan, ipinakita ng karanasan ng mga karatig-lalawigan na ang mga pamayanang marunong magpahalaga sa kanilang kasaysayan ay mas matatag laban sa krisis.",
            "   Samakatuwid, nararapat lamang na maging mapanuri ang bawat mamamayan. Hindi natin dapat ipagpalit ang ating nakaraan sa mabilisang ginhawa. Sa halip, pag-isahin natin ang talino ng kabataan at karunungan ng mga nakatatanda upang bumuo ng progresibong bayang may dangal."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    add_heading_3(doc, "Mga Karaniwang Kamalian sa Paggamit ng mga Pang-ugnay:")
    add_body_p(
        doc,
        "1. Maling Gamit ng 'Kung Kaya't' at 'Dahil Dito': Tandaan na ang 'kung kaya't' ay nagpapahayag ng kinalabasan o bunga. Hindi ito dapat gamitin kung ang kasunod na sugnay ay nagpapahayag ng sanhi.\n"
        "2. Labis na Paggamit ng Iisang Transisyon (Overuse): Ang paulit-ulit na paggamit ng 'at,' 'tapos,' o 'kaya' sa bawat pangungusap ay nagpapababa sa kalidad ng sulatin. Pag-iba-ibahin ang mga salitang ginagamit.\n"
        "3. Maling Paglalagay ng Pagsalungat: Ang paggamit ng 'ngunit' o 'subalit' ay nangangailangan ng tunay na magkasalungat na kaisipan. Kung pareho ang direksiyon ng ideya, gamitin ang 'bukod dito' o 'gayundin.'"
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 13: GAWAIN 7.1 AT GAWAIN 7.2 (30% ACTIVITY)
    # =========================================================================
    add_heading_2(doc, "Bahaging Gawain at Paglalapat para sa Aralin 7 (30% Activity)")
    
    add_callout_box(
        doc,
        title="Gawain 7.1: Pagsusuri ng Apat na Dimensiyon ng Konteksto sa Akda",
        body_lines=[
            "Panuto: Balikan ang kuwentong 'Ang Puno sa Liwasan.' Punan ang talahanayan sa ibaba sa pamamagitan ng pagtukoy sa partikular na bahagi ng kuwento na nagpapakita ng bawat uri ng konteksto. Ipaliwanag kung paano nakatulong ang kontekstong ito sa pagbabago ng pananaw ng mga tauhan.",
            "Pamantayan sa Pagmamarka: Kawastuhan ng Pagsusuri (5 pts), Lalim ng Paliwanag (5 pts), Organisasyon ng Wika (5 pts) = Kabuuang 15 Puntos."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    act1_headers = ["Dimensiyon ng Konteksto", "Patunay na Bahagi sa Kuwento", "Mapanuring Paliwanag sa Epekto sa Tauhan"]
    act1_data = [
        ["Kontekstong Pangkasaysayan", "(Isulat dito ang sipi o pangyayari sa kuwento...)", "(Ipaliwanag kung paano ito nagbago sa desisyon...)"],
        ["Kontekstong Sosyo-Kultural", "(Isulat dito ang sipi o pangyayari sa kuwento...)", "(Ipaliwanag kung paano ito nagbago sa desisyon...)"],
        ["Kontekstong Biograpikal", "(Isulat dito ang sipi o pangyayari sa kuwento...)", "(Ipaliwanag kung paano ito nagbago sa desisyon...)"],
        ["Kontekstong Pampanitikan", "(Isulat dito ang sipi o pangyayari sa kuwento...)", "(Ipaliwanag kung paano ito nagbago sa desisyon...)"]
    ]
    add_custom_table(doc, act1_headers, act1_data, col_widths=[2.0, 2.3, 2.2])

    add_callout_box(
        doc,
        title="Gawain 7.2: Pagpapatibay ng Pananaw gamit ang Apat na Haligi",
        body_lines=[
            "Panuto: Pumili ng ISA sa mga sumusunod na napapanahong isyu sa ating lipunan. Bumuo ng isang mapanuring pananaw na binubuo ng isang kumpletong talata na nagtataglay ng Apat na Haligi (Dahilan, Paliwanag, Halimbawa, Ebidensiya). Salungguhitan ang bawat haligi sa iyong isinulat.",
            "Paksa A: Paggamit ng Artificial Intelligence (AI) sa Paggawa ng mga Takdang-Aralin sa Paaralan.",
            "Paksa B: Pagpapatupad ng No-Cell-Phone Policy sa loob ng Silid-Aralan sa Oras ng Klase.",
            "Paksa C: Pagpapanatili ng mga Tradisyunal na Jeepney laban sa Modernisasyon ng Transportasyon."
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    doc.add_page_break()

    # =========================================================================
    # PAHINA 14: GAWAIN 7.3 AT MAPANURING PROYEKTO
    # =========================================================================
    add_heading_2(doc, "Bahaging Pagsasanay at Paglalapat para sa Aralin 7")
    
    add_callout_box(
        doc,
        title="Gawain 7.3: Pagsasaayos ng Disorganisadong Talata gamit ang Transisyon",
        body_lines=[
            "Panuto: Basahin ang magulong talata sa ibaba. Pansinin na putol-putol ang mga pangungusap at walang wastong pang-ugnay. Muling isulat ang talata sa iyong kuwaderno sa pamamagitan ng paglalagay ng angkop na mga transisyong gramatikal (bukod dito, subalit, dahil dito, sa katunayan, samakatuwid).",
            "Magulong Talata:",
            "\"Gusto ng mga mag-aaral na magkaroon ng libreng Wi-Fi sa liwasan. Marami ang hindi makabili ng load para sa online research. May mga naglalaro lamang ng online games sa halip na mag-aral. Nagreklamo ang mga magulang. Nagdesisyon ang kapitan na limitahan ang oras ng libreng internet. Naging mas kapaki-pakinabang ang liwasan para sa lahat.\""
        ],
        color_fill="F4F7FA",
        border_color="1B365D"
    )

    add_heading_3(doc, "Mapanuring Paglalapat: Pagsulat ng Liham sa Pamunuan ng Bayan")
    add_body_p(
        doc,
        "Ikaw ay inatasan bilang kinatawan ng kabataan sa inyong barangay. Sumulat ng isang pormal na liham-panukala na may tatlong talata na naglalahad ng iyong mapanuring pananaw tungkol sa isang pamanang pook o kaugalian sa inyong lugar na nangangailangan ng proteksiyon. Siguraduhing gamitin ang:"
    )
    add_body_p(
        doc,
        "• Unang Talata: Paglalahad ng Sitwasyon at Kontekstong Pangkasaysayan ng pook o kaugalian.\n"
        "• Ikalawang Talata: Ang iyong Mapanuring Pananaw gamit ang Apat na Haligi (Dahilan, Paliwanag, Halimbawa, Ebidensiya).\n"
        "• Ikatlong Talata: Konklusyon at Kongkretong Rekomendasyon gamit ang mga Transisyong Gramatikal."
    )

    rubric_headers = ["Pamantayan sa Pagmamarka", "Napakahusay (5)", "Mahusay (4)", "Nalilinang (3)", "Puntos"]
    rubric_data = [
        ["Nilalaman at Konteksto", "Malalim, tumpak ang konteksto at ebidensiya", "May konteksto ngunit kulang sa lalim", "Mababaw at walang malinaw na konteksto", "/5"],
        ["Apat na Haligi ng Pananaw", "Kumpleto at malinaw ang apat na haligi", "May tatlong haliging naipakita", "Isa o dalawang haligi lamang", "/5"],
        ["Gamit ng mga Transisyon", "Likas, tama, at epektibo ang mga pang-ugnay", "May 1-2 maling gamit ng pang-ugnay", "Putol-putol at kulang sa transisyon", "/5"],
        ["Wika at Gramatika", "Walang mali sa baybay, bantas, at sintaks", "May bahagyang kamalian sa bantas", "Maraming maling baybay at bantas", "/5"]
    ]
    add_custom_table(doc, rubric_headers, rubric_data, col_widths=[2.2, 1.5, 1.5, 1.5, 0.8])

    doc.add_page_break()

    # =========================================================================
    # PAHINA 15: MABILISANG PAGTATAYA SA ARALIN 7 (FORMATIVE ASSESSMENT)
    # =========================================================================
    add_heading_2(doc, "Mabilisang Pagtataya sa Aralin 7 (Formative Assessment)")
    add_body_p(
        doc,
        "Panuto: Basahing mabuti ang bawat aytem. Piliin ang titik ng pinakawastong sagot at isulat ito sa patlang bago ang bilang.",
        bold_prefix="Pangkalahatang Panuto: "
    )

    quiz_items = [
        ("1. Alin sa mga sumusunod ang pangunahing katangian ng panitikang tuluyan na nagpapaiba rito sa tula?\n"
         "A. Gumagamit ito ng sukat at tugma sa dulo ng bawat linya.\n"
         "B. Binubuo ito ng mga pangungusap at talatang sumusunod sa natural na daloy ng wika.\n"
         "C. Eksklusibo lamang itong isinusulat para sa mga itatanghal sa entablado.\n"
         "D. Hindi ito kailanman maaaring maglaman ng emosyon o damdamin ng may-akda."),

        ("2. Nais mong suriin kung bakit ang mga akda noong panahon ng pananakop ng Hapon ay maikli at nakasulat sa Tagalog. Anong konteksto ang iyong tinitingnan?\n"
         "A. Kontekstong Biograpikal   B. Kontekstong Pampanitikan   C. Kontekstong Pangkasaysayan   D. Kontekstong Pangheograpiya"),

        ("3. Ang paniniwala ng mga taga-San Jose sa sagradong ugnayan ng puno ng balete at ng kanilang mga ninuno ay halimbawa ng anong konteksto?\n"
         "A. Kontekstong Sosyo-Kultural   B. Kontekstong Pang-ekonomiya   C. Kontekstong Pisikal   D. Kontekstong Pang-akademiko"),

        ("4. Bakit itinuturing na 'hungkag' ang paghuhusga sa isang sinaunang kuwento kung hindi gagamitin ang konteksto?\n"
         "A. Dahil mawawalan ng trabaho ang mga historyador sa unibersidad.\n"
         "B. Dahil maipapataw ang modernong pananaw sa isang panahong may kakaibang kalagayan at pangangailangan.\n"
         "C. Dahil magiging masyadong mahaba ang pagsusuri ng mambabasa.\n"
         "D. Dahil labag ito sa batas ng karapatang-sipi."),

        ("5. Alin sa mga sumusunod ang halimbawa ng isang 'Walang Suportang Opinyon'?\n"
         "A. Ayon sa datos ng PSA, tumaas ng 4% ang ani ng palay ngayong taon.\n"
         "B. Tamad ang lahat ng kabataan ngayon dahil laging nakatutok sa cellphone.\n"
         "C. Ang puno ng balete ay may edad na mahigit 200 taon batay sa pagsusuri ng mga botanist.\n"
         "D. Mahalaga ang diyalogo upang marinig ang panig ng bawat sektor ng pamayanan."),

        ("6. Aling haligi ng pananaw ang sumasagot sa katanungang 'Ano ang kongkretong patunay o datos na sumusuporta sa iyong kaisipan?'\n"
         "A. Dahilan   B. Paliwanag   C. Halimbawa   D. Ebidensiya"),

        ("7. 'Nais ng kabataan ang mabilis na internet; ________, hindi nila nais na sirain ang makasaysayang liwasan.' Anong transisyon ang angkop?\n"
         "A. dahil dito   B. subalit   C. bukod dito   D. samakatuwid"),

        ("8. Aling transisyon ang nagpapahiwatig ng pagbubuod o pinal na konklusyon ng isang talata?\n"
         "A. Sa kabuuan   B. Sa kabilang dako   C. Higit pa rito   D. Unang-una"),

        ("9. Ano ang naging papel ni Lolo Tasio sa kuwentong 'Ang Puno sa Liwasan'?\n"
         "A. Siya ang kontraktor na nagpatigil sa suweldo ng mga manggagawa.\n"
         "B. Siya ang nagbukas sa kultural at pangkasaysayang konteksto ng puno para sa kabataan.\n"
         "C. Siya ang alkalde na nagpasa ng ordinansa laban sa pagputol ng mga kahoy.\n"
         "D. Siya ang turistang kumuha ng litrato ng lumang liwasan."),

        ("10. Paano nakatutulong ang pormulang 'TEKSTO + KONTEKSTO = MAS MALALIM NA PAG-UNAWA' sa pag-iwas sa fake news?\n"
         "A. Tinuturuan tayo nitong huwag nang magbasa ng balita kailanman.\n"
         "B. Sinasanay tayo nitong suriin ang pinagmulan, motibo, at panahon kung kailan ginawa ang impormasyon bago maniwala.\n"
         "C. Pinipilit tayo nitong maniwala sa lahat ng sinasabi ng mga matatanda.\n"
         "D. Ginagawa nitong mas madaling mag-share ng mga post sa social media.")
    ]

    for item in quiz_items:
        add_body_p(doc, item)

    add_callout_box(
        doc,
        title="EXIT TICKET / PAGNINILAY SA ARALIN 7",
        body_lines=[
            "1. Isang mahalagang kaisipan na tumatak sa akin ngayon ay: ________________________________________________",
            "2. Ang isang kasanayan na kailangan ko pang paghusayan sa pagsulat ng pananaw ay: __________________________"
        ],
        color_fill="FAFAFA",
        border_color="CCCCCC"
    )

    doc.add_page_break()
