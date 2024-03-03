from functools import *


def fibonacci(n):  # returns nth term in fibonacci sequence
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n


def insertion_sort(length, array):  # sorts the first [len] terms in [array] by insertion algorithm
    counter = 0
    if length <= 1:
        return
    for i in range(1, length):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            counter += 1
        array[j + 1] = key
    return counter

def locate_position(superset, subset):  # returns the position(s) of a subset in a superset
    positions = ''
    for i in range(len(superset)):
        if superset[i] == subset[0]:
            if superset[i:i + len(subset)] == subset:
                positions += str(i + 1) + ' '
    return positions


def read_fasta_file(file_path="test.txt"):
    dataset = {}

    with open(file_path, "r") as f:
        current_key = None
        current_sequence = ""

        for line in f:
            line = line.strip()

            if line.startswith(">"):
                if current_key is not None:
                    dataset[current_key] = current_sequence
                current_key = line[1:]
                current_sequence = ""
            else:
                current_sequence += line

        # Add the last sequence to the dictionary
        if current_key is not None:
            dataset[current_key] = current_sequence

    return dataset

def rosalindint_to_int(string):  # converts "2 3 -6 123 23 -19" --> [2, 3, -6, 123, 23, -19]
    ints = []
    for i in string.split():
        ints.append(int(i))
    return ints


def merge_sorted_lists(len1, arr1, len2, arr2):
    newarr = []
    for i in range(len1 + len2):
        if len(arr1) == 0 and len(arr2) == 0:
            break
        try:
            if arr1[0] < arr2[0]:
                newarr.append(arr1[0])
                arr1.pop(0)
            else:
                newarr.append(arr2[0])
                arr2.pop(0)
        except:
            if len(arr1) > len(arr2):
                newarr.append(arr1[0])
                arr1.pop(0)
            else:
                newarr.append(arr2[0])
                arr2.pop(0)
    return newarr


def binary_search(n, arr, low, high):  # returns index of n in arr, low is generally 0, high is generally len(arr) -1
    if low <= high:
        mid = (low + high) // 2
        if n == arr[mid]:
            return mid + 1  # returns index + 1
        elif n < arr[mid]:
            return binary_search(n, arr, low, mid - 1)
        elif n > arr[mid]:
            return binary_search(n, arr, mid + 1, high)
    else:
        return -1


def factorial(n):
    if n in [0, 1, 2]:
        return n
    else:
        return n * factorial(n - 1)


def transpose(matrix):  # matrix something like [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] <-- 4x3 matrix
    num_columns = len(matrix[0])
    result = [[] for _ in range(num_columns)]
    row_counter = 0
    for row in matrix:
        element_counter = 0
        for element in row:
            result[element_counter].append(element)
            element_counter += 1
        row_counter += 1
    return result
