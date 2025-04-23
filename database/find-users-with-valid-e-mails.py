import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def check(mail):
        if mail[0].isalpha() and mail.endswith("@leetcode.com"):
            for i in mail[:mail.index("@")]:
                if not (i.isalnum() or i in "_.-"):
                    return False
        else:
            return False

        return True

    return users[users["mail"].apply(lambda x: check(x))]