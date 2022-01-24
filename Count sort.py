nums = [1,1,4,2,1,3]


m = max(nums)
temp=[0] * (m+1)
output=[0] * (len(nums))

for num in nums:
    temp[num] += 1
    
for i in range(1, len(temp)):
    temp[i] += temp[i-1]

for i in range(len(nums)-1, -1, -1):
    output[temp[nums[i]]-1] = nums[i]
    temp[nums[i]] -= 1

print("input: ", nums)
print("output: ", output)
