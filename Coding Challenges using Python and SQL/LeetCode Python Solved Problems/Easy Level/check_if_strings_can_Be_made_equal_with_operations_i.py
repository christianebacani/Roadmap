# 2839.) Check if Strings Can be Made Equal With Operations I
# Categories: String

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        lst_s1 = list(s1)
        lst_s2 = list(s2)

        for _ in range(2):
            for i in range(len(lst_s1)):
                for j in range(len(lst_s1)):
                    if j - i != 2:
                        continue

                    character_i = lst_s1[i]
                    character_j = lst_s1[j]

                    lst_s1[i] = character_j
                    lst_s1[j] = character_i

                    if ''.join(lst_s1) == ''.join(lst_s2):
                        return True
        
        for _ in range(2):
            for i in range(len(lst_s2)):
                for j in range(len(lst_s2)):
                    if j - i != 2:
                        continue

                    character_i = lst_s2[i]
                    character_j = lst_s2[j]

                    lst_s2[i] = character_j
                    lst_s2[j] = character_i

                    if ''.join(lst_s2) == ''.join(lst_s1):
                        return True
        
        return False