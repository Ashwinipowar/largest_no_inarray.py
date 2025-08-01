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






#method easy
def find_largest(nums):
    largest = nums[0]
    n = len(nums)
    
    for i in range(n):
        largest = max(largest, nums[i])
        
    return largest

nums = [22, 3, 5, 6, 666, 88, 99, 0]
print(find_largest(nums))  #  Now return is allowed
