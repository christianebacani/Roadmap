# Question: Remove All the Marked Elements of a List
# Categories: 7 Kyu

class List:
    def remove_(self, integer_list: list[int], values_list: list[int]) -> list[int]:
        result = []
        
        for i in range(len(integer_list)):
            if integer_list[i] not in values_list:
                result.append(integer_list[i])
        
        return result