"""HW6.4 Little Free Library Kiosk TUI.

Author: Enzo Hins
Version: 9/29/2025
"""

from library import inventory, list_books, search_books, remove_book, add_book


prompt = """===================================
Welcome to the Little Free Library!
===================================

This kiosk supports the following actions:

1. List the books
2. Search for a book by title
3. Take a book (let us know which title you're taking)
4. Give a book (let us know that you're donating or returning a title)
0. Exit

Please enter the number for the action you wish to perform:
"""


def main(books):
    """Provide a Text-based User Interface for the Little Library.

    Args:
        books (list): a list of book titles (strings)

    Returns:
        action_log (list): a list of actions performed by the user
    """

    action_log = []

    while (True):
        print(prompt)
        choice = input()

        if choice == "List":
            action_log.append("1")
            books_length = len(list_books(books))
            print(f"Listed {books_length} books of the {books} in inventory \n")

        elif choice == "Search":
            action_log.append("2")
            search_query = input("Enter book title (or part of it) to search for: ")
            print(f"Results: {search_books(books, search_query)}")

        elif choice == "Remove":
            action_log.append("3")
            remove_query = input("Enter the book title you are taking: ")
                
            if (remove_book(books, remove_query)):
                print(f"Enjoy reading {remove_query}!")
                    
            else:
                print(f"Sorry, we don't have {remove_query} right now.")

        elif choice == "Add":
            action_log.append("4")
            add_query = input("Enter the title you are donating or returning: ")
            new_length = add_book(books, add_query)
            print("Thank you for your donation! The Little Free" 
            + f"Library now has {new_length} books.")
                
        elif choice == "Exit":
            print("Thank you for visiting the Little Free Library!")
            return action_log
        
        else:
             print("Invalid choice: WRONG THING THEY ENTERED")
            

if __name__ == "__main__":
    # the imported inventory is a collection of 3 different sized libraries for
    # your testing purposes, try them all!
    lib = inventory["small"]
    # lib = inventory["medium"]
    # lib = inventory["large"]

    print(main(lib))
