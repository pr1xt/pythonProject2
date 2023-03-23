num = list(input().split())
i = 0

num = "".join(num)
num = list(num)

for x in range(len(num)):
    if num[x] == "+":
        num[x] = "0.1"
    if num[x] == "-":
        num[x] = "-0.1"
    if num[x] == "*":
        num[x] = "0.2"
    if num[x] == "/":
        num[x] = "-0.2"

while True:
    if i == len(num) - 1:
        break
    if float(num[i]) >= 1 and float(num[i+1]) >= 1:
        num[i] = num[i] + num[i+1]
        num.pop(i+1)
        i -= 1
    i += 1
#print(num)
i = 0

while True:
    if i == len(num):
        break
    if num[i] == "0.1":
        num[i-1] = int(int(num[i-1]) + int(num[i+1]))
        num.pop(i)
        num.pop(i)
        i -= 1
    if num[i] == "-0.1":
        num[i-1] = int(int(num[i-1]) - int(num[i+1]))
        num.pop(i)
        num.pop(i)
        i -= 1
    if num[i] == "0.2":
        num[i-1] = int(int(num[i-1]) * int(num[i+1]))
        num.pop(i)
        num.pop(i)
        i -= 1
    if num[i] == "-0.2":
        num[i-1] = int(int(num[i-1]) / int(num[i+1]))
        num.pop(i)
        num.pop(i)
        i -= 1
    i += 1

print(*num)
