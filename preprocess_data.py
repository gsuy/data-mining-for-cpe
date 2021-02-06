#from openpyxl import Workbook
import openpyxl
File = openpyxl.load_workbook('Data.xlsx')
sheet = File.active
#sheet['A2'] = "sucess"
#File.save('Data.xlsx')
def normalization(s):
    colum = sheet[s]
    max_ = 0
    min_ = 999.0
    for i in range(1,751):
        if colum[i].value > max_:
            max_ = colum[i].value
        if colum[i].value < min_:
            min_ = colum[i].value
    for ii in range(1,751):
        v = colum[ii].value
        newV = (v - min_)/(max_ - min_) * (30-1) + 1
        colum[ii].value = newV

def checkZero():
    ar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    for n in ar:
        colum = sheet[n]
        for nn in range(1,751):
            if colum[nn].value == 0:
                colum[nn].value = 0.01

def missing(in_):
    colum = sheet['B']
    i = sheet[in_]
    temp = ''
    tempp = 0
    save = None
    for num in range(1,361):
        if i[num].value == None:
            if temp == '':
                temp = colum[num].value
            if colum[num].value != temp:
                i[save].value = tempp / 11
                tempp = 0
                temp = colum[num].value
            save = num
        elif i[num].value != None:
            if temp == '':
                temp = colum[num].value
                tempp = i[num].value
            elif colum[num].value == temp:
                tempp += i[num].value
            elif colum[num].value != temp:
                i[save].value = tempp / 11
                tempp = 0
                temp = colum[num].value
            if num == 360:
                i[save].value = tempp / 11

missing('J')
missing('K')

colum = sheet['B']
arr = ['AA', 'AXP', 'BA', 'BAC', 'CAT', 'CSCO', 'CVX', 'DD', 'DIS', 'GE', 'HD', 'HPQ', 'IBM', 'INTC', 'JNJ', 'JPM', 'KRFT', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'PFE', 'PG',
'T', 'TRV', 'UTX', 'VZ', 'WMT', 'XOM']
for i in range(1,751):
    for ii in range(30):
        if colum[i].value == arr[ii]:
            colum[i].value = ii+1 

normalization('H')
normalization('K')
checkZero()
colum = sheet['P']
classA = sheet['Q']
classB = sheet['R']
classC = sheet['S']
classD = sheet['T']
for a in range(1,751):
    check = colum[a].value
    if check >= 0 and check <= 0.4:
        classA[a].value = 1
        classB[a].value = 0
        classC[a].value = 0
        classD[a].value = 0
    elif check > 0.4 and check <= 0.8:
        classA[a].value = 0
        classB[a].value = 1
        classC[a].value = 0
        classD[a].value = 0
    elif check > 0.8 and check <= 1.2:
        classA[a].value = 0
        classB[a].value = 0
        classC[a].value = 1
        classD[a].value = 0
    elif check > 1.2 and check <= 1.6:
        classA[a].value = 0
        classB[a].value = 0
        classC[a].value = 0
        classD[a].value = 1
normalization('B')
normalization('D')
normalization('E')
normalization('F')
normalization('G')
normalization('I')
normalization('J')
normalization('L')
normalization('M')
normalization('N')
normalization('O')
File.save('Data.xlsx')