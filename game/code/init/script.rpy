# Гра починається тут.

label start:
    $ right2 = Position(xalign=0.8, yalign=1.1)
    $ left2 = Position(xalign=0.2, yalign=1.1)
    scene сон with dissolve

    #$ renpy.notify('Gained achievement: "О дивний новий світ..."')


    play music "audio/Сцена 1/ТемаСну.mp3" fadeout 1
    play sound "audio/Сцена 1/Ємбіент.mp3"


#    menu:
#        "Сцена 2":
#            jump scene_two
#        "Сцена 3":
#            jump scene_three
#        "Сцена 4":
#            jump scene_four
#        "Сцена 5":
    #        jump scene_five
    #    "Сцена 6":
    #        jump scene_six
    #    "Сцена 7":
    #        jump scene_seven
    #    "Сцена 8":
    #        jump scene_eight
        #"Сцена 9":
    #        jump scene_nine
    #    "Сцена 10":
    #        jump scene_ten
    #    "Сцена 11":
    #        jump scene_eleven
    #    "Сцена 12":
    #        jump scene_twelve
    #    "Сцена 13":
    #        jump scene_thirteen
    #    "Сцена 14":
    #        jump scene_final
    #    "Грати далі":
    #        "..."

    "{i}Тут так світло і спокійно, що хочеться співати."

    "{i}Навколо так багато зеленого кольору."

    "{i}Прохолодний, прозорий подих вітру — і ось зелені ромби на шкірястих, шорстких стовпах тремтять."

    "{i}Жовті кола біля ніг нахилилися під силою повітря."

    "{i}Щось мені підказує, що все довкола — живе. Хоч то й не люди."

    "{i}Витягуються, повзуть вгору тонкі нитки живої зелені."

    "{i}Як все це дивно. Здається, ще трохи — і я почую кришталевий передзвін їхніх голосів."

    play sound "audio/Сцена 1/Сміх1.mp3"
    play sound "audio/Сцена 1/Ємбіент.mp3"
    голос1 "Павка! Давай з нами!"

    "{i}Я не впізнаю голос, але знаю, що це кличе мене друг."

    павка "Я зараз, тільки…"

    "{i}Вітерець торкається щік і запускає у волосся свої незримі прохолодні нитки. Так приємно…"

    "{i}Все навколо ніжиться у вітрі."

    play sound "audio/Сцена 1/Сміх2.mp3"

    голос2 "Павко, хутчіш сюди! Бо почнемо без тебе!"

    "{i}Цей чудовий чарівний звук."

    menu:
        "Прислухатись":

            stop music fadeout 1
            play music "audio/Сцена 1/Флейта.mp3" fadeout 2

            "{i}Дівчата і хлопці в кольоровому просторому одязі сидять на лавці і співають."

    "..."

    "{i}Схоже, ці приємні звуки створює один з хлопців."

    "{i}Музика народжується в нього під пальцями, коли він прикладає їх до отворів на довгастому предметі."

    голос1 "{i}{b}Над синім морем"

    голос1 "{i}{b}Моря зелені"

    play sound "audio/Сцена 1/Сміх1.mp3" fadeout 3
    голос2 "Приєднуйся, Павко! Чи ти забула пісню, яку сама придумала?"

    голос1 "{i}{b}А там понад світом — стоока безодня"

    "{i}Ой, що це там, вдалині? Витягуються з землі до самого неба, такі високі…"

    scene гори with dissolve

    '{i}Звідкись приходить слово "гори".'

    голос1 "{i}{b}Світи нескінченні"

    голос1 "{i}{b}Моря прозорі"

    "{i}А над горами — безкрайній біло-рожевий простір."

    "{i}Я вдома – на волі. Так і має бути."

    scene фон with dissolve
    stop music fadeout 2
    "..."

    stop sound fadeout 3
    jump scene_two
