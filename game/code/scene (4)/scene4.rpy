label scene_four:

    image машина_анімована = Movie(size=(2030, 1080), play="images/Scene 4/машина_анімована.ogv")

    #show павка нейтральна at center
    scene машина
    show павка нейтральна at center with dissolve
    play music  "audio/Сцена 4/МістоАмбієнт2.mp3" fadeout 1
    "{i}Інкі не помічає мого наближення, бо відвернулась до авто і приймає годіум"
    show павка задумлива at left2 with dissolve
    play sound  "audio/Сцена 4/ПрийомГодіуму.mp3" fadeout 1
    show інкі годіум at right2 with dissolve
    "{i}Ранок тільки настав. Цікаво, вкотре вона вже закидується?"

    play sound  "audio/Сцена 3/ВилитиГодіум.mp3" fadeout 1

    menu:
        "{i}Привітатися":
            show павка весела at left2 with dissolve
            павка "Слава засновникам Купола!"

            show інкі налякана at right2 with dissolve
            інкі"Слава! Слава! Слава!!!"
        "{i}Запитати, чи не зарано для годіуму":
            $відносини_інкі +=1
            show павка рішуча at left2 with dissolve
            павка "Чи не зарано для годіуму?"

            show інкі збуджена at right2 with dissolve
            інкі"А? Що? Павка, це ти? Слава засновникам!"

    play music  "audio/Сцена 4/ТемаПавкиТаІнкі.mp3" fadeout 1
    show інкі збуджена at right2
    show павка задумлива at left2
    "{i}Я все ще не придумала, що мені прославляти"

    menu:
        "{i}Слава тверезості":
            "{i}..."
        "{i}Слава пилу під ногами":
            "{i}..."

    show павка нейтральна at left2
    show інкі весела at right2

    інкі"Ти запізнилась. Я чекала на тебе і вирішила прийняти ще одну дозу. Як рекомендує доктор Хакім: двічі в ранці, двічи ввечері"
    інкі"Ти виглядаєш жахливо! Знову пропустила ранковий прийом?"

    show павка задумлива at left2
    show інкі задумлива at right2
    "{i}Інкі намагається зблизитися. Чесно кажучи, навіть не знаю, як я до цього ставитися"
    "{i}Чи хочу я з нею дружити? Або можливо навіть щось більше?"

    menu:
        "{i}Це тебе не обходить":
            show павка роздратована at left2
            show інкі нейтральна at right2
            інкі "Ти права, мене це не обходить. Кожна людина сама повинна вирішувати свої проблеми."
            інкі "Але навіщо навмисне ускладнювати собі життя, відмовляючись від годіуму? Я тебе не розумію"

        "{i}Та, ти це знаєш":
            $відносини_інкі +=1
            show павка сумна at left2

            show інкі здивована at right2
            інкі "От дивачка. Кайфуєш від депресії та безпросвітності?"

            show інкі весела at right2
            інкі "Годіум дозволяє побачити справжні кольори світу. Ти просто не знаєш, що втрачаєш"

    show інкі весела at right2

    show павка сумна at left2
    інкі "Годіум поєднує, ти ж знаєш, що це так"

    show павка нейтральна at left2
    інкі "Час вирушати. Сьогодні важкий день, багато квитків на ремонт по всьому місту."
    play sound "audio/Сцена 4/СіданняВМашину.mp3"
    "{i}*Сідає в машину*"

    show інкі задумлива at right2
    інкі"Точно не хочеш трошки? В мене є додаткова доза. Ось побачиш, тобі полегшає"

    show машина_анімована behind  павка with dissolve

    "{i}'Годіум поєднує'. А як же. Все її життя — лише низка втеч від реальності і випадкових сексуальних зв'язків."

    show павка задумлива at left2
    павка "А нащо тобі запасна доза?"

    show інкі нейтральна at right2

    show павка рішуча at left2
    павка "Ти ж сказала, що вже прийняла другу вранішню за рекомендацією доктора Хакіма"

    павка "Чи то вже була не друга?"

    show інкі весела at right2
    інкі"Де друга, там і третя. Годіуму забагато не буває"

    show павка здивована at left2
    павка "Ще як буває!"

    show інкі роздратована at right2
    інкі "І взагалі, чого ти причепилась? Тільки давай ти не будеш знову штовхати мені свої безумні ідеї про життя без годіуму"

    show павка задумлива at left2
    "{i}Нє, ну справді — не розповідати ж їй зараз про те, що зробив зі мною Робі…"

    show інкі весела at right2
    інкі"Завдяки годіуму мені життя в кайф. Нащо відмовлятись від того, що дозволяє тобі забути про проблеми?"

    show павка нейтральна at left2
    павка "Інкі?"

    show інкі здивована at right2
    інкі"М-м-м?"

    павка "В тебе все гаразд?"

    show павка сумна at left2
    інкі"…"

    show інкі рішуча at right2
    інкі"В мене все тіп-топ. Я найкраща, пам‘ятаєш?"

    show павка нейтральна at left2
    show інкі збуджена at right2
    інкі "О, ти бачила нову рекламу годіуму45?"

    show павка рішуча at left2
    павка "Подивись вниз, Інкі. Ти ніколи не помічала, що в Оазі більше трансконекторів, ніж житлових будинків?"

    інкі"Ні, а що? Ой, дивись, там нова реклама! Треба буде в кінці робочого дня заїхати та зберегти її для моєї колекції"

    show інкі весела at right2
    інкі"Хто вживає годіум56 — той дещо краще за хліб їсть!"

    "{i}Знов вона за старе"

    show інкі збуджена at right2
    інкі"Хто вживає годіум57 — для того трансконектор це справжній дім!"

    павка "Дякую за цитату."

    show інкі весела at right2
    інкі "На здоров'я!"

    павка "Ти ж знаєш, що всі ці слогани генеруються алгоритмами, налаштованими на довжину хвиль нашого мозку, щоб впасти в пам'ять якомога краще?"

    show інкі скептична at right2
    інкі "Ти так кажеш, наче в цьому є щось погане"

    show інкі весела at right2
    інкі "Вони налаштовані на те, щоб приносити задоволення."

    show інкі скептична at right2
    інкі "Ти ж не хочеш сказати, що ти проти задоволення, м-м-м?"

    menu:
        "{i}Наркотики, Інкі, це не єдиний спосіб відчути задоволення.":
            павка "Наркотики, Інкі, це не єдиний спосіб відчути задоволення."

        "{i}Не можна жити одним задоволенням":
            павка "Не можна жити одним задоволенням"
            павка "І тікати весь час від проблем — це теж не найкраща історія."


    інкі "Та? І яку альтернативу ти мені пропонуєш?"

    show павка сумна at left2
    show інкі здивована at right2

    павка "Знаєш, чому я кинула приймати годіум?"

    інкі "Давно цікаво. Розкрий мені свою таємницю, кицюню!"

    show павка замріяна at left2
    show інкі нейтральна at right2
    павка "Я відкрила для себе дещо нове. Музику. І вона заменила мені годіум"
    павка "Музика може допомогти і тобі. Ти можеш вживати менше"

    show павка здивована at left2
    show інкі роздратована at right2
    інкі "І нащо ти штовхаєш мені це застаріле лайно? Хочеш навіяти мені бедтріп?"

    show павка задумлива at left2
    "{i}Здається, вона одразу пошкодувала, що це сказала. Хоча може, приструнити ці матюкливі пориви?"

    menu:
        "{i}Поругатися на Інкі":
            $ лайка_інкі = True
            show павка роздратована at left2
            show інкі скептична at right2
            павка "Деякі речі це не лайно, Інкі! Лайно — це те, як ти зі мною розмовляєш!"

            show інкі нейтральна at right2
            павка "Якщо не можеш інакше, тоді краще давай просто помовчимо, ок?"

            show інкі здивована at right2
            інкі "Ну бля-яха му-уха. Що ж ти сьогодні така зла?"

            павка "Та де я зла? Це в тебе скоро передоз буде"

            інкі "Ну добре, добре. Вибач! Давай закінчимо цю розмову, просто закінчимо і забудемо, добре? "

        "{i}Ігнорувати неадеквашку":
            $відносини_інкі +=1
            show павка нейтральна at left2
            show інкі нейтральна at right2
            "{i}Що це я бачу в її очах? Вдячність?"


    show інкі розгублена at right2
    show павка нейтральна at left2
    інкі "Все це лайно змушує мене хвилюватися"

    show павка задумлива at left2
    "{i}Інкі тягнеться за новою дозою..."

    menu:

        "{i}Зупинити Інкі":
            $відносини_інкі =1
            play sound "audio/Сцена 5/ЗвукПляшкиЯкуХоваютьНазад.mp3"
            show павка здивована at left2
            show інкі роздратована at right2
            інкі "Відчепися від мене! Я тебе не вчу жити, і ти мене не вчи!"

            павка "Інкі…"

            інкі "Так, бляха-муха, в мене проблеми! Великі проблеми! "

            show інкі збуджена at right2
            інкі "І тому мені треба прийняти годіум сорок п'ятий — і знов засіяти!"

        "{i}Нехай зловживає ":
            $ годіум_інкі = 1
            show інкі приймає_годіум at right2
            show павка задумлива at left2
            інкі "Гик! Наче знов розвиднюється."

    show павка нейтральна at left2
    show інкі весела at right2
    інкі "Доречі, ми під'їзжаємо до першого трансконектору. Подивимося, що там у квитку на ремонт…"

    show інкі задумлива at right2
    інкі '"Автомат не видає годіум". Як гадаєш, в чому з ним проблема?'

    show павка весела at left2
    павка "Я не гадаю, я знаю"

    show інкі здивована at right2
    павка "Хтось знов його хакнув і вкрав увесь годіум"


    інкі "Нам, що оновили програму сповіщення? Оту, як там її… Ну ту…"

    павка "Звісно ні. В нас все так само. Але щоб здогадатися, що на периферії міста у 9 з 10 випадків нас викликають переустановити прогру після крадіжки — багато розуму не треба."

    show інкі нейтральна at right2
    інкі "Та ладно тобі, в тебе завищені вимоги!"

    show павка роздратована at left2
    павка "Як ти могла забути Кларіссіму? Ти ж в ній кожен день копирсаєшся. Можна сказати, ти в ній живеш! Невже годіум настільки роз'їв тобі мозок?"

    інкі "Та ні. То все вік"

    павка "Тобі 21, Інкі! Треба менше вживати!"


    if відносини_інкі >= 2:

        if лайка_інкі == True :
            show інкі роздратована at right2
            show павка роздратована at left2

            інкі "Будеш зі мною так говорити — я скажу слово на букву Л."

            павка "Л… "

            menu:
                "{i}Ліпосоми?":
                    "..."
                "{i}Лесбійка?":
                    "..."
                "{i}Лазня?":
                    "..."

            show інкі весела at right2
            "{i}Лайно!!"

            show павка весела at left2
            павка "О ні, ти знов сказала це слово…"

            інкі "Так, сказала"
            інкі "І бачиш — тобі вже  майже весело"

        if лайка_інкі == True :
            show інкі сумна at right2
            show павка сумна at left2

            інкі "Кицюню, за що ти так на мене насіла сьогодні?"

            інкі "Ти не уявляєш собі, скільки лайна мені довелося вигребсти від своїх…"

            інкі "Просто дай мені спокій і лізь в душу, гаразд?"

            "{i}Оу, схоже я справді заділа її за живе"

            павка "Вибач, не буду."

            павка "Але якщо захочеш поговорити - я завжди поруч."

            інкі "…"

    if відносини_інкі < 2:

        if годіум_інкі == 1:

            show інкі весела at right2
            show павка нейтральна at left2

            інкі "Пфф, ватева"
            інкі "Зовсім вже з катушок злітаєш без регулярної дози"

        if годіум_інкі == 0:
            show інкі роздратована at right2
            show павка здивована at left2
            інкі "Пішла ти."
            павка "…"

    scene фон
    stop music fadeout 3
    інкі "Ми на місці."
    "..."
    jump scene_five
