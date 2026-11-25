def remove_value(nums: list[int], value: int) -> list[list[int], int] | None:
    if len(nums) == 0:
        return None

    write: int = 0
    for read in range(len(nums)):
        if nums[read] != value:
            nums[write] = nums[read]
            write += 1
    return list[nums, write]


def move_zeros(nums: list[int]) -> list[int] | None:
    if len(nums) == 0:
        return None

    left: int = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1

    while left < len(nums):
        nums[left] = 0
        left += 1

    return nums


nums: list[int] = [0, 1, 0, 3, 12]

print(f"Nums: {nums}\nNums after replacing zeroes: {move_zeros(nums)}")
