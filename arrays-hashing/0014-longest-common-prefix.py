class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            result = result + strs[0][i]
            for a in range(len(strs)):
                if i == len(strs[a]):
                    return result[:i]
                if strs[0][i] != strs[a][i]:
                    result = result[:i]
                    return result

        return result
