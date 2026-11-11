class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = set()
        for item in nums:
            if item in hash:
                return True
            hash.add(item)
        return False
