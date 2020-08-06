"""
Use top-down design to write at least two
functions that implement an addressbook application
"""

def addressbook():
    print("1) Look up a person by last name\n" + "2) Add a person to the address book\n" + "3) Quit\n")

    sel = input("Enter your choice: ")

    if sel == '1':
        find_last_name = input('Please enter the last name to look up: ')
        address_book = open("texts/addressbook.txt", "r")
        eof = False
        last_data_list = []
        while not eof:
            for i in range(6):
                last_data_list.append(address_book.readline().rstrip())

            if last_data_list[0] == find_last_name:
                eof = True
                print(last_data_list[0] + " " + last_data_list[1] + "\n" +
                    last_data_list[2] + "\n" + last_data_list[3] + "\n" + last_data_list[4] + "\n" + last_data_list[5])

            elif last_data_list[0] == '':
                eof = True
                print("Sorry no correspondence.")

        address_book.close()

    elif sel == '2':
        last_name = input('Please enter the last name: ')
        name = input('Please enter the name: ')
        street = input('Please enter the street: ')
        city_state_zip = input('Please enter the city, the state, and the zip code: ')
        home_phone = input('Please enter the home phone: ')
        mobile_phone = input('Please enter the last name: ')
        address_book = open("texts/addressbook.txt", "a")

        address_book.write(last_name)
        address_book.write("\n")
        address_book.write(name)
        address_book.write("\n")
        address_book.write(street)
        address_book.write("\n")
        address_book.write(city_state_zip)
        address_book.write("\n")
        address_book.write(home_phone)
        address_book.write("\n")
        address_book.write(mobile_phone)

        address_book.close()

    else:
        print('Done')


def main():
    addressbook()

if __name__ == "__main__":
    main()