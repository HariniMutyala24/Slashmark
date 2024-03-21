import random

def generate_passwords(lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    generated_pw_list = []

    for length in lengths:

        password = ""
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]

        password = replace_with_digit(password)
        password = replace_with_capital_letter(password)

        generated_pw_list.append(password)

    return generated_pw_list

def replace_with_digit(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password) // 2)
        password = password[:replace_index] + str(random.randrange(10)) + password[replace_index + 1:]
    return password

def replace_with_capital_letter(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password) // 2, len(password))
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def main():
    num_pws = int(input("How many passwords do you want to generate? "))

    print("Generating " + str(num_pws) + " passwords")

    pw_lengths = []

    print("Minimum length of password should be 3")

    for i in range(num_pws):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        pw_lengths.append(length)

    passwords = generate_passwords(pw_lengths)

    for i, pw in enumerate(passwords, start=1):
        print("Password #" + str(i) + " = " + pw)

main()
