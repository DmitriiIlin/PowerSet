import string,random
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!
        input_string=str(value)
        return sum(ord(input_string[i])**(i+1) for i in range(len(input_string)))%self.size

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        value=str(value)
        if None in self.slots:
            slot_adr=self.hash_fun(value)
            print("----------")
            print(slot_adr)
            while self.slots[slot_adr]!=None:
                if self.size-slot_adr-1>=self.step:
                    slot_adr=slot_adr+self.step
                else:
                    slot_adr=self.step-(self.size-slot_adr)
            print(slot_adr,self.size,self.step)
            print("----------")
            return slot_adr
        else: 
            return None
 
    def put(self, value):
         # записываем значение по хэш-функции
         # возвращается индекс слота или None,
         # если из-за коллизий элемент не удаётся
         # разместить 
        input_string=str(value)
        slot_adr=self.seek_slot(input_string)
        if slot_adr!=None:
            self.slots[slot_adr]=input_string
            return slot_adr
        else:
            return None

    def find(self, value):
         # находит индекс слота со значением, или None
        value=str(value)
        flag=False
        for i in range(len(self.slots)):
            if self.slots[i]==value:
                flag=True
                return i
            else:
                i+=1
        if flag==False:
            return None

class PowerSet(HashTable):
    #Реализация класса PowerSet-аналог множества
    def __init__(self,sz,stp):
        super(PowerSet,self).__init__(sz,stp)
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def size(self):
        #Метод возвращает кол-во ненулевых элементов множества.
        elements_A=self.slots
        count=0
        for i in range(0,len(elements_A)):
            if elements_A[i]!=None:
                count+=1
            else:
                pass 
        return count

    def get(self,value):
        #Метод возвращает True если в множестве имеется значение value, в противном случае False
        input_string=str(value)
        if self.find(input_string)!=None:
            return True
        else: 
            return False

    def put(self,value):
        #Реализация метода put для класса потомка с учетом проверки на наличие идентичного значения / элемента
        input_string=str(value)
        is_in_PowerSet=self.find(input_string)
        if is_in_PowerSet==None:
            slot_adr=self.seek_slot(input_string)
            if slot_adr!=None:
                self.slots[slot_adr]=input_string
                return slot_adr
            else:
                return None
        else: 
            return None
    
    def remove(self,value):
        #Удаление элемента из множества PowerSet
        input_string=str(value)
        is_in_PowerSet=self.find(input_string)
        if is_in_PowerSet!=None:
            self.slots[self.find(input_string)]=None
            return True
        else:
            return False

    def intersection(self,Powerset_B):
        #Метод возвращает множество элементов которые есть как в исходном множестве так и в множестве Powerset_B 
        elements_A=self.slots
        elements_B=Powerset_B.slots
        elements_C=[]
        for i in range(0,len(elements_A)):
            for j in range(0,len(elements_B)):
                if elements_A[i]==elements_B[j] and elements_A[i]!=None:
                    elements_C.append(elements_A[i])
                else:
                    pass
        PowerSet_C=PowerSet(len(elements_C),1)
        for i in range(0,len(elements_C)):
            PowerSet_C.put(str(elements_C[i]))
        return PowerSet_C

    def union(self,PowerSet_B):
        #Метод объединяет два множества в одно, без повторения элементов
        elements_A=self.slots
        elements_B=PowerSet_B.slots
        elements_C=[]
        for i in range(0,len(elements_A)):
            if elements_A[i]!=None:
                elements_C.append(elements_A[i])
            else:
                pass
        for j in range(0,len(elements_B)):
            if elements_B[j]!=None and elements_B[j] not in elements_A:
                elements_C.append(elements_B[j])
            else:
                pass
        PowerSet_C=PowerSet(len(elements_C),1)        
        for i in range(0,len(elements_C)):
            PowerSet_C.put(str(elements_C[i]))
        return PowerSet_C 

    def difference(self,PowerSet_B):
        #Результатом данного метода яляется множество элементов которое содержиться в исходном множестве но не содержиться в множестве параметре          
        elements_A=self.slots
        elements_B=PowerSet_B.slots
        elements_C=[]
        for i in range(0,len(elements_A)):
            if elements_A[i]!=None and elements_A[i] not in elements_B:
                elements_C.append(elements_A[i])
            else:
                pass
        PowerSet_C=PowerSet(len(elements_C),1) 
        for i in range(0,len(elements_C)):
            PowerSet_C.put(elements_C[i])
        return PowerSet_C

    def issubset(self,PowerSet_B):
        #Метод проверяет является ли множество параметр частью исходного множества.
        elements_A=self.slots
        elements_B=PowerSet_B.slots
        elements_B_without_None=[]
        result=False
        if elements_B==None:
            return None
        for i in range(0,len(elements_B)):
            if elements_B[i]!=None:
                elements_B_without_None.append(elements_B[i])
        for i in range(0,len(elements_B_without_None)):
            if elements_B_without_None[i] in elements_A:
                result=True
            else:
                result=False
                break
        return result
    









"""
a=PowerSet(23,4)
a.put("A")
a.put("S")
a.put("D")
a.put("F")
print(a.slots)
print("#######")
b=PowerSet(17,2)
b.put("A")
b.put("H")
b.put("F")
print(b.slots)
print("#######")
C=a.intersection(b)
print(C.slots)
D=a.union(b)
print(D.slots)
F=a.difference(b)
print("@@@@@@@@")
print(F.slots)
a.put("H")
print(a.issubset(b))"""




