nums = input().split()
nums1 = nums[0]
nums2 = nums[1]

if (int(nums1[::-1]) > int(nums2[::-1])):
    print(nums1[::-1])
else:
    print(nums2[::-1])