class SortedList:
    def __init__(self, values):
        self.values = sorted(values)
        self.length = len(self.values)

    def add(self,val):
        pos = self.findPos(val)
        self.values.insert(pos,val)
        self.length += 1

    def findPos(self, val):
        left = 0
        right = self.length - 1
        while left < right:
            mid = (left + right) // 2
            if self.values[mid] < val:
                left = mid + 1
            else:
                right = mid
        return left

    def popLeft(self):
        if self.length == 0:
            return None
        self.length -= 1
        left = self.values[0]
        self.values = self.values[1:]
        return left

    def popRight(self):
        if self.length == 0:
            return None
        self.length -= 1
        right = self.values[-1]
        self.values = self.values[0:-1]
        return right
    
    def __str__(self):
        return str(self.values)