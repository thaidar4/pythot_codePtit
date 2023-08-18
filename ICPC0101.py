quantity = int(input())
numbers = input()
number_list = numbers.split()

number_list = [int(num) for num in number_list]

def remove_pairs(nums):
    filtered_nums = []
    for num in nums:
        if not filtered_nums or (num + filtered_nums[-1]) % 2 != 0:
            filtered_nums.append(num)
        else:
            filtered_nums.pop()
    return filtered_nums

filtered_list = remove_pairs(number_list)
count = len(filtered_list)
print(count)