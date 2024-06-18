# -*- coding: utf-8 -*-

"""
Pay Calculation Module

Author: Muhammet Yagcioglu
Description: This module calculates total and overtime pay based on input hours and rate.
Creation Date: March 13, 2024
Time Spent: 1 hours
Safety-Critical Compliance: Yes.

Note: Assumes a maximum of 168 hours in a week to avoid unbounded loops and ensure static loop bound verification.
"""

def calculate_pay(hour_worked: float, hourly_rate: float) -> tuple:
    """
    Calculates the total pay, considering regular and overtime payments.
    
    Parameters:
        hour_worked (float): Hours worked in a week. Must be in the range [0, 168].
        hourly_rate (float): Payment rate per hour.
    
    Returns:
        tuple: Contains overtime pay and total pay.
    
    Raises:
        ValueError: If input values are out of expected range.
    """
    
    # Input validation to ensure safety and reliability in critical applications
    if not (0 <= hour_worked <= 168) or hourly_rate < 0:
        raise ValueError("Invalid input: Hours worked must be between 0 and 168, and hourly rate must be non-negative.")
    
    # Fixed upper bound for hours worked
    regular_hours = min(hour_worked, 40)
    overtime_hours = max(0, hour_worked - 40)
    
    # Avoiding complex control flow
    overtime_pay = overtime_hours * hourly_rate * 1.5
    regular_pay = regular_hours * hourly_rate
    
    total_pay = regular_pay + overtime_pay
    return (overtime_pay, total_pay)

# Main execution
if __name__ == "__main__":
    try:
        # Simple input handling
        hour_worked = float(input("Enter the hour worked: "))
        hourly_rate = float(input("Enter the hourly rate: "))
        
        overtime_pay, total_pay = calculate_pay(hour_worked, hourly_rate)
        print(f"Overtime Pay: {overtime_pay}")
        print(f"Total Pay: {total_pay}")
        
    except ValueError as e:
        print(f"Input error: {e}")
