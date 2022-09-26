#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:32:37 2021

@author: vsriya23
"""

def decoder(encoded, n):
    """
    workflow of function:
        - split the string into separate words
        - make a list of decoded words: iterate through words and decode each char of the word with the help of chr() and ord() functions and use .join to join the characters of each word 
        - join all the words from the list decoded_words to generate the final decoded string
    """
    words = encoded.split(' ')
    
    decoded_words = [''.join([chr(ord(ch) + n) for ch in word])for word in words]
    decoded_string = ' '.join(decoded_words)
    
    
    
    return decoded_string

if __name__ == "__main__":
    fin = open("q5_test.txt")
    data = fin.read().splitlines()
    fin.close()

    data[1] = int(data[1])
    text, n = data
    
    plain = decoder(text,n)
    
    print(plain)

