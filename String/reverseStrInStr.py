class Solution:
    def reverseStr(self, strs:str)->str:
        s = strs[::-1]
        s = ' '.join(word[::-1] for word in s.split())
        return s
    # def reverseStr2(self, strs:str)->str:

if __name__ == '__main__':
    strs = "Hello World!"
    print(Solution().reverseStr(strs))