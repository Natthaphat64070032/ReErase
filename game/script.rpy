﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("???")
define m = Character(_("ทาคุโตะ ยูกิ"), color="#2760c9")
define girl1 = Character(_("โซโนซากิ มินะ"), color="#38c72b")
define male1 = Character(_("คิตากาวะ จุนอิจิ"), color="#da9e1d")

default friendshipg1 = 0
default friendshipm1 = 0
default allfriend = friendshipg1 + friendshipm1
# The game starts here.

label start:

    play music "audio/Ideal and the Real.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    mc "เรื่องทีเกิดขึ้นหลังจากนี้เป็นเรื่องที่ผ่านมาหลายปีแล้ว"
    mc "ถ้าจะให้พูดคือมันไม่มีผลอะไรกับปัจจุบันที่ผมใช้ชีวิตอยู่แล้ว"
    mc "แต่มันเป็นสิ่งที่ค้างคาในใจผมมาตลอด"
    mc "สมัยผมเรียนมัธยมในช่วงหนึ่งผมได้มีเพื่อนร่วมชั้นผู้หญิงคนหนึ่ง"
    mc "เรามีความทรงจำร่วมกันหลายๆอย่าง ชีวิตโดยรวมอยู่ในขั้นปกติ เธอกับผมนั้นหลังจบแล้วก็ยังคงเป็นเพื่อนที่ดีต่อกัน"
    mc "จนกระทั่งวันหนึ่ง"
    mc "เกิดเหตุการณ์ผู้ร้ายก่อเหตุคดีอุกฉกรรจ์ในเขตพักอาศัย มีผู้เคราะห์ราย 3 ราย หนึ่งในนั้นคือเพื่อนสนิทผม.."
    mc "ส่วนอีก 2 ราย คือพ่อและแม่ของเธอ"
    mc "พ่อและแม่ของเธอเสียชีวิตในเหตุการณ์เธอคนเป็นคนเดียวที่รอดมาได้..."
    stop music
    scene black
    with fade
    mc "แต่… "
    mc "เธอไม่เหมือนเดิมอีกแล้ว"
    play music "audio/Alleycat.mp3"
    mc "จากเหตุการณ์นั้นเธอได้เป็นผู้เห็นเหตุการณ์ทั้งหมด เธอกลายเป็นคนจิตไม่สมประกอบ ไม่สามารถใช้ชีวิต หรือจดจำอะไรได้"
    mc "เธอเป็นผู้เคราะห์ร้ายจากเหตุการณ์ที่เหล่าโจรพวกนั้นได้ปล้นชีวิตครอบครัว และรวมถึงอนาคตของเธอ"
    mc "หลังจากนั้นผมจึงไปเยี่ยมเธอที่โรงพยาบาลเป็นประจำ..."

    #ห้องวิจัย
    scene bg lab
    with fade
    show mc sad at right
    with dissolve
    
    mc "งานที่ผมทำนั้นเป็นงานวิจัยเกี่ยวกับรักษาผู้ป่วยทางจิต ซึ่งเป็นสิ่งที่ผมตั้งใจทำมาตลอดหลังจากเกิดเหตุการณ์นั้นขึ้น"

    mc "แต่ในขณะเดียวกันมันส่งผลต่อผู้ร่วมลงทุน เพราะมันอาจขัดต่อผลประโยชน์พวกเขาได้"

    mc "เนื่องจากงานวิจัยชิ้นนี้เป็นการฟื้นฟู ความคิด ความทรงจำ ของผู้ได้รับบาดแผลทางจิตใจ ซึ่งผมคิดว่าคงไปขัดผลประโยชน์ใครบางคน งานวิจัยของผมจึงถูกตัดงบประมาณจากเจ้าของทุน"

    mc "หลังจากเรียนจบมาเป็นนักวิจัย ผ่านเหตุการณ์ที่ทำให้เหมือนเสียเพื่อนคนสำคัญ หมกมุ่นอยู่กับงานวิจัยที่ไปไม่ถึงเป้าหมาย โดนตัดงบประมาณ จนตอนนี้เป็นเหมือนคนตกงาน"

    mc "ผมได้แต่รับงานเล็กๆเพื่อหารายได้มาประทังชีวิตไปวันๆ เป็นเพราะผมยังพยายามไม่พอรึเปล่าถึงไม่สามารถช่วยคนรอบข้างได้เลย การไม่สามารถก้าวต่อไปได้ ทำให้จมปลักอยู่กับที่จนเป็นคนไร้จุดหมายเป็นเดือนๆ..."
    scene black
    with fade
    mc "แต่แล้วในวันหนึ่ง ผมได้รับพลังบางอย่าง พลังที่สามารถเปลี่ยนความจริง แก้ไขทั้งอดีตและปัจจุบันให้เป็นอย่างที่คิดได้ ผมได้ใช้พลังนั้นเพื่อช่วยเธอให้กลับมาใช้ชีวิตได้อีกครั้ง แต่ผลของมันคือทำให้เธอจำผมไม่ได้"

    mc "เพราะการเปลี่ยนแปลงอดีตเพื่อให้เธอรอดนั้น"
    mc " -คือการที่เธอต้องไม่เจอผม "
    mc "เหตุการณ์นั้นก็จะไม่เกิดขึ้น แต่นั่นก็เกินพอแล้วขอแค่เธอมีชีวิตรอดก็พอ"

    mc "พลังที่ได้มานี้ถ้าคิดจะใช้มันเพื่อที่จะได้ไม่มีผู้เคราะห์ร้ายอีก มันจะถูกรึเปล่า?"
    scene bg city
    with dissolve
    mc "หากผมช่วยทุกคนเพื่อให้โลกนี้มีแต่ความสุขโดยให้สิ่งที่ทุกคนต้องการ"
    mc "ผมจะกลายเป็นผู้ทำลายความตั้งใจของคนพยายามอย่างหนักเพื่อได้ใช้ชีวิตในแบบที่ต้องการไหม?"
    mc "ถ้าเกิดคนที่ผมช่วยให้ไม่เจอเคราะห์ร้ายกลายเป็นคนไม่ดีขึ้นมาล่ะ"
    mc "ผมรู้ว่าการที่ทุกคนเติบโตขึ้นได้นั้น ย่อมมีทั้งความสุขใจและความเจ็บปวด ถึงผมจะไม่อยากให้ใครต้องเจ็บปวดเป็นผู้เคราะห์ร้ายอีก.."
    mc "แต่นั้นคือสิ่งที่ทุกคนต้องการรึเปล่าผมนั้นไม่สามารถรู้ได้ ตัวผมนั้นได้แต่คิดทบทวนว่าผมควรใช้พลังเพื่ออะไรกันแน่"
    mc "อะไรคือสิ่งที่ถูกต้อง"
    mc "อะไรคือนิยามของความถูกผิด"
    mc "หรือผมควรใช้ชีวิตเดินหน้าต่อไปในแบบที่ควรจะทำ"
    stop music fadeout 1.0
    scene black
    with fade
    "ผมควรจะทำอย่างไรดี"
    menu:
        "หวนคืนสู่จุดเริ่มต้น":
            jump start2
    label start2:
        play music "audio/FirstMemory.mp3"
        mc "นี่นายนะ"
        mc "นั้นไม่ใช่ที่นั่งนายนะ ที่นั้งเรียงตามเลขที่บนกระดานแล้วนะ"
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
        'ผมชื่อว่า"ทาคุโตะ ยูกิ"ถ้าให้พูดก็นักวิจัยธรรมดานี่แหละ'
        "แต่ตอนนี้เป็นนักเรียนมัธยมปลาย ที่่อยู่ตรงหน้าผมก็เพื่อนของผมเอง"
        "เวลามันเวียนกลับมาอีกแล้วสินะ"
        show mc almostcry at left
        with dissolve
        m "ขอโทษนะ พอดีเหม่อไปหน่อย ไม่ค่อยอยากจะมาเรียนเท่าไหร่เลย"
        m "แต่ดีใจมากเลยนะได้เจอเธออีก"
        show satonaka at right
        with dissolve
        girl1 "พูดอะไรของนายเนี่ยก็อยู่ด้วยกันมาตลอดไม่ใช่รึไง หัวกระแทกพื้นมาสิหรือเล่นเกมจนดึก"
        menu :
            "เราควรตอบว่าอะไร"
            "แค่คิดไปเรื่อยนะขอโทษด้วย":
                $ friendshipg1 += 1
                jump story
            "ขอบคุณมากนะที่ยังได้มาเจอกัน":
                $ friendshipg1 += 2
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
        "ผมติดอยู่ในวังวงบ้าบอนี้มาซักพักใหญ่ๆแล้วครับ จะพูดว่าผมเป็นเด็กมัธยมก็คงไม่ได้แล้ว"
        "ผมนั้นช่วยใครไว้ไม่ได้เลย"
        "ถึงจะมีพลังที่สุดวิเศษขนาดนี้สำหรับใครหลายๆคนแต่สำหรับผมแล้วมันทำให้ผมลำบากใจ"
        "ผมกลับรู้สึกถึงความรับผิดชอบที่ทุกครั้งเวลาผมต้องการแก้อะไรสักอย่างให้ดีขึ้นแล้วมัน..."
        "กลับแย่กว่าเดิมทุกครั้ง"
        show mc almostcry at left
        with dissolve
        m "วันนี้ผมขอตัวกลับบ้านก่อนนะรู้สึกไม่สบายเลย"
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
        "นั้นสินะ ตอนปี 1 เราพึ่งย้ายมาเรียนในเมืองนี่ ของอะไรเลยแทบไม่มีเลย"
        "ตอนนั้นคิดว่าชีวิตคงจะสดใสได้เจอเพื่อนใหม่ๆ แต่ยัยนั่นดันสอบติดแล้วเข้ามาได้ในโรงเรียนเดียวกันอีก"
        "จริงๆไม่ได้เกลียดหรอกนะ แต่การได้เห็นเธอทุกวันมันเป็นการย้ำเตือนตัวผมเองมากกว่า"
        "ว่าจริงๆแล้วผมช่วยเธอไม่ได้"
        stop music fadeout 1.0
        play sound "audio/knocking.mp3"
        mc "นี่! ยูกิอยู่รึเปล่า?"
        hide mc shirt sad at right
        show mc curious at right
        "มินะ? มาทำไมกัน"
        girl1 "ไหนบอกว่าไม่สบายไง ก็เลยวันนี้ลาเรียนแล้วซื้อของมาฝาก"
        play music "audio/out of mere play.mp3"
        "ยัยนั้นยุ่งไม่เข้าเรื่องอีกแล้ว"
        menu :
            "ทำอะไรดี"
            "เดินไปเปิดประตู":
                $ friendshipg1 += 1
                jump story21
            "ปล่อยเฉยๆ":
                jump story22
    
    label story21:
        hide mc shirt red at right
        show satonaka smile at right
        with dissolve
        girl1 "โห ห้องโล่งชะมัดเลยนะ ต่างจากห้องฉันคนละขั้วเลย"
        girl1 "เอานี้อาหารแวะไปซื้อมาให้ ถึงจะเล็กน้อยแต่ถ้าไม่สบายจะปล่อยให้ท้องว่างไม่ได้นะ"
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
        m "นี้เธอทำอะไรเนี่ยยยยยยยยยยย"
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
        girl1 "เพราะงั้นฉันที้่เป็นเพื่อนนายมาตั้งนาน ดูออกอยู่แล้ว จู่ๆคนอย่างนายจะออกจากโรงเรียนมาเฉยๆโดยไม่คิดอะไร"
        girl1 "ไม่ค่อยเหมือนนายที่ฉันรู้จักเลยนะ"
        stop music fadeout 1.0
        play music "audio/Recollections.mp3"
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
        "นั้นสินะ"
        "มินะพูดถูกแล้ว"
        "ถ้าหากเรายังคงทำตัวไม่ได้เรื่องแบบนี้สุดท้ายก็จะไม่เกิดประโยชน์กับใครเลย"
        hide satonaka smile
        show satonaka sad at right
        with dissolve
        girl1 "อ่ะ นี้อยู่กับนายจนเย็นขนาดนี้แล้วหรอ"
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
        play music "audio/New Days.mp3"
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
                jump choice1_2

        label choice1_1:
            girl1 "พักผ่อนบ้างก็ดีนะนายนะ"
            girl1 "แล้วนี่ถ้าฉันจำไม่ผิดหมอนั้นก็สอบเข้ามาได้ด้วยนะ"
            m "หมอนั้น?"
            girl1 "เจ้าคิตากาวะไง ที่นายไม่ค่อยถูกโฉลกเท่าไหร่"
            m "เดี๋ยวนะไม่ใช่แค่เราสองคนหรอ"
            "ที่ผมย้อนรอบก่อนมันไม่ใช่แบบนี้ หมอนั้นไม่เคยอยู่ที่นี่"
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
            girl1 "ได้ยินกับเห็นใน SNS เพื่อนๆในห้องละดูถ้าจะโด่งดังในหมู่สาวๆใช้ได้เลย"
            "มันผิดปกติ"
            "ถ้าพูดให้ถูกก็คือทุกครั้งที่ผมย้อนมาหมอนั้นไม่เคยอยู่ที่นี่เลย"
            "มันเกิดอะไรขึ้นกันแน่"
            jump story2_1

    label story2_1:
        scene classroom
        with dissolve
        "หมอนั่นอยู่นี่งั้นหรอ เป็นไปได้ยังไงกัน"
        "ก็ทุกครั้งที่เราย้อนกลับมาไม่เคยมีหมอนั้นอยู่เลยนี่นา"
        show akechi smile at right
        with dissolve
        male1 "คิดถึงฉันอยู่งั้นหรอ หน้าเครียดมาเชียว"
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
            male1 "ได้ยินว่านายไม่สบายก็เลยไม่ได้มางั้นสินะ ใช่เลยผมนั่งข้างหลังนายนี่เองหลังจากนี้ 1 ปีก็ฝากตัวด้วยนะครับ"
            jump story2_2

        label choice2_2:
            male1 "เย็นชากับผมจังเลยนะครับ คิดว่าไหนๆก็เป็นเพื่อนร่วมห้องกันอีกก็ควรจะมาทักทายไว้ก่อน"
            hide akechi smile at right
            show akechi at right
            male1 "แต่ไม่แปลกใจหรอกนะครับ คุณทาคุโตะเป็นแบบนี้มาตั้งแต่สมัยก่อนแล้ว"
            "หมอนี้ยังเหมือนเดิมไม่เปลี่ยนเลย สดใส เข้ากันได้กับทุกคน"
            "จะว่าไปก็ควรจะตอบไปให้ดูไม่เปลี่ยนสินะ"
            show mc hood2 at left
            with dissolve
            m "นายก็ยังสดใสเหมือนเดิมเลย ไม่คิดว่าเพื่อนๆจะตกใจบ้างหรอ"
            m "แล้วก็อีกอย่างเดี๋ยวก็เริ่มเรียนแล้วไม่ไปห้องตัวเองหรอ"
            hide akechi smile at right
            show akechi smile at right
            male1 "ยังไม่รู้สินะครับ เพราะเมื่อวานคุณทาคุโตะไม่สบาย"
            male1 "ผมนั่งด้านหลังตรงนี้เองครับ หลังจากนี้ 1 ปีฝากตัวด้วยนะครับ"
            jump story2_2

    label story2_2:
        stop music fadeout 1.0
        scene black
        with fade
        centered "พักกลางวัน"
        play music "audio/Tsuiokunokakera.mp3"
        "หลังจากนี้การตัดสินใจการกระทำเราจะส่งผลแล้วสินะ"
        "เพราะที่ผ่านมาที่เราทำไป"
        "ก็เหมือนรอบที่ผ่านๆมา"
        "ครั้งนี้ต้องไม่เหมือนเดิม"
        "เราได้โอกาสแล้ว แถมครั้งนี้ยังมีเพื่อนอย่างจุนอิจิ"
        "การที่หมอนั้นได้มาโผล่ที่นี้ต้องไม่ใช่เรื่องบังเอิญอย่างแน่นอน"
        scene bg canteen
        with dissolve
        "คิดมากไปก็เท่านั้น จริงๆโรงเรียนนี้อาหารก็ยังอร่อยเหมือนเดิมเลย"
        if friendshipg1 >= 1 and friendshipm1 >= 1:
            jump story2_2best
            label story2_2best:
            girl1 "คิดจะแยกตัวคนเดียวอีกแล้วหรอนายนะ"
            male1 "ถ้าไม่รังเกียจผมขอนั่งด้วยคนนะครับ"
            show akechi smile at right
            with dissolve
            show satonaka warm smile2 at left
            with dissolve
            m "ทั้งสองคน..."
            m "ตามมาถึงนี้เลยงั้นหรอ จะว่าไปทั้งคู่ไปสนิทกันตอนไหนเนี่ย"
            hide akechi smile at right
            show akechi at right
            male1 "ก็เพราะคุณทาคุโตะนั้นแหละครับทำให้พวกผมเป็นห่วง"
            hide satonaka warm smile2 at left
            show satonaka2 at left
            girl1 "นายนะทำให้พวกเราเป็นห่วงนะ"
            girl1 "แค่มาเรียนวันแรกก็โดนเรียนหนีไปซะแล้ว"
            male1 "เพราะงั้นผมเลยคิดว่าถ้ามาดูแลคุณหน่อยน่าจะดีครับ"
            girl1 "นายทำตัวแปลกๆมาตั้งแต่เมื่อวานแล้วนะ"
            male1 "ผมเห็นด้วยกับที่คุณโซโนซากิพูดนะครับ คุณทาคุโตะดูไม่สดใสเหมือนเมื่อก่อนเลย"
            hide akechi at right
            show akechi smile at right
            male1 "หรือจะให้พูดคือรู้สึกเหมือนคนละคนเลยละครับ"
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
            jump story2_3

        elif friendshipm1 >= 1 and friendshipg1 == 0:
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
            male1 "งั้นเจอกันหลังเลิกเรียนครับ ผมมีคนอยากให้เจอด้วย คนที่คุณคิดนั้นแหละครับ"
            jump story2_3

        elif friendshipg1 >= 1 and friendshipm1 == 0:
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
            girl1 "อีกอย่างนายที่เคยรู้จักก็ไม่่ค่อยคิดมากอะไรแบบนี้ด้วย"
            girl1 "ออกจะดูเป็นคนเลื่อยลอยไม่ค่อยสนใจเรื่องข้างหน้าแล้วใช้ชีวิตไปเรื่อยๆ"
            girl1 "แต่นี้เหมือนนายคิดมากมาตั้งนานแล้ว"
            hide satonaka warm smile at right
            show satonaka at right
            girl1 "งั้นเรื่องนี้ไว้แค่นี้ก่อนทางนี้ข้าวหน้าเนื้อก็จะหายร้อนแล้วด้วย"
            play sound "audio/School Bell.wav"
            girl1 "อย่างที่คิดเลยงั้นหลังเลิกเรียนเจอกันนะ ก่อนนี้บอกหมอนั้นไว้แล้วละเพราะงั้นต้องมาด้วยละ"
            m "เอ๊ะ!?"
            m "ได้เลยแล้วเจอกันนะ ขอบคุณมากนะ"
            jump story2_3
    label story2_3:
        stop music fadeout 1.0
        scene black
        with fade
        centered "เลิกเรียน"
        
    label bad_end1:
        stop music fadeout 1.0
        play music "audio/Haru wa Yuku.mp3" volume 0.6
        scene black
        with fade
        "มันจบแล้ว"
        "เรื่องราวความเลวร้ายทั้งหมด"
        "มันจบลงแล้ว แต่สิ่งที่ต้องแลก"
        "มันก็เกินกว่าที่ตัวผมนั้นเองจะรับไหว"
        "มันหนักหนาเหลือเกิน"
        "ถ้าหากผมอยู่คนเดียวคงไม่ไหวแน่ๆ"
        "แต่อย่างน้อยในวันนี้เธอก็อยู่กับผม"
        "และคงจะ"
        "ไม่จากผมไปไหนอีกแล้ว"
        "ถึงผมจะไม่รู้ว่าที่ทำไปมันถูกรึเปล่า"
        "แต่แค่ได้อยู่กับเธอแบบนี้ตลอดไป"
        "ผมก็พร้อมที่จะใช้ชีวิตต่อแล้ว"
        stop music fadeout 3.0
        centered "END"
        
    label trueend:
        stop music fadeout 1.0
        play music "audio/Never More.mp3" volume 0.6
        scene sky
        with dissolve
        "เรื่องราวทั้งหมดผมไม่รู้ว่าควรเป็นแบบนี้รึเปล่า"
        "แต่ในทางที่ผมได้ตัดสินใจนั้น ผมมั่นใจว่าต้องถูก"
        "บางครั้งสิ่งที่เราทำมันอาจจะดูเป็นสิ่งที่ผิดในตอนตัดสินใจ แต่ว่าเราทุกคนไม่ได้มีโอกาสแก้อดีตกันทั้งนั้น"
        "เพราะงั้นการได้ลองทำอะไรให้เต็มที่คงจะดีที่สุดละนะ"
        "ขอบคุณทุกคนที่เล่นมาจนจบด้วยครับ หากมีโอกาศหน้า ยังคาดหวัง"
        "ที่จะได้เจอกับทุกคนอีกนะครับ"
        scene black
        with fade
        stop music fadeout 3.0
        centered "FIN"
        
    # This ends the game.

    return
