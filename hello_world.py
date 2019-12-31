import random


def main():
    pass


if __name__ == "__main__":
    main()


def ask_user_info():
    age = input('What is your age?\n')
    name = input('What is your name?\n')
    print('Hello. nice to meet you ' + name)


def calculate():
    principal = float(input('What is your initial capital?'))
    interest = float(input('What is the interest rate?'))
    years = int(input('How long are you planning to invest?'))
    for i in range(years):
        total = principal * float((1 + interest) ** float(i + 1))
        print(f"{i + 1} year and the total is {total:.2f}")


# Similar to do while loop
def test():
    while True:
        try:
            num = int(input("Please enter a number: "))
            break
        except ValueError:
            print('Enter a number you dumb fuck, not a letter ')

    print(num)


def print_shit():
    for i in range(1, 22):
        if i % 2 != 0:
            print(i)


def guess_number():
    secret_number = 7
    while True:
        guess = int(input('Please enter a number: '))
        if guess == secret_number:
            print('You guessed it')
            break
        else:
            print('Please try again!')


def string_functions(string):
    new = []
    for c in string:
        r = random.randint(0, 1)
        if r == 0:
            new.append(c.upper())
        else:
            new.append(c.lower())
    return ''.join(new)


print(string_functions("Hello, testing new function"))


def hide_string():
    message = str(input("Please enter a string in uppercase: "))
    secret_message = ""
    for c in message:
        secret_message += str(ord(c) - 23)  # works with both lower and uppercase

    norm_string = ""
    for c in range(0, len(secret_message) - 1, 2):
        char_code = secret_message[c] + secret_message[c + 1]
        norm_string += chr(int(char_code) + 23)  # works with both lower and uppercase

    print(f"the secret message converted to Unicode {secret_message}")
    print(f"original message is {norm_string}")


# hide_string()


def caesar_cypher():
    message = input("Please enter a message: ")
    unit_shift = int(input("Please enter the key to be shifted from 1 to 26 (a - z): "))
    encrypted_message = cipher_helper(message, unit_shift)

    print(f"The encrypted message is: {cipher_helper(message, unit_shift)}")
    print(f"The decrypted message is: {cipher_helper(encrypted_message, -unit_shift)}")


def cipher_helper(message, unit_shift) -> str:
    new_message = ""
    for char in message:
        # Convert the character at i index message into Unicode and add unit shift to it
        char_encode = ord(char)
        char_encode += unit_shift
        # If the character at said index is an alphabetical letter then do these
        if char.isalpha():
            if char.isupper():
                if char_encode > ord("Z"):
                    char_encode -= 26
                elif char_encode < ord("A"):
                    char_encode += 26
            else:
                if char_encode > ord("z"):
                    char_encode -= 26
                elif char_encode < ord("a"):
                    char_encode += 26
            new_message += chr(char_encode)
        else:
            new_message += char

    return new_message


caesar_cypher()



