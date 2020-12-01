# day1 part 1
import os
def main():
    file = open("C:/Users/Mark/Desktop/aoc2020/day1/part1/input.txt", "r")
    numbers = []
    for line in file:
        numbers.append(line.strip())
    check(numbers)




def check(numbers):
    for i in range(len(numbers)):
            # if i==0:
            #     pass
            if int(numbers[0]) + int(numbers[i]) == 2020:
                print(int(numbers[0]) * int(numbers[i]))
                return
    print(len(numbers))
    numbers.pop(0)
    check(numbers)
    


main()


