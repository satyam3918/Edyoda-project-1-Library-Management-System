#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 03:09:55 2020

@author: satyam
"""

from Book import Book
from User import Member , Librarian
from Catalog import Catalog

book = Book({"Machine learning using python":[3,"Andreas C Muller", 2019, 378] })
m1 = Member("Satyam swet","kolkata",21,355976254, "NA")
catlog = Catalog()

while(True):
    print("welcome")
    print("1 - display books")
    print("2 - issue book")
    print("3 - return books")
    print("4 - search  by name")
    print("5 - search by author name")
    print("6 - add book")
    print("7 - remove book")
    
    choice = input()
    if choice not in ["1","2","3","4","5","6","7"]:
        print("enter correct choice  \n")
        continue
    else:
        choice = int(choice)
        if choice == 1:
            print("books available {} ".format(Book.name))
            Book.display_books()
            print("\n")
            
        elif choice == 2:
            book = input("name of book you want to issue")
            student = input("enter your name")
            m1.issue_book(book,student)
            print("\n")
            
        elif choice == 3:
            book = input("name of book you want to return")
            student = input("enter your name")
            m1.return_book(book,student)
            
        elif choice == 4:
            book_name = input("enter the name of the book")
            Catalog.searchbyname(book_name)
            print("\n")
            
        elif choice == 5:
            author = input("enter the name of the author")
            Catalog.searchbyauthor(author)
            print("\n")
            
        elif choice == 6:
            libr = Librarian("Shekhar suman","howrah",23,456782125,"Na")
            book_name = input("name of the book which is going to be added")
            quantity = int(input())
            author = input("name of the author")
            publish_date = input("enter publish year")
            pages = input("total number of pages in book")
            libr.addBook(book_name,quantity,author,publish_date,pages)
            print("\n")
            
        elif choice == 7:
            book_name = input("name of the book which is going to be added")
            quantity = int(input())
            author = input("name of the author")
            publish_date = input("enter publish year")
            pages = input("total number of pages in book")
            libr.removebook(book_name,quantity,author,publish_date,pages)
            print("\n")
            
        else:
            print("not a valid choice")
            
        
            
            
            
            
            
        
            
            
