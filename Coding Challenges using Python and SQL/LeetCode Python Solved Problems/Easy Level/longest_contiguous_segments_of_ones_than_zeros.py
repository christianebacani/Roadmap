# 1869.) Longet Contiguous Segments of Ones than Zeros
# Categories: String

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        length_of_contiguous_segment_of_1s = []
        length_of_contiguous_segment_of_0s = []
        
        for i in range(1, len(s) + 1):
            for j in range(len(s)):
                subarray = s[j : j + i]

                if '0' in subarray:
                    continue

                if len(subarray) not in length_of_contiguous_segment_of_1s:
                    length_of_contiguous_segment_of_1s.append(len(subarray))
        
        for i in range(1, len(s) + 1):
            for j in range(len(s)):
                subarray = s[j : j + i]

                if '1' in subarray:
                    continue
                
                if len(subarray) not in length_of_contiguous_segment_of_0s:
                    length_of_contiguous_segment_of_0s.append(len(subarray))
        
        if max(length_of_contiguous_segment_of_1s, default=0) > max(length_of_contiguous_segment_of_0s, default=0):
            return True
        
        return False