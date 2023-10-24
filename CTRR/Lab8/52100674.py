# -*- coding: utf-8 -*-
"""52100674.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YRCxLUfQvQZEMR54tZKpU8dTGZB-Zfgf
"""

# Exercise 1
Andersen = {"The Emperor's New Clothes", "The Little Mermaid", "The Little Match Girl", "The Snow Queen"}
print(Andersen)

# Exercise 2
Shakespeare = {"Romeo and Juliet", "Hamlet", "King Lear", "Macbeth", "A Midsummer Night’s Dream", "A Comedy of Errors"}
print(Shakespeare)

# Exercise 3
Tragedy = {"Medea", "Octavia", "Oedipus", "Ur-Hamlet", "Romeo and Juliet", "King Lear", "Macbeth", "The Little Mermaid", "The Little Match Girl"} 
Comedy = {"The Three Musketeer", "The Clouds", "A Midsummer Night’s Dream", "A Comedy of Errors", "The Emperor’s New Clothes", }
Uncategorized = {"Don Quixote", "Rapunzel", "Cinderella", "Hamlet", "The Snow Queen"}

print(Tragedy)
print(Comedy)
print(Uncategorized)

# Exercise 4
Shakespeare_Tragedy = Shakespeare - Tragedy
print(Shakespeare_Tragedy)

# Exercise 5
Andersen_Comedy = {}
for i in Andersen:
  for j in Comedy:
    if i==j:
      Andersen_Comedy.add(i)
print(Andersen_Comedy)

# Exercise 6
def Myissubset(A, B):
  for i in A:
    if i not in B:
      return False
  return True

def Myissuperset(A, B):
  for i in B:
    if i not in A:
      return False
  return True

def Myisdisjoint(A, B):
  for i in A:
    if i in B:
      return False
  return True

print(Myissubset(Shakespeare,Andersen_Comedy))
print(Myissuperset(Tragedy,Shakespeare_Tragedy))
print(Myisdisjoint(Andersen,Shakespeare))
print(Myisdisjoint(Tragedy,Comedy))
print(Myisdisjoint(Andersen_Comedy,Uncategorized))
print(Myisdisjoint(Andersen,Shakespeare_Tragedy))

# Exercise 7
Work = Andersen.union(Shakespeare, Tragedy, Comedy, Uncategorized, Andersen_Comedy, Shakespeare_Tragedy)
print(Work)

# Exercise 8
Author = {'Andersen', 'Shakespeare', 'Unknown'}
print(Author)

# Exercise 9
Author_Of = {
    'Hamlet': 'Shakespeare',
    'Romeo and Juliet': 'Shakespeare',
    'King Lear': 'Shakespeare',
    'Macbeth': 'Shakespeare',
    'A Midsummer Night’s Dream': 'Shakespeare',
    'A Comedy of Errors': 'Shakespeare',
    'Medea': 'Unknown',
    'Octavia': 'Unknown',
    'Oedipus': 'Unknown',
    'Ur-Hamlet': 'Unknown',
    'The Three Musketeers': 'Unknown',
    'The Clouds': 'Unknown',
    'The Emperor’s New Clothes': 'Andersen',
    'The Little Mermaid': 'Andersen',
    'The Little Match Girl': 'Andersen',
    'The Snow Queen': 'Andersen',
    'Don Quixote': 'Unknown',
    'Rapunzel': 'Unknown',
    'Cinderella': 'Unknown'
}
print(Author_Of['Hamlet'])

# Exercise 10
def dictinvert(d):
    inv = {}
    for k, v in d.items():
        keys = inv.setdefault(v, [])
        keys.append(k)
    return inv
Written_By = dictinvert(Author_Of)
print(Written_By['Shakespeare'])

# Exercise 11
Work_Count = {}
# Iterate over the sets and update the counts
for work in Work:
    count = 0
    for s in [Shakespeare_Tragedy, Andersen_Comedy, Tragedy, Comedy, Uncategorized]:
        if work in s:
            count += 1
    Work_Count[work] = count
print(Work_Count)

# Exercise 12
text = "Within the content of Exercise section count how many words are in this section of the Lab."
word_count = 1
for i in text:
  if i == " ":
    word_count = word_count + 1
print(word_count)

# Exercise 13
from collections import Counter

text = "Within the content of Exercise section count how many words are in this section of the Lab."
word_list = text.split()

word_count = Counter(word_list)
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_word_count:
    print(f"{word}: {count}")