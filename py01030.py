from math import gcd

nums = input()
nums = nums.split()
n = int(nums[0])
k = int(nums[1])

start = 10 ** (k - 1)
end = 10 ** k - 1

counter = 0  

for number in range(start, end + 1):
    if gcd(n, number) == 1:
        print(number, end=" ")
        counter += 1

        if counter % 10 == 0:
            print()  

if counter % 10 != 0:
    print()
