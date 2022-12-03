def count_peaks(numbers):
    count = 0
    for i in range(len(numbers) - 2):
        if numbers[i] < numbers[i + 1] > numbers[i + 2]:
            count += 1
    return count


if __name__ == "__main__":
    A = [0, 5, 23, 14, 8, 13, 3, 0]
    print(count_peaks(A))
