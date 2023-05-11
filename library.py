class Book:
    def __init__(self, title, author, number_of_pages, type_of_book):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.type_of_book = type_of_book

    def print_info(self):
        print(
            f"The title of this book is {self.title}. It was written by {self.author}. "
            "It has {self.number_of_pages} pages. The type of this book is {self.type_of_book}"
        )


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_books(self):
        for book in self.books:
            book.print_info()

    def borrow_book(self, title):
        title = title.lower()
        matched_books = list(
            filter(lambda book: book.title.lower() == title, self.books)
        )
        if matched_books:
            self.books.remove(matched_books[0])
            return matched_books[0]
        return None


csclibrary = Library()


def get_books_from_text_file():
    with open("books.txt", "r") as book_file:
        books_info = book_file.readlines()
        books_detail_map = []
        for book in books_info:
            book = book.strip()
            book_infos = book.split(",")
            book_detail_map = {
                "Title": "",
                "Author": "",
                "Number of Pages": "",
                "Type of Book": "",
            }
            for book_info in book_infos:
                key, value = book_info.split(":", 1)
                book_detail_map[key.strip()] = value.strip()
            books_detail_map.append(book_detail_map)
    return books_detail_map


# print(get_books_from_text_file())
def create_books_from_file():
    books_detail = get_books_from_text_file()
    list_of_books = []
    for book_detail in books_detail:
        book = Book(
            title=book_detail["Title"],
            author=book_detail["Author"],
            number_of_pages=book_detail["Number of Pages"],
            type_of_book=book_detail["Type of Book"],
        )
        list_of_books.append(book)
    return list_of_books


def add_books_to_library():
    list_of_books = create_books_from_file()
    for book in list_of_books:
        csclibrary.add_book(book)


def main():
    add_books_to_library()
    csclibrary.print_books()
    while True:
        title = input("Enter the title of the book you want to borrow: ")
        borrow_response = csclibrary.borrow_book(title)
        if borrow_response is None:
            continue
        else:
            csclibrary.print_books()
            break


if __name__ == "__main__":
    main()
