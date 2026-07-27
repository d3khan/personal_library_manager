from library_manager import Book, Library
import json

library = Library
try: 
    with open("library.json", "r") as db:   
        cache = json.load(db)
        for i in cache:
            book = Book(i.get("Title"), i.get("Author"), i.get("Year"), i.get("Read"))
            library.add(library, book)
except Exception:
    print("Failed to load library\n\n")

while True:
    option = 0
    welcome = "Welcome to d3khan's library"
    print("-" * len(welcome))
    print(welcome)
    print("Select one of the options below to cotinue\n")
    
    print("1. Add book")
    print("2. Remove all books by title or author")
    print("3. Find a book")
    print("4. List all books in library")
    print("5. Show reading stats")
    print("6. Save")
    print("7. Save and Exit...\n")

    try:
        option = int(input("Type a number to select an option: "))
    except Exception:
        print("Type one of the numbers\n\n")
    
    if not ((option >= 1) or (option <= 6)):
        pass

    if option == 7:
        break

    if option == 6:
        with open("library.json", "w") as db:
            json.dump(library.as_array(library), db, indent=4)
        print("Saved\n\n")

    if option == 5:
        library.stats(library)

    if option == 4:
        library.display_all(library)

    if option == 3:
        print("Fill in the filters \nLeave empty to not add that filter")
        title = input("Title: ")
        author = input("Author: ")
        try:
            year = int(input("Year: "))
        except Exception:
            year = None
        is_read = input("Read y/n: ")
        read = bool

        if is_read.lower() == "y" or is_read.lower == "yes":
            read = True
        elif is_read.lower() == "n" or is_read.lower == "no":
            read = False
        else:
            read = None

        query = library.find(library, title, author, year, read)
        if len(query) < 1:
            print("Nothing Found\n\n")
        print(" ") # whitespace for formatting
        for i in query:
            print(f"Title: {i.title} | Author: {i.author} | Year: {i.year} | Read: {i.read}\n")

    if option == 2:
        print("Fill in the filters \nLeave empty to not add that filter")
        title = input("Title: ")
        author = input("Author: ")
        if len(author) < 1:
            author = None

        library.remove(library, title, author)
        if (not title == None)and (not author == None):
            print(f"All books with name {title} or by {author} have been successfully removed\n\n")
        elif not title == None:
            print(f"All books with name {title} have been successfully removed\n\n")
        elif not author == None:
            print(f"All books by {author} have been successfully removed\n\n")
        else:
            print("No title or author was given. \nNothing was deleted\n\n")

    if option == 1:
        print("Fill in the books details")
        title = input("Title: ")
        author = input("Author: ")
        try:
            year = int(input("Year: "))
        except Exception:
            year = None
        is_read = input("Read y/n: ")
        read = bool

        if is_read.lower() == "y" or is_read.lower == "yes":
            read = True
        elif is_read.lower() == "n" or is_read.lower == "no":
            read = False
        else:
            read = None

        book = Book(title, author, year, read)
        library.add(library, book)
        print(f"{title} by {author} has been added\n\n")

with open("library.json", "w") as db:
    json.dump(library.as_array(library), db, indent=4)