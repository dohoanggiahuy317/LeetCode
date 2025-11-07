class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_li = [homepage]
        self.forw_li = []

    def visit(self, url: str) -> None:
        self.back_li.append(url)
        self.forw_li = []
        return self.back_li[-1]

    def back(self, steps: int) -> str:
        shift = min(steps, len(self.back_li) - 1)

        for _ in range(shift):
            url = self.back_li.pop()
            self.forw_li.append(url)

        return self.back_li[-1]

    def forward(self, steps: int) -> str:
        shift = min(steps, len(self.forw_li))

        for _ in range(shift):
            url = self.forw_li.pop()
            self.back_li.append(url)

        return self.back_li[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forw_li(steps)