import datetime
import sys

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from Book.models import Book, Category, Author

# Create your views here.
from django.views import View


def index(request):
    return HttpResponse("This is My Book Store Application")


class CategoryOperations(View):

    def validateCategory(self,name):
        if Category.objects.filter(CategoryName = name).exists():
            return False
        else:
            return True

    def addCategory(self, categoryName):
        if not self.validateCategory(categoryName):
            print("Category already exits")
        else:
            try:
                Category.objects.create(CategoryName=categoryName)
                print('Success')
            except:
                print('Oops! ', sys.exc_info()[0], ' Occured')

    def getListOfCategories(self):
        categoryObject = Category.objects.all()
        for i in categoryObject:
            print(i.CategoryName)


class AuthorOperations(View):

    def validateName(self,name):
        if len(name)>30 or Author.objects.filter(AuthorName = name).exists():
            return False
        else:
            return True

    def validatePhone(self,phone):
        if len(phone)<=15 and phone.isdigit() and (not Author.objects.filter(PhoneNumber = phone).exists()):
            return True
        else:
            return False

    def validateDate(self,date):
        try:
            datetime.datetime.strptime(date,'%Y-%m-%d')
            return True
        except:
            return False


    def addAnAuthor(self, authorName, phoneNumber, birthDate, deathDate):
        if not self.validateName(authorName):
            print('Name of Author either already exists or length <= 30 characters')
        elif not self.validatePhone(phoneNumber):
            print('Phone number either already present or invalid!!! (should contain only digits with len<=15 digits)')
        elif not (self.validateDate(birthDate) and self.validateDate(deathDate)):
            print('Date should be in format YYYY-MM-DD and Month and Days should be valid')
        elif birthDate > deathDate:
            print('Birthdate cant be later than deathdate')
        else:
            try:
                Author.objects.create(AuthorName=authorName, PhoneNumber=phoneNumber,
                                                     BirthDate=birthDate, DeathDate=deathDate)
                print('Success')
            except:
                print('Oops! ', sys.exc_info()[0], ' Occured')

    def getAllAuthorName(self):
        authorObject = Author.objects.all()
        for i in authorObject:
            print(i.AuthorName)

class BookOperations(View):

    def validateTitle(self,title):
        if len(title)>50 or len(title)<0 or Book.objects.filter(Title = title).exists():
            return False
        else:
            return True

    def isPresentAuthor(self,author):
        if Author.objects.filter(AuthorName = author).exists():
            return True
        else:
            return False

    def validatePublisher(self,publisher):
        if len(publisher)>50:
            return False
        else:
            return True

    def validateDate(self,date):
        try:
            datetime.datetime.strptime(date,'%Y-%m-%d')
            return True
        except:
            return False

    def isPresentCategory(self,category):
        if Category.objects.filter(CategoryName = category).exists():
            return True
        else:
            return False

    def addBookToCatalog(self,title,author,publisher,publishdate,category,price,soldcount):
        if not self.validateTitle(title):
            print("Title should be <50 character length and shouldn't be already present")
        elif not self.isPresentAuthor(author):
            print('Author Name doesnt exist')
        elif not self.validatePublisher(publisher):
            print('Publisher name should be <=50 characters')
        elif not self.validateDate(publishdate):
            print('Date should be in format YYYY-MM-DD and Month and Days should be valid')
        elif not self.isPresentCategory(category):
            print('Category name doesnt exist')
        else:
            try:
                authorObject = Author.objects.get(AuthorName = author)
                categoryObject = Category.objects.get(CategoryName = category)
                Book.objects.create(Title = title,Author = authorObject, Publisher = publisher, PublishDate = publishdate,
                                    Category = categoryObject, Price = price, SoldCount = soldcount)
                print('Success')
            except:
                print('Oops! ', sys.exc_info()[0], ' Occured')

    def getMostBooksSoldByAuthor(self,authorId):
        bookObject = Book.objects.filter(Author_id = authorId)
        if bookObject.exists():
            max = bookObject[0]
            for i in bookObject:
                if i.SoldCount > max.SoldCount:
                    max = i
            print('Most book sold by Author is : ',max)
        else:
            print('Author Id does not exist')

    def getMostBooksSoldByCategory(self,categoryId):
        bookObject = Book.objects.filter(Category_id = categoryId)
        if bookObject.exists():
            max = bookObject[0]
            for i in bookObject:
                if i.SoldCount > max.SoldCount:
                    max = i
            print('Most book sold by Category is : ',max)
        else:
            print('Category Id does not exist')

    def searchBook(self,searchString):
        print('Searching string in AuthorName, CategoryName and Book Title')
        authorObject = Author.objects.filter(AuthorName__icontains = searchString)
        categoryObject = Category.objects.filter(CategoryName__icontains = searchString)
        booksFound = Book.objects.filter(Q(Category__in = categoryObject) | Q(Author__in = authorObject) | Q(Title__icontains = searchString))
        if booksFound.count()>0:
            print('Following books are found basis searchString')
            print(booksFound)
        else:
            print('No books found with the given search string')

    def getBooksByAuthor(self,authorId):
        try:
            bookObject = Book.objects.filter(Author_id = authorId)
            if bookObject.count()>0:
                for i in bookObject:
                    print(i)
            else:
                print('No books found with given author id')
        except:
            print('Oops!', sys.exc_info()[0],' occured')