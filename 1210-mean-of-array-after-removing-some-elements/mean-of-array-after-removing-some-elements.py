class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        arr2 = arr[n // 20 : n - n // 20]
        return sum(arr2) / len(arr2)
