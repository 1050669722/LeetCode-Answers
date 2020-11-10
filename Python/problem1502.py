class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # if len(arr) == 2:
        #     return True
        # arr.sort()
        # tmp = arr[1] - arr[0]
        # for i in range(2, len(arr)):
        #     if arr[i] - arr[i - 1] != tmp:
        #         return False
        # return True

        if len(arr) == 2:
            return True
        arr.sort()
        for i in range(1, len(arr) - 1):
            if 2 * arr[i] != arr[i - 1] + arr[i + 1]:
                return False
        return True
