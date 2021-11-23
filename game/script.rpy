﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("???")
define m = Character(_("ทาคุโตะ ยูกิ"), color="#2760c9")
define girl1 = Character(_("โซโนซากิ มินะ"), color="#38c72b")

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
    stop music
    scene black
    with fade
    "ผมควรจะทำอย่างไรดี"
    menu:
        "หวนคืนสู่จุดเริ่มต้น":
            jump start2
    label start2:
        play music "audio/FirstMemory.mp3"
        mc "นี้นายนะ"
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
        'ผมชื่อว่า"ทาคุโตะ ยูกิถ้า"ให้พูดก็นักวิจัยธรรมดานี้แหละ'
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
                jump story
            "ขอบคุณมากนะที่ยังได้มาเจอกัน":
                jump story
    label story:
        scene classroom
        show satonaka at right
        with dissolve
        girl1 "นายนี้ละก็นะ"
        girl1 "เตรียมตัวได้แล้วนะคาบแรกจะเริ่มแล้ว"
        hide satonaka at right
        with dissolve
        "โดยรวมแล้วพลังที่ผมพูดถึงคือนี้แหละครับ"
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
        girl1 "เดี๋ยวสินี้นายพึ่งเปิดเรียนวันแรกเองนะ"
        hide mc almostcry at right
        with dissolve
        girl1 "เป็นอะไรของเขากันนะวันนี้"
        scene bg old room
        show mc shirt sad
        with dissolve
        "ห้องของเรายังโล่งอยู่เลย"
        "นั้นสินะ ตอนปี 1 เราพึ่งย้ายมาเรียนในเมืองนี้ ของอะไรเลยแทบไม่มีเลย"
        "ตอนนั้นคิดว่าชีวิตคงจะสดใสได้เจอเพื่อนใหม่ๆ แต่ยัยนั่นดันสอบติดแล้วเข้ามาได้ในโรงเรียนเดียวกันอีก"
        "จริงๆไม่ได้เกลียดหรอกนะ แต่การได้เห็นเธอทุกวันมันเป็นการย้ำเตือนตัวผมเองมากกว่า"
        "ว่าจริงๆแล้วผมช่วยเธอไม่ได้"
            


    label end:
        scene sky
        with dissolve
        "FIN"
    # This ends the game.

    return
