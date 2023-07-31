class TwoSum:
     def __init__(self):
             pass
     def get_two_sum(self, arr, target):
             results = []
             for i in range(len(arr)):
                     for j in range(i+1, len(arr)):
                             if arr[i] + arr[j] == target:
                                     results.append([i, j])
             return results

two_sum = TwoSum()
a = [10, 20, 10, 40, 50, 30, 70]
target = 50
results = two_sum.get_two_sum(a, target)
print(results)