with open('day9_input.txt') as f:
    all_nums = [int(l.strip()) for l in f.readlines() if l.strip()]

def valid(nums, target):
    for i in range(len(nums)):
        if (target- nums[i]) in nums[i+1:]:
            return True
    return False

def first_invalid(nums, window):
    rolling = nums[:window]
    i = window
    while True:
        num = nums[i]
        if not valid(rolling, num):
            return num
        rolling.pop(0)
        rolling.append(num)
        i += 1

def sum_window(nums, target):
    for i in range(len(nums)):
        num = nums[i]
        if num >= target:
            continue
        for j in range(i+1, len(nums)):
            num += nums[j]
            if num == target:
                return nums[i:j+1]
            elif num > target:
                break

f = first_invalid(all_nums, 25)
window = sum_window(all_nums, f)
print(min(window) + max(window))