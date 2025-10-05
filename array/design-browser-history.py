class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur_page = 0
        
    def visit(self, url: str) -> None:
        while self.cur_page < len(self.history) - 1:
            self.history.pop()
        self.history.append(url)
        self.cur_page += 1

    def back(self, steps: int) -> str:
        x = max(0,self.cur_page - steps)
        self.cur_page = x
        return self.history[self.cur_page]

    def forward(self, steps: int) -> str:
        x = min(len(self.history) - 1 , self.cur_page + steps)
        self.cur_page = x
        return self.history[self.cur_page]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)