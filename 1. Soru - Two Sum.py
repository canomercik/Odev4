class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def FindIndexes(self):
        indexes = {}
        for i, value in enumerate(self.nums): 
            remaining = self.target - value # Her sayı eklendiğinde onu target değerine tamamlayan bir sayı var mı diye bakıyoruz.
            if remaining in indexes:
                return (indexes[remaining], i)
            indexes[value] = i
        return None

#Örnek
nums = [-1,3,15,4,2,-5,-7]
target = 8
twoSum = TwoSum(nums, target)
result = twoSum.FindIndexes()

if result:
    print(f"Indexes: [{result[0]}, {result[1]}]")
else:
    print("No Index Found For Target.")
