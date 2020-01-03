import os
from sys import argv


# sys.argv is a list in python, which contains the command-line arguments passed to the script.
def test_read_file():
    with open("./data2.txt", mode="r",  encoding="utf-8") as my_file:
        line_num = 1
        while True:
            line = my_file.readline()
            if not line:
                break
            print(f"Line {line_num} : {line}", end="")


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
    test_read_file_2()
    print(os.getcwd())


if __name__ == '__main__':
    main()
