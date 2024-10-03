class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:  #If the book is not checked out
            self._is_checked_out = True   #It is checked out
            return True
        return False         #If it was already checked out
        
    def return_book(self):
        if self._is_checked_out: #If the book was checked out
            self._is_checked_out = False #It is back in the box
            return True
        return False #If it wasn't checked out
    
    def is_available(self):
        return not self._is_checked_out    #If the book is available to read
        
    


class Library:
    
    def __init__(self):
        self._books = []      #Empty list for the books
        

    def add_book(self, book):
        self._books.append(book)     #Add the new book in the box

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True
            
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(book.title)

    

            


    
    

