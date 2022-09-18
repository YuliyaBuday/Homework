# задача 36
age_person = int(input("Введите возраст человека:"))
if age_person > 0 and age_person <= 2:
    print("Возраст человека соответствует",age_person * 10.5, "годам жизни собаки")
elif age_person < 0:
    print("Возраст введен неправильно")
else:
    print("Возраст человека соответствует",2 * 10.5 + (age_person - 2) * 4, "годам жизни собаки")

# задача 39
name_month = str(input("Введите название месяца:"))
if name_month == "январь" or name_month == "март" or name_month == "май" or name_month == "июль" or name_month == "август" or name_month == "октябрь" or name_month == "декабрь":
    print("В указанном вами месяце 31 день")
elif name_month == "февраль":
    print("В указанном вами месяце может быть как 28, так и 29 дней")
else:
    print("В указанном вами месяце 30 дней")

# задача 49
month = int(input("Введите год вашего рождения:"))
if month == 2000 or (month - 2000) % 12 == 0:
    print("Дракон")
elif month == 2001 or (month - 2000) % 12 == 1:
    print("Змея")
elif month == 2002 or (month - 2000) % 12 == 2:
    print("Лошадь")
elif month == 2003 or (month - 2000) % 12 == 3:
    print("Коза")
elif month == 2004 or (month - 2000) % 12 == 4:
    print("Обезьяна")
elif month == 2005 or (month - 2000) % 12 == 5:
    print("Петух")
elif month == 2006 or (month - 2000) % 12 == 6:
    print("Собака")
elif month == 2007 or (month - 2000) % 12 == 7:
    print("Свинья")
elif month == 2008 or (month - 2000) % 12 == 8:
    print("Крыса")
elif month == 2009 or (month - 2000) % 12 == 9:
    print("Бык")
elif month == 2010 or (month - 2000) % 12 == 10:
    print("Тигр")
elif month == 2011 or (month - 2000) % 12 == 11:
    print("Кролик")
else:
    print("Неверный год рождения")


# задача 52
grade = str(input("Введите оценку:"))
if grade == "A+":
    print("Введенная буквенная оценка соответствует числовой оценке", 4.0)
elif grade == "A":
    print("Введенная буквенная оценка соответствует числовой оценке", 4.0)
elif grade == "A-":
    print("Введенная буквенная оценка соответствует числовой оценке", 3.7)
elif grade == "B+":
    print("Введенная буквенная оценка соответствует числовой оценке", 3.3)
elif grade == "B":
    print("Введенная буквенная оценка соответствует числовой оценке", 3.0)
elif grade == "B-":
    print("Введенная буквенная оценка соответствует числовой оценке", 2.7)
elif grade == "C+":
    print("Введенная буквенная оценка соответствует числовой оценке", 2.3)
elif grade == "C":
    print("Введенная буквенная оценка соответствует числовой оценке", 2.0)
elif grade == "C-":
    print("Введенная буквенная оценка соответствует числовой оценке", 1.7)
elif grade == "D+":
    print("Введенная буквенная оценка соответствует числовой оценке", 1.3)
elif grade == "D":
    print("Введенная буквенная оценка соответствует числовой оценке", 1.0)
elif grade == "F":
    print("Введенная буквенная оценка соответствует числовой оценке", 0)

else:
    print("Неверно введена оценка")

# задача 42
#часть 1
nota = str(input("Ваедите ноту:"))
if nota == "C4":
    print("Частота 261,63")
elif nota == "D4":
    print("Частота 293.66")
elif nota == "E4":
    print("Частота 329.63")
elif nota == "F4":
    print("Частота 349.23")
elif nota == "G4":
    print("Частота 392.00")
elif nota == "A4":
    print("Частота 440.00")
elif nota == "B4":
    print("Частота 493.88")
else:
    print("Ошибка")

# часть 2
octava = int(input("Введите номер октавы в научной нотации:"))
nota = str(input("Введите ноту:"))

if nota == "C":
    print("Частота", 261.63 / (2 ** (4 - octava)))
elif nota == "D":
    print("Частота", 293.66 / (2 ** (4 - octava)))
elif nota == "E":
    print("Частота", 329.63 / (2 ** (4 - octava)))
elif nota == "F":
    print("Частота", 349.23 / (2 ** (4 - octava)))
elif nota == "G3":
    print("Частота", 392.00 / (2 ** (4 - octava)))
elif nota == "A":
    print("Частота", 440.00 / (2 ** (4 - octava)))
elif nota == "B":
    print("Частота", 493.88 / (2 ** (4 - octava)))
else:
    print("Ошибка")

# задача 43
sound = float(input("Введите частоту:"))

if sound == 261.63 or sound >= 260.63 and sound <= 262.63:
    print("Соответствует ноте C4")
elif sound == 293.66 or sound >= 292.66 and sound <= 294.66:
    print("Соответствует ноте D4")
elif sound == 329.63 or sound >= 328.63 and sound <= 330.63:
    print("Соответствует ноте E4")
elif sound == 349.23 or sound >= 348.23 and sound <= 350.23:
    print("Соответствует ноте  F4")
elif sound == 392.00 or sound >= 391.00 and sound <= 393.00:
    print("Соответствует ноте  G4")
elif sound == 440.00 or sound >= 439.00 and sound <= 441.00:
    print("Соответствует ноте  A4")
elif sound == 493.88 or sound >= 492.88 and sound <= 494.88:
    print("Соответствует ноте  B4")
else:
    print("Ноты,соответствующей введенной частоте, не существует")

