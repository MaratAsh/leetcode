from typing import List



class Solution:
    @staticmethod
    def get_number_digits(number: int) -> int:
        count = 0
        while number > 0:
            number //= 10
            count += 1
        return count

    @staticmethod
    def insert_count(chars: List[str], ptr, count):
        _count = count - 1
        digits = Solution.get_number_digits(count)
        if _count % 10 == 9:
            i = 0
            while i < digits:
                chars[ptr + digits - i - 1] = str((count // 10 ** i) % 10)
                i += 1
        else:
            chars[ptr + digits - 1] = str(count % 10)
        return digits


    def compress(self, chars: List[str]) -> int:
        ptr = 0
        ptr_n = 1
        prev_count = 1
        for i in range(1, len(chars)):
            if chars[ptr] == chars[i]:
                prev_count += 1
                ptr_n = ptr + Solution.insert_count(chars, ptr + 1, prev_count)
            elif prev_count == 1:
                ptr += 1
                ptr_n = ptr
                chars[ptr] = chars[i]
            else:
                ptr = ptr_n + 1
                ptr_n = ptr
                chars[ptr] = chars[i]
                prev_count = 1
        return ptr_n + 1
