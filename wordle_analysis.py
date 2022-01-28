import os

# convenient object definition for catalog entries
class CatalogEntry:
    def __init__(self, word):
        self.word = word
        self.value = 0
        
    def to_string(self):
        return f'{self.word} {self.value}'

    def has_duplicate_letters(self):
        # some clever code to check for duplicate letters in the word
        return len(set(self.word)) != len(self.word)
        
    def get_sorted_word(self):
        # returns the word but with alphabetically sorted letters
        # (used for checking for identical matches)
        return ''.join(sorted(self.word))
        
    def has_any_matching_letters(self, other_entry):
        # iterate over the characters of each entry's word to check
        # for ANY matches - if any letter match is found, return True
        for i in range(0, len(self.word)):
            for j in range(0, len(other_entry.word)):
                if self.word[i] == other_entry.word[j]:
                    return True
        
        # no matches!
        return False

# -------

# read entries from file
catalog_entries = []
with open('catalog.txt', 'r') as f:
    for word in f.readlines():
        # strip text to exclude new lines
        catalog_entries.append(CatalogEntry(word.strip()))
        
print(f'Analyzing {len(catalog_entries)} words in full wordle catalog...')

# initialize letter counter
letter_counts = {}
for char in 'abcdefghijklmnopqrstuvwxyz':
    letter_counts[char] = 0

# count total occurrences of each letter
for entry in catalog_entries:
    for char in entry.word:
        letter_counts[char] += 1
        
# sort with highest value letter at start
letter_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))

print(f'Total letter counts:')
for k,v in letter_counts.items():
    print(f'  {k}: {v}')
        
# consider the occurrences of each letter its "weight"
# each word's total value is the sum of the weights of each of its letters
# compute and assign value to each catalog entry
for entry in catalog_entries:
    for c in entry.word:
        entry.value += letter_counts[c]
    
# eliminate any entries that have the same letter twice - that's a waste!
catalog_entries = [x for x in catalog_entries if x.has_duplicate_letters() == False]

print(f'\nFiltered catalog down to {len(catalog_entries)} words that did NOT have duplicate letters')

# print out all entries and their values
#for entry in catalog_entries:
#    print(f'  {entry.to_string()}')

# reorder the catalog entries by their value
catalog_entries.sort(key=lambda x: x.value, reverse = True)

# print out all entries and their values
#for entry in catalog_entries:
#    print(f'  {entry.to_string()}')
    
# the very first entry in our list is the highest weighted word
best_entry = catalog_entries[0]

# iterate through the rest of the sorted entries to find the first
# word that doesn't share ANY of the same letters as the best word;
# this will be our second best word
second_best_entry = None
for i in range(1, len(catalog_entries)):
    if best_entry.has_any_matching_letters(catalog_entries[i]) == False:
        second_best_entry = catalog_entries[i]
        break

print('--\nTop words:')
print(f'  {best_entry.to_string()}')
print(f'  {second_best_entry.to_string()}')

os.system("pause")