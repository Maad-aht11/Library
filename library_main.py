import csv
import time
import library
import datetime
#Test for correct email

#Create function to validate if user can check out books
def validate_check_out(id_number):
    current_user = library.User.id_user_pair.get(id_number)
    if (len(current_user.books_checked_out) >= 3):
        print("You are not allowed to check this book out because you already have 3 books checked_out")
        return False
    elif (current_user.money_owed > 0):
        print("You are not allowed to check this book out because you have an outstanding balance on yoru account")
        return False
    else:
        return True

#Create function to check out book from library
def check_out_book(user, book_index):
    user.books_checked_out.append(library.Book.books_list)
    pass

#Create function to represent loading time
def loading_time():
    print("Loading ", end="", flush=True)
    for i in range(3):
        time.sleep(1)
        print(". ", end="", flush=True)
    print("\n", flush=True)

#Create a function to simulate logging in
def log_in():
    id_input = input("Please enter your ID number to log into your profile: ")
    if (library.User.id_user_pair.get(id_input) is  None):
        print("That is not a valid id in our system")
        return False
    else:
        return True
    pass
    

#Load in libary books
with open("booksdata.csv", "r") as book_in:
    book_data = csv.reader(book_in)
    for row in book_data:
        book_name = row[0]
        if book_name == "Name":
            continue
        book_author = row[1]
        book_release_date = row[2]
        book_language = row[3]
        book_genre = row[4]
        book_age_class = row[5]
        book_price = row[6]
        book_is_checked_out = False
        book = library.Book(book_name, book_author, book_release_date, book_language, 
                            book_genre, book_age_class, book_price, book_is_checked_out)
        library.Book.books_list.append(book)

#Fill in list of books avaialble to be checked out
for book in library.Book.books_list:
    library.Book.available_books.append(book)

#Print main menu
def main_menu(simulated_date):
    print()
    print("Main Menu \n")
    print("Enter the number that corresponds with what you would like to do")
    print("------------------------------------------------------- \n")
    print("1. View all of the library's books")
    print("2. View all books available for check out (requires sign in)")
    print("3. View profile information")
    print("4. Create a user profile")
    print("5. Simulate 1 week passing")
    print("6. Exit the program \n")
    print (f"Current date: {simulated_date.strftime("%m/%d/%Y")}")
    print("-------------------------------------------------------")


#Run program
simulated_date = datetime.datetime.now()
print("Welcome to Maad's Library! \n")
main_menu(simulated_date)
user_input = input()
while (user_input != 5):

    if (user_input == '1'):
        loading_time()
        for book in library.Book.books_list:
            print(book.name)

    elif (user_input == '2'):
        id_input = input("Please enter your ID number to validate your profile: ")
        if (library.User.id_user_pair.get(id_input) is  None):
            print("That is not a valid id in our system")
        else:
            loading_time()
            increment = 1
            for book in library.Book.available_books:
                    print(f"{increment}. {book.name}")
                    increment += 1
            book_num_input = input("Enter the number corresponding with the book you want to check out \n" \
            "If you want to return to the main menu, type 'x' ")
            print("")
            if (book_num_input.lower() == 'x'):
                continue
            else:
                book_num_input = int(book_num_input)
                is_allowed = validate_check_out(id_input)
                if (is_allowed):
                    current_user = library.User.id_user_pair.get(id_input)
                    current_user.books_checked_out.update({ datetime.datetime.now(): library.Book.available_books[book_num_input-1]})
                    print(f"You successfully checked out {library.Book.available_books[book_num_input-1].name}")
                    library.Book.available_books.pop(book_num_input-1)
                    library.Book.books_list[book_num_input-1].is_checked_out = True

    elif (user_input == '3'):
        id_input = input("Please enter your ID number to validate your profile: ")
        if (library.User.id_user_pair.get(id_input) is  None):
            print("That is not a valid id in our system")
        else:
            current_user = library.User.id_user_pair.get(id_input)
            print("--------- User Profile Hub --------- \n \n \n")   
            print("1. View checked out books")
            print("2. View books passed return")
            print("3. Return a book")
            print("4. Pay an outstanding balance ")
            print(f"Current balance owed: {current_user.total_money_owed}")
            print("------------------------------------")
            choice_input = input("Enter the option you would like to choose")
            if (choice_input == '1'):
                print("--------- Checked out books ---------")
                for date, book in current_user.books_checked_out.items():
                    print(f"You checked out {book.name} on {date.strftime("%m/%d/%Y")}")
            elif (choice_input == '2'):
                print("--------- Books passed return ---------")
                for date, book in current_user.total_books_passed_due.items():
                    print(f"{book.name} needed to be returned by {date.strftime("%m/%d/%Y")}")
            elif (choice_input == '4'):
                amount_to_pay = input("Please enter how much of your balance you would like to pay off")
    elif (user_input == '4'):
        print("Thank you for choosing to become a user")
        entered_name = input("Please enter your full name: ")
        enetered_birthday = input("Please enter your birthday in the following format: DD/MM/YYYY ")
        user = library.User(books_checked_out={}, books_passed_return=0, money_owed=0, id=None,
                            name=entered_name, birthday=enetered_birthday)
        library.User.id_user_pair.update({user.id:user})
        print(f"You have now been registered as a user and your unique id is {user.id}")

    elif (user_input == '5'):
        simulated_date = simulated_date + datetime.timedelta(days=7)
        for user in library.User.id_user_pair.values():
            if (len(user.books_checked_out) > 0):
                for date_checked_out, book in user.books_checked_out.items():
                    return_date = date_checked_out+datetime.timedelta(days=14)
                    if (simulated_date > return_date):
                        user.total_money_owed += 10
                    user.total_books_passed_due.update({return_date:book})

    main_menu(simulated_date)
    user_input = input()
    
