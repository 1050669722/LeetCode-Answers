class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # import sys
        # max_ = -sys.maxsize
        # for account in accounts:
        #     if sum(account) > max_:
        #         max_ = sum(account)
        # return max_

        # accounts.sort(key=lambda x: sum(x), reverse=True)
        # return sum(accounts[0])

        return sum(sorted(accounts, key=lambda x: sum(x), reverse=True)[0])
