class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = homepage
        self.history = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.history.append(self.curr)
        self.forward_stack = []
        self.curr = url

    def back(self, steps: int) -> str:
        while steps > 0 and self.history:
            self.forward_stack.append(self.curr)
            self.curr = self.history.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.history.append(self.curr)
            self.curr = self.forward_stack.pop()
            steps -= 1
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.future(steps)