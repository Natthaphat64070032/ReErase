# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("เทส")


# The game starts here.

label start:

    play music "audio/Ideal and the Real.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show test normal
    with dissolve
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    mc "สมัยผมเรียนมัธยมในช่วงหนึ่งผมได้มีเพื่อนร่วมชั้นผู้หญิงคนหนึ่ง"

    mc "เรามีความทรงจำร่วมกันหลายๆอย่าง ชีวิตโดยรวมอยู่ในขั้นปกติ เธอกับผมนั้นหลังจบแล้วก็ยังคงเป็นเพื่อนที่ดีต่อกัน"

    scene bg tower
    with fade

    mc "จนกระทั่งวันหนึ่ง เกิดเหตุการณ์ผู้ร้ายก่อเหตุคดีอุกฉกรรจ์ในเขตพักอาศัย มีผู้เคราะห์ราย 3 ราย 1 ในนั้นคือเพื่อนสนิทผม ส่วนอีก 2 ราย คือพ่อและแม่ของเธอ พ่อและแม่ของเธอเสียชีวิตในเหตุการณ์เธอคนเป็นคนเดียวที่รอดมาได้"

    # This ends the game.

    return
