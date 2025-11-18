#!/usr/bin/env python3
"""
Simple Python Script - Greeting Program
"""
# Test Jira automation and GitHub ruleset




def main():
    # Get user's name
    name = input("What's your name? ")

    # Get user's age
    age = input("How old are you? ")

    # Print greeting
    print(f"\nHello, {name}! You are {age} years old.")

    # Simple calculation
    try:
        age_num = int(age)
        years_to_100 = 100 - age_num
        print(f"You have approximately {years_to_100} years until you turn 100!")
    except ValueError:
        print("Please enter a valid number for age next time!")

if __name__ == "__main__":
    main()
