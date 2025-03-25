# 1436.) Destination City
# Categories: Array, Hash Table, String

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        destination_cities = []
        
        for i in range(len(paths)):
            destination_cities.append(paths[i][1])
        
        for destination_city in destination_cities:
            last_destination = True

            for path in paths:
                if destination_city == path[0]:
                    last_destination = False
                    break
            
            if last_destination:
                return destination_city
            
            