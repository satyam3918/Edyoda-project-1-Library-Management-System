#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:51:03 2020

@author: satyam
"""

class Book:
    def __init__(self,count_dict,name):
        self.Count_book_dict = count_dict
        self.name = name
        self.bookd = {}
        self.bookc = {}
        
    def display_books(self):
        
        
        for books in self.Count_book_dict.items():
            print(books)