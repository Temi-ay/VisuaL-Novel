define Andre = Character("Andre", color="#040404") 
define Caleb = Character("Caleb", color="#DE8F2D") 


## Point these at your real files inside game/images/
image bg room = im.Scale("images/Luxury penthouse living room file_0000000082d081f4a4ed676ca900e914.png", 1920, 1080)
image bg hallway = im.Scale("images/Rooftop terrace at sunset file_000000009ef081f4b16d4e23d281860f.png", 1920, 1080)
image bg forest = im.Scale("images/ForestAndCabinPack_1080p_PNG/fnc_slope_night1.png", 1920, 1080)
image bg conference_room = im.Scale("images/After_Hours_Office/images/meeting_day.png", 1920, 1080)
image bg dark = im.Scale("images/Screenshot 2026-10-05 220812.png", 1920, 1080)

image caleb neutral ="images/Main Character/02_Casual/casual_neutral.png"
image caleb concerned = "images/Main Character/02_Casual/casual_confused.png"
image caleb annoyed = "images/Main Character/02_Casual/casual_annoyed.png"
image caleb shocked = "images/Main Character/02_Casual/casual_shocked.png"
image caleb angry = "images/Main Character/02_Casual/casual_angry.png"
image caleb sad = "images/Main Character/02_Casual/casual_sad.png"

image andre neutral = "images/Main Lead/02_Casual/casual_neutral.png"
image andre concerned = "images/Main Lead/02_Casual/casual_confused.png"
image andre annoyed = "images/Main Lead/02_Casual/casual_annoyed.png"
image andre sad = "images/Main Lead/02_Casual/casual_sad.png"
image andre shocked = "images/Main Lead/02_Casual/casual_shocked.png"
image andre angry = "images/Main Lead/02_Casual/casual_angry.png"




transform sprite_left:
    zoom 0.7
    xalign 0.15
    yalign 1.0

transform sprite_right:
    zoom 0.7
    xalign 0.85
    yalign 1.0

default pressed_andre = False

label start:
    scene bg conference_room with fade

    narrator "The first time Caleb Harrison saw Andre Sinclair in eight years, he almost walked out of the room."
    narrator "Almost."

    show caleb neutral at sprite_left with dissolve

    narrator "Instead, he stayed. Standing beside the enormous table."

    show andre neutral at sprite_right with dissolve  

    narrator "Andre looked exactly like the caleb he used to know. who hehas trid to forget for years"
    narrator "But Older. Stronger. More confident. And more dangerous than ever."
    narrator "Andre looked composed and refined far from when they were kids, Andre's eyes met Caleb's."

    scene bg forest with dissolve
    hide caleb
    hide andre

    narrator "And for a moment, it was like they were back eight years ago."
    narrator "Back when they were fifteen, running through the woods behind the estate."

    narrator "{i}Catch me if you can, Caleb!{/i}"
    

    scene bg conference_room with dissolve
    show caleb neutral at sprite_left
    show andre neutral at sprite_right 

    narrator "But that is far from the present. Caleb looked away."

    Andre "You are late."

    narrator "Andre's voice hasn't changed much but more Cold, commanding, and unyielding."

    Caleb "I wasn't aware you were tracking me."
    Andre "i'm not."
    Caleb "Good."

    narrator "The tension in the room was suffocating. Their fathers has arranged this meeting, then left the two of them alone with it."
    narrator "The chairs were set across each other."
    narrator "Caleb and Andre sat down, their eyes locked in a silent battle of wills."

    narrator "On the table lay a folder with a single line:"
    narrator "{i}CONSOLIDATION AGREEMENT{/i}"

    show caleb annoyed at sprite_left
    Caleb "This has to be a joke."
    Caleb "After years of rivalry, our fathers have decided to merge our companies into one?"

    narrator "Andre jaw tightened. He hadn't known either."

    Caleb "Why would either family agree to this?"
    Andre "Because the alternative is losing both companies. That's what my father's note said."

    narrator "Caleb looked at the empty chair at the head of the table, where his father should have been."
    narrator "That was when Caleb knew. Something was wrong. Very wrong."

    narrator "Beside the folder sat a small black box, with a note in Alexander Laurent's hand: {i}It's time you both learned the truth.{/i}"


    narrator "Andre stared at the box. His face went pale."
    narrator "Caleb noticed."

    Caleb "You know what that is."

    narrator "Andre didn't answer."

    ## --- First choice ---
    menu:
        "Press him":
            $ pressed_andre = True
            Caleb "Andre."
            narrator "Nothing."
            narrator "Caleb felt something twist painfully in his chest. He hadn't called him by that name in years."

        "Say nothing and watch":
            narrator "Caleb said nothing. He watched the color drain from Andre's face, and a question settled heavily in his chest."
            narrator "Why was Andre afraid?"

    narrator "Caleb opened the box."

    narrator "Inside was an old photograph. Two boys stood beside a lake. One was Caleb. The other was Andre."
    narrator "They were smiling."
    narrator "On the back were six handwritten words:"
    narrator "{i}When they discover this, tell them everything.{/i}"

    show caleb shocked at sprite_left

    narrator "Caleb stared at the handwriting. He recognized it immediately."
    narrator "His grandfather's."
    narrator "His heart began beating faster."

    Caleb "What does this mean?"

    narrator "Nobody answered."

    Andre "Your grandfather didn't die because of an accident."

    narrator "Caleb froze."
    narrator "Andre looked directly at him."

    Andre "He was murdered."

    narrator "And suddenly, the hatred Caleb had carried for eight years wasn't nearly as simple as it had been yesterday."

    jump chapter_2


