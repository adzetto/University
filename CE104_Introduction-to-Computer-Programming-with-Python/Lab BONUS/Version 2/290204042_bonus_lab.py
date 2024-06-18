def create_digits(number):
    digit_list = []
    n = number
    while n > 0:
        digit = n % 10 
        digit_list.insert(0, digit)
        n = n // 10
    return digit_list

def avg(number):
    sum=0
    for i in create_digits(number):
        sum += i
    return sum / len(create_digits(number))

def std(number):
    sum=0
    avg_nu = avg(number=number)
    for i in create_digits(number):
        sum += (i-avg_nu)**2
    return (sum/len(create_digits(number)))**0.5

def main():
    std_number = 290204042
    list = create_digits(number=std_number)
    avg_val = avg(number=std_number)
    std_val = std(number=std_number)
    print(f"Your student number contains digits {list} and its avg is {avg_val:.4f}. Hence, standard deviation of this is {std_val:.4f}")

main()


#----------------------------------------------------------------
#Or it can be done by the string manipulation
#
#def main():
#    student_number = "290204042"
#    digits = [int(digit) for digit in student_number]
#    average = avg(digits)
#    std_deviation = std(digits, average)
#    print("Average of digits:", average)
#    print("Standard deviation of digits:", std_deviation)
#
#def avg(numbers):
#    return sum(numbers) / len(numbers)
#
#def std(numbers, mean):
#    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
#    return variance**0.5
#
#if __name__ == "__main__":
#    main()
#----------------------------------------------------------------