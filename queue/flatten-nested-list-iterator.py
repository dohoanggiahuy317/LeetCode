class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.stack = []

        n = len(nestedList)
        for i in range(n-1, -1, -1):
            self.stack.append(nestedList[i])

    
    def next(self) -> int:
        elem = self.stack.pop()
        return elem.getInteger()
    
    def hasNext(self) -> bool:
        if len(self.stack) == 0:
            return False

        elem = self.stack.pop()

        while not elem.isInteger():
            elem_li = elem.getList()
            
            if len(elem_li) > 0:
                for i in range(len(elem_li)-1, -1, -1):
                    self.stack.append(elem_li[i])

            if not self.stack:
                return False
            
            elem = self.stack.pop()

        self.stack.append(elem)
        # print(self.stack)
        return True