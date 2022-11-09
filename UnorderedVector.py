import numpy as np


class UnorderedVector:
    def __init__(self, maxLen):
        self.maxLen = maxLen
        self.lastPosition = -1
        self.value = np.empty(self.maxLen, dtype=int)

    def print(self):
        if self.lastPosition == -1:
            return 'Empty Array.'
        else:
            for i in range(self.lastPosition+1):
                print('index ', i, '= .:. value = ', self.value[i])

    def insert(self,value):
        if self.lastPosition + 1 == self.maxLen:
            print('Maximum capacity was reached')
        else:
            self.lastPosition += 1
            self.value[self.lastPosition] = value

    def search(self,value):
        for i in range(self.lastPosition+1):
            if self.value[i] == value:
                return i
        return -1

    def delete(self, value):
        indexValue = self.search(value)
        if indexValue == -1:
            return 'Not found - Impossible to delete'
        else:
            for i in range(indexValue, self.lastPosition):
                self.value[i] = self.value[i+1]
            self.lastPosition -= 1
