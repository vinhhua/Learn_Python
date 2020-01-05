import os
from sys import argv


# sys.argv is a list in python, which contains the command-line arguments passed to the script.
def test_read_file():
    path = os.getcwd()
    with open(path, mode="r",  encoding="utf-8") as my_file:
        line_num = 1
        while True:
            line = my_file.readline()
            if not line:
                break
            print(f"Line {line_num} : {line}", end="")
            line_num += 1


def write_file():
    path = "./data2.txt"
    text = "Add this into the file\n"
    try:
        my_file = open(path, mode='a', encoding="utf-8")
    except FileNotFoundError as err:
        print("The file you're looking for does not exist")
        print(err.args)
    else:
        my_file.write(text)
        my_file.close()
    finally:
        print("File closed.")


def test_read_file_2():
    try:
        my_file = open("./data2.txt", mode="r", encoding="utf-8")
    except FileNotFoundError as err:
        print("The file you're looking for is not found")
        print(err.args)
    else:
        print("File: ", my_file.read())
        my_file.close()
    finally:
        print("File closed.")


def main():
    write_file()
    test_read_file_2()
    print(os.getcwd())


if __name__ == '__main__':
    main()
