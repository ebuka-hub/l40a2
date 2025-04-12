class Libary:
    def __init__(self, name):

        self.name = name
        self.books = []

        def add_book(self, book_name):

            self.books.append(book_name)
            print(f""{book_name})

            def show_books(self):

                if self.books:
                    print(f"\n  books available in {self.name}:")
                    for book in self.books:
                        print(f"- {book}")
                else:
                    print("NO books in the libary!")

            def borrow_book(self, book_name):

                if book_name in self.books:
                    self.bookd.remove(book_name)
                    print(f'You borrowed "{book_name}".Enjoy reading!')
                else:
                    print(f'Sorry, "{book_name}"nis not avaliable!')

                    #create a Libary object
                    my_libary = Libary("Kids Libary")

                    # Add books
                    my_libary.add_book("Harry Potter")
                     my_libary.add_book("Alice in wonderland")
                      my_libary.add_book("Charlie and the chocolate Factory")

                      #show available books
                      my_libary.show_books()
