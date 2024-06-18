"""
Author: Muhammet Yağcıoğlu
Date Created: Thu, 7 Mar, 2024
Last Modified: Thu, 7 Mar, 2024

Purpose:
Calculate the percentage distribution of males and females in a classroom setting.

Time Spent on Development: Approximately 10 minutes
"""

def safe_input(prompt, error_msg="Invalid input. Please enter a non-negative integer."):
    validate_input = lambda input_text: (int(input_text) if input_text.isdigit() and int(input_text) >= 0 else None)
    while True:
        user_input = validate_input(input(prompt))
        if user_input is not None:
            return user_input
        print(error_msg)

def calculate(n_m, n_f):
    total = n_m + n_f
    if not total:
        print("No students are registered in the class.")
        return
    
    print(f"Percentage of males in the class: {n_m / total * 100:.2f}%")
    print(f"Percentage of females in the class: {n_f / total * 100:.2f}%")

if __name__ == "__main__":
    n_m = safe_input("Enter the number of males registered in the class: ")
    n_f = safe_input("Enter the number of females registered in the class: ")
    calculate(n_m, n_f)