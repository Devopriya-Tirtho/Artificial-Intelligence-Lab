# -*- coding: utf-8 -*-
"""
Creasoningeated on Tue Sep  1 03:50:11 2020

@authoreasoning: Hp
"""


class reasoning:
    def __init__(self, pr1, pr2, conslusion, t):
        self.pr1 = pr1
        self.pr2 = pr2
        self.conslusion = conslusion
        self.t = t


list = []
T = 'True'

list.append(reasoning('A', 'B', 'D', 0))
list.append(reasoning('D', 'T', 'E', 0))
list.append(reasoning('D', 'E', 'F', 0))
list.append(reasoning('F', 'C', 'G', 0))
list.append(reasoning('B', 'G', 'H', 0))
list.append(reasoning('B', 'G', 'D', 0))
list.append(reasoning('D', 'H', 'I', 0))
list.append(reasoning('I', 'T', 'K', 0))


kb = dict()
kb['A'] = 'True'
kb['B'] = 'True'
kb['C'] = 'True'
kb['T'] = 'True'
kb['D'] = 'False'
kb['E'] = 'False'
kb['F'] = 'False'
kb['G'] = 'False'
kb['H'] = 'False'
kb['I'] = 'False'
kb['K'] = 'False'


print("Propositions are taken into action one by one:")
print("\n")


for i in list:
    if kb[i.pr1] == 'True' and kb[i.pr2] == 'True' and i.conslusion == 'D':
        kb['D'] = 'True'

flag = 0
begin = 0
storage = ''
l = []


while 1:
    for i in list:
        if kb[i.pr1] == 'True' and kb[i.pr2] == 'True' and i.t == 1 and i.conslusion == 'E':
            flag = 1        
            break
        if i.conslusion == 'K' and begin == 0:

            if kb[i.pr1] == 'False':

                storage = i.pr1
                l.append(i.conslusion)
                l.append(storage)
            else:
                storage = i.pr2
                l.append(storage)
            print(i.pr1 + " & " + i.pr2 + " -> " + i.conslusion)
            i.t = 1
            begin = 1
        elif i.conslusion == storage:
            if kb[i.pr1] == 'False':
                storage = i.pr1
                l.append(storage)
            elif kb[i.pr2] == "False":
                storage = i.pr2
                l.append(storage)
               
            i.t = 1
            print(i.pr1 + " & " + i.pr2 + " -> " + i.conslusion)

    if flag == 1:
        l.append('D')
        l.append('C')
        l.append('B')
        l.append('A')
        break
    
    
print("\n")

sz = len(l) -1
while sz >= 0:
    kb[l[sz]] = "True"
    print("After reasoning "+ l[sz]+" "+"is added to the KnowledgeBase")
    sz = sz - 1
    
    
print("\n")    
print("The Final KnowledgeBase is: \n")  

  
sz = len(l) -1
while sz >= 0:
    kb[l[sz]] = "True"
    print(l[sz] +" " +kb[l[sz]] +": is a fact")
    sz = sz - 1    
    

a = str(input('Give the first input of a rule: '))
b = str(input('Give the second input of a rule: '))
print("\n")    

if a == 'A' and b == 'B':
    print('A & B -> D       : If a tiger and a lion lives in a jungle, then a lion starts fighting')
elif a == 'D' and b == 'T':
    print("D -> E           :If a lion starts fighting, then a tiger starts fighting")
elif a == 'D' and b == 'E' :
    print("D & E -> F       :If a lion starts fighting and a tiger starts fighting, then the lion wins")
elif a == 'F' and b == 'C':
    print("F & C -> G       :If a lion wins and there is an elephant in another jungle, then the elephants comes to the jungle")
elif a == 'B' and b == 'G':
    print("B & G -> H       : If a lion is in the jungle and an elephant is in the jungle, then the elephant starts fighting")
elif a == 'D' and b == 'H':
    print("D & H -> I       : If a lion starts fighting and an elephant starts fighting, then the elephant wins")
elif a == 'I' and b == 'T':
    print("I - > k          :If the elephant wins, then the elephant becomes the king of the jungle")

