
books = ["Project Hail Mary", "The Hobbit", "Sherlock Holmes", 
        "The Hobbit", "Dune"]


def display_book():
    print("= Little Free Library =")
    print(f"Count: {len(books)}")
    print(f"{books}\n")


def find_book():
    user_input = input("Enter the title of a book to find: ")
    copies = books.count(user_input)
    if copies == 1:
        string = "copy"
    else:
        string = "copies"
    print(f"We have {copies} {string} of '{user_input}' available.\n")


def take_book():
    user_input = int(input("Enter the index of a book to take: "))
    print(f"you took {books[user_input]}")
    books.pop(user_input)
    print(books)


def append_book():
    user_input = input("What book would you like to leave? ")
    books.append(user_input)
    print(f"{books}\n")
    

if __name__ == "__main__":
    display_book()
    find_book()
    take_book()
    append_book()
    
