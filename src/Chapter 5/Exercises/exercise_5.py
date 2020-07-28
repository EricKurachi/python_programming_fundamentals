"""
Write a function called allEvens that given a list of integers, returns a new list
containing only the even integers
"""

def all_evens(integers_list):
    evens_list = []
    for n in integers_list.split():
        if int(n) % 2 == 0:
            evens_list.append(n)
    return evens_list

def main():
    integers_list = input("Please enter a list of integers separating each number with a space: ")
    evens = all_evens(integers_list)
    print(evens)


if __name__ == "__main__":
    main()