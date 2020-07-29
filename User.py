#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:57:34 2020

@author: satyam
"""

from Book import Book

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        
class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.bookc = {}
        self.bookd = {}
        
    
    def no_of_book(self,name,book):
        if name not in self.bookc:
            self.bookc[name] = [book]
            return len(self.bookc[name])
        else:
            if len(self.bookc[name]) <= 2:
                self.bookc[name].append(book)
                return len(self.bookc[name])
            else:
                return len(self.bookc[name])
            
    def issue_book(self,book,name,days = 10):
        if book in Book.Count_book_dict.keys():
            if book.Count_book_dict[book][0]>=1:
                if (book,name) not in self.bookd.keys():
                    if self.no_of_book(name,book)<=2:
                        self.bookd.update({(book,name):days})
                        Book.Count_book_dict[book][0] -= 1
                        for value in self.bookd.keys():
                            if value == (book,name):
                                print("Book is issued by you")
                    else:
                        print("you can issue only 2 books")
                else:
                    print("the book is already issued")
            else:
                print("the book is not available")
        else:
            print("this book is not available")
            
            
    def return_book(self,book,name):
        if (book,name) in self.bookd.keys():
            self.bookc[name].remove(book)
            self.bookd.pop((book,name))
            Book.Count_book_dict[book][0] += 1
            print("returned sucessfully")
            
        else:
            print("please give correct detail")
            
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,librarian_id):
        super().__init__(name, location, age, aadhar_id)
        self.librarian_id = librarian_id
        
    def addBook(self,book_name,quantity, author,publish_date, pages):
            if quantity>0:
                if book_name in Book.Count_book_dict.keys():
                    Book.Count_book_dict[book_name][0]+=quantity
                else:
                    Book.Count_book_dict.update({book_name:[quantity, author,publish_date, pages]})
                    print("book is added")
            else:
                print("please enter valid number")
                
    def removebook(self,book_name,quantity,author,publish_date,pages):
        if quantity>0:
            if book_name in Book.Count_book_dict.keys():
                if Book.Count_book_dict[book_name][0]>=1:
                    Book.Count_book_dict[book_name][0]-=quantity
                    if Book.Count_book_dict[book_name][0] < 0 :
                        Book.Count_book_dict[book_name][0]+=quantity
                        print("enter correct quantity")
                    else:
                        print("book removed")
                else:
                    Book.Count_book_dict.pop(book_name)
                    print("sorry we dont have this book")
            else:
                print("enter correct book name and quantity")
                
        else:
            print("enter valid number")
                
                
    
    
            
            
                                
                    
            
    
        
    