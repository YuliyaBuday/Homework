import csv

file = open("Books.csv", "w")
line = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(line))
line = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(line))
line = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(line))
line = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(line))
line = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(line))

file.close()

file=open("Books.csv", "a") #открываем файл в режиме дозаписи, информация добавляется в конец файла
line= str(input("Введите данные: название книги, автор, год выпуска:"))#запрос на ввод инф от пользователя
file.write(str(line))#добавляем введенную пользователем информацию в конец файла
file.close()

with open('Books.csv') as f:# выводим информацию с файла, с новой строки все
    reader = csv.reader(f)
    for row in reader:
        print(row)
