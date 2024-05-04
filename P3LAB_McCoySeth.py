"""
Seth McCoy
4/6/2024
P3LAB
LAB: Leap Year in the "Branching" chapter in ZyBook
"""
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    year = int(input())
    if is_leap_year(year):
        print(f"{year} - leap year")
    else:
        print(f"{year} - not a leap year")

if __name__ == "__main__":
    main()