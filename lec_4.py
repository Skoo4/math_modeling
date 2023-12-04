def sredn_arifm(arr : list) -> float:
    return sum(arr) / len(arr)

while True:
    nums = list(map(int, input().split()))
    print(sredn_arifm(nums))