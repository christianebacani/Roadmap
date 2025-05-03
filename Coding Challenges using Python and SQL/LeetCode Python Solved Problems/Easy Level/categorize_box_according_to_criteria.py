# 2525.) Categorize Box According to Criteria
# Categories: Math

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        categories = []

        volume_of_the_box = length * width * height

        if ((length >= 10 ** 4) or (width >= 10 ** 4) or (height >= 10 ** 4)) or (volume_of_the_box >= 10 ** 9):
            categories.append('Bulky')
        
        if mass >= 100:
            categories.append('Heavy')


        if 'Bulky' in categories and 'Heavy' in categories:
            return 'Both'

        elif 'Bulky' not in categories and 'Heavy' not in categories:
            return 'Neither'
        
        elif 'Bulky' in categories and 'Heavy' not in categories:
            return 'Bulky'
        
        else:
            return 'Heavy'