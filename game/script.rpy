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

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    mc "คุณได้สร้างเกมจาก Ren'py."

    mc "เมื่อคุณเพิ่อมเรื่องราว ตัวละคร เพลง คุณสามารถปล่อยมันสู่ชาวโลกได้!"

    mc ""

    # This ends the game.

    return
