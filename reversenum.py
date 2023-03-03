from turtle import*
bgcolor('black')
pencolor('pink')
width(20)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
    forward(250)
    circle(34,90)


penup()
goto(85,30)
pendown()
circle(80,360)
penup()
goto(110,130)
pendown()
circle(7,360)
def reverce():
    num = eval(input("Enter number:"))
    lst = []
    for i in iter(str(num)):
        lst.append(i)
    lst.reverse()
    str1 = ""
    for i in lst:
        str1 = str1 + i
    print(str1)


# reverce()
num = 123
num5 = (str(num)[::-1])
num = 321
nnum = 0
while num != 0:
    digit = num % 10
    nnum = nnum * 10 + digit
    num //= 10
print(nnum)


def avg():
    n = 5
    l = []
    for i in range(n):
        ele = eval(input("enter num:"))
        l.append(ele)
    print(sum(l) / 2)


# avg()

def fibo():
    num = eval(input("Enter number:"))
    num1 = 0
    num2 = 1
    while num > 0:
        print(num1, end=",")
        result = num1 + num2
        num1 = num2
        num2 = result
        num = num - 1


# fibo()

def fact(x):
    x = x - 1
    if x == 1:
        return 1
    else:
        return (x * fact(x - 1))


# fact(5)

def perfectsum():
    n = eval(input("enter length of list"))
    lst = []
    target = eval(input("enter target value:"))
    for i in range(n):
        lst.append(eval(input("enter list elements:")))
    # r=[x for power]


# perfectsum()

def pattern1():
    n = 5
    for i in range(n):
        print("* ", end="")
    s = 1
    print()
    for j in range(s):
        print("* ", end="")
        for k in range(3):
            print("  ", end="")
        print("*")
    for i in range(n):
        print("* ", end="")


# pattern1()

def pattern2():
    s = 6
    while s > 0:
        n = s
        while n > 0:
            print("*", end="")
            n = n - 1
        print()
        s = s - 1


# pattern2()

def pattern3():
    n = 6
    for i in range(n):
        print("* ", end="")
    print()
    for i in range(n):
        j = n - 1
        for k in range(j):
            if (i == 0):
                print("*")


# pattern3()
def pattern4():
    num = 6
    for i in range(num):
        if i == 0:
            print(" " * (num - i) + "*")
        elif i == num - 1:
            print(" " * (num - i) + "* " * num)
        else:
            print()
            # print(" "*(num-i)"* " "*[i-1]"+ "*")


# pattern4()

def pattern5():
    n = 5
    arr = range(1, n + 1)
    arr_str = list(map(str, arr))
    for i in range(n):
        print(" ".join(arr_str[:i + 1]))


#pattern5()

def pattern6():
    n = 5
    arr = range(1, n + 1)
    arr_str = list(map(str, arr))
    for i in range(n,0,-1):
        print(" ".join(arr_str[:i]))
#pattern6()

def pattern7():
    n = 5
    for i in range(1,n+1):
        if i==1:
            print("1 ")
        elif i==n:
            print(""*list(range(1,n+1)))
        else:
            print("1 "+ " "*(i-2) + str(i))
#pattern7()

#n = 5
def arr_str(arr):

    arr_str = map(str, arr)
    return " ".join(arr_str)

#for i in range(1,n+1):
    temp=range(i,i+1)
    print(" "*(n-i)+arr_str(temp) +" "+arr_str(reversed(temp[:-1])))

def secondmax():
    lst=[10,12,8,7,2,20,40]
    s=len(lst)
    temp=0
    for i in range(s):
        j=i+1
        for j in range(s):
            if lst[i]>lst[j]:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
    print(lst[1])
secondmax()

def chchange(st):
    s=len(st)
    n=s//2
    r=st[::-1]
    new=""
    for i in range(n):
        new=new+st[i]
        new=new+r[i]
    for i in range(len(st)):
        if st[i]not in (new):
            new=new+st[i]

    print(new)

#chchange("slftw")
#chchange("ABCDEFG")

def numberpattern(a,b,c):
    num=(a*100)+(b*10)+c
    patt=num*10+b
    for i in range(b):
        print(num,end="")
        c=c+1
        for i in range(c-1):
            print(patt,end="")
        print(num,end="")
    print("2",end="")

numberpattern(2,3,3)