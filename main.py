import requests
import csv

# Getting user query

query = ""

print("What is your query?")

while (len(query) < 3):
    query = input()

# Using API to get response

API_URL = 'https://openlibrary.org/search.json'
LIMIT = 50

params = {
    "limit": LIMIT,
    "q":query
}

respose = requests.get(API_URL, params=params)
data = respose.json()
docs = data.get("docs", [])

# Choosing fields to save

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

# Sending "Success Message"

print("Saved", saved_books_num, "books to books.csv")