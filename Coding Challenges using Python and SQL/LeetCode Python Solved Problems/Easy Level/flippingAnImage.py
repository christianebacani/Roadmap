# 832.) Flipping an Image
# Categories: Array, Two Pointers, Bit Manipulation, Matrix, Simulation

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        result = []
        
        for i in range(len(image)):
            flipped_image = image[i][::-1]
            
            for j in range(len(flipped_image)):
                if flipped_image[j] == 1:
                    flipped_image[j] = 0
                
                else:
                    flipped_image[j] = 1
            
            result.append(flipped_image)
    
        return result