class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
    
    
    def open():
        return ("Openning......")
        
    def close():
        return ("Closing... the book")
        
book = Book("The Hobbit",356)
print(book.title)
print(book.pages) 
print(Book.open())
print(Book.close())

