#1.create a function getting two input from user & print the following

def csk(f,s):
    print("first number is:",f,"\nsecond number is:",s,"\n")
# adding two number:
    value = f+s
    print("addition of two numbers is :",value,"\n")
#substracting two numbers:
    value = f-s
    print("substraction of two numbers is :", value,"\n")
#dividing two numbers :
    value = f/s
    print("division of two numbers is :", value,"\n")
#multiplying two numbers:
    value = f*s
    print("multiplication of two numbers is :", value,"\n")

f =int(input("enter input 1 here:\n"))
s = int(input("enter input 2 here:\n"))
csk(f,s)



#2. create following covid() & it should accept patient name,and body temperature,by default the body temperature should be 98 degree
def covid(q,w):
    print("patient name is :",q,"\tbody temperature:",w)

q = input("enter patients name:\n")
m = input("enter temperature :")
if m.isalpha() == True:
    w = 98
else:
    w = m
covid(q,w)
