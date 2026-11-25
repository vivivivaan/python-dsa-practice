def max_and_count(arr: list[int]) -> list[int,int]:
    max: int = arr[0]
    count: int = 1
    
    for i in range(len(arr)):
        val: int = arr[i]
        if max < val:
            max = val
            count = 1
        elif val == max:
            count += 1
    
    return [max,count]

nums: list[int] = [10,20,30,40,90,60,90,70,90,80,90,90]

print(f'Max: {max_and_count(nums)[0]} | Count: {max_and_count(nums)[1]}')
