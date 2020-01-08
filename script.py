import utils
import sorts

def by_title_ascending(book_a, book_b):
    return book_a["title_lower"] > book_b["title_lower"]

bookshelf = utils.load_books("books_small.csv")
# for book in bookshelf:
#     print(book["title"])

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
    print(book["title"])
