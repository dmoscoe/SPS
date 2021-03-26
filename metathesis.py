# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:18:36 2021

@author: dmosc
"""

"""Input: a list of words.
Output: a list of metathesis pairs contained in the input list.

A metathesis pair is a pair of anagrams formed by exchanging exactly two letters. Examples: [steels, sleets], [tour, rout]"""

"""Part 1:
    Input: a list of words.
    Output: a dictionary in which each key is an alphabetically-sorted string (a signature), and each value is a list of words that are anagrams of the signature. I got the code for this part from the Think Python solutions on GitHub."""
    
def signature(s):
    """s is a string. Returns the signature of s, a string containing all the letters of s in alphabetical order."""
    t = list(s)
    t.sort()
    t = "".join(t)
    return t

def all_anagrams(filename):
    """filename is a list of words. Returns a dictionary in which each key is a signature, and each value is a list of words that are anagrams of the signature."""
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

"""Part 2:
    Input: a list of words.
    Output: a list of metathesis pairs contained in the input list. I wrote this code."""
    
def mp_check(s,t):
    """Assumes s, t are strings of equal length. Returns True if s, t are metathesis pairs. Otherwise, returns False."""
    matches = []
    for i in range(len(s)):
        matches.append(s[i] == t[i])
    return sum(matches) == len(s) - 2 #If the anagrams fail to match at exactly 2 locations then they are metathesis pairs.

def nxt(m,n,g):
    """For a pairwise comparison of every element in a list, this method tells us the next elements to compare. The previous comparison was elements m and n. The length of the list is g."""
    if m == g - 2:
        return -1, -1 #the pairwise comparison is complete
    elif n < g - 1: #If n is not yet at the end of the list
        return m, n + 1
    else:
        return m + 1, m + 2

def find_mps(d):
    """d is a dictionary produced by all_anagrams. Returns a list of all metathesis pairs in d."""
    mp = []
    for key in d:
        check = (0,1)
        if len(d[key]) > 1 and check[1] > 0:
            if mp_check(d[key][check[0]], d[key][check[1]]):
                mp.append([d[key][check[0]], d[key][check[1]]])
        check = nxt(check[0], check[1], len(d[key]))
    return mp

######

filename = "words.txt"

anagrams = all_anagrams(filename)

mps = find_mps(anagrams)

print(mps)