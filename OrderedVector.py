import numpy as np


class OrderedVector:
    def __init__(self, max_len):
        self.max_len = max_len
        self.lastPosition = -1
        self.value = np.empty(self.max_len, dtype=int)

    def print(self):
        if self.lastPosition == -1:
            return 'Empty Vector'
        else:
            for i in range(self.lastPosition + 1):
                print('index ', i, '= .:. value = ', self.value[i])

    def insert(self, value):
        key_index = 0
        if self.lastPosition + 1 == self.max_len:
            return 'Maximum capacity was reached'
        else:
            for i in range(self.lastPosition+1):
                if self.value[i] >= value:
                    key_index = i
                    break
                if self.lastPosition == i:
                    key_index = i+1
            for i in range(self.lastPosition+1, key_index, -1):
                self.value[i] = self.value[i - 1]
            self.value[key_index] = value
            self.lastPosition += 1

    def search(self, value):
        for i in range(self.lastPosition+1):
            if self.value[i] == value:
                return i
            if self.value[i] > value or i == self.lastPosition:
                return -1

    def delete(self, value):
        key_index = self.search(value)
        if key_index == -1:
            return 'Value cannot be deleted'
        else:
            for i in range(key_index, self.lastPosition+1):
                self.value[i] = self.value[i+1]
            self.lastPosition -= 1
