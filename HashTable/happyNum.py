def getSum(nums:int):
    sum = 0
    while nums:
        nums, r = divmod(nums, 10)
        sum += r ** 2
    return sum

def happyNum(nums:int):
    record = set()
    while True:
        sum = getSum(nums)
        if sum == 1:
            return True
        if sum in record:
            return False
        else:
            record.add(sum)
            nums = sum
if __name__ == '__main__':
    nums = 18
    print(happyNum(nums))
