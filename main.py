import requests
import csv

# Defining constant variables

API_URL = 'https://openlibrary.org/search.json'
LIMIT = 50

# Getting user query
def get_query():
    query = ""

    while True:
        print("What is your query?")
        query = input().strip()
        if (len(query) >= 3):
            return query
        print("The query should be atleast 3 characters")


# Using API to get response
def fetch_API(query:str):

    params = {
        "limit": LIMIT,
        "q":query
    }

    try:
        respose = requests.get(API_URL, params=params)
        data = respose.json()
        books = data.get("docs", [])
        return books
    except:
        raise ValueError("The API couldn't fetch with Openlibrary")


# Filtering all the books to after year 2000
def filtering(books):
    try:
        return filter(lambda x: x["first_publish_year"] > 2000, books)
    except:
        raise ValueError("There was an error while filtering the books (docs)")

# Saving books to the books.csv file
def save(books_filtered):

    # Choosing fields to save, and starting the counter
    fields = ["title", "author_name", "first_publish_year", "publisher"]
    saved_books_num = 0

    # Starting the process, using CSV writer
    try:
        with open("books.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()

            for book in books_filtered:
                    row = {
                        "title": book.get("title"),
                        "author_name": book.get("author_name"),
                        "first_publish_year": book.get("first_publish_year"),
                        "publisher": book.get("publisher"),
                    }
                    writer.writerow(row)

                    saved_books_num += 1
    
        return saved_books_num
    except:
        raise ValueError("There was an error saving filtered books (docs) into books.csv")

if __name__ == "__main__":
    q = get_query()
    books = fetch_API(q)
    filtered_books = filtering(books)
    saved_num = save(filtered_books)

    # Sending "Success Message"
    print("Saved", saved_num, "books in books.csv")