for x in range(1, 11):
    print('{0:2d}{1:4d}{2:5d}'.format(x, x*x, x*x*x)) # d - это типо отступ
d=(input("Что записать в файл?"))
k = int(input("Сколько раз вписать?"))
#f = open('C:\Programming\pythonProject2\\filed.txt', 'r', encoding="utf-8")#Открыть+читать
m = open('C:\Programming\pythonProject2\\Wfiled.txt', 'w', encoding="utf-8")#создать+открыть
#m.write("")# запись в файл
#print(f.read()) - вывод в консоль содержимого файла файлед.тхт
### k РАЗ ПИШЕМ d  В ОДИН ФАЙЛ
for x in range(0, k):
    m = open('C:\Programming\pythonProject2\\Wfiled.txt', 'a', encoding="utf-8")  # создать+открыть
    m.writelines("  "+d+"\n")