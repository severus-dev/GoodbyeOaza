label scene_five:
    $обіцянка_інкі = False

    play music "audio/Сцена 5/КопіяТемаМіста.mp3" fadeout 1
    scene автомат_годіум_стрічка with dissolve

    show інкі весела at right2 with dissolve
    show павка нейтральна at left2 with dissolve

    інкі "О! Наглядаючі тут вже побували"
    show інкі здивована at right2

    інкі "Ти була права — його обікрали"
    show інкі задумлива at right2

    інкі "Може в тебе дар передбачення?"

    show павка весела at left2
    павка "Не кажи дурниць, Інкі. Краще допоможи мені зняти ці стрічки"

    show павка задумлива at left2
    play sound "audio/Сцена 5/ЗвукЦелофановихСтрічок.mp3"

    scene автомат_годіум with dissolve

    "{i}Інкі не можна знати, що я допомагаю підпільній організації. Треба придумати, як мені ввести ті знаки в код програми і не спалитися"
    show інкі роздратована at right2 with dissolve
    інкі "Так, подивимося, що тут у нас…"

    play sound "audio/Сцена 5/ЗвукВідкриттяАвтомату.mp3"
    show інкі весела at right2
    show павка нейтральна at left2 with dissolve
    інкі "Як я і думала. Годіуму немає"

    інкі "…"
    show інкі роздратована at right2
    show павка здивована at left2
    інкі "Але це ще не все! Уявляєш, тут не тільки годіум поцупили, ще й викачали весь код"

    інкі "ВЕСЬ! КОД!!!11"
    show павка здивована at left2
    show інкі задумлива at right2
    "{i}Такого ще не було. Може, то справа рук організації, до якої належить Лайя?"

    show інкі здивована at right2
    show павка рішуча at left2
    павка "Оце хлопці дали жару…"

    show павка налякана at left2
    інкі "Що? Ти їх знаєш?"

    show павка розгублена at left2
    павка "Звісно ні... Але погодься — зробити той обсяг роботи в такий короткий час, це треба мати вражаючі здібності"

    show інкі задумлива at right2
    show павка нейтральна at left2
    інкі "І як наглядаючі могли упустити це? Просто не вкладається в голові"

    show інкі весела at right2
    show павка налякана at left2
    інкі "Треба викликати наглядаючих"

    павка "Тількі не це!"

    show інкі скептична at right2
    show павка розгублена at left2
    інкі "А-га! Злякалася, що всі дізнаються, що ти в нас Невживанка?"

    "{i}Йой, щось я розхвилювалася"

    "{i}Інкі не можна знати, що я допомагаю підпільній організації"

    павка "І не злякалася зовсім. Просто…"

    інкі "Просто що?"

    "{i}І справді, що?"

    menu:
        "Нав'яжуть бюрократію":
            show інкі скептична at right2
            show павка весела at left2
            павка "Просто не хочу гаяти свій час на посиденьки над їхньою бюрократією. Ну ти знаєш — в них купа документації. Ми знов всю обідню перерву в їхньому відділку просидимо"
        "Де наглядаючі — там і нещасні випадки":
            show інкі скептична at right2
            show павка рішуча at left2
            павка "Не хочу залучати сюди наглядаючих. Де наглядаючі — там завжди хто-небудь помирає або травмується"

    show інкі нейтральна at right2
    show павка нейтральна at left2
    if відносини_інкі < 2:
        інкі "Як скажеш. Мені пофіг, якщо чесно. Але якщо що — вся відповідальність на тобі."
    else:
        show інкі задумлива at right2
        інкі "Та та… Мабуть, і справді краще не треба…"


    show інкі нейтральна at right2
    show павка нейтральна at left2
    павка "Давай просто надішлемо їм повідомлення, як закінчимо тут і виїдемо в наступний сектор"

    інкі "Бо це ж ми в секторі А-91О, тут злочинність зашкалює"

    show інкі налякана at right2
    інкі "Якщо якийсь фрік знов до нас приїбеться, то мені тиждень бедтріпів гарантований"

    show інкі рішуча at right2
    інкі "Передай мені голографічну карту під номером 91-ОЩ. Я постараюся тут швиденько закінчити"

    menu:
        "{i}Зробити що вона каже":
                show інкі рішуча at right2
                show павка рішуча at left2

    play sound "audio/Сцена 5/ЗвукВідкриттяАвтоматуГарний.mp3"

    "Так, коли мова йде про трансконектори, Інкі не має рівних"

    "Технік другої ступіні у ї 21 — це вам не хухри мухри!"

    show павка нейтральна at left2
    інкі "А знаєш, Павко, я вчора читала в новинах, що сектор А104-Р тепер перший в антирейтингу по самогубствах"

    show павка сумна at left2
    павка "М-хм. Ми ж тамтешній трансконектор минулого тижня три рази ремонтували!"

    інкі "Отож-бо й воно… І то тільки в нашу зміну. Які там хакери — там ніхто не париться. В людей агресія зашкалює, ось вони й крушать все, що бачать"

    show павка задумлива at left2
    павка "Здається, туди зменшили постачання годіуму? На три чи чотири кредити?"

    інкі "Ну то й що? Вони можуть більше працювати, щоб потрапити в кращі райони…"

    інкі "Я ж змогла якось видертися звідти… Через нестачу годіуму в мене був важкий стан, але я наполегливо працювала і тому тепер живу в самій Оазі"

    show павка рішуча at left2
    павка "Не у всіх є ті можливості, що були в тебе. В когось є малі діти або хворі в сім'ї — вони не працюють. А їсти всі хочуть"

    павка "Хто має більше часу та сил, той розвиває свою кар'єру. А хто ні — той вішається на колготках або з даху стрибає"

    інкі "Так, але в мене…"

    show інкі весела at right2
    інкі "Забудь"

    інкі "Я просто найкраща!"

    show інкі рішуча at right2
    інкі "Так, а тепер не заважай мені — маю ввести код"

    define робі = Character("???")

    show павка налякана at left2
    show робі злий at center with dissolve
    робі "Гей ти, де мій годіум, жінко?"

    show робі роздратований at center
    "{i}О мій бог"

    "{i}Кого я бачу"

    "{i}Як же він жахливо виглядає"

    show павка рішуча at left2
    define робі = Character("Робі")

    інкі "Віджени того придурка. Він мені світло затуляє"

    show робі злий at center
    робі "Де мій годіум? Я тебе питаю, дурепо!"

    show робі роздратований at center
    павка "Пане, прохання відійти — ви заважаєте працювати ремонтній бригаді"

    show робі злий at center
    робі "Я заслужив свій базовий годіум! І я нікуди не піду з цього місця, поки його не отримаю!"

    show робі роздратований at center
    павка "Прошу вас, пане, відійдіть"

    show робі злий at center
    робі "Ти що, охрініла?"

    if відносини_інкі >=2:

        if годіум_інкі < 1:
            play sound "audio/Сцена 5/ЗвукПляшкиЯкуХоваютьНазад.mp3"
            show павка рішуча at left2
            show інкі роздратована at right2

            інкі "Та дай ти йому той годіум... Он у мене в машині ще доза є. Пожалій людину."
            show інкі рішуча at right2
            show павка сумна at left2
            "{i}Ти просто не знаєш, що це за людина, Інкі"

        if годіум_інкі = 1:

            show павка сумна at left2
            show інкі розгублена at right2
            інкі "Я б віддала йому свою дозу, але в мене зайвої не лишилося. Доведеться тобі щось вигадати"

            "{i}О, я вже знаю що мені робити!"


            show робі роздратований at center
            menu:
                "Застосувати електрошокер":
                    scene автомат_годіум at shaking
                    play sound "audio/Сцена 5/ЗвукЕлектрошокера.mp3"
                    show робі злий at center
                    show павка зла at left2
                    show інкі розгублена at right2
                    павка "Ось тобі, сволото"
                    scene автомат_годіум
                    робі "Ай, боляче! Не можна бути такою злою, дівчино!"

                    павка "Поговори мені ще"

                    show робі сумний at center
                    робі "Та добре, добре! Йду. Бачиш — я пішов"

                    show павка рішуча at left2
                    show інкі рішуча at right2
                    інкі "Не ображайтеся на мою подругу — в неї поганий ранок. За годину трансконектор працюватиме справно!"

                    show робі роздратований at center
                    робі "Поганий ранок, ага… Гадюка, така сама, як моя колишня…"

                    hide робі роздратований
                    інкі "Ну от. Він пішов, і наче навіть не вибісив мене. Чого не скажеш про тебе…"

                    павка "Пізніше розповім. Якщо настрій буде"
                    
                "Дати Робі годіум":
                    $обіцянка_інкі = True
                    $відносини_інкі = відносини_інкі+1
                    show павка нейтральна at left2
                    павка "Ось, тримай. За годину автомат буде в робочому стані"
                    show робі задоволений at center
                    робі "Молодець, жінко! Так тримати!"

                    інкі "Ну от. Він пішов, все обійшлося. Зробили добру справу — допомогли людині з ломкою"
                    hide робі злий


    if відносини_інкі < 2:
        show робі злий at center
        show павка рішуча at left2
        show інкі роздратована at right2

        інкі "Здихайся вже його. Я не можу в таких умовах працювати"
        show інкі рішуча at right2
        show павка розгублена at left2
        "{i}Якби це було так просто! Що ж мені робити?"

        if годіум_інкі < 1:
            menu:
                "Дати Робі годіум Інкі":
                    play sound "audio/Сцена 5/ЗвукПляшкиЯкуХоваютьНазад.mp3"
                    $відносини_інкі = відносини_інкі -1

                    show павка рішуча at left2
                    show інкі рішуча at right2
                    show робі злий at center
                    павка "Ось, тримай. За годину автомат буде в робочому стані"

                    show робі задоволений at center
                    робі "Молодець, жінко! Так тримати!"

                    hide робі задоволений with dissolve
                    show інкі роздратована at right2
                    інкі "Гей, ти що, віддала йому мою дозу? Геть здуріла??"

                    menu:
                        "Вибачитись":
                            show павка розгублена at left2
                            show інкі роздратована at right2
                            $відносини_інкі = відносини_інкі+1
                            $обіцянка_інкі = True
                            павка "Вибач, на мене щось найшло. Треба було швидко реагувати, і я зробила те, що перше прийшло в голову"

                            show павка весела at left2
                            павка "Не гнівайся на мене, гаразд? Після роботи пригощу тебе подвійним 36-м, і знову засяєш як сонечко, е?"

                            show інкі нейтральна at right2
                            інкі "Ну гаразд, тільки якщо подвійним. Ти сьогодні сама на себе не схожа"

                            show інкі весела at right2
                            інкі "Ну що ж, хоч зробили добру справу - допомогли людині з ломкою"

                        "Відрізати" :
                            show інкі роздратована at right2
                            show павка роздратована at left2
                            $відносини_інкі = відносини_інкі-1

                            павка "Заспокойся. Ти свою дозу сьогодні вже отримала. Не скупися на щастя для інших"

                            show інкі сумна at right2
                            інкі "Щось занадто багато охочих до мого щастя останнім часом"

                            show павка нейтральна at left2
                            інкі "Я такого від тебе не очікувала, кицюне"

                "Застосувати електрошокер":
                    scene автомат_годіум at shaking
                    show інкі рішуча at right2
                    show павка зла at left2
                    show робі наляканий at center

                    play sound "audio/Сцена 5/ЗвукЕлектрошокера.mp3"

                    павка "Ось тобі, сволото"
                    scene автомат_годіум
                    show інкі рішуча at right2
                    show павка зла at left2
                    show робі злий at center
                    робі "Ай, боляче! Не можна бути такою злою, дівчино!"

                    павка "Поговори мені ще"

                    show робі сумний at center

                    show павка рішуча at left2
                    робі "Та добре, добре! Йду. Бачиш — я пішов"
                    show інкі весела at right2
                    інкі "Не ображайтеся на мою подругу — в неї поганий ранок. За годину трансконектор працюватиме справно!"

                    show робі роздратований at center
                    робі "Поганий ранок, ага… Гадюка, така сама, як моя колишня…"
                    hide робі роздратований with dissolve

                    інкі "Ну от. Він пішов, і наче навіть не вибісив мене. Чого не скажеш про тебе…"

                    show павка нейтральна at left2
                    show інкі задумлива at right2
                    павка "Пізніше розповім. Якщо настрій буде"
                    show інкі скептична at right2
                    інкі "Тримай це при собі, люба. Мені на сьогодні вистачає проблем"

        #if годіум_інкі <= 1:
            #show інкі рішуча at right2
            #show павка зла at left2
            #show робі наляканий at center
