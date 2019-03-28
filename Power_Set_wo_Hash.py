class PowerSet():
    #Реализация класса через список
    def __init__(self):
        self.slots=[]
    
    def size(self):
        #Возвращает кол-во элементов в множестве
        return len(self.slots)

    def put(self,value):
        #Добавление значения в мнжество (если его нет в множестве)
        if value==None:
            pass
        else:
            if value not in self.slots:
                self.slots.append(value)
            else:
                pass
    
    def get(self,value):
        #возвращает True если value имеется в множестве
        if value==None:
            return None
        else:
            if value in self.slots:
                return True
            else:
                return False
    
    def remove(self,value):
        #Возвращает True если значение удалено иначе False
        if value==None:
            return None
        else:
            for i in range(0,self.size()):
                if self.slots[i]==value:
                    self.slots.remove(value)
                    return True
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
        PowerSet_C=PowerSet()
        for i in range(0,len(elements_C)):
            PowerSet_C.put(elements_C[i])
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
        PowerSet_C=PowerSet()        
        for i in range(0,len(elements_C)):
            PowerSet_C.put(elements_C[i])
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
        PowerSet_C=PowerSet() 
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
            if elements_B[i] in elements_A:
                result=True
            else:
                result=False
                break
        return result

"""a=PowerSet()
a.put(23)
a.put(3)
a.put(223)
b=PowerSet()
b.put(23)
b.put(356)
b.put(223)
b.put("dfg")
b.put("223")
print(a.intersection(b).slots)
print(a.union(b).slots)
print(b.issubset(b))"""


