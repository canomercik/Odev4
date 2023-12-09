class ThreeSum:
    def __init__(self, nums):
        self.nums = nums

    def FindThreeSum(self):
        self.nums.sort()
        result = []
        for i in range(len(self.nums) - 2):
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue

            left = i + 1
            right = len(self.nums) - 1
            
            while left < right:
                total = self.nums[i] + self.nums[left] + self.nums[right]

                if total == 0: # Üçünün toplamının 0 ettiği kondisyonu arıyoruz.
                    result.append([self.nums[i], self.nums[left], self.nums[right]])
                    while left < right and self.nums[left] == self.nums[left + 1]:
                        left += 1
                    while left < right and self.nums[right] == self.nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0: # Toplam 0'dan küçükse sağa kaydır.
                    left += 1
                else:
                    right -= 1
        
        return result


# Example

nums = [-1,0,1,2,-1,-4]
threeSumExample = ThreeSum(nums)
result = threeSumExample.FindThreeSum()
print("Output:", result)
