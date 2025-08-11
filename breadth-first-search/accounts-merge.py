class EmailNode:
    def __init__(self, email, acc_holder):
        self.email = email
        self.acc_holder = acc_holder

class AccHolder:
    def __init__(self, acc_id, name):
        self.acc_id = acc_id
        self.name = name

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        handled_email = defaultdict(lambda : AccHolder)
        acc_id = 0
        
        for name, *emails in accounts:

            acc_holder = AccHolder(acc_id, name)
            acc_id += 1

            for email in emails:
                if email in handled_email:
                    prev_acc_holder = handled_email[email]
                    min_id = min(prev_acc_holder.acc_id, acc_holder.acc_id)

                    acc_holder.acc_id = min_id
                    prev_acc_holder.acc_id = min_id
                
                handled_email[email] = acc_holder

        temp = [(value.acc_id, key, value.name) for key, value in handled_email.items()]
        temp.sort()
        ans = []
        curr_id = -1
        while temp:
            acc_id, email, name = temp.pop(0)
            if acc_id != curr_id:
                curr_id = acc_id
                ans.append([name])
            ans[-1].append(email)
            
        return ans
                    

        