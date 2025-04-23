# 2511.) Maximum Enemey Forts That Can Be Captured
# Categories: Array, Two Pointers

class Solution:
    def captureForts(self, forts: list[int]) -> int:
        number_of_enemy_captured_while_travelling = []

        for i in range(len(forts)):
            if forts[i] != 1:
                continue

            for j in range(len(forts)):
                if j < i and forts[j] == -1:
                    travelled_forts = forts[j + 1 : i]
                
                elif i < j and forts[j] == -1:
                    travelled_forts = forts[i + 1 : j]

                else:
                    continue

                if 1 not in travelled_forts and -1 not in travelled_forts:
                    number_of_enemy_captured_while_travelling.append(travelled_forts.count(0))
        
        return max(number_of_enemy_captured_while_travelling, default=0)