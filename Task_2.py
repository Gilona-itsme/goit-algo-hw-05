def fractional_binary_search(arr: list[float], target: list[float]) -> tuple[int, float | None]:
    low = 0
    high = len(arr) - 1
    upper_bound = None
    iterations = 0
 
    while low <= high:
        iterations += 1
 
        mid = (high + low) // 2
 
        if arr[mid] >= target:
            upper_bound = arr[mid]
            high = mid - 1

        else:
            low = mid + 1

    return iterations, upper_bound

data_arr = [2.1, 3.3, 4.5, 4.0, 10.04, 4.10]
target1 = 4.4
target2 = 1.0
target3 = 11.04
iters, result = fractional_binary_search(data_arr, target1) 
print(f"Array: {data_arr}")
print(f"Iterations: {iters} \n Upper limit: {result}")
iters, result = fractional_binary_search(data_arr, target2) 

print(f"Iterations: {iters} \n Upper limit: {result}")


iters, result = fractional_binary_search(data_arr, target3) 

print(f"Iterations: {iters} \n Upper limit: {result}")
