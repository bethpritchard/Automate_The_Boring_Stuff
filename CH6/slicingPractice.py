def slicingPractice(nums):

    lastChar = nums[-1]
    nums1 = nums[1]
    nums2 = nums[1:3]
    nums3 = nums[2:5:2]
    nums4 = nums[:-4]
    nums5 = nums[:4]
    nums6 = nums[-5:]
    nums7 = nums[5:]


    print(f'''
range is {nums}
Last char is {lastChar}
nums[1] slice is {nums1} 
nums[1:3] slice is {nums2} 
nums[2:5:2] is {nums3}
nums[:-4] is {nums4}
nums[:4] is {nums5}
nums[-5:] is {nums6}
nums[5:] is {nums7}''')



mynums = list(range(20))

slicingPractice(mynums)