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

    respose = requests.get(API_URL, params=params)
    data = respose.json()
    docs = data.get("docs", [])
    return docs

# Choosing fields to save
def filter_and_save(docs):
    fields = ["title", "author_name", "first_publish_year", "publisher"]

    # Filtering and saving books to the CSV file

    saved_books_num = 0

    with open("books.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for doc in docs:
            first_publish_year = doc.get("first_publish_year")
        
            if (first_publish_year > 2000):
                row = {
                    "title": doc.get("title"),
                    "author_name": doc.get("author_name"),
                    "first_publish_year": doc.get("first_publish_year"),
                    "publisher": doc.get("publisher"),
                }
                writer.writerow(row)

                saved_books_num += 1
    
    return saved_books_num

# Sending "Success Message"



if __name__ == "__main__":
    q = get_query()
    docs = fetch_API(q)
    saved_num = filter_and_save(docs)

    print("Saved", saved_num, "books in books.csv")