import os
import json

LIBRARY_FILE = "library.txt"

class Book:
    def __init__(self, title, author, year, genre, read):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read = read  # Boolean

    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"{self.title} by {self.author} ({self.year}) - {self.genre} - {status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "read": self.read
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["author"],
            data["year"],
            data["genre"],
            data["read"]
        )


class LibraryManager:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self):
        print("\nAdding a Book")
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = input("Enter the publication year: ")
        genre = input("Enter the genre: ")
        read_input = input("Have you read this book? (yes/no): ").strip().lower()
        read = read_input == "yes"
        self.books.append(Book(title, author, year, genre, read))
        print("Book added successfully.")

    def remove_book(self):
        print("\nRemoving a Book")
        title = input("Enter the title of the book to remove: ").strip()
        original_len = len(self.books)
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        if len(self.books) < original_len:
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def search_book(self):
        print("\nSearch for a Book")
        print("Search by:\n1. Title\n2. Author")
        choice = input("Enter your choice: ").strip()
        query = input("Enter your search term: ").strip().lower()

        matches = []
        if choice == "1":
            matches = [book for book in self.books if query in book.title.lower()]
        elif choice == "2":
            matches = [book for book in self.books if query in book.author.lower()]

        if matches:
            print("\nMatching Books:")
            for i, book in enumerate(matches, 1):
                print(f"{i}. {book}")
        else:
            print("No matching books found.")

    def display_books(self):
        print("\nYour Library:")
        if not self.books:
            print("No books in your library yet.")
        else:
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def display_stats(self):
        print("\nLibrary Statistics:")
        total = len(self.books)
        read_count = sum(1 for book in self.books if book.read)
        percentage = (read_count / total * 100) if total > 0 else 0
        print(f"Total books: {total}")
        print(f"Percentage read: {percentage:.1f}%")

    def save_books(self):
        with open(LIBRARY_FILE, "w") as f:
            json.dump([book.to_dict() for book in self.books], f)
        print("Library saved successfully.")

    def load_books(self):
        if os.path.exists(LIBRARY_FILE):
            with open(LIBRARY_FILE, "r") as f:
                try:
                    data = json.load(f)
                    self.books = [Book.from_dict(item) for item in data]
                    print("Library loaded from file.")
                except json.JSONDecodeError:
                    print("Error reading library file. Starting with an empty library.")
        else:
            print("No saved library found. Starting with an empty library.")

    def main_menu(self):
        while True:
            print("\nWelcome to your Personal Library Manager!")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_stats()
            elif choice == "6":
                self.save_books()
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = LibraryManager()
    manager.main_menu()
