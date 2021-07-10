x = tuple()
lst1 = (654,65,84,87,49,12,35,37,68)
lst2 = ("sd","sdf","frs","gtsf","gtds","sdc","awd","grs","ss")
x = zip(lst1,lst2)
#for y in x:
print(list(x))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
lst3 =[]
asd1 = ("sed","erfd","sefs","qwer","tyui","fghj","zxcv","vfrg")
for i in range(1,9):
    lst3.append(i)
#print(lst3,asd1)
qwe2 = zip(tuple(lst3),asd1)
print(list(qwe2))
#----------------------------------------------------------------------------------------------------------------------------------------------------------
y =[]
lst4 = [35,64,78,52,64,789,46,238,7]
y = sorted(lst4)
print(y)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def fun(variable):
    if variable%2 == 0:
        return False
    else:
        return True
dfg4 =[]
s = int(input("enter how many number you want to add:\n"))
for w in range(s):
    s5 = int(input("enter number:"))
    dfg4.append(s5)
print(dfg4)

f = filter(fun,dfg4)

print('The filtered odd numbers are:')
print(list(f))







































































































































