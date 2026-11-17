class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hmm = set()
        for x in nums:
            if x in hmm:
                return True
            else:
                hmm.add(x)
        return False
