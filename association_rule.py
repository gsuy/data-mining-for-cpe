import random
import matplotlib.pyplot as plt
import numpy

def Random_transaction():
    rand = []
    for i in range(1000):
        if i <= 799:
            randint = random.randrange(2,6) #สุ่ม สินค้าที่ซื้อ ตั้งแต่ 2-5  item ในแต่ละ transaction
            temp = []
            for ii in range(randint):
                temp.append(item[random.randrange(0,50)]) #สุ่มสินค้าจาก 50 item
            rand.append(temp)
        elif i > 799:
            randint = random.randrange(6,9) #สุ่ม สินค้าที่ซื้อ ตั้งแต่ 6-8  item ในแต่ละ transaction
            temp = []
            for ii in range(randint):
                temp.append(item[random.randrange(0,50)]) #สุ่มสินค้าจาก 50 item
            rand.append(temp)
    return rand

def CheckArraySize2(a,b):
    anwser = 0
    a0 = 0    
    a1 = 0
    for i in b:
        if a[0] == i:
            a0 = a0 + 1
        if a[1] == i:
            a1 = a1 + 1
    if a0 > 0 and a1 > 0:
        anwser = 1
    return anwser

def CheckArraySize3(a,b):
    anwser = 0
    a0 = 0    
    a1 = 0
    a2 = 0
    for i in b:
        if a[0] == i:
            a0 = a0 + 1
        if a[1] == i:
            a1 = a1 + 1
        if a[2] == i:
            a2 = a2 + 1
    if a0 > 0 and a1 > 0 and a2 > 0:
        anwser = 1
    return anwser

def CheckForJoin(a,b):
    ret = 0
    for i in a:
        for ii in b:
            if i == ii:
                ret = 1
    return ret

def merge(aa,bb):
    a = aa.copy()
    b = bb.copy()
    a.sort()
    b.sort()
    arr = []
    while a != [] or b != []:
        if a == [] and b != []:
                arr.extend(b)
                b = []
        elif b == [] and a != []:
                arr.extend(a)
                a = []
        elif a[0] == b[0]:
            arr.append(a[0])
            a.pop(0)
            b.pop(0)
        elif a[0] < b[0]:
            arr.append(a[0])
            a.pop(0)
            
        elif a[0] > b[0]:
            arr.append(b[0])
            b.pop(0)
    return arr

def findProb(arr,data):
    copy = arr.copy();
    part = []
    part0 = arr.copy();
    part0.pop(0)
    part1 = arr.copy();
    part1.pop(1)
    part2 = arr.copy();
    part2.pop(2)
    part.append(part0)
    part.append(part1)
    part.append(part2)
    ans = []
    temp = []
    count3 = countProb(arr,3,data)
    for i in range(3):
        temp.append("[" + str(arr[i]) + "]" + " -> " + str(part[i]))
        temp.append(count3/countProb(arr[i],1,data))
        ans.append(temp)
        temp = []
        temp.append(str(part[i]) + " -> " +"[" + str(arr[i])+ "]")
        temp.append(count3/countProb(part[i],2,data))
        ans.append(temp)
        temp = []
    return ans
    
def countProb(arr,n,data):

    count = 0
    if n == 1:
        for i in data:
            for ii in i:
                if arr == ii:
                    count = count + 1
                    break
    elif n == 2:
        for ii in range(len(data)):
            count = count + CheckArraySize2(arr,data[ii])

    elif n == 3:
        for iii in range(len(data)):
            count = count + CheckArraySize3(arr,data[iii])

    return count

#-----------------------------------------------------------------------

min_sup = 12
item = [] #ข้อมูลสินค้าจำนวน 50 ชนิด
for i in range(50):
    item.append(i+1)

dataset = Random_transaction() #สร้างข้อมูลขึ้นมา
# print("Dataset: ",dataset)

C1 = [0]*50
for i in dataset: #นับจำนวนสินค้าที่ซื้อไป L1
    for ii in i:
        C1[ii-1] = C1[ii-1] + 1
# print("C1: ",C1)

L1 = item #สร้างมาเก็บตัวที่ผ่าน min_sup
for i in range(len(C1)): #ตรวจว่าผ่าน min_sup หรือไม่
    if C1[i] < min_sup:
        C1[i] = 0
        L1.remove(i+1) #item รอบ L1 ที่ผ่าน min_sup

print("C1: ",C1)
print("L1: ",L1)
print("---------------------------------------------------------------")

#---------------------------------------------------------------------

L2 = []
for i in range(len(L1)): #ทำการ join L1 ตัวเข้าด้วยกัน
    for ii in range(len(L1)):
        temp = []
        temp.append(L1[i])
        if ii > i:
            temp.append(L1[ii])
            L2.append(temp)

C2 = [0]*len(L2)

for i in range(len(L2)): #นับ L2
    for ii in dataset:
        C2[i] = C2[i] + CheckArraySize2(L2[i],ii)

Out = [] #สร้างมาเก็บค่าที่ไม่ผ่าน min_sup ของ L2 เพื่อไว้ไปกรอง L3
for i in range(len(C2)): #ตรวจว่าผ่าน min_sup หรือไม่
    if C2[i] < min_sup:
        Out.append(L2[i])
        C2[i] = 0
        L2[i] = 0 

for i in range(L2.count(0)):
    C2.remove(0) #count_item รอบ L2 ที่ผ่าน min_sup
    L2.remove(0) #item รอบ L2 ที่ผ่าน min_sup

print("L2: ",L2)
print("C2: ",C2)
print("---------------------------------------------------------------")

#---------------------------------------------------------------------

L3 = []
for i in range(len(L2)): #ทำการ L2 ตัวเข้าด้วยกัน
    for ii in range(len(L2)):
        if ii > i and CheckForJoin(L2[i],L2[ii]) == 1:
            L3.append(merge(L2[i],L2[ii]))

for i in range(len(L3)): #เปลี่ยนตัวซ้ำเป็น 0
    for ii in range(len(L3)):
        if i != ii and L3[i] == L3[ii]:
            L3[ii] = 0

for i in range(L3.count(0)): #ลบตัวซ้ำออก
    L3.remove(0)

for i in range(len(Out)): #กรองตัวที่ไม่ผ่าน min_sup โดยใช้ out ที่เก็บไว้
    for ii in L3:
        if CheckArraySize2(Out[i],ii):
            L3.remove(ii)

print("L3: ",L3)

C3 = [0]*len(L3)

for i in range(len(L3)): #นับ ที่ join แล้ว ที่มีขนาด 3
    for ii in dataset:
        C3[i] = C3[i] + CheckArraySize2(L3[i],ii)

print("C3: ",C3)
print("*หมายเหตุ L1,L2,L3 คือสิ่งที่เก็บชื่อของ item,C1,C2,C3 คือสิ่งที่เก็บจำนวนที่ซื้อ item นั้นๆ",
"ซึ่งลำดับใน array ของ C1,C2,C3 จะตรงกับลำดับ item ใน L1,L2,L3")
print("---------------------------------------------------------------")

#---------------------------------------------------------------------
#หา min_conf
Final = []
print("min_conf : ")
for i in L3:
    Final.extend(findProb(i,dataset))

for i in Final:
    print(i)

print("---------------------------------------------------------------")

#---------------------------------------------------------------------
