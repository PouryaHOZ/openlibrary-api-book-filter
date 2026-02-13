import requests
import csv

# Getting user query

query = ""

print("What is your query?")

while (len(query) < 3):
    query = input()

# Using API to get response

url = 'https://openlibrary.org/search.json'

params = {
    "first_publish_in": "[2000+TO+*]",
    "limit": 50,
    "q":query
}

respose = requests.get(url, params=params)
data = respose.json()
docs = data.get("docs", [])

# Choosing fields to save

fields = ["title", "author_name", "first_publish_year", "publisher"]

# Saving books to the CSV file

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for doc in docs:
        row = {
            "title": doc.get("title"),
            "author_name": doc.get("author_name"),
            "first_publish_year": doc.get("first_publish_year"),
            "isbn": doc.get("isbn"),
        }
        writer.writerow(row)

# Sending "Success Message"

print("Saved", len(docs), "books to books.csv")