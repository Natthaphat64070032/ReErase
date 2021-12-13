# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character(_("???"), color="#ffffff")
define m = Character(_("ทาคุโตะ ยูกิ"), color="#2760c9")
define girl1 = Character(_("โซโนซากิ มินะ"), color="#38c72b")
define male1 = Character(_("คิตากาวะ จุนอิจิ"), color="#da9e1d")
define ac = Character(_("ทุกคน"), color="#ffffff")

default friendshipg1 = 0
default friendshipm1 = 0
default allfriend = friendshipg1 + friendshipm1
# The game starts here.

label start:

    play music "audio/Ideal and the Real.ogg"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    mc "เรื่องที่เกิดขึ้นหลังจากนี้เป็นเรื่องที่ผ่านมาหลายปีแล้ว"
    mc "ถ้าจะให้พูดคือมันไม่มีผลอะไรกับปัจจุบันที่ผมใช้ชีวิตอยู่แล้ว"
    mc "แต่มันเป็นสิ่งที่ค้างคาในใจผมมาตลอด"
    mc "สมัยผมเรียนมัธยมในช่วงหนึ่งผมได้มีเพื่อนร่วมชั้นผู้หญิงคนหนึ่ง"
    mc "เรามีความทรงจำร่วมกันหลายๆอย่าง ชีวิตโดยรวมอยู่ในขั้นปกติ เธอกับผมนั้นหลังจบแล้วก็ยังคงเป็นเพื่อนที่ดีต่อกัน"
    mc "เพื่อนที่ดีมากๆเลยล่ะ"
    mc "จนกระทั่งวันหนึ่ง"
    mc "เกิดเหตุการณ์ผู้ร้ายก่อเหตุคดีอุกฉกรรจ์ในเขตพักอาศัย มีผู้เคราะห์รายสามราย"
    mc "หนึ่งในนั้นคือเพื่อนสนิทผม.."
    mc "ส่วนอีกสองราย คือพ่อและแม่ของเธอ"
    mc "พ่อและแม่ของเธอเสียชีวิตในเหตุการณ์เธอคนเป็นคนเดียวที่รอดมาได้..."
    stop music fadeout 2.0
    scene black
    with fade
    mc "แต่…หลังจากตอนนั้น..."
    mc "เธอไม่เหมือนเดิมอีกแล้ว"
    play music "audio/Alleycat.ogg"
    mc "จากเหตุการณ์นั้นเธอได้เป็นผู้เห็นเหตุการณ์ทั้งหมด เธอกลายเป็นคนจิตไม่สมประกอบ"
    mc "ไม่สามารถใช้ชีวิตได้เหมือนผู้คนปกติ เธอสูญเสียแม้แต่ความทรงจำที่พวกเรารู้จักกัน"
    mc "เธอเป็นผู้เคราะห์ร้ายจากเหตุการณ์ที่เหล่าโจรพวกนั้นได้ปล้นชีวิตครอบครัว และรวมถึงอนาคตของเธอ"
    mc "หลังจากนั้นผมจึงไปเยี่ยมเธอที่โรงพยาบาลเป็นประจำ..."
    mc "เพื่อหวังว่าซักวันจะทำอะไรให้เธอได้บ้าง"
    #ห้องวิจัย
    scene bg lab
    with fade
    show mc sad at right
    with dissolve
    mc "งานที่ผมทำนั้นเป็นงานวิจัยเกี่ยวกับรักษาผู้ป่วยทางจิต ซึ่งเป็นสิ่งที่ผมตั้งใจทำมาตลอดหลังจากเกิดเหตุการณ์นั้นขึ้น"
    mc "แต่ในขณะเดียวกันมันส่งผลต่อผู้ร่วมลงทุนในงานวิจัยผม"
    mc "ไม่รู้ว่าเนื่องจากอะไร แต่ผมคิดว่ามันอาจขัดต่อผลประโยชน์พวกเขาได้"
    mc "เนื่องจากงานวิจัยชิ้นนี้เป็นการฟื้นฟู ความคิด ความทรงจำ "
    mc "ของผู้ได้รับบาดแผลทางจิตใจ"
    mc "หากงานวิจัยนี้สำเร็จผู้ที่มีบาดแผลทางจิตใจ ผู้เคราห์ร้ายจากเหตุการณ์จนใช้ชีวิตไม่ได้"
    mc "เขาจะกลับมาใช้ชีวิตได้ตามปกติได้"
    mc "สำหรับผมคิดว่าโลกนี้ค่อนข้างจะโหดร้ายกับผู้คนที่พยายามทำอะไรซักอย่าง"
    mc "โดยเรื่องพวกนั้นตัวผมเองก็ไม่สามารถแก้ไขอะไรได้"
    mc "จริงๆงานวิจัยนี้เป็นการชดใช้สิ่งที่ผมอยากทำ"
    mc "แต่ว่านั้นก็เป็นได้เพียงความคิดที่ไม่เป็นจริง"
    mc "หลังจากเรียนจบมาเป็นนักวิจัย ผ่านเหตุการณ์ที่ทำให้เหมือนเสียเพื่อนคนสำคัญ"
    mc "หมกมุ่นอยู่กับงานวิจัยที่ไปไม่ถึงเป้าหมาย เป็นแค่ฝันลมๆแล้งๆ" 
    mc "ทำให้โดนตัดงบประมาณ จนตอนนี้เป็นเหมือนคนตกงาน"
    mc "ผมได้แต่รับงานเล็กๆเช่นงานรับให้คำปรึกษาทางจิต หรือช่วยตามงานโรงเรียนต่างๆ"
    mc "เพื่อหารายได้มาประทังชีวิตไปวันๆ"
    mc "ถึงจะพูดว่ารับงานให้คำปรึกษาแต่ตัวผมเองนั้นก็ยังไม่สามารถก้าวข้ามความรู้สึกตัวเองได้"
    mc "เป็นเพราะผมยังพยายามไม่พอรึเปล่าถึงไม่สามารถช่วยคนรอบข้างได้เลย"
    mc "การไม่สามารถก้าวต่อไปได้ ทำให้จมปลักอยู่กับที่จนเป็นคนไร้จุดหมายเป็นเดือนๆ..."
    scene black
    with fade
    mc "แต่แล้วในวันหนึ่ง ผมได้รับพลังบางอย่าง พลังที่สามารถเปลี่ยนความจริง"
    mc "แก้ไขทั้งอดีตและปัจจุบันให้เป็นอย่างที่คิดได้ ผมได้ใช้พลังนั้นเพื่อช่วยเธอให้กลับมาใช้ชีวิตได้อีกครั้ง"
    centered "หรือพูดอีกอย่างคือผมสามารถย้อนเวลาไปแก้ไขอดีตได้"
    mc "แต่ผลของมันคือทำให้เธอจำผมไม่ได้"
    mc "เพราะการเปลี่ยนแปลงอดีตเพื่อให้เธอรอดนั้น"
    centered "คือการที่เธอต้องไม่เจอผม"
    mc "เหตุการณ์นั้นก็จะไม่เกิดขึ้นต่อไปจะไม่มีผู้เคราห์ร้ายหรืออาจเปลี่ยนผู้เคราห์ร้ายเป็นผู้อื่น"
    mc "แต่นั่นก็เกินพอแล้วขอแค่เธอมีชีวิตรอดก็พอ"
    mc "พลังที่ได้มานี้ถ้าคิดจะใช้มันเพื่อที่จะได้ไม่มีผู้เคราะห์ร้ายอีก มันจะถูกรึเปล่า?"
    mc "ผมสามารถใช้พลังนี้เพื่อใครก็ได้"
    scene bg city
    with dissolve
    mc "หากผมช่วยทุกคนเพื่อให้โลกนี้มีแต่ความสุขโดยให้สิ่งที่ทุกคนต้องการ"
    mc "ผมจะกลายเป็นผู้ทำลายความตั้งใจของคนพยายามอย่างหนักเพื่อได้ใช้ชีวิตในแบบที่ต้องการไหม?"
    mc "ถ้าเกิดคนที่ผมช่วยให้ไม่เจอเคราะห์ร้ายกลายเป็นคนไม่ดีขึ้นมาล่ะ"
    mc "ผมรู้ว่าการที่ทุกคนเติบโตขึ้นได้นั้น ย่อมมีทั้งความสุขใจและความเจ็บปวด..."
    mc "ถึงผมจะไม่อยากให้ใครต้องเจ็บปวดเป็นผู้เคราะห์ร้ายอีก.."
    mc "แต่นั้นคือสิ่งที่ทุกคนต้องการรึเปล่าผมนั้นไม่สามารถรู้ได้"
    mc "ตัวผมนั้นได้แต่คิดทบทวนว่าผมควรใช้พลังเพื่ออะไรกันแน่"
    mc "เพียงแค่ผมช่วยคนผิดคนก็อาจจะทำให้ชีวิตอีกคนพังทลายได้"
    mc "ผมนั้นไม่รู้เลยว่าอะไรคือสิ่งที่ถูกต้อง"
    mc "อะไรคือนิยามของความถูกผิด"
    mc "หรือผมควรใช้ชีวิตเดินหน้าต่อไปในแบบที่ควรจะทำ"
    mc "ทิ้งทุกอย่าง"
    mc "เลิกยึดติด"
    stop music fadeout 3.0
    scene black
    with fade
    centered "แต่จิตใจผมไม่แข็งแกร่งพอที่จะทำแบบนั้นได้"
    centered "ผมควรจะทำอย่างไรดี"
    menu:
        "หวนคืนสู่จุดเริ่มต้น":
            jump start2
    label start2:
        play music "audio/FirstMemory.ogg"
        mc "นี่นายนะ"
        mc "นั่นไม่ใช่ที่นั่งนายนะ ที่นั่งเรียงตามเลขที่บนกระดานแล้วนะ"
        "อะไรเนี่ย...?"
        "เสียงนี้มัน..?"
        "ไม่สิก็เธอน่าจะ..."
        show satonaka at right
        with dissolve
        girl1 "พึ่งเปิดเทอมก็มาหลับอยู่ในห้องตั้งแต่เช้าเลยหรอ ไหวรึเปล่าเนี่ยนายนะ"
        "แบบนี้มัน...อีกแล้วสินะ.."
        scene classroom
        with dissolve
        "ใช่สินะ มันเกิดขึ้นอีกแล้ว"
        "พลังที่ผมพูดถึง"
        "การย้อนเวลา"
        'ผมชื่อว่า"ทาคุโตะ ยูกิ"ถ้าให้พูดก็นักวิจัยธรรมดานี่แหละ'
        "แต่ตอนนี้เป็นนักเรียนมัธยมปลาย ที่่อยู่ตรงหน้าผมก็เพื่อนของผมเอง"
        "เพื่อนผมที่เคยพูดถึง"
        "เวลามันเวียนกลับมาอีกแล้วสินะ"
        show mc almostcry at left
        with dissolve
        m "ขอโทษนะ พอดีเหม่อไปหน่อย"
        m "วันนี้ขอโทษนะไม่ค่อยมีสมาธิเรียนเท่าไหร่เลย"
        m "แต่ดีใจมากเลยนะได้เจอเธออีก"
        show satonaka at right
        with dissolve
        girl1 "พูดอะไรของนายเนี่ยก็อยู่ด้วยกันมาตลอดไม่ใช่รึไง"
        girl1 "หัวกระแทกพื้นมาหรือเล่นเกมจนดึกล่ะเนี่ย"
        menu :
            "เราควรตอบว่าอะไร"
            "แค่คิดไปเรื่อยนะขอโทษด้วย":
                jump story
            "ขอบคุณมากนะที่ยังได้มาเจอกัน":
                jump story
    label story:
        scene classroom
        show satonaka at right
        with dissolve
        girl1 "นายนี่ละก็นะ"
        girl1 "เตรียมตัวได้แล้วนะคาบแรกจะเริ่มแล้ว"
        hide satonaka at right
        with dissolve
        "โดยรวมแล้วพลังที่ผมพูดถึงคือนี่แหละครับ"
        "หากผมไม่พอใจในชีวิตตัวเอง หรืออะไรก็ตามผมสามารถย้อนกลับมาเริ่มใหม่ได้"
        "โดยไม่รู้ว่าผมจะถูกย้อนกลับมาที่ไหน"
        "ควรทำอะไร"
        "ผมติดอยู่ในวังวงบ้าบอนี้มาซักพักใหญ่ๆแล้วครับ"
        "จะพูดว่าผมเป็นเด็กมัธยมก็คงไม่ได้แล้ว"
        "ผมนั้นช่วยใครไว้ไม่ได้เลย"
        "ถึงจะมีพลังที่สุดวิเศษขนาดนี้สำหรับใครหลายๆคนแต่สำหรับผมแล้วมันทำให้ผมลำบากใจ"
        "ผมกลับรู้สึกถึงความรับผิดชอบที่ทุกครั้งเวลาผมต้องการแก้อะไรสักอย่างให้ดีขึ้นแล้วมัน..."
        "กลับแย่กว่าเดิมทุกครั้ง"
        show mc almostcry at left
        with dissolve
        m "วันนี้ผมขอตัวกลับบ้านก่อนนะรู้สึกไม่สบายเลย"
        m "ฝากบอกคุณครูด้วยนะว่าลาเรียนด้วยนะ ขอโทษจริงๆ"
        show satonaka at right
        with dissolve
        girl1 "เดี๋ยวสินี่นายพึ่งเปิดเรียนวันแรกเองนะ"
        hide mc almostcry at right
        with dissolve
        girl1 "เป็นอะไรของเขากันนะวันนี้"
        scene bg old room
        with dissolve
        "ห้องของเรายังโล่งอยู่เลย"
        show mc shirt sad at right
        with dissolve
        "นั่นสินะ ตอนปี 1 เราพึ่งย้ายมาเรียนในเมืองนี้ ของอะไรเลยแทบไม่มีเลย"
        "ตอนนั้นคิดว่าชีวิตคงจะสดใสได้เจอเพื่อนใหม่ๆ แต่ยัยนั่นดันสอบติดแล้วเข้ามาได้ในโรงเรียนเดียวกันอีก"
        "จริงๆไม่ได้เกลียดหรอกนะ แต่การได้เห็นเธอทุกวันมันเป็นการย้ำเตือนตัวผมเองมากกว่า"
        "ว่าจริงๆแล้วผมช่วยเธอไม่ได้"
        "คงต้องโทษตัวเองที่ยังจะย้อนกลับมาด้วยความมั่นใจครึ่งๆกลางๆสินะ"
        stop music fadeout 1.5
        play sound "audio/knocking.ogg"
        mc "นี่! ยูกิอยู่รึเปล่า?"
        hide mc shirt sad at right
        show mc shirt at right
        "มินะ? มาทำไมกัน"
        girl1 "ไหนบอกว่าไม่สบายไง วันนี้ก็เลยลาเรียนแล้วซื้อของมาฝาก"
        play music "audio/out of mere play.ogg"
        girl1 "เปิดประตูหน่อยสิ"
        "ยัยนั่นยุ่งไม่เข้าเรื่องอีกแล้ว"
        menu :
            "ทำอะไรดี"
            "เดินไปเปิดประตู":
                jump story21
            "ปล่อยเฉยๆ":
                jump story22

    label story21:
        hide mc shirt red at right
        show satonaka smile at right
        with dissolve
        girl1 "โห ห้องโล่งชะมัดเลยนะ ต่างจากห้องฉันคนละขั้วเลย"
        girl1 "เอานี่อาหารแวะไปซื้อมาให้ ถึงจะเล็กน้อยแต่ถ้าไม่สบายจะปล่อยให้ท้องว่างไม่ได้นะ"
        m "ขอบคุณนะ"
        girl1 "เอาน่าเรื่องแค่นี้อีกนี้นายคงไม่ได้ป่วยการเมืองใช่รึเปล่า"
        menu :
            "ตอบดีๆนะ"
            "ไม่สบายจริงๆนะ":
                $ friendshipg1 += 2
                jump sick
            "ก็แค่ไม่อยากเรียนเอง":
                $ friendshipg1 += 1
                jump fakesick
        label sick:
            girl1 "งั้นก็คิดถูกจริงๆที่โดดเรียนตามมาด้วย"
            girl1 "จะได้มีคนดูแลนายด้วยไง ยังไงก็อยู่คนเดียวไม่ใช่หรอ"
            "ไม่รู้ว่าเพราะอะไรแต่เรื่องมันกลายเป็นแบบนี้ซะแล้ว"
            jump story2
        label fakesick:
            girl1 "ว่าแล้วเชียว นี่ก็เหมือนกันแหละหน่า เปิดเทอมวันแรกจะไม่ไปหน่อยก็คงไม่เป็นไร"
            m "เอาจริงหรอเนี่ย"
            jump story2
    label story22:
        hide mc shirt red at right
        show satonaka angry at right
        with dissolve
        girl1 "ไม่อยู่หรอ คิดว่าเป็นพวกติดห้องซะอีก"
        girl1 "งั้นลองสักหน่อยละกัน"
        play sound "audio/breakdoor.mp3"
        with hpunch
        m "นี่เธอทำอะไรเนี่ยยยยยยยยยยย!!!"
        girl1 "ถ้าอยู่ก็เปิดประตูดีๆสิ ถ้าเกิดนายเป็นอะไรขึ้นมาจะทำยังไงละเนี่ย"
        girl1 "ส่วนเรื่องประตูนี่ขอโทษด้วยแล้วกันนะ"
        "ตายแน่ๆเรา ไหนจะเรื่องประตูอีก แต่เห็นเธอสดใสแบบนี้ก็ดีแล้วละ"
        hide satonaka angry at right
        show satonaka curious at right
        girl1 "โห ห้องโล่งชะมัดเลยนะ ต่างจากห้องฉันคนละขั้วเลย"
        girl1 "เอานี้อาหารแวะไปซื้อมาให้ ถึงจะเล็กน้อยแต่ถ้าไม่สบายจะปล่อยให้ท้องว่างไม่ได้นะ"
        jump story2

    label story2:
        show satonaka curious at right
        with dissolve
        girl1 "แล้วนี่เป็นอะไรเนี่ย บอกมาตรงๆนะ อุตส่าห์มาหาทั้งที"
        show satonaka smile at right
        with dissolve
        girl1 "เอาเถอะคงไม่ถามนายหรอก นานๆทีนายก็เป็นแบบนี้ อยากจะหาที่สงบแล้วแวะมาอยู่คนเดียว"
        girl1 "แล้วนี่เจอเรื่องอะไรไม่ดีมาใช่ไหม นานๆทีจะเล่าให้เพื่อนฟังก็ได้นะ"
        girl1 "ฉันนะ เวลาเจอเรื่องแย่ๆก็ชอบกลับไปคิดคนเดียวเหมือนกัน แต่หลายครั้งมันก็ไม่ได้อะไรนะ"
        girl1 "เพราะงั้นฉันที่เป็นเพื่อนนายมาตั้งนาน ดูออกอยู่แล้ว จู่ๆคนอย่างนายจะออกจากโรงเรียนมาเฉยๆโดยไม่คิดอะไร"
        girl1 "ไม่ค่อยเหมือนนายที่ฉันรู้จักเลยนะ"
        stop music fadeout 1.0
        play music "audio/Recollections.ogg"
        "ตัวผมนั้นคงไม่กล้าเล่าเรื่องที่เกิดขึ้นให้ฟังหรอก"
        scene black
        with fade
        "จริงๆแล้วผมไม่ควรกลับมากล้าเจอหน้าคุยกับเธอด้วยซ้ำ"
        "ทุกคนน่าจะเคยได้ยินเรื่อง Butterfly Effect กันใช่ไหม"
        "หากเกิดบางสิ่งที่อาจจะเป็นเรื่องเล็กน้อยจากจุดเริ่มต้น แต่เกิดการเปลี่ยนแปลงของผลลัพธ์ไปเรื่อยๆ"
        "จนสุดท้ายมันจะออกมาในทางที่คาดไม่ถึงเลยละ"
        "การที่ผมพูดแต่ละคำพูด"
        "แต่ละประโยคโดยไม่ให้สนใจความรู้สึกตัวเองก็คงเป็นไปไม่ได้"
        scene bg old room
        with dissolve
        show satonaka smile at right
        with dissolve
        girl1 "นายนะ เป็นอย่างนี้มานานแล้วนะ เอาแต่คิดไปเรื่อยไม่สนเรื่องตัวเองบ้างเลย"
        girl1 "เอาแต่กดดันตัวเองไปก็ไม่ได้อะไรหรอกนะ เพราะงั้นทำไมไม่มาลองใหม่กันอีกครั้งละ"
        "นั่นสินะ"
        "มินะพูดถูกแล้ว"
        "ถ้าหากเรายังคงทำตัวไม่ได้เรื่องแบบนี้สุดท้ายก็จะไม่เกิดประโยชน์กับใครเลย"
        hide satonaka smile
        show satonaka sad at right
        with dissolve
        girl1 "อ่ะ นี่อยู่กับนายจนเย็นขนาดนี้แล้วหรอ"
        girl1 "ยังไงก็พรุ่งนี้อย่าลืมไปโรงเรียนให้ได้นะ"
        hide satonaka sad
        with dissolve
        show mc shirt sad2 at left
        with dissolve
        m "ขอบคุณมากนะ ขอบคุณจริงๆ"
        m "ดีใจจริงๆที่ได้เจอเธออีก..."
        stop music fadeout 1.0
        scene black
        with fade
        centered "วันต่อมา"
        play sound "audio/bird.wav"
        "เช้าแล้วหรอ"
        "นี่เราใช้เวลาเสียไปวันนึงเลยหรอ"
        scene bg old room
        with dissolve
        "ถ้างั้นจะอยู่เฉยๆไม่ได้แล้วสินะ"
        "เตรียมตัวไปโรงเรียนก่อนละกัน"
        scene black
        with fade
        centered "ระหว่างทาง"
        play music "audio/New Days.ogg"
        scene subway
        with dissolve
        girl1 "บังเอิญจังเลยนะ นี่ยูกิใช่ไหม"
        "ปวดหัวตั้งแต่เช้าเลยนะเนี่ย"
        girl1 "เดี๋ยวนี้เย็นชาขึ้นนะไม่คิดจะตอบหน่อยรึไง"
        show satonaka at right
        with dissolve
        girl1 "คิดจะหลบหน้ากันรึไง คนเค้าเป็นห่วงนะ"
        show mc hood2 at left
        with dissolve
        menu :
            "ตอบอะไรดีนะ"
            "อรุณสวัสดิ์นอนดึกไปหน่อยเลยยังมึนๆน่ะ":
                $ friendshipg1 += 1
                jump choice1_1
            "เสียงดังตั้งแต่เช้าเลยเดี๋ยวคนอื่นก็มองกันมาหรอก":
                $ friendshipg1 -= 1
                jump choice1_2

        label choice1_1:
            girl1 "พักผ่อนบ้างก็ดีนะนายนะ"
            girl1 "แล้วนี่ถ้าฉันจำไม่ผิดหมอนั่นก็สอบเข้ามาได้ด้วยนะ"
            m "หมอนั่น?"
            girl1 "เจ้าคิตากาวะไง ที่นายไม่ค่อยถูกโฉลกเท่าไหร่"
            m "เดี๋ยวนะไม่ใช่แค่เราสองคนหรอ"
            "ที่ผมย้อนรอบก่อนมันไม่ใช่แบบนี้ หมอนั่นไม่เคยอยู่ที่นี่"
            "คงต้องลองเสี่ยงละนะ"
            jump story2_1

        label choice1_2:
            hide satonaka
            show satonaka warm angry at right
            girl1 "สงสัยช่วงนี้จะกินยาผิดขวดจริงๆ ช่วงนี้ไม่เป็นมิตรเลยนะนายเนี่ย"
            girl1 "คนเค้าเป็นห่วงตั้งแต่เช้า เมื่อวานก็อุตส่าห์ไปหาไม่คิดจะสำนึกบุญคุณกันเลยหรอ"
            m "ขอบคุณมากจริงๆ"
            hide satonaka
            show satonaka at right
            with dissolve
            girl1 "ได้ยินว่าเจ้าคิตากาวะ ที่นายไม่ค่อยถูกโฉลกจะอยู่ห้องเดียวกันนะ"
            m "หมอนั้นสอบเข้าที่นี่ได้ด้วยหรอ?"
            girl1 "แล้วก็เห็นใน SNS เพื่อนๆในห้องละดูถ้าจะโด่งดังในหมู่สาวๆใช้ได้เลย"
            "มันผิดปกติ"
            "ถ้าพูดให้ถูกก็คือทุกครั้งที่ผมย้อนมาหมอนั่นไม่เคยอยู่ที่นี่เลย"
            "มันเกิดอะไรขึ้นกันแน่"
            jump story2_1

    label story2_1:
        scene classroom
        with dissolve
        "หมอนั่นอยู่นี่งั้นหรอ เป็นไปได้ยังไงกัน"
        "ก็ทุกครั้งที่เราย้อนกลับมาไม่เคยมีหมอนั่นอยู่เลยนี่นา"
        show akechi smile at right
        with dissolve
        male1 "คิดถึงฉันอยู่งั้นหรอ หน้าเครียดมาเชียว"
        male1 "เปิดเรียนทั้งทีแล้ว สดใสหน่อยสิครับ"
        "พูดถึงปีศาจปีศาจก็มา"
        menu :
            "ตอบอะไรดีนะ"
            "ไม่ได้เจอกันนานเลยนะ ดีจังที่เจอกันอีก":
                $ friendshipm1 += 1
                jump choice2_1
            "จะโผล่มาทำไมละเนี่ย คิดว่าหลุดพ้นจากนายแล้วแท้ๆ":
                jump choice2_2

        label choice2_1:
            hide akechi smile at right
            show akechi at right
            male1 "ผมก็คิดอย่างนั้นเหมือนกันครับ ไหนๆก็เจอคนรู้จักแล้วถ้าไม่ทักทายก็คงเสียมารยาท"
            male1 "จะว่าไปดูเหมือนเพื่อนๆร่วมชั้นจะดูสดใสจังเลยนะครับ"
            "หมอนี่เป็นคนเข้ากับคนง่ายมากๆ ซึ่งต่างจากตัวผมลิบลับเลย"
            "ไม่ได้การถ้าไม่ตอบไปคงจะดูแปลกๆสินะ"
            show mc hood2 at left
            with dissolve
            m "จะว่าไปนายก็อยู่ห้องนี้ด้วยงั้นหรอ"
            hide akechi smile at right
            show akechi smile at right
            male1 "ได้ยินว่านายไม่สบายก็เลยไม่ได้มางั้นสินะ ใช่เลยผมนั่งข้างหลังนายนี่เอง หลังจากนี้ 1 ปีก็ฝากตัวด้วยนะครับ"
            jump story2_2

        label choice2_2:
            male1 "เย็นชากับผมจังเลยนะครับ คิดว่าไหนๆก็เป็นเพื่อนกันก็ควรจะมาทักทายไว้ก่อน"
            hide akechi smile at right
            show akechi at right
            male1 "แต่ไม่แปลกใจหรอกนะครับ คุณทาคุโตะเป็นแบบนี้มาตั้งแต่สมัยก่อนแล้ว"
            "หมอนี่ยังเหมือนเดิมไม่เปลี่ยนเลย สดใส เข้ากันได้กับทุกคน"
            "จะว่าไปก็ควรจะตอบไปให้ดูไม่เปลี่ยนสินะ"
            show mc hood2 at left
            with dissolve
            m "นายก็ยังสดใสเหมือนเดิมเลย ไม่คิดว่าเพื่อนๆจะตกใจบ้างหรอ"
            m "แล้วก็อีกอย่างเดี๋ยวก็เริ่มเรียนแล้วไม่ไปห้องตัวเองหรอ"
            hide akechi smile at right
            show akechi smile at right
            male1 "ยังไม่รู้สินะครับ เพราะเมื่อวานคุณทาคุโตะไม่สบาย"
            male1 "ผมนั่งด้านหลังตรงนี้เองครับ หลังจากนี้ 1 ปีฝากตัวด้วยนะครับ"
            male1 "ยังคาดหวังความเป็นมิตรจากคุณอยู่นะครับ"
            jump story2_2

    label story2_2:
        stop music fadeout 1.0
        scene black
        with fade
        centered "พักกลางวัน"
        play music "audio/Tsuiokunokakera.ogg"
        "หลังจากนี้การตัดสินใจการกระทำเราจะส่งผลแล้วสินะ"
        "เพราะที่ผ่านมาที่เราทำไป"
        "ก็เหมือนรอบที่ผ่านๆมา"
        "ครั้งนี้ต้องไม่เหมือนเดิม"
        "เราได้โอกาสแล้ว แถมครั้งนี้ยังมีเพื่อนอย่างจุนอิจิ"
        "การที่หมอนั้นได้มาโผล่ที่นี้ต้องไม่ใช่เรื่องบังเอิญอย่างแน่นอน"
        scene bg canteen
        with dissolve
        "คิดมากไปก็เท่านั้น จริงๆโรงเรียนนี้อาหารก็ยังอร่อยเหมือนเดิมเลย"
        "คงดูแปลกสินะ เด็กมัธยมมานั่งกินข้าวเที่ยงคนเดียวแบบนี้"
        "ปกติก็ต้องเป็นช่วงที่เกาะกลุ่มอยู่กับเพื่อนๆ ไม่แยกตัวแบบนี้"
        "ชั่งมันเถอะ ยังไงเราก็ไม่ใช่เด็กมัธยมแล้วจะไปคิดมากเรื่องแบบนี้ก็เสียเวลา"

        if friendshipg1 >= 3 and friendshipm1 >= 1:
            jump story2_2best
            label story2_2best:
            girl1 "คิดจะแยกตัวคนเดียวอีกแล้วหรอนายนะ"
            male1 "ถ้าไม่รังเกียจผมขอนั่งด้วยคนนะครับ"
            show akechi smile at right
            with dissolve
            show satonaka warm smile2 at left
            with dissolve
            m "ทั้งสองคน..."
            m "ตามมาถึงนี่เลยงั้นหรอ จะว่าไปทั้งคู่ไปสนิทกันตอนไหนเนี่ย"
            hide akechi smile at right
            show akechi at right
            male1 "ก็เพราะคุณทาคุโตะนั้นแหละครับทำให้พวกผมเป็นห่วง"
            hide satonaka warm smile2 at left
            show satonaka2 at left
            girl1 "นายน่ะทำให้พวกเราเป็นห่วงนะ"
            girl1 "แค่มาเรียนวันแรกก็โดดเรียนหนีไปซะแล้ว"
            male1 "เพราะงั้นผมเลยคิดว่าถ้ามาดูแลคุณหน่อยน่าจะดีครับ"
            girl1 "นายทำตัวแปลกๆมาตั้งแต่เมื่อวานแล้วนะ"
            male1 "ผมเห็นด้วยกับที่คุณโซโนซากิพูดนะครับ คุณทาคุโตะดูไม่สดใสเหมือนเมื่อก่อนเลย"
            hide akechi at right
            show akechi smile at right
            male1 "หรือจะให้พูดคือรู้สึกเหมือนคนละคนเลยล่ะครับ"
            "หมอนี่ยังดูน่ารำคาญเหมือนเดิมเลย"
            "แต่แบบนี่ก็ไม่เลวหรอกนะ"
            m "ขอบคุณนะทั้งคู่เลย ขอบคุณจริงๆ"
            hide satonaka2 at left
            show satonaka warm smile2 at left
            girl1 "เห็นไหม นายเปลี่ยนไปจริงๆด้วย ขอบคุณพวกเราแบบนี้"
            girl1 "ก็พวกเราเป็นเพื่อนกันไม่ใช่หรอ"
            male1 "แต่ถ้าคุยกันแบบนี้น่าจะไม่ได้รับประทานอาหารจนเวลาหมดนะครับ"
            play sound "audio/School Bell.wav"
            male1 "งั้นหลังเลิกเรียนมาเจอกันหน่อยนะครับ อย่าหนีไปละครับ คุณทาคุโตะ"
            "ทุกอย่างเกิดขึ้นหลังจากนี้ตัวผมนั้น"
            "ไม่ได้คิดเลยว่าเรื่องหลังจากนี้มันจะบานปลายไปได้มากกว่านี้"
            jump story2_3

        elif friendshipm1 >= 1 and friendshipg1 < 3 :
            jump story2_2m
            label story2_2m:
            male1 "ถ้าไม่รังเกียจผมขอนั่งด้วยคนนะครับ"
            show akechi smile at right
            with dissolve
            m "นี่นายตามมาด้วยหรอ"
            m "ตามมาถึงนี่เลยหรอ"
            hide akechi smile at right
            show akechi at right
            male1 "อยู่ๆเปิดเรียนวันแรกก็หายไปแบบนั้นเลยคิดว่าต้องมีอะไรแน่ๆ"
            male1 "คิดว่าการเป็นห่วงคนรู้จักก็ไม่ใช่อะไรแปลกไม่ใช่หรอครับ"
            male1 "แต่ทาคุโตะก็ดูจริงจังกว่าเมื่อก่อนมากเลยทั้งสายตา ทั้งคำพูด"
            hide akechi at right
            show akechi smile at right
            male1 "หรือจะให้พูดคือเหมือนคนละคนกับตอนม.ต้นเลยครับ"
            male1 "เพราะงั้นผมในฐานะที่ต้องเป็นเพื่อนร่วมห้องกันอย่างน้อยอีก 1 ปีแถมยังรู้จักกันมาก่อน"
            hide akechi smile at right
            show akechi at right
            male1 "จะให้ปล่อยเพื่อนที่รู้จักไว้คงไม่ได้หรอกครับ"
            m "ขอบคุณนายนะ ขอบคุณจริงๆ"
            male1 "เรื่องแค่นี้ปล่อยไม่ได้หรอกครับ"
            play sound "audio/School Bell.wav"
            male1 "แต่ว่าก่อนจะเข้าเรื่องกันผมว่ารอเลิกเรียนดีกว่านะครับ"
            male1 "งั้นเจอกันหลังเลิกเรียนครับ ผมมีคนอยากให้เจอด้วย คนที่คุณคิดนั่นแหละครับ"
            "หลังจากนี้จะมีอะไรเกิดขึ้นตัวผมก็ไม่อาจจะรู้ได้"
            "แต่ว่าครั้งนี้มันไม่เหมือนครั้งก่อนๆ โอกาสที่ได้มาผมจะเสียมันไปไม่ได้"
            jump story2_3

        else:
            jump story2_2g
            label story2_2g:
            girl1 "คิดจะแยกตัวคนเดียวอีกแล้วหรอนายนะ"
            show satonaka warm smile at right
            with dissolve
            m "นี่เธอตามมาด้วยหรอ"
            hide satonaka warm smile at right
            show satonaka at right
            girl1 "คิดว่าจะปล่อยนายไว้ตัวคนเดียวรึยังไง"
            girl1 "เมื่อวานก็เห็นมากับตาแล้วว่านายไม่ปกติช่วงนี้"
            girl1 "ก็เลยคิดว่ามีเรื่องต้องคุยกับนายให้ชัดเจน"
            hide satonaka at right
            show satonaka warm smile at right
            girl1 "อีกอย่างนายที่เคยรู้จักก็ไม่ค่อยคิดมากอะไรแบบนี้ด้วย"
            girl1 "ออกจะดูเป็นคนเลื่อนลอยไม่ค่อยสนใจเรื่องข้างหน้าแล้วใช้ชีวิตไปเรื่อยๆ"
            girl1 "แต่นี่เหมือนนายคิดมากมาตั้งนานแล้ว"
            hide satonaka warm smile at right
            show satonaka at right
            girl1 "งั้นเรื่องนี้ไว้แค่นี้ก่อนทางนี้ข้าวหน้าเนื้อก็จะหายร้อนแล้วด้วย"
            play sound "audio/School Bell.wav"
            girl1 "อย่างที่คิดเลยงั้นหลังเลิกเรียนเจอกันนะ ก่อนหน้านี้บอกหมอนั่นไว้แล้วล่ะเพราะงั้นต้องมาด้วยล่ะ"
            m "เอ๊ะ!?"
            m "ได้เลยแล้วเจอกันนะ ขอบคุณมากนะ"
            "อยากกลับมาช่วยเธอ แต่กลับรู้สึกเหมือนโดนช่วยซะเอง"
            "ครั้งนี้ต้องทำให้ได้... ช่วยเธอให้ได้เลย"
            jump story2_3

    label story2_3:
        stop music fadeout 1.0
        scene black
        with fade
        centered "เลิกเรียน"
        scene bg old room
        with dissolve
        play sound "audio/knocking.ogg"
        show satonaka warm smile2 at left
        with dissolve
        girl1 "รบกวนหน่อยนะ"
        show akechi smile at right
        with dissolve
        male1 "รบกวนหน่อยนะครับ"
        play music "audio/Like a dream come true.ogg"
        m "...?"
        m "เดี๋ยวนะ ที่ไม่ได้บอกสถานที่ว่าที่ไหนก็เพราะงี้สินะ..."
        male1 "ใช่เลยครับไหนๆก็จะมารบกวนทั้งทีแล้วก็ต้องเป็นห้องคุณทาคุโตะนี่แหละครับ"
        girl1 "เพื่อนมาห้องทั้งทีไม่เตรียมอาหารให้หน่อยหรอ"
        m "คนเค้าก็พึ่งกลับมาจากโรงเรียนเหมือนกันนะ"
        male1 "ผมเห็นด้วยเรื่องรับแขกควรมีอาหารเหมือนกับที่คุณโซโนซากิพูดนะครับ"
        m "ทั้งคู่นี้มัน..."
        "แต่ผมก็ไม่ได้คิดว่ามันเลวร้ายหรอกนะ"
        "มีเพื่อน ได้ใช้ชีวิตมัธยมปลายอีกครั้ง"
        "เป็นเด็กมัธยมปลายแบบนี้ก็ไม่เลวเลยเลย"
        m "เข้าใจแล้วๆ"
        ac "รบกวนด้วยนะ"
        scene bg old room
        with dissolve
        centered "ผ่านไปครึ่งชั่วโมง"
        show mc shirt2 at left
        m "นี่อาหารมาแล้วนะ"
        m "ไม่แน่ใจว่าจะชอบกันรึเปล่า"
        "ตัวเราเองก็ไม่ได้ทำอาหารกินเองนานแล้วด้วยสิ"
        "ก่อนหน้านี้เราตอนทำงานพอกลับมาจากทำงานเสร็จในแต่ละวัน"
        "ก็เอาแต่อาศัยร้านสะดวกซื้อตลอดเลย ไม่มีเวลาจะทำอาหารกินเองด้วยซ้ำ"
        "ดีสุดก็แค่ข้าวปั้น ถึงจะเคยทำเพราะต้องประหยัดงบก็เถอะ"
        "ยังไงเรื่องนี้ก็เป็นไม่กี่เรื่องที่มั่นใจละนะ"
        scene curry
        with dissolve
        girl1 "โหนี่ดูน่ากินจังเลยนะเนี่ย"
        male1 "เพราะงี้เลยอยู่ตัวคนเดียวได้โดยไม่ต้องออกไปซื้ออาหารข้างนอกสินะครับ"
        male1 "แต่ฝีมือนี่ถือว่าเหนือกว่าเด็กมัธยมปลายอีกนะครับ งานอดิเรกหรอครับเนี่ย"
        menu :
            "ตอบอะไรดี"
            "แค่นิดหน่อยเอง":
                $ friendshipg1 += 1
                $ friendshipm1 += 1
            "ถ้าเรื่องอาหารไว้ใจได้เลย":
                $ friendshipg1 += 1
                $ friendshipm1 += 1
        scene bg old room
        with dissolve
        show satonaka warm smile2 at left
        with dissolve
        girl1 "อาหารอร่อยเลยนะเนี่ย อร่อยกว่าแกงกะหรี่ตามร้านอาหารอีก"
        girl1 "เก่งขนาดนี้เปิดร้านอาหารยังได้เลยนะ"
        hide satonaka warm smile2 at left
        show satonaka2 at left
        girl1 "เอาเวลาที่ไหนไปฝึกมาล่ะเนี่ยไหนจะเรื่องสอบเข้าอีกนายนี่เก่งจังเลยนะเนี่ย"
        show akechi at right
        with dissolve
        male1 "จริงๆผมก็สงสัยนะครับ เห็นเป็นคนเงียบๆแบบนี้แต่กลับมีด้านแปลกๆที่ไม่คิดว่าจะมีเยอะเลย"
        hide akechi at right
        show akechi smile at right
        male1 "ถามไปคุณทาคุโตะคงเลี่ยงที่จะไม่ตอบเพราะงั้นเรามาเข้าเรื่องกันดีกว่าครับ"
        stop music fadeout 1.0
        male1 "คุณทาคุโตะ คุณไม่ใช่เด็กมัธยมปลายสินะครับ"
        play music "audio/Reasoning.ogg"
        girl1 "เอ๊ะ นี่คิตากาวะ นายไม่สบายตรงไหนรึเปล่า ที่เรามานี่ไม่ใช่ว่าเพราะเป็นห่วงหมอนี่หรอ"
        hide satonaka2 at left
        show satonaka warm sad2 at left
        girl1 "แล้วคำถามไร้สาระนี่มันอะไรเนี่ย"
        hide akechi smile at right
        show akechi at right
        male1 "ผมจริงจังครับ คิดว่าคนที่ไม่เลือกเข้าโรงเรียนเดียวกับคุณแบบผมมาเข้าโรงเรียนเดียวกับคุณทาคุโตะ"
        male1 "มันไม่แปลกไปหน่อยหรอครับ คุณเองก็น่าจะรู้ตัว"
        male1 "ว่าพวกเราไม่ใช่เด็กแล้วนะครับ"
        "อะไรกัน"
        "นี่แสดงว่าเราไม่ได้คิดไปเองหรอว่าครั้งก่อนๆหมอนี่ไม่ได้อยู่"
        male1 "ถ้าถามว่าผมรู้ได้ยังไง ก็เพราะรอบนี้ผมกลับมาก่อนที่คุณเลือกทางที่ผิดยังไงละครับ"
        male1 "จะว่ากันแล้วคุณที่ผมรู้จัก"
        male1 "ตายไปแล้วครับ"
        m "เอ๊ะ?"
        m "เมื่อกี้คงคิดว่านายล้อเล่น แต่นี่จริงจังสินะ"
        hide satonaka warm sad at left
        with dissolve
        show mc shirt2 at left
        with dissolve
        menu :
            "ตอบดีๆนะ"
            "ใช่แล้วละ":
                $ friendshipm1 += 2
                male1 "เป็นอย่างที่คิดไว้จริงๆสินะครับ"
            "พูดเรื่องอะไรของนายเนี่ย":
                $ friendshipm1 -= 1
                male1 "ถึงจะปฏิเสธแบบนี้ผมก็ยังไม่ปัดข้อสงสัยหรอกนะครับ"
                male1 "แต่ว่าอย่างน้อยก็อยากจะให้ไว้ใจเพื่อนกันหน่อย"
        m "ถ้านายว่าอย่างนั้นก็ตามนั้นล่ะ"
        male1 "งั้นผมจะถามตรงๆเลยที่คุณกลับมาในเวลานี้"
        male1 "เพราะคุณโซโนซากิสินะครับ"
        male1 "จากที่ผมรู้มาคงไม่มีเหตุผลอื่นแล้วละครับ"
        hide mc shirt2 at left
        show mc shirt sad2 at left
        m "ใช่แล้วล่ะ"
        hide akechi at right
        with dissolve
        show satonaka warm angry at right
        with dissolve
        girl1 "อธิบายมาเดี๋ยวนี้เลยนะว่าเกิดอะไรขึ้น"
        girl1 "แล้วฉันไปเกี่ยวอะไรกับเรื่องบ้าๆที่่พวกนายพูดถึงเนี่ย"
        hide mc shirt sad2 at left
        with dissolve
        show akechi2 at left
        male1 "เรื่องนั้นผมจะอธิบายให้ฟังเองละกันครับ"
        stop music fadeout 1.0
        male1 "การที่ให้คุณทาคุโตะเขาอธิบายด้วยตัวเองจะเป็นการทำร้ายเขาเกินไปครับ"
        play music "audio/Freedom and Security.ogg" volume 0.6
        scene bg lab
        with dissolve
        show akechi2 at left
        with dissolve
        male1 "คุณทาคุโตะในโลกของผม เขาเป็นนักวิจัยเกี่ยวกับโรคสุขภาพทางจิต"
        male1 "จากที่ผมรู้มาเพราะกลุ่มเพื่อนๆ คุณทาคุโตะดูมุ่งมั่น จริงจังมากๆ"
        male1 "คุณทาคุโตะตั้งใจทำงานถึงจะไปไม่ได้สวยเท่าไหร่ แต่ก็มีความพยายาม"
        male1 "แต่แค่ความพยายามคงทำให้สำเร็จดั่งหวังไม่ได้ใช่ไหมละครับ"
        male1 "ดังนั้นผมเลยคาดเดาแรงจูงใจคุณจากตรงนั้น"
        male1 "แต่ในโลกที่ผมอยู่นั้นคุณทาคุโตะ จบการใช้ชีวิตตัวเองไม่ได้ดีเท่าไหร่ครับ"
        scene black
        with fade
        centered "คุณน่ะฆ่าตัวตายไปในโลกที่ผมมา"
        scene bg lab
        with dissolve
        show akechi2 at left
        with dissolve
        male1 "ครอบครัวคุณโซโนซากิเสียชีวิตจากเหตุคนร้ายเข้าบุกที่พักอาศัย"
        male1 "มีเพียงคุณโซโนซากิที่รอดมาได้ครับ แต่ว่าก็ไม่ใช่ในฐานะคนปกติแล้ว"
        male1 "นั่นเป็นเหตุผลที่ให้คุณทาคุโตะเลือกเป็นนักวิจัยทางจิต"
        male1 "แต่สุดท้ายแล้วไม่ว่าจะพยายามเท่าไหร่อาการคุณก็ไม่สามารถรักษาได้"
        male1 "แทนที่คุณทาคุโตะเลือกจะเดินหน้าใช้ชีวิตต่อไป"
        male1 "คงเป็นช่วงนี้ล่ะครับ ชีวิตผมจะถูกย้อนกลับมาที่วัยมัธยมปลาย"
        male1 "ซึ่งถ้ายอมรับแบบนี้ต้นเหตุคงเป็นผลที่เกิดจากจากคุณทาคุโตะแล้วล่ะครับ"
        male1 "คุณทาคุโตะในโลกผม เหมือนจะเห็นไปอีกแบบนะครับ"
        male1 "เพราะก่อนที่ผมจะย้อนกลับมาได้ซึ่งปกติน่าจะเกิดพร้อมคุณ"
        male1 "แต่ก่อนหน้านี้ผมเห็นเรื่องคุณฆ่าตัวตาย แล้วทำให้ผมถูกส่งย้อนกลับมา"
        male1 "มันไม่ควรจะเป็นแบบนั้นใช่ไหมล่ะครับ"
        male1 "เพราะคุณไม่จำเป็นต้องฆ่าตัวตายซะหน่อย เว้นแต่คุณหมดกำลังใจในการใช้ชีวิต"
        male1 "แต่มันก็ไม่สมเหตุสมผลอยู่ดี ถ้าหากคุณฆ่าตัวตาย แล้วตัวคุณที่คุยกับผมในตอนนี้มาจากช่วงเวลาครั้งไหน"
        male1 "บางทีผมอาจจะมาจากคนละช่วงเวลากับคุณที่มีความคล้ายกันก็ได้ครับ"
        male1 "แต่การที่ผมไปเกี่ยวข้องด้วยนี้ก็ไม่สนุกซะเลยนะครับ"
        male1 "เรื่องแบบนี้ผมทนดูเฉยๆไม่ได้หรอกครับ"
        male1 "เพราะงั้นผมถึงได้เล่าให้คุณทาคุโตะฟังรวมถึงคุณโซโนซากิด้วยครับ"
        stop music fadeout 2.0
        scene bg old room
        with dissolve
        play music "audio/Alleycat.ogg"
        show akechi smile2 at left
        with dissolve
        male1 "แต่ไม่ต้องตกใจไปหรอกครับ เพราะผมเองก็พึ่งรู้ถึงพลังตัวเอง"
        male1 "ย้อนเวลาได้นี่วิเศษไปเลยนะครับ แต่ประเด็นที่ผมรู้ตัวคือทุกครั้งที่ผมย้อนเวลา"
        hide akechi smile2 at left
        show akechi2 at left
        male1 "คุณมักจะทำสิ่งที่เปลี่ยนไปในแต่ละครั้งต่างจากคนอื่นๆ"
        male1 "อีกอย่างเพราะว่าผมไม่ได้สนิทกับคุณมากตั้งแต่มัธยมต้นผมก็เลยไม่ได้คุยอะไรมาก"
        male1 "นอกจากรู้ว่าคุณนั้นสนิทกับคุณโซโนซากิมากๆ"
        male1 "อีกอย่างที่ผมย้อนกลับมาได้แล้วเจอตัวคุณได้ง่ายๆนั้นเพราะผมย้อนด้วยตัวเองไม่ได้"
        male1 "ทุกครั้งที่คุณย้อนกลับมา ผมจะโดนย้อนกลับมาด้วย"
        male1 "ด้วยความที่เราไม่ได้สนิทกันเลย พวกเราเลยไม่คิดที่จะติดต่อกัน"
        male1 "โดยไม่รู้ว่าการกระทำพวกเรานั้นส่งผลกระทบกันทั้งคู่"
        male1 "ครั้งนี้ผมก็เลยยอมให้ทุกอย่างเป็นเหมือนรอบก่อนๆและรอมาถามคุณตรงๆ"
        male1 '"พลังแบบนี้มันไม่ได้สนุกนะครับ ถ้าจะใช้กรุณาวางแผนอย่างรอบคอบด้วย"'
        male1 "เพราะคุณผมก็เลยใช้ชีวิตต่อไม่ได้ด้วย"
        hide akechi at left
        show akechi smile2 at left
        male1 "เพราะงั้นถ้าอะไรที่ผมช่วยได้ก็บอกมาได้เลยครับ"
        male1 "อย่าพึ่งกลัวผมไปนะผมไม่ได้มาขู่"
        show mc shirt sad at right
        with dissolve
        m "รู้อยู่แล้วละ ยังไงก็ขอบคุณมากนะ"
        m "นายนี่ดูสังเกตคนอื่นมากกว่าที่คิดไว้เยอะเลยนะ"
        male1 "ถ้าไม่ใช่เรื่องที่เกี่ยวข้องกับตัวผมก็ไม่ได้อยากจะยุ่งหรอกครับ"
        hide akechi smile2 at left
        show akechi2 at left
        male1 "ถึงจะดูว่าผมเข้ากับเพื่อนๆได้แต่จริงๆแล้วตัวผมก็ไม่ได้มีเพื่อนมากนักหรอกครับ"
        hide akechi at left
        show akechi smile2 at left
        male1 "เพราะงั้นก็หลังจากนี้จนกว่าเรื่องแปลกๆนี้จะจบขอฝากตัวด้วยนะครับ"
        menu :
            "ตอบดีๆนะ"
            "ได้เลยละ ขอบคุณมากนะ":
                $ friendshipm1 += 2
                male1 "ทางผมต่างหากที่ต้องขอบคุณที่ไว้ใจครับ"
                male1 "จริงๆคิดว่าการคุยกับคุณน่าจะเป็นเรื่องที่ยากกว่านี้"
            "นายจะยุ่งไม่เข้าเรื่องรึเปล่าเนี่ย":
                male1 "มองผมเป็นคนแบบนั้นหรอครับ"
                male1 "แต่ไม่แปลกละนะครับ"
                male1 "การที่คุณจะไม่ไว้ใจผมก็ไม่เกินที่คาดไว้ครับ"
        hide akechi smile2 at left
        show akechi2 at left
        male1 "งั้นวันนี้ผมขอตัวก่อนนะครับที่เหลือฝากอธิบายคุณโซโนซากิด้วยครับ"
        play sound "audio/closingdoor.mp3"
        hide akechi2 at left
        with dissolve
        stop music fadeout 1.0
        show satonaka warm sad2 at left
        with dissolve
        girl1 "หมอนั่นทิ้งไปแบบนี้เลยหรอ"
        girl1 "ถ้างั้นอธิบายมานะว่าเรื่องมันอะไรเนี่ย"
        girl1 "เรื่องมันมาพร้อมกันเต็มไปหมดเลยแบบนี้ฉันรับไม่ไหวนะ"
        play music "audio/Tsuiokunokakera.ogg"
        girl1 "คิดว่าเป็นเรื่องธรรมดา ทำไมมันเกี่ยวข้องกับนาย หมอนั่น"
        girl1 "แล้วก็ยังพูดถึงเรื่องอนาคตของฉันอีก..."
        girl1 "ทั้งหมดที่ว่ามาเป็นเรื่องจริงงั้นหรอ..."
        menu :
            "ตอบดีๆนะ"
            "ไม่ต้องห่วงถึงเป็นเรื่องจริงจะไม่ให้เป็นแบบนั้นอีกแล้วละ":
                $ friendshipg1 += 1
                girl1 "พูดให้สบายใจสินะ"
            "ทั้งหมดเป็นเรื่องจริงที่ผมแก้ไขเองไม่ได้...":
                $ friendshipg1 += 2
                girl1 "งั้นเองหรอ..."
        hide satonaka warm sad2 at left
        show satonaka warm smile2 at left
        girl1 "แต่ยังไงก็ขอบคุณนะ"
        hide satonaka warm sad2 at left
        show satonaka warm blush2 at left
        girl1 "ถ้าจากที่ฟังมาก็ไม่ได้คิดกับฉันแค่เพื่อนสินะ"
        girl1 "ชั่งมันเถอะ ใช่ไหม"
        girl1 "ขอบคุณนะ ก็ไม่รู้หรอกว่าไปทำอะไรให้กับนายบ้าง"
        girl1 "เพราะอย่างนี้ วันแรกที่ไปโรงเรียนเลยหลบหน้าฉันกับเพื่อนๆสินะ"
        hide satonaka warm blush2 at left
        show satonaka warm smile2 at left
        girl1 "จะว่าไปถึงไปบอกเรื่องนี้กับใครๆ ก็คงว่าบ้ากันทั้งนั้นแหละ"
        girl1 "แต่พวกนายทั้งคู่ไม่ใช่คนจะล้อเล่นอะไรแบบนี้"
        girl1 "ถ้าอย่างนั้นมีอะไรก็ติดต่อมาได้ตลอดเลยนะ"
        girl1 "ยังไงเราก็เพื่อนกันอยู่แล้ว"
        girl1 "สำหรับฉันในตอนนี้ล่ะนะ"
        girl1 "งั้นวันนี้ฉันกลับก่อนนะ"
        show mc shirt sad at right
        with dissolve
        m "ขอบคุณนะ ที่ยอมฟังเรื่องบ้าๆแบบนี้"
        m "ไม่คิดว่าจะบอกใครได้ก็เลยเก็บไว้คนเดียวตลอด"
        girl1 "ไม่เป็นไรอยู่แล้ว"
        hide satonaka warm sad2 at left
        show satonaka warm blush2 at left
        girl1 "ยังไงวันนี้ก็ขอบคุณเรื่องแกงกะหรี่ด้วยนะ"
        girl1 "ขอตัวกลับก่อนเดี๋ยวดึกแล้วจะโดนทางบ้านว่าเอา"
        play sound "audio/closingdoor.mp3"
        hide satonaka warm blush2 at left
        with dissolve
        "ขอบคุณจริงๆนะ"
        "ใช้ไม่ได้เลยจริงๆ.... ตัวเรา"
        "สร้างความลำบากให้คนอื่นจริงๆไปแล้วสิ"
        "แล้วยังลากเธอมาเกี่ยวอีก"
        "ครั้งนี้จะพยายามให้ดีที่สุดนะ"
        stop music fadeout 2.0
        scene black
        with fade
        centered "Chapter: 0\nวันที่ 2\nโอกาสที่ย้อนกลับมา"

    label routetest:
        scene black
        with fade
        menu :
            "ทดสอบ"
            "End1":
                jump greenend
            "End2":
                jump blueend
            "End3":
                jump brownend

    #ENDING ROUTE PART 1
    label greenend:
        stop music fadeout 1.0
        play music "audio/Hana no Uta.ogg" volume 0.6
        scene black
        with fade
        "...?"
        "ในที่สุด..."
        "มันก็จบแล้ว"
        "เรื่องราวความเลวร้ายทั้งหมด"
        "มันจบลงแล้ว..."
        "แต่สิ่งที่ต้องแลก"
        "มันก็เกินกว่าที่ตัวฉันนั้นเองจะรับไหว"
        "มันหนักหนาเหลือเกิน"
        "ทำไมต้องเจอเรื่องแบบนี้ด้วย"
        "ไม่เข้าใจ"
        "ไม่เข้าใจว่าทำไมต้องเป็นแบบนี้"
        "ถ้าหาก..."
        "ถ้าหากฉันอยู่คนเดียวคงไม่ไหวแน่ๆ"
        "โลกอันโหดร้ายนี้"
        "แต่อย่างน้อยในวันนี้เขาก็อยู่ด้วยกัน"
        "และคงจะ...ได้แค่หวังว่าเขา..."
        "ไม่จากฉันไปไหนอีกแล้ว"
        "ถึงฉันจะไม่รู้ว่าที่ทำไปมันถูกรึเปล่า"
        "แต่แค่ได้อยู่กับเขาแบบนี้ตลอดไป"
        "ก็พร้อมที่จะใช้ชีวิตต่อแล้ว"
        mc "ไปกันเถอะนะ"
        mc "ออกไปใช้ชีวิตที่พวกเราได้รับมา"
        girl1 "อื้อ ขอบคุณมากนะ"
        stop music fadeout 3.0
        "ขอบคุณที่อยู่ด้วยกันจนถึงตอนนี้นะ"
        "ซักวันเราคงจะได้เจอกันใหม่"
        "หวังว่าวันนั้นคงมาถึง"
        centered "END"
        return

    label blueend:
        stop music fadeout 1.0
        play music "audio/Never More.ogg" volume 0.6
        scene sky
        with dissolve
        "เรื่องราวทั้งหมดผมไม่รู้ว่าควรเป็นแบบนี้รึเปล่า"
        "แต่ในทางที่ผมได้ตัดสินใจนั้น ผมมั่นใจว่าต้องถูก"
        "บางครั้งสิ่งที่เราทำมันอาจจะดูเป็นสิ่งที่ผิดในตอนตัดสินใจ แต่ว่าเราทุกคนไม่ได้มีโอกาสแก้ไขอดีตกันทั้งนั้น"
        "เพราะงั้นการได้ลองทำอะไรให้เต็มที่คงจะดีที่สุดละนะ"
        "ไม่ว่าพวกเราจะตัดสินใจอะไรไปมันก็ย่อมส่งผลตามมา"
        "แต่เพราะแบบนั้นการที่ผมได้โอกาสแบบนี้มันก็ดีมากกว่าคนอื่นๆ"
        "โอกาสที่จะแก้ความผิดพลาดของตัวเอง โอกาสที่จะสร้างความลำบากให้ผู้อื่น"
        "แต่ทุกอย่างที่ว่ามามันก็ได้จบลงแล้ว"
        "เพราะการตัดสินใจ"
        "เพราะเพื่อนๆ"
        "เพราะสังคม"
        "ทุกสิ่งทุกอย่างที่ผสมให้เป็นตัวเราในวันนี้ทำให้เรามีแนวคิดที่เปลี่ยนไปในทุกๆวัน"
        "ถึงจะเป็นแบบนั้นการที่เราพยายามทำดีที่สุดเพื่อไม่ให้เสียใจภายหลัง"
        "นั่นก็เป็น"
        "วิธีที่ดีที่สุดแล้วจริงๆ"
        "ยังไงก็ขอบคุณที่เดินทางกันมาด้วยกันถึงตอนนี้"
        "หวังว่ายังจะมีโอกาส"
        "ที่จะได้เจอกับทุกคนอีกนะครับ"
        scene black
        with fade
        stop music fadeout 3.0
        centered "FIN"
        return


    label brownend:
        stop music fadeout 1.0
        play music "audio/Cage.ogg" volume 0.8
        scene black
        with fade
        "จบแล้วงั้นหรอ"
        "เรื่องทั้งหมดก็เป็นแบบนี้สินะ"
        "เพราะอะไรถึงได้กลับมานะ"
        "เพราะอยากจะช่วยคนอื่นๆงั้นหรอ"
        "ตัวเราเองก็ดูเหมือนเป็นคนเห็นแก่ตัวเลยไม่ใช่หรอ"
        "ทั้งๆที่เหตุผลของเราจริงๆแล้วมันก็แค่การอยากจะใช้ชีวิต"
        "อยากใช้ชีวิตให้เหมือนปกติโดยที่ไม่ต้องไปยุ่งกับเรื่องบ้าๆ"
        "พบเจอพลังบ้าๆแบบนี้"
        "เลยพยายามเข้าสังคม"
        "เข้าหาทุกคน"
        "ไล่ตามความฝันตัวเอง"
        "และติดในวังวน"
        "ที่ผ่านมาเราก็ทำเพื่อตัวเองเท่านั้น"
        "ทำทุกอย่างด้วยตัวเอง"
        "ไม่คิดที่จะพึ่งพาใครหรือช่วยเหลือใคร"
        "แต่ก็เพราะแบบนี้ละนะ ก็เลยพอเข้าใจอะไรมาได้บ้าง"
        "การทำเพื่อคนอื่นนี่..."
        centered "ไม่เลวเหมือนกันนะ"
        stop music fadeout 3.0
        centered "END"
        return

# This ends the game.
