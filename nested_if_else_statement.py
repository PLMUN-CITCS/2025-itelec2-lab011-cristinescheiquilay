age_str = input("Enter your age: 20 ")
membership_str = input("Are you a member? (Yes/No): no ")
age = int(age_str)
membership = membership_str.strip().lower()
if age >= 18:
    if membership == "yes":
        print("Access granted.")
    else:
        print("Membership required for access.")
else:
    print("Access denied. Must be at least 18 years old.")
