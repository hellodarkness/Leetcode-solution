# Write a function to find the longest common prefix string amongst an array of strings.
#

def longestCommonPrefixHorizontal(self, strs):
    if not strs:
        return ''
    for g in range(0, len(strs) - 1):
        t = strs[g]
        lcp = ''
        for i in range(0, len(strs[0]) - 1):
            if t[i] == strs[g + 1][i]:
                lcp = lcp + t[i]
            else:
                break
        t = lcp
    return lcp