label chapter_2:
    scene bg conference_room with fade
    show caleb shocked at sprite_left
    show andre concerned at sprite_right
    Caleb "What do you mean he was murdered?"

    show andre neutral at sprite_right
    narrator "Andre looked at the folder, looking away from Caleb. He wasn't sure what to say."

    show caleb angry at sprite_left

    menu:
        "Lash out":

            Caleb "Look at me Andre."
            Caleb "Is all you know how to do run away? You are such a coward."

            show caleb sad at sprite_left
            Caleb "....."
            Caleb "Just like back then. You always were."

            show andre sad at sprite_right
            show caleb neutral at sprite_left

            narrator "Andre looked hurt and Caleb was once again in a position where those he loves hide things from him and he is left in the dark."
            narrator "He was angry and hurt. He wanted to know the truth. He wanted to know why his grandfather was murdered."

            show andre neutral at sprite_right

            Andre "You still have the habit of ignoring others' feelings. Not everything has to go your way."

            show caleb angry at sprite_left

            narrator "Andre stands up to leave but Caleb stops him, grabbing him by the arm."

            Caleb "Where do you think you are going? You are not leaving until you tell me the truth."

            show andre angry at sprite_right

            Andre "You think I have all the answers?"

        "Stay calm":

            show caleb neutral at sprite_left

            Caleb "Andre. Look at me."
            narrator "Caleb let out a slow breath. Shouting had never once gotten Andre to talk."
            Caleb "Please. I'm not trying to fight you. I just need to understand."

            show andre sad at sprite_right

            narrator "Andre's shoulders dropped, just slightly."

            Andre "...I need some air."

            narrator "Andre stood to leave. Caleb caught him gently by the sleeve."

            Caleb "Don't walk away from this too."

            show andre concerned at sprite_right

            narrator "Andre stopped."

            Andre "I don't have all the answers, Caleb."

    Caleb "You knew about the box."

    Andre "I knew it existed."

    Caleb "That's not what I asked."

    narrator "Andre's expression hardened."

    Andre "I was told never to open it."

    Caleb "By who?"

    narrator "Andre remained silent."

    Caleb "Your father?"

    Andre "..."

    Caleb "Of course."

    narrator "Caleb stepped closer."

    Caleb "For eight years, I thought your family was responsible."

    Andre "Responsible for what?"

    show caleb shocked at sprite_left

    narrator "The question stopped Caleb."

    Caleb "You know exactly what I'm talking about."

    Andre "No. I don't."

    narrator "For the first time, Andre looked genuinely confused."

    Andre "What happened that night?"

    narrator "Caleb stared at him."

    narrator "Andre wasn't pretending."

    Caleb "You... don't remember?"

    Andre "Remember what?"

    narrator "Caleb's anger began to fade, replaced by something far more unsettling."

    narrator "Maybe Andre hadn't known."

    narrator "Maybe the story Caleb had been told for eight years wasn't the whole story."

    show caleb neutral at sprite_left

    Caleb "The night my grandfather died."

    Andre "I wasn't there."

    Caleb "You were."

    Andre "No."

    Caleb "I saw you."

    Andre "Caleb, I was fifteen."

    narrator "Silence filled the room."

    Andre "So were you."

    narrator "Caleb looked away."

    narrator "He remembered the woods. The lake. Andre running ahead of him."

    narrator "Then the shouting."

    narrator "Then nothing."

    show andre concerned at sprite_right

    Andre "What do you remember?"

    Caleb "I don't know."

    Andre "Then stop blaming me for something neither of us remembers."

    narrator "Caleb looked back at him."

    narrator "For the first time in eight years, they weren't enemies."

    narrator "They were two people who had been given different pieces of the same story."

    show caleb neutral at sprite_left

    Caleb "Then we find out what really happened."

    Andre "Together?"

    menu:
        "Admit you need him":
            Caleb "...Yes. Together."
            Caleb "I can't do this alone. And I think you can't either."

            show andre neutral at sprite_right

            Andre "Was that so hard to say?"

            Caleb "Don't push it."

        "Keep your guard up":
            Caleb "Don't make it sound like I want to."

            Andre "You don't."

            Caleb "Good."

    narrator "Andre almost smiled."

    narrator "Almost."

    narrator "Then the lights went out."

    scene bg dark with Dissolve(0.3)
    pause 1.0

    scene bg conference_room with fade

    narrator "The room fell completely silent."

    narrator "A second later, something clicked."

    show caleb shocked at sprite_left

    Caleb "What was that?"

    show andre concerned at sprite_right

    Andre "The box."

    narrator "A small red light appeared beneath it."

    narrator "Then a recording began to play."

    narrator "{i}If you're hearing this, then both families have finally brought you together.{/i}"

    narrator "Caleb froze."

    narrator "{i}There are things you were never supposed to know.{/i}"

    narrator "{i}And there are people who will do anything to keep them buried.{/i}"

    narrator "The recording stopped."

    narrator "Caleb and Andre stared at each other."

    Caleb "Who recorded that?"

    Andre "I don't know."

    narrator "A second click came from inside the box."

    narrator "A second compartment opened."

    show caleb shocked at sprite_left

    narrator "Inside was a key."

    narrator "And beneath it, a single photograph."

    narrator "It was their Grandfather's picture from when they were young and there was someone else, someone neither of them seem to recognise"
    
    return
  