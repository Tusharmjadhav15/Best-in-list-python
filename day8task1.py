#1----------------------------------------------------------------------------------------------------------------------
#program to merge to dictionaries


def Merge(dict1,dict2):
    s = {** dict1,** dict2}
    return s


dict1={"tushar":84,"akshay":56,"rahul":69,"rudra":87,"manish":90}
dict2 = {"rakesh":45,"vishal":81,"rohit":23,"punit":54}
dict5 = Merge(dict1,dict2)
print(dict5)

#2-----------------------------------------------x---------------------------------------------------------------------
#program to sort value from decending to asending and convert it into set


lst = ["ashish","nayan","mayank","george","tushar"]
lst.sort(reverse=True)
print("sorted list from descending to ascending:\n",lst)
k = set(lst)
print("converting list into set:\n",k)


#3---------------------------------------------------------------------------------------------------------------------
#program to list no of item in dictionary and sort it with and without using function

y =[]
unsorted_list=[]
sorted_list=[]
d = {'shape':[1,2,4,5,6,8,9],'base': 65,"cube":68,"diameter":[4,5,7,8,0,9,2,1,]}
for i in d.keys():
    y.append(i)
    unsorted_list.append(i)
y.sort()          # by using inbuilt sort function
print("using function\n",y)

# sorting list without using function
while unsorted_list:
    minimum = unsorted_list[0]
    for j in unsorted_list:
        if j < minimum:
            minimum = j
    sorted_list.append(minimum)
    unsorted_list.remove(minimum)

print(sorted_list)

#4------------------------------------x--------------------------------------------------------------------------------
# program to take string as input and
# change the first occurence with user input


inp = input("enter string here:\n")
rpl = input("enter the character that has to be change with first word:\n")
new_str = inp.replace(inp[0], rpl ,1)
print(new_str)


#5----------------------------x-----------------------------------------------x------------------------------------------
# program to take string as input and
# change all the occurence  of the first character with the user input


input_123456 = input("enter string here:\n")
rpg_123456 = input("enter the character that has to be replaced with first character:\n")
new_sword = input_123456.replace(input_123456[0], rpg_123456 )
print(new_sword)

#6------------------------------------------x-----------------------------x---------------------------------------------
#program to find the repeated elements in list

a_sh = ["a","c","s","f","r","s","c","h","a","b","g","h"]
b_sh = []
c_sh = []
for i in a_sh:
    if i not in b_sh:
        b_sh.append(i)
    elif i not in c_sh:
        c_sh.append(i)
    else:
        None
print("the repeated charaters are:", c_sh )


#7-------------------------x-------------------------------------------------------------x------------------------------
# program to sum three values and divide it by value given by user


a =  65
b = 265
c = 354
sum = a+c+b
ins= int(input("enter number here to divide the sum:\n"))
print("question no.7 output:\n",sum/ins)

#8-----------------------------x------------------------------------------------------------x---------------------------
#program to find mean ,median,mode
#mean

lst_1=[2,3,3]                                                   # three given numbers
lst2 = lst_1
addi = 0
for q in lst_1:
    addi = addi +q
#print("addition",addi)
lenngth = len(lst_1)
mean = addi /lenngth
print("mean:",mean)


#median
lst2.sort()
n = len(lst2)
if n % 2 ==0:
    median1 = lst2[n//2]
    median2 = lst2[n//2-1]
    median = (median1+median2)/2
else:
    median = lst2[n // 2]
print("median is:"  + str(median))


#mode
yia = lst_1
yia.sort()
l1=[]

i = 0
while i < len(yia):
    l1.append(yia.count(yia[i]))
    i += 1

dia1 = dict(zip(yia , l1))

dia2 = {k for (k,v) in dia1.items() if v== max(l1)}

print("Mode is/are:" + str(dia2))

#-----------------------------------------x-----------------------------------------------x-----------------------------
#program to swap cases of a given string


a_123 ,b_123 = "tushar","jadhav"
temp = a_123
a_123=b_123
b_123=temp
print(a_123,b_123)

#----------------------------------------x------------------------------------------------x----------------------------
#program to convert decimal into binary and octal number system


dec = 124
print("the decimal value of " , dec, "is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")


