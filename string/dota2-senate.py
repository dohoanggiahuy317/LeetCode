class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dic = {"R": [], "D": []}


        for x in range(len(senate)):
            if senate[x] == "R":
                dic['R'].append(x)
            else:
                dic["D"].append(x)


        counter = 0
        while len(dic["R"]) > 0 and len(dic["D"]) > 0:
            
            if dic["R"][0] == counter:
                dic["D"].pop(0)

                temp = dic["R"].pop(0)
                dic["R"].append(temp)
            elif dic["D"][0] == counter:
                dic["R"].pop(0)

                temp = dic["D"].pop(0)
                dic["D"].append(temp)

            counter = (counter + 1) % len(senate)

        if len(dic["R"]) > 0:
            return "Radiant"
        else:
            return "Dire"
       
        