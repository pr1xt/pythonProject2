num = list(input().split())
i = 0

num = "".join(num)
num = list(num)

for x in range(len(num)):
    if num[x] == "+":
        num[x] = "-0.11"
    if num[x] == "-":
        num[x] = "-0.1"
    if num[x] == "*":
        num[x] = "-0.22"
    if num[x] == "/":
        num[x] = "-0.2"

while True:
    if i == len(num) - 1:
        break
    if num[i] == "." or num[i+1] == ".":
        i += 1
        continue
    if float(num[i]) >= 0 and float(num[i+1]) >= 0:
        num[i] = num[i] + num[i+1]
        num.pop(i+1)
        i -= 1
    i += 1
print(num)
i = 0

while True:
    if i == len(num):
        break
    if num[i] == "-0.11":
        num[i-1] = float(float(num[i-1]) + float(num[i+1]))
        num.pop(i)
        num.pop(i)
        i -= 1
    if num[i] == "-0.1":
        num[i-1] = float(float(num[i-1]) - float(num[i+1]))
        num.pop(i)
        num.pop(i)
        i -= 1
    if num[i] == "-0.22":
        num[i-1] = float(float(num[i-1]) * float(num[i+1]))
        num.pop(i)
        num.pop(i)
        i -= 1
    if num[i] == "-0.2":
        num[i-1] = float(float(num[i-1]) / float(num[i+1]))
        num.pop(i)
        num.pop(i)
        i -= 1
    i += 1

print(*num)