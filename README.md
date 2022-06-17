# MyBookStore
This is a django project calling certain APIs related to insertion and retrieval of information about books. Basic aim of this project is to build APIs and call them to perform a specific task.

## Motivation
This project is part of the assignment provided by Happay, this assignment expects to build required API functions for a Book Model.

## What the code does?
Views.py and Models.py are main files with APIs along with other files definining application name, path etc. \
1. Models.py contains 3 classes namely Author, Book and Category. These classes contains certain fields along with some constraints depending on the reuirements.\
2. View.py contains all the required functions to insert or retrieve the model objects from database. \

### Model Classes:

1. Author: This model class contains 5 fields named Author_id,AuthorName, PhoneNumber, BirthDate and DeathDate. AuthorName and PhoneNumber should be unique in the database.\
2. Category: This model class contains 2 fields named Category_id and CategoryName only.\
3. Book: This is the main model class that uses above 2 models as a Foreign Key.This contains all the information related to books. This model has 8 fields named Title,Author,Publisher,PublishDate,Category,Price and SoldCount.\

### View Classes:

1. AuthorOperations: This class contains all the operations to be performed with Author model class. It contains below functions:\
a. addAnAuthor(authorName,phoneNumber,birthDate,deathDate): It takes 4 parameters as input and add a new Author (if not already exists).\
b. getAllAuthorName(): This function returns all the Author names available in database.\

2. CategoryOperations:\
a. addCategory(categoryName): It takes Category name as input and adds a new Category (if not already exists)\
b. getListOfCategories(): This function returns all the Categories avaialable in the database.\

3. BookOperations:\
a. addBookToCatalog(title,author,publisher,publisheddate,category,price,soldcount): This method takes 7 parameters as input and adds a new book (if Title not already exist)\
b. getMostBooksSoldByAuthor(AuthorId): Takes Author_id as input and returns the book title with highest Sold Count.\
c. getMostBooksSoldByCategory(CategoryId): Takes Category_id as input and returns the book title with highest Sold Count.\
d. searchBook(searchString): This method applies lookup in AuthorName, CategoryName and Book Title and returns all the books containing input string.\
e. getBooksByAuthor(Author_id): Takes Author_id as input and returns all the books having mentioned Author.\

## How to run the code
To run any function, I am using Command line. Below are the steps to run any method:
1. Open your django environment and go to terminal. Execute command python manage.py shell\
2. import necessary classes from views.py. Ex: from Book.views import AuthorOperations, BookOperations, CategoryOperations\
3. Create object of particular class say, book. Ex: bookObject = BookOperations()\
4. Now call the function which is required. Ex: to search a book, execute bookObject.searchBook('title1') -> Shows all the books having title1 in them. \
5. similarly, call the functions mentioned above basis requirements. \

Note: I am using python shell as the main aim of this project was to build APIs. Frontend can be implemented to view the results in more interactive way.\
