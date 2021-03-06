﻿#Тест взят отсюда: https://zen.yandex.ru/media/duhovnya_zaryadka/test-na-tip-myshleniia-uznaite-svoi-sklad-uma-5ad9fb35fd96b16ef1253a28
#Записываем данные:
questions = [['Мне легче сделать что-либо самому, чем объяснять это другим людям. ','ПДМ'],
             ['Знакомый или близкий мне запах, вызывает у меня воспоминания о прошлых событиях. ','НОМ'],
             ['Я люблю читать книги. ','СЛМ'],
             ['Различные хобби и увлечения делают жизнь людей насыщенней и ярче. ','КМ'],
             ['Я с большим интересом составлял бы компьютерные программы. ','АСМ'],
             ['Я стараюсь сделать лучше даже идеально выполненную работу. ', 'КМ'],
             ['Известные мне звуки или мелодии вызывают у меня различные воспоминания. ','НОМ'],
             ['Мне нравится работа журналиста, ведущего, комментатора. ','СЛМ'],
             ['Я люблю играть в логические игры (шахматы, шашки и т.д.). ', 'АСМ'],
             ['Я быстро схватываю если мне объясняют на предметах или рисунках. ', 'ПДМ']]
#Утверждения и соответсвующие им типы мышления
answers = [] #Список для записи типов мышления, соответствующих вопросам с утв. ответом
types = [] #Типы мышления, присутсвующие у тестирующегося
#Выбираются аббр. которых набралось больше всего (соотв. планке) во время опроса
ToT = ['ПДМ', 'НОМ', 'СЛМ', 'КМ', 'АСМ'] #Просто список аббревиатур т. м.
DoT = {
    'ПДМ': """ПДМ или Предметно-действенное мышление.
Люди с таким типом хорошо скоординированы.
Они усваивают полученную информацию через движения.
Их золотыми руками создан весь окружающий нас мир!
Без них нереально осуществить самую блестящую идею.""",
    'НОМ': """НОМ или Наглядно-образное мышление.
Данным типом обладают люди, с творческим складом ума.
Они созданы, что бы творить!
Музыканты, актеры, поэты, художники, архитекторы, продюсеры, режиссеры должны отличаться от других превосходным наглядно-образным мышлением.
Если по результатам теста у вас преобладает именно этот тип, то наверняка вы имеете творческие задатки.
Развивайте их, если еще не начали!""",
    'СЛМ': """СЛМ или Словесно-логическое мышление.
Люди с таким типом имеют хорошо подвязанный язык.
Они доходчиво могут обосновать свою точку зрения или объяснить что-либо.
Если по результатам теста у вас преобладает данное мышление, то вы - прирожденный оратор!""",
    'КМ': """КМ или Креативное мышление.
Возможно вы замечали за собой, что умеете нестандартно мыслить и смотреть на банальные вещи под другим углом.
Это незаменимое и очень важное качество в жизни каждого человека.
Люди с таким мышлением часто производят фурор среди окружающих.""",
    'АСМ': """АСМ или Абстрактно-символическое мышление.
Данный тип описывает людей, которые любят точные науки, такие как физика, математика, аналитика, экономика и др.
Если по результатам теста у вас преобладает АСМ, то вы имеете феноменальные способности для открытий в любых областях!""",
    } #Словарь с описаниями т. м.

print("""Привет! Этот тест поможет тебе определить твой тип мышления.
Он состоит из 10 утверждений на которые ты должен отвечать:
\"+\" - если согласен
и \"-\" - соответсвенно если не согласен.
Ответы типа \"Да/Нет\", \"Yes/No\", \"0/1\" принимаются, но с учётом регистра!
(То есть важно написать: \"Да\", а не \"да\").
Давай начнём! Жми \"Enter\"\n""") #Приветсвие
input()
for quest in questions:
    #Цикл опроса:
    ans= str(input(quest[0])) #Считываем ответ, выдавая утверждение
    print('\n')
    if ((ans == '+') or (ans == '1') or (ans == 'Yes') or (ans == 'Да')):
        answers.append(quest[1]) #Если утв. добавляем в спиок ответов нужную аббревиатуру
    elif ((ans == '-') or (ans == '0') or (ans == 'No') or (ans == 'Нет')):
        continue #И пропускаем, если не утв.
    else:
        print('Ошибка ответ некорректный! Перезапустите тест!')
        input()
        exit(1) #В случае некорректного ответа, выёживаемся
print('\n')
plank = answers.count('ПДМ') #Задаём начальную планку
types.append('ПДМ') #Задаём начальный тип мышления
for key in answers:
    #Обрабатываем ответы:
    #Ищем каких аббревиатур больше, добавляем их в types
    keycount = answers.count(key)
    if (keycount > plank):
        plank = keycount
        types.clear()
        types.append(key)
    elif ((keycount == plank) and not(key in types)):
        types.append(key)
    else:
        continue

if (len(types) > 1):
    print("У вас сразу несколько типов мышления сочетаются в одной голове! Такое мышление называют синтетическим.") #Сообщаем тестируемому о том, что он особенный
for t in types:
    print(DoT[t]) #Выдаём описания
    print('\n')
#Конец!
input()
