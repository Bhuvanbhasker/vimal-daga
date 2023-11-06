import pymongo

# Connect to the MongoDB server (replace with your MongoDB connection string)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or access a database
db = client["bookstore"]

# Create or access a collection within the database
collection = db["books"]

# Create
def create_book(title, author):
    data = {"title": title, "author": author}
    collection.insert_one(data)
    print(f"Book '{title}' by {author} added to the collection.")

# Read
def list_books():
    books = collection.find()
    print("Books in the collection:")
    for book in books:
        print(f"- {book['title']} by {book['author']}")

# Update
def update_book(title, new_author):
    update_query = {"title": title}
    new_data = {"$set": {"author": new_author}}
    collection.update_one(update_query, new_data)
    print(f"Book '{title}' updated with a new author: {new_author}.")

# Delete
def delete_book(title):
    delete_query = {"title": title}
    collection.delete_one(delete_query)
    print(f"Book '{title}' deleted from the collection.")

if __name__ == "__main__":
    # Example usage
    create_book("The Great Gatsby", "F. Scott Fitzgerald")
    create_book("To Kill a Mockingbird", "Harper Lee")
    list_books()
    update_book("The Great Gatsby", "Ernest Hemingway")
    delete_book("To Kill a Mockingbird")
