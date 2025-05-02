# 2739.) Total Distance Traveled
# Categories: Math, Simulation

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total_distance = 0
        total_fuel_liters = 0

        while mainTank > 0:
            mainTank -= 1
            total_fuel_liters += 1
            total_distance += 10

            if total_fuel_liters % 5 != 0:
                continue

            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
        
        return total_distance