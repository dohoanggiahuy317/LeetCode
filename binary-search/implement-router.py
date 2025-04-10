class Router:

    def __init__(self, memoryLimit: int):
        self.queue = []
        self.holder = set()
        self.limit = memoryLimit
        self.curr_time = -1
        self.dest_dict = {}
        
    def findLeft(self, lst:  List[int], x: int) -> int:
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] < x:
                lo = mid+1
            else:
                hi = mid
        return lo

    def findRight(self, lst: List[int], x: int) -> int:
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] <= x:
                lo = mid+1
            else:
                hi = mid
        return lo

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if timestamp == self.curr_time:
            if (source, destination) in self.holder:
                return False
        else:
            self.holder = set()
            self.curr_time = timestamp

        while len(self.queue) >= self.limit:
            ps, pd, pt = self.queue.pop(0)
            if pt == self.curr_time and (ps, pd) in self.holder:
                self.holder.remove((ps, pt))
            if pt in self.dest_dict[pd]:
                self.dest_dict[pd].remove(pt)

        self.holder.add((source, destination))
        self.queue.append((source, destination, timestamp))
        
        if destination not in self.dest_dict:
            self.dest_dict[destination] = set()
        
        self.dest_dict[destination].add(timestamp)
        return True


    def forwardPacket(self) -> List[int]:
        if self.queue:
            ps, pd, pt = self.queue.pop(0)
            if pt == self.curr_time:
                self.holder.remove((ps, pd))
            if pt in self.dest_dict[pd]:
                self.dest_dict[pd].remove(pt)
            return [ps, pd, pt]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_dict:
            return 0
        lst = sorted(list(self.dest_dict[destination]))
        lo = self.findLeft(lst, startTime)
        ri = self.findRight(lst, endTime)
        return ri - lo



# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)