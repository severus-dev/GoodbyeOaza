label scene_five:
    $обіцянка_інкі = False

    play music "audio/Сцена 5/КопіяТемаМіста.mp3" fadeout 1
    scene автомат_годіум_стрічка with dissolve
    show інкі весела at right2 with dissolve
    show павка нейтральна at left2 with dissolve
    інкі "О! Перевіряючі тут вже побували."

    show інкі здивована at right2 with dissolve
    інкі "Ти була права — його обікрали."

    show інкі задумлива at right2 with dissolve
    інкі "Може в тебе дар передбачення?"

    show павка весела at left2 with dissolve
    павка "Не кажи дурниць, Інкі. Краще допоможи мені зняти ці стрічки."

    show павка задумлива at left2 with dissolve
    play sound "audio/Сцена 5/ЗвукЦелофановихСтрічок.mp3"
    scene автомат_годіум with dissolve

    "{i}Інкі не повинна знати, що я допомагаю підпільній організації. Треба бути обережною і не спалитися."

    show павка задумлива at left2 with dissolve
    show інкі роздратована at right2 with dissolve
    інкі "Так, подивимося, що тут у нас…"

    play sound "audio/Сцена 5/ЗвукВідкриттяАвтомату.mp3"
    show інкі весела at right2 with dissolve
    інкі "Ну звичайно. Годіуму немає."

    show інкі задумлива at right2 with dissolve
    інкі "…"

    show інкі роздратована at right2 with dissolve
    інкі "Але це ще не все! Уявляєш, тут не тільки годіум поцупили, ще й викачали весь код."

    show інкі здивована at right2 with dissolve
    інкі "ВЕСЬ! КОД!!!11"

    show павка здивована at left2 with dissolve
    "{i}Такого ще не було. Може, то справа рук організації, до якої належить Лайя?"

    show павка рішуча at left2 with dissolve
    павка "Оце хлопці дали жару…"

    show інкі скептична at right2 with dissolve
    інкі "Ще скажи, що захоплюєшся їх роботою."

    show павка розгублена at left2 with dissolve
    павка "Звісно ні... Але погодься — зробити такий обсяг роботи в такий короткий час, це треба мати вражаючі здібності."

    show інкі задумлива at right2 with dissolve
    інкі "І як перевіряючі могли упустити це? Просто не вкладається в голові."

    show інкі весела at right2 with dissolve
    інкі "Треба їх викликати."

    show павка налякана at left2 with dissolve
    павка "Тількі не це!"

    show інкі скептична at right2 with dissolve
    інкі "А-га! Злякалася, що всі дізнаються, що ти в нас Невживанка?"

    show павка розгублена at left2 with dissolve
    "{i}Йой, щось я розхвилювалася."

    "{i}Треба взяти себе в руки."

    show павка рішуча at left2 with dissolve
    павка "І не злякалася зовсім. Просто…"

    menu:
        "Не хочу затягувати цей день":
            show павка весела at left2 with dissolve
            $відносини_інкі +=1
            павка "Не хочу затягувати цей день без необхідності. Ти справді хочеш зайвих пару годин тут стирчати і давати їм свідчення?"

            павка "Ми знов пропустимо обідню перерву. А ти можеш не встигнути зайти до свого улюбленого трансконектору після роботи!"

            if відносини_інкі < 2:
                show інкі нейтральна at right2 with dissolve
                інкі "Гаразд, вмовила. Не те щоб я хотіла з тобою тут тусити зайві дві години."
            else:
                show інкі задумлива at right2 with dissolve
                інкі "Кицюню, а ти маєш рацію. Та ну їх нафіг, самі винуваті…"

        "Якщо швидко тут закінчимо, за день більше встигнемо":
            show павка рішуча at left2 with dissolve
            павка "Якщо тут не затримуватись, встигнемо більше зробити."

            павка "Більше відремонтованих автоматів - краща звітність в кінці місяця. Шариш?"

            if відносини_інкі < 2:
                show інкі нейтральна at right2 with dissolve
                інкі "Ок, як скажеш. Але якщо що, вся відповідальність на тобі."
            else:
                show інкі задумлива at right2 with dissolve
                інкі "Слушна думка, додаткова премія в цьому місяці мені точно не завадить…"

    show павка нейтральна at left2 with dissolve
    павка "Давай просто надішлемо їм повідомлення, як закінчимо тут і виїдемо в наступний сектор."

    show павка сумна at left2 with dissolve
    павка "Бо це ж ми в секторі А-91О, тут злочинність зашкалює."

    show інкі налякана at right2 with dissolve
    інкі "Точно! Якщо якийсь фрік знов до нас причепиться, мені тиждень бедтріпів гарантований."

    show інкі рішуча at right2 with dissolve
    інкі "Гаразд, тоді давай до роботи. Передай мені електронний ключ під номером 91-ОЩ. Я спробую тут швиденько закінчити."

    menu:
        "Зробити що вона каже":
            show павка весела at left2 with dissolve
            павка "Тримай."

    play sound "audio/Сцена 5/ЗвукВідкриттяАвтоматуГарний.mp3"
    "{i}Коли мова йде про трансконектори, Інкі немає рівних."

    "{i}Технік другого розряду у ї 21 — це вам не жарти!"

    show інкі нейтральна at right2 with dissolve
    інкі "До речі, вчора читала в новинах, що перший в антирейтингу по самогубствах тепер вже сектор А104-Р."

    show павка сумна at left2 with dissolve
    павка "М-хм. Ми ж минулого тижня туди тричі вилітали! Кожен раз - ремонт після пограбування."

    show інкі задумлива at right2 with dissolve
    інкі "Отож-бо й воно… І то тільки в нашу зміну. Які там хакери — там ніхто не париться. В людей дах зриває, ось вони й трощать все, що бачать."

    show павка задумлива at left2 with dissolve
    павка "Здається, до цього там були переобї з постачанням годіуму?"

    show інкі скептична at right2 with dissolve
    інкі "Ну то й що? Там просто люди такі, ну ти знаєш… неблагополучні."

    show інкі рішуча at right2 with dissolve
    інкі "От подивись на мене. Я теж з периферії, теж з дитинства годіуму не вистачало. Але я наполегливо працювала і тому тепер живу в самій Оазі."

    show павка рішуча at left2 with dissolve
    павка "Не у всіх є ті можливості, що були в тебе. В когось є малі діти або хворі родичі — вони не працюють. А годіум всім потрібен."

    павка "Хто має більше часу та сил, той вибивається в люди. А хто ні — той іде трансконектори бити або з даху стрибає."

    show інкі розгублена at right2 with dissolve
    інкі "Так, але в мене…"

    show інкі весела at right2 with dissolve
    інкі "Забудь."

    інкі "Я просто найкраща!"

    show інкі рішуча at right2 with dissolve
    інкі "А тепер не заважай мені — маю перевірити, чи все правильно зробила."

    define робі = Character("???")

    show павка налякана at left2 with dissolve
    show робі нарік злий at center with dissolve
    play music "audio/Сцена 6/ФлешбекРобі.mp3" fadeout 1
    робі "Гей ви, де мій годіум?"

    show робі нарік роздратований at center with dissolve
    show павка здивована at left2 with dissolve
    "{i}О мій бог. Кого я бачу!"

    show павка сумна at left2 with dissolve
    "{i}Як же він жахливо виглядає. Робі, що ти з собою зробив?"

    show інкі роздратована at right2 with dissolve
    define робі = Character("Робі")
    інкі "Віджени цього придурка. Він мені світло затуляє."

    show робі нарік злий at center with dissolve
    робі "Де мій годіум? Я тебе питаю, дурепо!"

    show павка рішуча at left2 with dissolve
    павка "Пане, прошу відійти — ви заважаєте працювати ремонтній бригаді."

    show робі нарік роздратований at center with dissolve
    робі "Я заслужив свій базовий годіум! І я нікуди не піду з цього місця, поки його не отримаю!"

    show павка роздратована at left2 with dissolve
    павка "Доведеться почекати. Відійдіть від апарату!"

    show робі нарік злий at center with dissolve
    робі "Ти що, охрініла?"

    if відносини_інкі >=2:

        if годіум_інкі == False:
            show інкі роздратована at right2 with dissolve
            інкі "Та дай ти йому той годіум... Он у мене в машині ще доза є. Пожалій людину."

            show павка сумна at left2 with dissolve
            "{i}Ти просто не знаєш, що це за людина, Інкі."

            show робі нарік роздратований at center with dissolve
            menu:
                "Застосувати електрошокер":
                    $ електрошок += 1
                    scene автомат_годіум at shaking
                    show робі нарік злий at center with dissolve
                    show павка зла at left2 with dissolve
                    show інкі розгублена at right2 with dissolve
                    play sound "audio/Сцена 5/ЗвукЕлектрошокера.mp3"
                    павка "Ось тобі, сволото."

                    scene автомат_годіум
                    show павка зла at left2 with dissolve
                    show інкі розгублена at right2 with dissolve
                    show робі нарік наляканий at center with dissolve
                    робі "АААА! Боляче! Не можна бути такою злою, дівчино!"

                    show павка роздратована at left2 with dissolve
                    павка "Поговори мені ще."

                    show робі нарік сумний at center with dissolve
                    робі "Та добре, добре! Йду. Бачиш — я пішов."

                    show інкі рішуча at right2 with dissolve
                    інкі "Не ображайтеся на мою подругу — в неї поганий ранок. За годину трансконектор працюватиме справно!"

                    show робі нарік роздратований at center with dissolve
                    робі "Поганий ранок, ага… Гадюка, така сама, як моя колишня…"

                    hide робі нарік роздратований with dissolve
                    show інкі весела at right2 with dissolve
                    інкі "Ну от. Він пішов, і наче навіть не встиг мене налякати."

                    show інкі скептична at right2 with dissolve
                    інкі "Чого не скажеш про тебе…"

                    show павка нейтральна at left2 with dissolve
                    павка "Пізніше розповім. Якщо настрій буде."

                "Дати Робі годіум":
                    $відносини_інкі += 1
                    show павка нейтральна at left2 with dissolve
                    play sound "audio/Сцена 5/ЗвукПляшкиЯкуХоваютьНазад.mp3"
                    павка "Ось, тримай. За годину автомат буде в робочому стані."

                    show робі нарік нейтральний at center with dissolve
                    робі "Молодець, жінко! Так тримати!"

                    hide робі нарік задоволений with dissolve
                    show інкі весела at right2 with dissolve
                    інкі "Ну от. Він пішов, все обійшлося. Зробили добру справу — допомогли людині з ломкою."

        if годіум_інкі == True:
            show інкі розгублена at right2 with dissolve
            інкі "Я б віддала йому свою дозу, але в мене зайвої не лишилося. Доведеться тобі щось вигадати."

            show павка рішуча at left2 with dissolve
            "{i}О, я вже знаю що мені робити!"

            show робі нарік роздратований at center with dissolve
            menu:
                "Застосувати електрошокер":
                    $ електрошок += 1
                    scene автомат_годіум at shaking
                    show робі нарік злий at center with dissolve
                    show павка зла at left2 with dissolve
                    show інкі розгублена at right2 with dissolve
                    play sound "audio/Сцена 5/ЗвукЕлектрошокера.mp3"
                    павка "Ось тобі, сволото."

                    scene автомат_годіум
                    show павка зла at left2 with dissolve
                    show інкі розгублена at right2 with dissolve
                    show робі нарік наляканий at center with dissolve
                    робі "АААА! Боляче! Не можна бути такою злою, дівчино!"

                    show павка роздратована at left2 with dissolve
                    павка "Поговори мені ще."

                    show робі нарік сумний at center with dissolve
                    робі "Та добре, добре! Йду. Бачиш — я пішов."

                    show інкі рішуча at right2 with dissolve
                    інкі "Не ображайтеся на мою подругу — в неї поганий ранок. За годину трансконектор працюватиме справно!"

                    show робі нарік роздратований at center with dissolve
                    робі "Поганий ранок, ага… Гадюка, така сама, як моя колишня…"

                    hide робі нарік роздратований with dissolve
                    show інкі весела at right2 with dissolve
                    інкі "Ну от. Він пішов, і наче навіть не встиг мене налякати."

                    show інкі скептична at right2 with dissolve
                    інкі "Чого не скажеш про тебе…"

                    show павка нейтральна at left2 with dissolve
                    павка "Пізніше розповім. Якщо настрій буде."

    if відносини_інкі < 2:
        show інкі роздратована at right2 with dissolve
        інкі "Здихайся вже його. Я не можу в таких умовах працювати."

        show павка розгублена at left2 with dissolve
        "{i}Якби це було так просто! Що ж мені робити?"

        if годіум_інкі == False:
            menu:
                "Дати Робі годіум Інкі":
                    play sound "audio/Сцена 5/ЗвукПляшкиЯкуХоваютьНазад.mp3"
                    $відносини_інкі -= 1
                    show павка рішуча at left2 with dissolve
                    павка "Ось, тримай. За годину автомат буде в робочому стані."

                    show робі нарік нейтральний at center  with dissolve
                    робі "Молодець, жінко! Так тримати!"

                    hide робі нарік задоволений with dissolve
                    show інкі роздратована at right2 with dissolve
                    інкі "Гей, ти що, віддала йому мою дозу? Геть здуріла??"

                    menu:
                        "Вибач, на мене щось найшло":
                            $обіцянка_інкі = True
                            $відносини_інкі += 1
                            show павка розгублена at left2 with dissolve
                            павка "Вибач, на мене щось найшло. Треба було швидко реагувати, і я зробила те, що перше прийшло в голову."

                            show павка весела at left2 with dissolve
                            павка "Не гнівайся на мене, гаразд? Після роботи пригощу тебе подвійним 36-м, і знову засяєш як сонечко, е?"
                            $ renpy.notify('Gained achievement: "Подвійні стандарти"')

                            show інкі нейтральна at right2 with dissolve
                            інкі "Ну гаразд, тільки якщо подвійним. Ти сьогодні сама на себе не схожа."

                            show інкі весела at right2 with dissolve
                            інкі "Ну що ж, хоч зробили добру справу - допомогли людині з ломкою."

                        "Заспокойся. Ти свою дозу сьогодні вже отримала" :
                            show павка роздратована at left2 with dissolve
                            $відносини_інкі -= 1
                            павка "Заспокойся. Ти свою дозу сьогодні вже отримала. Не скупися на щастя для інших."

                            show інкі сумна at right2 with dissolve
                            інкі "Щось занадто багато охочих до мого щастя останнім часом."

                            інкі "Я такого від тебе не очікувала, кицюне."

                "Застосувати електрошокер":
                    $ електрошок += 1
                    scene автомат_годіум at shaking
                    show павка зла at left2 with dissolve
                    show робі нарік наляканий at center with dissolve
                    show інкі роздратована at right2 with dissolve
                    play sound "audio/Сцена 5/ЗвукЕлектрошокера.mp3"
                    павка "Ось тобі, сволото."

                    scene автомат_годіум
                    show павка зла at left2
                    show інкі розгублена at right2
                    show робі нарік наляканий at center 
                    робі "ААА! Боляче! Не можна бути такою злою, дівчино!"

                    show павка роздратована at left2 with dissolve
                    павка "Поговори мені ще."

                    show робі нарік сумний at center with dissolve
                    робі "Та добре, добре! Йду. Бачиш — я пішов."

                    show інкі весела at right2 with dissolve
                    інкі "Не ображайтеся на мою подругу — в неї поганий ранок. За годину трансконектор працюватиме справно!"

                    show робі нарік роздратований at center with dissolve
                    робі "Поганий ранок, ага… Гадюка, така сама, як моя колишня…"

                    hide робі нарік роздратований with dissolve
                    show інкі весела at right2 with dissolve
                    інкі "Ну от. Він пішов, і наче навіть не встиг мене налякати."

                    show інкі скептична at right2 with dissolve
                    інкі "Чого не скажеш про тебе…"

                    show павка нейтральна at left2 with dissolve
                    павка "Пізніше розповім. Якщо настрій буде."

                    show інкі скептична at right2 with dissolve
                    інкі "Тримай це при собі, люба. Мені своїх проблем вистачає."

        #if годіум_інкі <= 1:
            #show інкі рішуча at right2
            #show павка зла at left2
            #show робі нарік наляканий at center
