# Program to check eligibility based on age and citizenship

# Input
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen (yes/no): ").lower()

# Check eligibility
if age >= 18 and citizenship == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
