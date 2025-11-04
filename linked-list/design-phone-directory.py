class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = set([x for x in range(maxNumbers)])
        self.used = set()

    def get(self) -> int:
        if not self.available:
            return -1

        phone = self.available.pop()
        self.used.add(phone)
        return phone

    def check(self, number: int) -> bool:
        return (number in self.available)

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.available.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)