#
            #play sound "audio/Сцена 5/ЗвукЕлектрошокера.mp3"
#
            #павка "Ось тобі, сволото"

            #робі "Ай, боляче! Не можна бути такою злою, дівчино!"

            #павка "Поговори мені ще"

            #show робі нарік сумний at center

            #show павка рішуча at left2
            #робі "Та добре, добре! Йду. Бачиш — я пішов"
            #show інкі весела at right2
            #інкі "Не ображайтеся на мою подругу — в неї поганий ранок. За годину трансонектор працюватиме справно!"

            #show робі нарік роздратований at center
            #робі "Поганий ранок, ага… Гадюка, така сама, як моя колишня…"
            #hide робі роздратований with dissolve

            #інкі "Ну от. Він пішов, і наче навіть не вибісив мене. Чого не скажеш про тебе…"

            #show павка нейтральна at left2
            #show інкі задумлива at right2
            #павка "Пізніше розповім. Якщо настрій буде"

            #show інкі скептична at right2
            #інкі "Тримай це при собі, люба. Мені на сьогодні вистачає проблем"

    show інкі рішуча at right2 with dissolve
    play music "audio/Сцена 5/КопіяТемаМіста.mp3" fadeout 1
    інкі "Зовсім трошки залишилося. Почекай, я зараз свою частину закінчу — і ти зможеш почати діагностику."

    show павка задумлива at left2 with dissolve
    "{i}Блін, він мене навіть не впізнав. Але ж я пішла від нього лише півроку тому!"

    "{i}І він так змінився. Схуд, зблід… А ще кажуть, що годіум не має поганих наслідків..."

    scene фон
    stop music fadeout 2
    "{i}Півроку тому..."

    jump scene_six
