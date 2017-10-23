'''
Write a function, that takes in a string, and returns an array of every possible combination of upper/lowercase letters, keeping the letters in the same order.

"a" => [a, A]
"ab" => [ab, Ab, aB, AB]
"abc" => [abc, Abc, aBc, abC, ABc, aBC, AbC, ABC]

'''

def permutator(arr):
    arr = list(arr)
    result = []

    # append the bare minimum
    result.append(arr[0])
    result.append(arr[0].upper())

    # loop through the array list passed in starting from 1
    for i in range(1, len(arr)):
        # copy the array thus far using slicing
        temp = result[:]

        # loop through the result as it grows
        for j in range(len(result)):
            # modify result at j and combine it with the next letter
            result[j] = result[j] + arr[i]
            # modify temp at j and combine it with the next letter uppercase
            temp[j] = temp[j] + arr[i].upper()

        # extend the result array with the new uppercase
        result.extend(temp)

    return result


print(permutator('ab'))
