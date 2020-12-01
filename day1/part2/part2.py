# day1 part 1
import os
def main():
    file = open("C:/Users/Mark/Desktop/aoc2020/day1/part2/input.txt", "r")
    numbers = []
    for line in file:
        numbers.append(line.strip())
    check(numbers)




def check(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if int(numbers[0]) + int(numbers[i]) + int(numbers[j]) == 2020:
                print(int(numbers[0]) * int(numbers[i]) * int(numbers[j]))
                return

    numbers.pop(0)
    check(numbers)
    


main()