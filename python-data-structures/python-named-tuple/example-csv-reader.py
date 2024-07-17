import csv
from collections import namedtuple

# Define a namedtuple for the CSV data
Book = namedtuple('Book', ['title', 'author', 'year'])

# Read data from a CSV file
with open('books.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row
    books = [Book._make(row) for row in reader]

# Accessing book data
for book in books:
    print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')