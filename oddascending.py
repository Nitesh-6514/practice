def oddascending():
    n=int(input())
    l=[int(n) for n in input().split()]
    print(l)
    indexs=[]
    odd=[]
    for i in range(n):
        if l[i]%2!=0:
            e=l[i]
            odd.append(e)
            indexs.append(i)
    odd.sort()
    for i in range(len(indexs)):
        r=indexs[i]
        l[r]=odd[i]
    print(l)
#oddascending()

def accept():
    n=int(input())
    l=[int(n) for n in input().split()]
    print(l)
#accept()

def result():
    print("Enter follwoing valuse:")
    ppt=float(input("Planned Production Time:"))
    tdt=float(input("Total Down Time:"))
    tp=float(input("Total Products:"))
    fp=float(input("Faulty Product:"))
    ict=float(input("Ideal Cycle Time:"))

    R=ppt-tdt
    print("Run time=",R)
    P=(ict*tp)/R
    print("Performance(P)=",P)
    A=R/ppt
    print("Availability(A)=",A)
    Q=(tp-fp)/tp
    print("Quality(Q)=",Q)
    OE=A*P*Q
    print("Overall Equipment Effectiveness=",OE)
    A=81
    if A<80:
        print("i) Reduce time required for material handling \n ii) Reduce Delay")
    else:
        print("Availability is good")
    if P<80:
        print("Reduce time required to clean the workstation and scrap removing")
    else:
        print("Performance is good")
    if Q<80:
        print("i) Reduce the count of faults product\nii)Try to match color changing")
    else:
        print("Quality is good")

result()

