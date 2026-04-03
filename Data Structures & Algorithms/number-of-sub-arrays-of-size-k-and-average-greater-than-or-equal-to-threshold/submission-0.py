class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = []
        windowSum = 0
        l = 0
        count = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                window.remove(arr[l])
                windowSum -= arr[l]
                l += 1
            window.append(arr[r])
            windowSum += arr[r]
            if len(window) == k:
                if windowSum / k >= threshold:
                    count += 1

        return count