# Wordle Analysis
A tool for finding the best two starting guesses in Wordle based on probability of the highest-occurring letters in the full catalog.

### Approach
1. Read entries from file ("catalog.txt" - alphabetical collection of all solutions + acceptable guesses)
2. Sum up the occurrences of every letter - treat theses sums as each letter's "weight"
3. Compute value of each word - the sum of the weight of each of its letters
4. Remove any word from the list that has the same letter twice (that's a waste of space)
5. Sort words based on their value
6. Best word is first word in the new sorted list
7. Second best word is the next word in the sorted list that contains NONE of the characters of the best word

### Output
#### Top words:
1. aeros (value: 27910)
2. unlit (value: 15887)
#### Total letter counts:
* s: 6664
* e: 6661
* a: 5989
* o: 4438
* r: 4158
* i: 3759
* l: 3370
* t: 3295
* n: 2952
* u: 2511
* d: 2453
* y: 2074
* c: 2028
* p: 2019
* m: 1976
* h: 1760
* g: 1644
* b: 1627
* k: 1505
* f: 1114
* w: 1039
* v: 694
* z: 434
* j: 291
* x: 288
* q: 112

Of 12971 words in full wordle catalog, filtered down to 8321 words that did NOT have duplicate letters
