#!/usr/bin/env python3


# built-in classes: int, float, bool, int

# assert is a keyword in Python that takes conditional expression
    # >>> if expression True, nothing happens. If False, program will crash
    # assert is used for testing purposes


class Book:
    
    def __init__(self, title, author=''):
        self.title = title
        self._page_count = None

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, new_page_count):
        if type(new_page_count) != int:
            print("page_count must be an integer")
        else:
            self._page_count = new_page_count

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

if __name__ == '__main__': # testing out the set_page_count function
    book = Book('The Road')
    book.set_page_count('some string')

