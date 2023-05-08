from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(ele) for ele in strs])
        print(max(strs))
        for char_i in range(min_len):
            for str_i in range(len(strs)-1):
                if strs[str_i][char_i] != strs[str_i+1][char_i]:
                    return strs[0][0:char_i]
        return strs[0][0:min_len]

print(Solution().longestCommonPrefix(["flower","flow","flight"]))