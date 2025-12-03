class Solution:
    def removeDuplicates(self, s:str):
        res = list(s)
        slow,fast = 0,0
        length = len(s)

        while fast < length:
            res[slow] = res[fast]

            if slow > 0 and res[slow] == res[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[0:slow])
if __name__ == '__main__':
    s = "aabccba"
    print(Solution().removeDuplicates(s))
