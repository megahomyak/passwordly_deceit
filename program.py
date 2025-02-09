import itertools

passwords = ["stupidfox", "bignosey"]

current_passwords = []
for count in itertools.count(1):
    postfix = (
        "st" if count == 1 else
        "nd" if count == 2 else
        "rd" if count == 3 else
        "th"
    )
    nth_password = input(f"Enter the {count}{postfix} password: ")
    current_passwords.append(nth_password)
    if current_passwords == passwords:
        print("Access granted.")
        break
