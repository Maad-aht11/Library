import random
import string
import datetime

class User:
    
    id_user_pair = {}
    id_list = []
    user_list = []
    total_library_users = 0
    total_money_owed = 0
    total_books_passed_due = 0
    
    def __init__(self, books_checked_out, books_passed_return, money_owed,
                 id, name, birthday):
        
        self._books_checked_out = books_checked_out
        self._books_passed_return = books_passed_return
        self._money_owed = money_owed

        id = random.randint(10000000, 99999999)
        while (id in self.id_list):
            id = random.randint(10000000, 99999999)
        self._id = str(id)

        name_status = False
        letter_status = False
        while (name_status == False):
            for i in name:
                if (i in string.punctuation or i.isdigit()):
                    letter_status = False
                    print("Error, you cannot have punctuation or numbers in your name")
                    name = input("Please enter your full name: ")
                    break
                else:
                    letter_status = True
            if (letter_status == True):
                name_status = True
            else:
                name_status = False
        self._name = name

        birthday_status = False
        while (birthday_status == False):
            try: 
                birthday = datetime.datetime.strptime(birthday, "%m/%d/%Y")
                birthday_status = True
            except:
                print("Incorrect date format, please try again!: ")
                birthday = input("Please enter your birthday in the following format: DD/MM/YYYY ")
        self._birthday = birthday

    @property
    def books_checked_out(self):
        return self._books_checked_out

    @property
    def books_passed_return(self):
        return self._books_passed_return
    
    @property
    def money_owed(self):
        return self._money_owed
    
    @property
    def id(self):
        return self._id
    
    @property 
    def name(self):
        return self._name
    
    @property
    def birthday(self):
        return self._birthday
    
    @books_checked_out.setter
    def books_checked_out(self, change_in_books):
        self._books_checked_out += change_in_books

    @books_passed_return.setter
    def books_passed_return(self, change_in_passed_books):
        self._books_passed_return += change_in_passed_books

    @money_owed.setter
    def money_owed(self, change_in_money):
        self._money_owed += change_in_money

    @name.setter
    def name(self, new_name):
        name_status = False
        letter_status = False
        while (name_status == False):
            for i in new_name:
                if (i in string.punctuation or i.isDigit()):
                    letter_status = False
                    print("Error, you cannot have punctuation or numbers in your name")
                    new_name = input("Enter your name: ")
                    break
                else:
                    letter_status = True
            if (letter_status == True):
                name_status = True
            else:
                name_status = False
        self._name = new_name

    @birthday.setter
    def birthday(self, new_birthday):
        birthday_status = False
        while (birthday_status == False):
            try: 
                new_birthday = datetime.datetime.strptime(new_birthday, "%d/%m/%Y")
                birthday_status = True
            except:
                print("Incorrect date format, please try again!: ")
        self._birthday = new_birthday

class Book:

    books_list = []
    available_books = [] 

    def __init__(self, name, author, release_date, language, genre, age_class, price,
                 is_checked_out):
        
        self._name = name
        self._author = author
        self._release_date = release_date
        self._language = language
        self._genre = genre
        self._age_class = age_class
        self._price = price
        self._is_checked_out = is_checked_out


    @property
    def name(self):
        return self._name
        
    @property
    def author(self):
        return self._author
        
    @property
    def release_date(self):
        return self._release_date
        
    @property
    def language(self):
        return self._language
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def age_class(self):
        return self._age_class
    
    @property
    def price(self):
        return self._price
    
    @property
    def is_checked_out(self):
        return self._is_checked_out
    
    @name.setter
    def name(self, name_to_add):
        self._name = name_to_add
    
    @author.setter
    def author(self, author_to_add):
        self._author = author_to_add

    @release_date.setter
    def release_date(self, added_release_date):
        self._release_date = added_release_date

    @language.setter
    def language(self, language_to_add):
        self._language = language_to_add

    @genre.setter
    def genre(self, genre_to_add):
        self._genre = genre_to_add

    @age_class.setter
    def age_class(self, age_class_to_add):
        self._age_class = age_class_to_add

    @price.setter
    def price(self, price_to_add):
        self._price = price_to_add

    @is_checked_out.setter
    def is_checked_out(self, status):
        self._is_checked_out = status
    
