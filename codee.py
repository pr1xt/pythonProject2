
for x in range(1, 11):
    print('{0:2d}{1:4d}{2:5d}'.format(x, x*x, x*x*x)) # d - это типо отступ
print("", end=" 2323 ")
print("never gonna give u up")
d=(input("КАК там с деньгами?"))
f = open('C:\Programming\pythonProject2\\filed.txt', 'r', encoding="utf-8")#Открыть+читать
m = open('C:\Programming\pythonProject2\\Wfiled.txt', 'w', encoding="utf-8")#создать+открыть
m.write("")# запись в файл
print(f.read())
### 100 РАЗ ПИШЕМ 11 01  В ОДИН ФАЙЛ

for x in range(1, 101):
    m = open('C:\Programming\pythonProject2\\Wfiled.txt', 'a', encoding="utf-8")  # создать+открыть
    m.writelines("  "+d+"\n")
print(d)