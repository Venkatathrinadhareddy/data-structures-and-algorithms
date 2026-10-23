import ctypes;
class DynamicArray:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.data = self.__createArray(self.size);

    def __createArray(self,capacity):
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n

    def append(self,item):
        if self.n==self.size:
            self.__increaseArrayLength(self.size*2)
        self.data[self.n] = item
        self.n = self.n + 1

    def remove_tail(self):
        if self.n != 0:
            print("Remvoed data :",self.data[self.n-1])
            self.n = self.n-1
        else:
            print('Value error - array is empty')

    def find(self,item):
        for i in range(self.n):
            if item == self.data[i]:
                return i
        return 'Value error - Item not found'

    def remove_head(self):
        newArray = self.__createArray(self.size)
        if self.n != 0:
            for i in range(self.n-1):
                newArray[i] = self.data[i+1]
            self.data = newArray
            self.n = self.n-1
        else:
            print('Value error - array is empty')

    def insert(self,pos,item):
        if pos > self.n:
            print("No position in existing array")
            return
        else:
            if self.n == self.size:
                self.__increaseArrayLength(self.size*2)
            for i in range(self.n,pos,-1):
                self.data[i] = self.data[i-1]
            self.data[pos] = item
            self.n = self.n + 1

    def clear(self):
        self.size =1
        self.n = 0

    def __increaseArrayLength(self,new_capacity):
        newArray = self.__createArray(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            newArray[i] = self.data[i]
        self.data = newArray

    def __str__(self):
        result =''
        for i in range(self.n):
            result = result + str(self.data[i]) + ","
        return "[" + result[:-1] + "]"

    def __delitem__(self,pos):
        if 0 < pos < self.n:
            for i in range(pos,self.n-1):
                self.data[i] = self.data[i+1]
            self.n = self.n -1


dy = DynamicArray()
dy.append(10)
dy.append(20)
dy.append(30)
dy.append(40)
dy.append(50)
dy.append(60)
# dy.remove_tail()
# dy.remove_tail()
# # dy.remove_tail()
# # dy.remove_tail()
# # dy.remove_tail()
# # dy.remove_tail()
# # dy.remove_tail()
# # dy.remove_tail()
# # dy.remove_tail()
# # dy.remove_tail()
# # dy.remove_tail()
# # print(len(dy))
# print(dy.find(40))
# print(dy.find(200))
# dy.remove_head()
# dy.remove_head()
# dy.clear()
dy.insert(6,100)
print(dy)
dy.__delitem__(10)
print(dy)
