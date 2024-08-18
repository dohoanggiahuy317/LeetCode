class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip4 = []
        ip6 = []

        if "." in queryIP:
            ip4 = queryIP.split(".")
        elif ":" in queryIP:
            ip6 = queryIP.split(":")
        else:
            return "Neither"

        
        if len(ip4) == 4:
            for x in ip4:
                if x.isdigit() == False:
                    return "Neither"
                if len(x) > 1 and x[0] == '0':
                    return "Neither"
                if int(x) < 0 or int(x) > 255:
                    return "Neither"
                
            return "IPv4"

        if len(ip6) == 8:
            for x in ip6:
                if len(x) > 4 or len(x) < 1:
                    return "Neither"
                for letter in x:
                    if letter not in 'abcdefABCDEF0123456789':
                        return "Neither"               
            return "IPv6"

        return "Neither"