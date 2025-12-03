from typing import List


class Solution:
    def replaceNumbers(self, s: str) -> str:
        number_count =sum(1 for ch in s if ch.isdigit())
        expand_len = len(s) + number_count  * 5
        res = ['']*expand_len
