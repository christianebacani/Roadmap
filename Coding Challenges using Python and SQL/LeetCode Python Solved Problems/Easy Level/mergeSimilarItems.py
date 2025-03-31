# 2363.) Mege Similar Items
# Categories: Array, Hash Table, Sorting, Ordered Set

class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        values = list(set(list(dict(items1).keys()) + list(dict(items2).keys())))
        values_and_weight = {}

        for i in range(len(values)):
            total_weight = 0
            
            for j in range(len(items1)):
                if values[i] == items1[j][0]:
                    total_weight += items1[j][1]
            
            for j in range(len(items2)):
                if values[i] == items2[j][0]:
                    total_weight += items2[j][1]
        
            values_and_weight[values[i]] = total_weight
        
        sorted_values = sorted(list(values_and_weight.keys()))
        ret = []
        
        for i in range(len(sorted_values)):
            for value, weight in values_and_weight.items():
                if sorted_values[i] == value:
                    ret.append([value, weight])
                    break

        return ret
                    