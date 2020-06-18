"""
Write a menu driven program that works with an address book file. Your program should have three menu
items, look up a name, add a contact, and quit.
"""

print("1) Look up a person by last name\n" + "2) Add a person to the address book\n" + "3) Quit\n")

sel = input("Enter your choice: ")

if sel == '1':
    find_last_name = input('Please enter the last name to look up: ')
    address_book = open("texts/addressbook.txt", "r")
    eof = False
    while not eof:
        last_name = address_book.readline().rstrip()
        first_name = address_book.readline().rstrip()
        street = address_book.readline().rstrip()
        city_state_zip = address_book.readline().rstrip()
        home_phone = address_book.readline().rstrip()
        mobile_phone = address_book.readline().rstrip()

        if last_name == find_last_name:
            eof = True
            print(first_name + " " + last_name + "\n" +
                  street + "\n" + city_state_zip + "\n" + home_phone + "\n" + mobile_phone)

        elif last_name == '':
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