#
            #play sound "audio/Сцена 5/ЗвукЕлектрошокера.mp3"
#
            #павка "Ось тобі, сволото"

            #робі "Ай, боляче! Не можна бути такою злою, дівчино!"

            #павка "Поговори мені ще"

            #show робі сумний at center

            #show павка рішуча at left2
            #робі "Та добре, добре! Йду. Бачиш — я пішов"
            #show інкі весела at right2
            #інкі "Не ображайтеся на мою подругу — в неї поганий ранок. За годину трансонектор працюватиме справно!"

            #show робі роздратований at center
            #робі "Поганий ранок, ага… Гадюка, така сама, як моя колишня…"
            #hide робі роздратований with dissolve

            #інкі "Ну от. Він пішов, і наче навіть не вибісив мене. Чого не скажеш про тебе…"

            #show павка нейтральна at left2
            #show інкі задумлива at right2
            #павка "Пізніше розповім. Якщо настрій буде"

            #show інкі скептична at right2
            #інкі "Тримай це при собі, люба. Мені на сьогодні вистачає проблем"


    show павка нейтральна at left2
    show інкі рішуча at right2
    інкі "Зовсім трошки залишилося. Почекай, я зараз свою частину закінчу — і ти зможеш приступити до діагностики"

    show павка задумлива at left2
    "{i}Блін, він мене навіть не впізнав"

    show павка сумна at left2
    "{i}Оце йому годіум мізки виніс. Але ж ми розлучилися тільки півроку тому!"

    "{i}І він так змінився. Схуд, зблід… В рекламі кажуть, що годіум не має поганих наслідків..."
    scene фон
    stop music fadeout 2
    "..."
    # ЗВУК ВИХОДУ З МАШИНИ
    jump scene_six
