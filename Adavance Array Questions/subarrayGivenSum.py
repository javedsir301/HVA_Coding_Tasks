def findSubarrayOfGivenSum(arr, sum):
    arrSize = len(arr)
    start = 0
    current_sum = 0
    end = 0

    while end < arrSize:
        current_sum += arr[end]

        while current_sum > sum and start <= end:
            current_sum -= arr[start]
            start += 1
        
        if current_sum == sum:
            subarray = arr[start:end + 1]
            print("Subarray:", subarray)
            return
        
        end += 1

    print("Not Possible")

arr = [1, 2, 3, 7, 5]
sum = 12
findSubarrayOfGivenSum(arr, sum)
