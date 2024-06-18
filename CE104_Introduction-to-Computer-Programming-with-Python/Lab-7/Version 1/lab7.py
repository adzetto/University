def main():
    number=int(input("Enter the number:"))
    if is_prime(number):
        print(f"Thu number primerly is {is_prime(number)}")
    else:
        print(f"Thu number primerly is {is_prime(number)}")
    
    
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            print(number)
            return True
    else:
        return False
    
main()