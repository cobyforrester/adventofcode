
### PART 1
p1_answer = 0
nums1 = []
nums2 = []
# read in the file and add numbers to 2 different arrays
with open("input.txt", "r") as file:
    for line in file:
        nums = line.split()
        nums1.append(int(nums[0]))
        nums2.append(int(nums[1]))

# sort the arrays to pair the smallest together
nums1.sort()
nums2.sort()

# find the distance between and add to p1_answer
for i in range(len(nums1)):
    p1_answer += abs(nums1[i] - nums2[i])

# print answer
print(f'Part 1: {p1_answer}')

### PART 2
p2_answer = 0

# create dict of occurrences in 
nums2_seen = {}
for num in nums2:
    if num in nums2_seen:
        nums2_seen[num] += 1
    else:
        nums2_seen[num] = 1

# figure out similarity
for num in nums1:
    p2_answer += num * nums2_seen.get(num, 0)

# print answer
print(f'Part 2: {p2_answer}')
