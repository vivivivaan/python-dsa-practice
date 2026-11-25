def max_product(nums: list[int]) -> int:
    length: int = len(nums)

    if length <= 3:
        return ValueError("The size of the nums must be greater than 3!")

    global_max: int = nums[0] * nums[1] * nums[2]

    for first in range(length):
        for second in range(first+1, length):
            for third in range(second, length):
                local_max: int = nums[first] * nums[second] * nums[third]
                global_max = max(global_max, local_max)
                third += 1
            second += 1
        first += 1

    return global_max


nums: list[int] = [150, 300, -500, -400, 75, 25, 200, 90]

print(f"The max sum of three numbers is: {max_product(nums)}")
