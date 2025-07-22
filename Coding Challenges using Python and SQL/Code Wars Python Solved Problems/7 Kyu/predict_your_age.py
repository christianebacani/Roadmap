# Question: Predict your age!
# Categories: 7 Kyu
import math

def predict_age(age_1: int, age_2: int, age_3: int, age_4: int, age_5: int, age_6: int, age_7: int, age_8: int) -> int:
    list_of_ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    
    for i in range(len(list_of_ages)):
        list_of_ages[i] = (list_of_ages[i] * list_of_ages[i])
    
    total_age = sum(list_of_ages)
    square_root_of_total_age = math.sqrt(total_age)
    answer = math.floor(square_root_of_total_age / 2)

    return answer