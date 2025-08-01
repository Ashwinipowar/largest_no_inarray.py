#method1
nums=[22,3,5,6,666,88,99,0]
largest=nums[0]
n=len(nums)

for i in range (0,n):
     largest =max(largest, nums[i])
     
print(largest)





#method2
nums=[22,3,5,6,666,88,99,0]
largest=float("-inf")
n=len(nums)

for i in range (0,n):
     largest =max(largest, nums[i])
     
print(largest)








#second largest no.
nums = [22, 3, 5, 6, 666, 88, 99, 0]

largest = float('-inf')
second_largest = float('-inf')

for i in range(len(nums)):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]

print(second_largest)







#method easy
def find_largest(nums):
    largest = nums[0]
    n = len(nums)
    
    for i in range(n):
        largest = max(largest, nums[i])
        
    return largest

nums = [22, 3, 5, 6, 666, 88, 99, 0]
print(find_largest(nums))  #  Now return is allowed
