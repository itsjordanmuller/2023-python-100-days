from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
# with app.app_context():
#     new_book = Book(
#         id=1, title="The Sixth Extinction", author="Elizabeth Kolbert", rating=9.8
#     )
#     db.session.add(new_book)
#     db.session.commit()

# READ ALL RECOrDS
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()
#     print(all_books)

# READ A SPECIFIC RECORD BY QUERY
# with app.app_context():
#     book = db.session.execute(
#         db.select(Book).where(Book.title == "The Sixth Extinction")
#     ).scalar()

# UPDATE A RECORD BY QUERY
# with app.app_context():
#     book_to_update = db.session.execute(
#         db.select(Book).where(Book.title == "The Sixth Extinction")
#     ).scalar()
#     book_to_update.rating = "9.9"
#     db.session.commit()

# UPDATE A RECORD BY PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(
#         db.select(Book).where(Book.id == book_id)
#     ).scalar()
#     book_to_update.title = "The Sixth Extinction: An Unnatural History"
#     db.session.commit()

# DELETE A SPECIFIC BOOK BY PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     db.session.delete(book_to_delete)
#     db.session.commit()
