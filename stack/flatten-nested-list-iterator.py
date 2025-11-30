class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.stack = []

        n = len(nestedList)
        for i in range(n-1, -1, -1):
            self.stack.append(nestedList[i])

    
    def next(self) -> int:
        elem = self.stack.pop()

        while not elem.isInteger():
            elem_li = elem.getList()
            new_elem = elem_li[0]
            rest_elems = elem_li[1:]

            for i in range(len(rest_elems)-1, -1, -1):
                self.stack.append(rest_elems[i])

            elem = new_elem

        return elem.getInteger()
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0