import sys
datalist = list(map(int,input("Load your grades ").split(" ")))
for x in range(0,len(datalist)):
    if  int(datalist[x])>10:
        print("ERROR try again")
        sys.exit()
print("Your normalised grades is: ",end="")
print(datalist)
sum_datalist = list(map(int, datalist))
print("Your average grade is: ",end="")
print(sum(sum_datalist)/len(sum_datalist))
