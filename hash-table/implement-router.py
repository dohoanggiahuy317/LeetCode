class Router:

    def __init__(self, memoryLimit: int):
        self.queue = []
        self.holder = {}
        self.limit = memoryLimit
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination) in self.holder and self.holder[(source, destination)] == timestamp:
            return False

        while len(self.queue) >= self.limit:
            ps, pd, pt = self.queue.pop(0)
            del self.holder[(ps, pd)]

        self.holder[(source, destination)] = timestamp
        self.queue.append((source, destination, timestamp))
        return True


    def forwardPacket(self) -> List[int]:
        if self.holder:
            ps, pd, pt = self.queue.pop(0)
            del self.holder[(ps, pd)]
            return [ps, pd, pt]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ans = 0
        ind = 0
        while ind < len(self.queue) and endTime >= self.queue[ind][2]:
            # print(self.queue[ind])
            if self.queue[ind][2] >= startTime and self.queue[ind][1] == destination:
                ans += 1
                
            ind += 1
        return ans



# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)