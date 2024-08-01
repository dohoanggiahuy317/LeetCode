class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len(
                    list(filter(
                        lambda x: x > 60,
                        list(
                            map(
                                lambda x: int(x[11:13]), 
                                details
                                )
                            ))
                    ))
                    