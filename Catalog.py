#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 02:34:11 2020

@author: satyam
"""

from Book import Book

class Catalog:
    def searchbyname(self,book_name):
        for key,value in Book.Count_book_dict.items():
            if book_name in Book.Count_book_dict.keys():
                print("book_name {} ")
                print("\n")
                
            else:
                print("we dont have this book")
                
    def searchbyauthor(self,Author):
        Author = input("Name of Author")
        for key,value in Book.Count_book_dict.items():
            if Author in Book.Count_book_dict.values():
                print("book_name: {}")
                
            else:
                print("we dont have this book in our library")