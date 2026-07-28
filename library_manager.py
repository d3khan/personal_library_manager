class Book:
    '''
    Class for creating books
    '''

    title = str
    author = str
    year = int
    read = bool

    def __init__(self, title=str, author=str, year=int, read=bool):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def as_dict(self):
        cache = {
            "Title": self.title,
            "Author": self.author,
            "Year": self.year,
            "Read": self.read
        }
        return cache


class Library:
    '''
    Class for managing books.
    '''

    shelf = [Book]
    shelf.clear() # to remove junk
    space_size = 0

    def __init__(self):
        for i in self.shelf:
            if self.space_size < len(i.title):
                self.space_size = len(i.title)

    def as_array(self):
        cache = [i.as_dict() for i in self.shelf]
        return cache 

    def add(self, book=Book):
        '''Add a book to this library'''
        self.shelf.append(book)

    def remove(self, title=str|None, author=str|None):
        '''Remove a book(s) from this library'''
        for i in self.shelf:
            if title == i.title or author == i.author:
                self.shelf.remove(i)

    def find(self, title=str | None, author=str | None, year=int | None, read=bool | None):
        '''Find all books with matching title, author, year or if read (case sensitive)'''

        matches = [Book]
        matches.clear() # to remove junk

        if title == None and author == None and year == None and read == None:
            return matches

        matches = [i for i in self.shelf if i.title == title or i.author == author or i.year == year or i.read == read]
        return matches
    
    def display_all(self):
        '''Shows all books in this library'''

        # space = self.space_size # I don't know how to use a variable to format f-strings
        if len(self.shelf) < 1:
            print("This library is empty\n\n")
        
        helper_var = " "
        print(f"\nTitle{helper_var:65} | Author{helper_var:29} | Year{helper_var}| Read{helper_var}")
        for i in self.shelf:
            print(f"{i.title:70} | {i.author:35} |{i.year:5} | {i.read}\n")
            # I don't know how to format it properly
            # I now do
    
    def stats(self):
        read = 0
        for i in self.shelf:
            if i.read:
                read+=1

        print(f"{read} out of {len(self.shelf)} books read\n\n")