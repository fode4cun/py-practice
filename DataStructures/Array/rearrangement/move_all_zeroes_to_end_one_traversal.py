"""
Move all zeroes to end
Using single traversal

Time complexity: O(n)
Space comlexity: O(1)
"""


def push_to_end(arr, n):
    count = 0  # Count of non-zero elements

    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1

    return arr


if __name__ == '__main__':
    arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    n = len(arr)
    print(push_to_end(arr, n))

    arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    assert push_to_end(arr, n) == [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]
