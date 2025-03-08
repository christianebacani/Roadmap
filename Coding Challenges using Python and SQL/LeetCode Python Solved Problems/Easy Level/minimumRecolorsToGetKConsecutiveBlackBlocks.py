# 2379.) Minimum Recolors to Get K Consecutive Black Blocks
# Categories: String, Sliding Window
 
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        number_of_operations = []

        for i in range(0, len(blocks)):
            sub_blocks = blocks[i : i + k]

            if len(sub_blocks) != k:
                break

            number_of_operation = 0

            for sub_block in sub_blocks:
                if sub_block == 'W':
                    number_of_operation += 1 

            number_of_operations.append(number_of_operation)

        return min(number_of_operations)

