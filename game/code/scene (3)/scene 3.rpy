label scene_three:

    scene трансконектор

    play music "audio/Сцена 3/МістоАмбієнт.mp3"
    "{i}Старий добрий трансконектор. Елітна приблуда, яку я, можливо, бачу в останній раз."

    "{i}Ті самі металеві стіни, ті самі багаті втичери. Закинулися зранку годіумом і втичуть у Лампи Радості."

    '{i}Чи може краще назвати їх "Лампивтичерами"? Сумна картина...'

    show павка рішуча at center with dissolve
    "{i}Он та сама лавочка. Мені туди."

    show павка налякана at center with dissolve
    "{i}Трохи лячно."

    show павка рішуча at center with dissolve
    "{i}Але спочатку треба взяти в автоматі пляшку годіуму."

    menu:
        "Взяти годіум":
            play sound "audio/Сцена 5/ЗвукПляшкиЯкуХоваютьНазад.mp3"

    show павка розгублена at center with dissolve
    "Не думала, що колись доведеться знову тримати в руках цю отруту. Сподіваюсь, хоча б не доведеться її вживати."

    menu:
        "Сісти":
            play sound "audio/Сцена 3/Шурхіт.mp3"

    show павка нейтральна at left2 with dissolve
    show лайя затемнений at right2 with dissolve
    лайя "Залізяці корозія."

    show павка замріяна at left2 with dissolve
    "{i}Це той самий приємний голос."

    show павка весела at left2 with dissolve
    павка "Людям — кайф."

    show павка розгублена at left2 with dissolve
    "{i}Як же все це дивно. А раптом за нами слідкують? Звідки мені знати, що он той хлопець — не агент Оази? Або он ті дві дівчини?"

    лайя "Не повертайся до мене. Роби вигляд, що приймаєш годіум."

    show павка здивована at left2 with dissolve
    "{i}Блін. Легше сказати ніж зробити."

    лайя "Непомітно вилий зміст флакону на підлогу."

    menu:
        "Зробити як він каже":
            play sound "audio/Сцена 3/ВилитиГодіум.mp3"
            "..."

    show павка задумлива at left2 with dissolve
    "{i}Це все дуже підозріло. А що як він хоче мною скористатись?"

    show павка сумна at left2 with dissolve
    "{i}Останній раз, коли я довірилася людині, все закінчилось дуже погано."

    show павка рішуча at left2 with dissolve
    "{i}Хоча який в мене вибір? Я вже прийшла сюди, значить, доведеться робити те, що він каже."

    show павка здивована at left2 with dissolve
    лайя "Зроби вигляд, наче годіум почав діяти."

    лайя "Наче розмовляєш сама з собою під дією препарату."

    menu:
        "Спробувати зробити як він каже":
            $покора_лайі += 1
            "..."

        "А можна без цього?":
            show павка налякана at left2 with dissolve
            павка "Це обов'язково? Я щось дуже не хочу цього робити."

            лайя "Довірся мені."

    play music "audio/Сцена 3/Дзвін1.mp3" fadeout 1
    show павка болить голова at left2 with dissolve
    "{i}Дідько, мозок знову починає шаліти від думки про дозу!"

    "{i}Мозочок, любий, будь ласка, тільки не зараз!"

    "{i}Доведеться застосувати перевірений способ..."

    menu:
        "Дати ладу дзвону в голові":
            stop music fadeout 1
            play music "audio/Пісні Павка/Мугикання.mp3" fadeout 1
            show павка співає at left2 with dissolve
            "..."

    stop music fadeout 1
    play music "audio/Сцена 3/МістоАмбієнт.mp3" fadeout 1
    show павка весела at left2 with dissolve
    "{i}Фух, відпустило. Це завжди мене заспокоює."

    show павка нейтральна at left2 with dissolve
    "{i}Мабуть, він це почув..."

    show павка усміхнена at left2 with dissolve
    павка "Ото дива! Все таке красиве, всі такі гарні! Он там красуня йде… Так, красуня. Може підійти познайомитися, га?"

    лайя "Мені доповідали, що ти особлива. Тепер я чую це на власні вуха."

    show павка нейтральна at left2 with dissolve
    павка "Музика — мій власний спосіб вижити в цьому світі."

    лайя "Твоє бажання звільнитися з під тиранії Купола — природне."

    лайя "Але шлях до свободи не буде легким. Нам потрібна допомога людини з твоїми навичками та рівнем доступу."

    show павка задумлива at left2 with dissolve
    "{i}А в повідомленні казав, що складно не буде…"

    "{i}Я можу про це сказати. Але раптом це його образить?"

    menu:
        "Звернути увагу на розбіжність у його словах":
            $відносини_лайя += 1

            show павка рішуча at left2 with dissolve
            павка "Так, я хочу втекти звідси. Але в в повідомленні ти казав, що складно мені не буде."

            show павка розгублена at left2 with dissolve
            павка "Я трохи хвилююся, як бачиш!"

            лайя "Ти прямолінійна. Мені це подобається."

            show павка весела at left2 with dissolve
            "{i}Так, я така!"

        "Посваритися на Лайю":
            $відносини_лайя -= 1
            show павка роздратована at left2 with dissolve
            павка "За кого ти мене приймаєш? Ти збрехав, що буде легко, щоб заманити мене сюди, так? Бо раніше ти інше казав!"

            show павка розгублена at left2 with dissolve
            павка "Я бляха-муха збентежена і розгублена!"

            лайя "В мене немає часу на безглузду сварку. Я тобі не ворог."

            show павка зла at left2 with dissolve
            "{i}Ага, так я і повірила! А чому тоді примушує робити речі, від яких мені дискомфортно? Не подобається він мені!"

        "Зробити вигляд, що не почула цього":
            $покора_лайі += 1

            show павка розгублена at left2 with dissolve
            "{i}Пальці холонуть, серце б'ється швидше. Це все відбувається ніби не зі мною."

            "{i}Це тривога, найдавніший людський інстинкт."

    show павка сумна at left2 with dissolve
    павка "Так, але... Я трохи хвилююся."

    show павка розгублена at left2 with dissolve
    павка "Для тебе, мабуть, це просто черговий робочий день. А для мене це останній день в зрозумілому мені світі."

    павка "Я багато років працювала, щоб отримати цю роботу. Щоб жити в Оазі, а не на периферії міста."

    show павка задумлива at left2 with dissolve
    павка "Кожен день мого життя — цеглина. І з них складається моє теперішнє."

    павка "А зараз все це буде зруйновано, і я не знаю, що чекатиме на мене в майбутньому."

    show павка сумна at left2 with dissolve
    павка "Я ДУЖЕ хочу опинитися на волі. На волі, а не в лапах перевіряючих."

    лайя "Я вже багато років живу так, наче кожен мій день — останній. Але я добре тебе розумію."

    лайя "Не хвилюйся, тобі нема чого боятись. Я був за межами Купола."

    show павка здивована at left2 with dissolve
    павка "Тоді чому ти зараз тут?"

    лайя "…"

    "{i}Як же хочется повернутися і подивитися йому в очі! Але це може бути небезпечно…"

    menu:
        "Обернутися і подивитися йому в очі":
            $ renpy.notify('Gained achievement: "Що казали його очі?"')
            $відносини_лайя += 1
            $покора_лайі -= 1
            play sound "audio/Сцена 3/Шурхіт.mp3"
            show павка весела at left2 with dissolve
            show лайя сумний2 at right2 with dissolve
            "..."

            show лайя злий2 at right2 with dissolve
            лайя "Що?!"

            menu:
                "Повернутись назад":
                    play sound "audio/Сцена 3/Шурхіт.mp3"

            show павка розгублена at left2 with dissolve
            лайя "Я не просто так сказав тобі не обертатися. Ти щойно поставила під загрозу і себе, і мене."

            show павка задумлива at left2 with dissolve
            "{i}Голос звучить металево і недоброзичливо. Схоже, йому не подобається, коли роблять не так, як він каже."

            show лайя нейтральний2 at right2 with dissolve
            show павка розгублена at left2 with dissolve
            павка "Вибач! Я не хотіла."

        "Просто чекати на відповідь":
            $покора_лайі += 1
            show павка нейтральна at left2 with dissolve
            show лайя затемнений at right2
            лайя "Зараз не час для сумнівів. Ти зробиш те, що я скажу, а натомість отримаєш те, чого так палко бажаєш."

            лайя "Свободу від Купола."

            лайя "Свободу від годіуму."

            лайя "Музику."

            show павка здивована at left2 with dissolve
            павка "Ти знаєш про музику?"

            лайя "Я знаю достатньо, щоб розуміти, чому за можливість її творити варто ризикнути всім, що в тебе є."

            лайя "Мій статус дає мені доступ до інформації, яку приховують від людей. Ти не уявляєш собі, наскільки далеко сягає брехня Оази."

            show павка задумлива at left2 with dissolve
            "{i}Може, він розповість щось про музику Давніх?"

            лайя "За межами Купола існує світ, Павко. Світ без годіуму і тиранії Оази. Де можна створювати що завгодно і не боятися переслідувань."

            menu:
                "Розкажи ще":
                    $відносини_лайя += 1
                    лайя "Я міг би розповісти тобі про Вічнозелене місто. Про стародавні манускріпти, що розмовляють музикою. Про Гори, що чекають на пісню Шукача, про Великий Плач і про Вежу Думок."

                    show павка здивована at left2 with dissolve
                    "{i}Звучить просто неймовірно! Може справді буде нагода поговорити про все це?"

                    лайя "Але все це не на часі. Можливо, колись у нас ще буде можливість поговорити."

                    show павка замріяна at left2 with dissolve
                    павка "А ти вмієш інтригувати! То яке у тебе для мене завдання?"

                "Я знала! Знала!!" :
                    $відносини_лайя += 1
                    show павка весела at left2
                    павка "Я так і думала!"

                    павка "Адже там немає годіуму і ніхто не забороняє створювати пісні!"

                    лайя "Ти розумніша, ніж здається. Це добре. Але ти навіть не уявляєш, про що говориш. Я теж не уявляв, доки не побачив на власні очі."

                    show павка замріяна at left2 with dissolve
                    "{i}Він мене інтригує. Здається, ми трохи схожі."

                    show павка рішуча at left2 with dissolve
                    павка "Так що ти хочеш, щоб я зробила? Я маю на увазі, що треба від мене організації, яку ти представляєш?"

                "Пфф. Спроба вразити detected":
                    $відносини_лайя += 1
                    $покора_лайі += 1
                    show павка роздратована at left2 with dissolve
                    павка "Я і так це знаю! Сподіваюсь, ти не говориш це тільки для того, щоб вразити мене?"

                    лайя "Ти нічого не знаєш, Павко. Світ за межами Купола більший, ніж ти можеш уявити. Втім, згодом ти сама все побачиш."

                    show павка задумлива at left2 with dissolve
                    "{i}Він постійно повторює, що я нічого не знаю і явно хоче справити враження. Треба обережніше з цим типом."

                    show павка рішуча at left2 with dissolve
                    павка "Так, скоро я сама все це побачу. То що я маю зробити, щоб ти допоміг мені вибратися з Купола?"

            лайя "Що ж, спершу ти повинна зібрати для мене інформацію."

            лайя "Ми збираємо дані про споживачів годіуму."

            menu:
                "Поцікавитися, навіщо це їм":
                    $покора_лайі -= 1
                    show павка задумлива at left2 with dissolve
                    павка "Навіщо це вам? Якщо це не черговий страшний секрет."

                    лайя "Я не можу тобі цього сказати."

                "Не сувати носа в чужі справи":
                    $покора_лайі += 1

            show павка нейтральна at left2 with dissolve
            лайя "Сьогодні ти вийдеш на роботу, як завжди. В місті чимало автоматів з годіумом, і деякі з них час від часу ламаються. Ви будете відповідати на виклики і приїжджати ремонтувати автомати, як завжди."

            show павка задумлива at left2 with dissolve
            "{i}Ага, сьогодні якраз багато роботи."

            лайя "Але сьогодні, як ти знаєш, не звичайний день. Замість свого стандартного діагностичного приладу ти будеш використовувати той, що знайдеш під місцем, на якому зараз сидиш."

            menu:
                "Пошарити рукою під сидінням":
                    play sound "audio/Сцена 3/Шурхіт.mp3"
                    show павка здивована at left2 with dissolve
                    "{i}Ой, до лави справді щось приліплено!"

            stop sound
            "{i}Виглядає так само, як мій прилад для діагностики. Цікаво, звідки в них такий точний дублікат?"

            show павка нейтральна at left2 with dissolve
            лайя "Як ти знаєш, кожен автомат обладнаний блоком для збору й обробки даних. Він знаходиться на основній платі, за центральним процесором."

            лайя "Ти приєднаєшся до нього за допомогою цього приладу та ініціюєш протокол діагностики. Після того, як процедура буде завершена, ти дістанеш прилад і закриєш кришку автомата."

            show павка задумлива at left2 with dissolve
            павка "І це все?"

            лайя "Не так вже й складно, правда? Після завершення робочого дня ти знищиш цей прилад у дезинтеграторі і вирушиш на вулицю Чисту, будинок 2."

            лайя "Там, біля рекламного білборду,на тебе чекатиме людина в капелюсі. Вона передасть тобі посвідчення технічного співробітника наукової експедиції."

            лайя "Захопи вдома теплий одяг і вирушай з цим посвідченням до південно-східної брами. Там, біля пункту пропуску, ти знайдеш групу вчених."

            лайя "Серед них буду і я. Підійди до мене і скажи, що ти моя нова асистентка. Разом ми вийдемо за межі Купола і ти будеш вільна."

            лайя "Запам'ятала?"

            show павка рішуча at left2 with dissolve
            павка "Так, кураторе Лайо."

            лайя "Добре. Є питання?"

            menu:
                "Що я скажу Інкі?":
                    show павка розгублена at left2 with dissolve
                    павка "Що я скажу своїй напарниці?"

                    лайя "Не кажи їй нічого — ані про мене, ані про свою місію. Якщо буде задавати питання — вигадай щось. Я знаю, що ти вважаєш її своєю подругою, але в нас немає підстав їй довіряти."

                    menu:
                        "Вона мені не подруга":
                            $покора_лайі += 1
                            show павка роздратована at left2 with dissolve
                            павка "Вона мені не подруга, ми просто працюємо разом."

                            лайя "Тим краще. Сподіваюсь, ти розумієш, що залишити нашу розмову в таємниці — в твоїх інтересах."

                        "Я не вмію брехати!":
                            show павка розгублена at left2 with dissolve
                            павка "А що як вона здогадається? В мене все на обличчі написано, я не зможу це приховати!"

                            лайя "Ти так довго успішно приховувала від усіх свою таємницю, і сьогодні теж впораєшся. Інакше ти наразиш себе на таку небезпеку, що навіть я не зможу тебе захистити."

                "Що, як мене побачать перевіряючі?":
                    show павка розгублена at left2 with dissolve
                    павка "Що, як мене побачить Перевіряючі?"

                    лайя "І що? Ти технік-ремонтник, виконуєш свою роботу. Хіба це протизаконно?"

                "А це точно безпечно?":
                    $покора_лайі -= 1
                    show павка розгублена at left2 with dissolve
                    павка "А це точно безпечно? На мене не почнеться полювання, чи ще щось?"

                    лайя "Ти вже наразила себе на небезпеку тим, що прийшла на зустріч зі мною. Але хіба цей ризик не вартий того, щоб нарешті звільнитися від тиранії Оази?"

                    show павка рішуча at left2 with dissolve
                    павка "Так, але... Ти не відповів на запитання."

                    лайя "Це безпечно. Як я сказав, ми просто збираємо інформацію. Все пройде плавно, якщо ти будеш вести себе розумно і не втрачатимеш пильності. Більшого гарантувати тобі я не можу."

            show павка нейтральна at left2 with dissolve
            павка "В мене є ще одне питання."

            лайя "Так?"

            show павка задумлива at left2 with dissolve
            павка '"Куратор". Слово наче знайоме, але воно застаріле. Що воно означає?'

            лайя "Провідник. Наставник."

            if відносини_лайя >= 3:
                #show лайя усміхнений2 at right2
                лайя "Чесно кажучи, я не люблю цей бюрократичний пафос. Будь ласка, називай мене просто Лайя."

                show павка усміхнена at left2 with dissolve
                define лайя = Character("Лайя", color = "ff0a54" )
                павка "Добре, Лайя."

            лайя "В мене до тебе теж є питання."

            #show лайя усміхнений2 at right2
            лайя "Мелодія, яку ти наспівала. Вона мені сподобалась. Як вона називається?"

            show павка здивована at left2 with dissolve
            "{i}Я навіть не здогадувалась, що мелодіям можна давати імена!"

            menu:
                "Коли зелінь ожива":
                    павка "{i}Коли зелінь ожива."

                "Там, поза атмосферою":
                    павка "{i}Там, поза атмосферою."

                "Душа вітру":
                    павка "{i}Душа вітру."

            show павка нейтральна at left2 with dissolve
            #show лайя усміхнений2 at right2
            лайя "Дякую, що поділилася."

            лайя "І дякую тобі за твою довіру."

            #show лайя нейтральний at right2
            лайя "Бувай."

            show павка усміхнена at left2 with dissolve
            павка "Слава заснов..."

            show павка роздратована at left2 with dissolve
            #show лайя злий at right2
            "{i}Стоп... Дурна звичка."

            show павка весела at left2 with dissolve
            павка "Бувай."

            #show лайя нейтральний at right2
            stop music fadeout 3
            scene фон with dissolve
            "{i}..."

            jump scene_four

    define лайя = Character("Куратор Лайя", color = "ff0a54" )
    show павка нейтральна at left2 with dissolve
    show лайя нейтральний2 at right2 with dissolve
    лайя "Зараз не час для сумнівів. Ти зробиш те, що я скажу, а натомість отримаєш те, чого так палко бажаєш."

    show лайя рішучий2 at right2 with dissolve
    лайя "Свободу від Купола."

    лайя "Свободу від годіуму."

    лайя "Музику."

    show павка здивована at left2 with dissolve
    павка "Ти знаєш про музику?"

    show лайя нейтральний2 at right2 with dissolve
    лайя "Я знаю достатньо, щоб розуміти, чому за можливість її творити варто ризикнути всім, що в тебе є."

    лайя "Мій статус дає мені доступ до інформації, яку приховують від людей. Ти не уявляєш собі, наскільки далеко сягає брехня Оази."

    show павка задумлива at left2 with dissolve
    "{i}Може він розповість щось про музику Давніх?"

    show лайя усміхнений2 at right2 with dissolve
    лайя "За межами Купола існує світ, Павко. Світ без годіуму і тиранії Оази. Де можна створювати що завгодно, і не боятися переслідувань."

    menu:
        "Розкажи ще":
            $відносини_лайя += 1
            $покора_лайі += 1
            show лайя рішучий2 at right2 with dissolve
            show павка здивована at left2 with dissolve
            лайя "Я міг би розповісти тобі про Вічнозелене місто. Про стародавні манускріпти, що розмовляють музикою. Про Гори, що чекають на пісню Шукача, про Великий Плач і про Вежу Думок."

            show павка здивована at left2 with dissolve
            "{i}Звучить просто неймовірно! Може справді буде нагода поговорити про все це?"

            show лайя нейтральний2 at right2 with dissolve
            лайя "Але все це не на часі. Можливо, колись у нас ще буде можливість поговорити."

            show павка замріяна at left2 with dissolve
            павка "А ти вмієш інтригувати! То яке у тебе для мене завдання?"

        "Я знала! Знала!!" :
            $відносини_лайя += 1
            show павка весела at left2 with dissolve
            павка "Я так і думала!"

            павка "Адже там немає годіуму і ніхто не забороняє створювати пісні!"

            show лайя усміхнений2 at right2 with dissolve
            лайя "Ти розумніша, ніж здається. Це добре. Але ти навіть не уявляєш, про що говориш. Я теж не уявляв, доки не побачив на власні очі."

            show павка замріяна at left2 with dissolve
            "{i}Він мене інтригує. Здається, ми трохи схожі."

            show павка рішуча at left2 with dissolve
            павка "Так що ти хочеш, щоб я зробила? Я маю на увазі, що треба від мене вашій організації?"

        "Пфф. Спроба вразити detected":
            $відносини_лайя -= 1
            $покора_лайі -= 1
            show павка роздратована at left2 with dissolve
            павка "Я і так це знаю! Сподіваюсь, ти не говориш це тільки для того, щоб вразити мене?"

            show лайя рішучий2 at right2 with dissolve
            лайя "Ти нічого не знаєш, Павко. Світ за межами Купола більший, ніж ти можеш уявити. Втім, згодом ти і сама все побачиш."

            show павка задумлива at left2 with dissolve
            "{i}Він постійно повторює, що я нічого не знаю і явно хоче справити враження. Треба обережніше з цим типом."

            show павка рішуча at left2 with dissolve
            павка "Так, скоро я сама все це побачу. То що я маю зробити, щоб ти допоміг мені вибратися з Купола?"

    show лайя нейтральний2 at right2 with dissolve
    лайя "Що ж, спершу ти повинна зібрати для мене інформацію."

    лайя "Ми збираємо дані про споживачів годіуму."

    menu:
        "Поцікавитися, навіщо це їм":
            $покора_лайі -= 1
            show павка задумлива at left2 with dissolve
            павка "Навіщо це вам? Якщо це не черговий страшний секрет."

            show лайя злий2 at right2 with dissolve
            лайя "Я не можу тобі цього сказати."

        "Не сувати свого носа в чужі справи":
            $покора_лайі += 1

    show лайя нейтральний2 at right2 with dissolve
    лайя "Сьогодні ти вийдеш на роботу як завжди. В місті чимало автоматів з годіумом, і деякі з них час від часу ламаються. Ви будете відповідати на виклики і приїжджати ремонтувати автомати, як завжди."

    show павка задумлива at left2 with dissolve
    "{i}Ага, сьогодні якраз багато роботи."

    лайя "Але сьогодні, як ти знаєш, не звичайний день. Замість свого стандартного діагностичного приладу ти будеш використовувати той, що знайдеш під місцем, на якому зараз сидиш."

    menu:
        "Пошарити рукою під сидінням":
            play sound "audio/Сцена 3/Шурхіт.mp3"
            show павка здивована at left2 with dissolve
            "{i}Ой, до лави справді щось приліплено!"

    stop sound
    "{i}Виглядає так само, як мій прилад для діагностики. Цікаво, звідки в них такий точний дублікат?"

    show павка нейтральна at left2 with dissolve
    лайя "Як ти знаєш, кожен автомат обладнаний блоком для збору і обробки даних. Він знаходиться на основній платі, за центральним процесором."

    лайя "Ти приєднаєшся до нього за допомогою цього приладу й ініціюєш протокол діагностики. Після того, як процедура буде завершена, ти дістанеш прилад і закриєш кришку автомата."

    show павка задумлива at left2 with dissolve
    павка "І це все?"

    show лайя усміхнений2 at right2 with dissolve
    лайя "Не так вже й складно, правда? Після завершення робочого дня ти знищиш цей прилад у дезинтеграторі і вирушиш на вулицю Чисту, будинок 2."

    show лайя нейтральний2 at right2 with dissolve
    лайя "Там, біля рекламного білборду на тебе чекатиме людина в капелюсі. Вона передасть тобі посвідчення технічного співробітника наукової експедиції."

    лайя "Захопи вдома теплий одяг і вирушай з цим посвідченням до південно-східної брами. Там, біля пункту пропуску, ти знайдеш групу вчених."

    лайя "Серед них буду і я. Підійди до мене і скажи, що ти моя нова асистентка. Разом ми вийдемо за межі Купола і ти будеш вільна."

    лайя "Запам'ятала?"

    show павка рішуча at left2 with dissolve
    павка "Так, кураторе Лайо."

    show лайя усміхнений2 at right2 with dissolve
    лайя "Добре. Є питання?"

    menu:
        "Що я скажу Інкі?":
            show павка розгублена at left2 with dissolve
            павка "Що я скажу своїй напарниці?"

            лайя "Не кажи їй нічого — ні про мене, ні про свою місію. Якщо буде задавати питання — вигадай щось. Я знаю, що ти вважаєш її своєю подругою, але в нас немає підстав їй довіряти."

            menu:
                "Вона мені не подруга":
                    $покора_лайі += 1
                    show павка роздратована at left2 with dissolve
                    павка "Вона мені не подруга, ми просто працюємо разом."

                    лайя "Тим краще. Сподіваюсь, ти розумієш, що залишити нашу розмову в таємниці — в твоїх інтересах."

                "Я не вмію брехати!":
                    show павка розгублена at left2 with dissolve
                    павка "А що, як вона здогадається? В мене все на обличчі написано, я не зможу це приховати!"

                    show лайя рішучий2 at right2 with dissolve
                    лайя "Ти так довго успішно приховувала від усіх свою таємницю, і сьогодні теж впораєшся. Інакше ти наразиш себе на таку небезпеку, що навіть я не зможу тебе захистити."

        "Що, як мене побачить перевіряючі?":
            show павка розгублена at left2 with dissolve
            павка "Що, як мене побачить перевіряючі?"

            лайя "І що? Ти технік-ремонтник, виконуєш свою роботу. Хіба це протизаконно?"

        "А це точно безпечно?":
            $покора_лайі -= 1
            show павка розгублена at left2 with dissolve
            павка "А це точно безпечно? На мене не почнеться полювання, чи ще щось?"

            show лайя рішучий2 at right2 with dissolve
            лайя "Ти вже наразила себе на небезпеку тим, що прийшла на зустріч зі мною. Але хіба цей ризик не вартий того, щоб нарешті звільнитися від тиранії Оази?"

            show павка рішуча at left2 with dissolve
            павка "Так, але... Ти не відповів на запитання."

            show лайя нейтральний2 at right2 with dissolve
            лайя "Це безпечно. Як я і сказав, ми просто збираємо інформацію. Все пройде плавно, якщо ти будеш вести себе розумно і не втрачатимеш пильності. Більшого гарантувати тобі я не мож."

    show павка нейтральна at left2 with dissolve
    show лайя нейтральний2 at right2 with dissolve
    павка "В мене є ще одне питання."

    show лайя здивований2 at right2 with dissolve
    лайя "Так?"

    show павка задумлива at left2 with dissolve
    павка '"Куратор". Слово наче знайоме, але воно застаріле. Що воно означає?'

    show лайя нейтральний2 at right2 with dissolve
    лайя "Провідник. Наставник."

    if відносини_лайя >= 3:
        show лайя усміхнений2 at right2 with dissolve
        лайя "Чесно кажучи, не люблю я весь цей бюрократичний пафос. Будь ласка, звертайся до мене просто Лайя."

        define лайя = Character("Лайя", color = "ff0a54" )
        show павка усміхнена at left2 with dissolve
        павка "Добре, Лайя."

    лайя "В мене до тебе теж є питання."

    show лайя усміхнений2 at right2 with dissolve
    лайя "Мелодія, яку ти наспівувала. Вона мені сподобалась. Як вона називається?"

    show павка здивована at left2 with dissolve
    "{i}Я навіть не здогадувалася, що мелодіям можна давати імена!"

    menu:
        "Коли зелень оживає":
            show павка усміхнена at left2 with dissolve
            павка "{i}Коли зелень оживає."

        "Поза атмосферою планети":
            show павка усміхнена at left2 with dissolve
            павка "{i}Поза атмосферою планети."

        "Душа вітру":
            show павка усміхнена at left2 with dissolve
            павка "{i}Душа вітру."

    show лайя усміхнений2 at right2 with dissolve
    лайя "Дякую, що поділилася."

    лайя "І дякую тобі за твою довіру."

    show лайя нейтральний2 at right2 with dissolve
    лайя "Бувай."

    show павка рішуча at left2 with dissolve
    павка "Слава заснов..."

    show павка роздратована at left2 with dissolve
    "{i}Стоп... Дурна звичка."

    show павка весела at left2 with dissolve
    павка "Бувай."

    show лайя нейтральний2 at right2 with dissolve
    stop music fadeout 3
    scene фон with dissolve
    "{i}..."

    jump scene_four
