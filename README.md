# Horspool Algorithm

## Project Description

This project enables searching for a specific word or phrase in a collection of text books by Walter Riso using the Horspool algorithm. The code reads the texts, executes the search, and displays the results ordered by the frequency of the word/phrase in each book, as well as the specific positions in the texts where they are found.

## Key Functions

### `failure_function(b)`

Calculates and returns the failure function for a pattern `b`.

- Creates a dictionary that stores the last occurrence of each character in the pattern.

### `horspool(a, b)`

Implements the Horspool algorithm to search for the pattern `b` in the text `a`.

- Utilizes the failure function to determine the shifts in the text, enhancing search efficiency.

## Code Logic

### Book Definition

- Defines a list of text files containing the books by Walter Riso and a corresponding list of titles.

### Reading and Searching the Books

- Prompts the user to input a word or phrase to search.
- If the input is a single word, it searches each book using the Horspool algorithm, counting occurrences and recording positions.
- The results are sorted and displayed in descending order of word frequency in the books.

### Phrase Search

- If the input is a phrase, a menu is presented to the user to choose among different search options:
  - Search the complete phrase.
  - Search each word of the phrase separately.
  - Both options.
- Depending on the selected option, the corresponding search is performed and results are displayed.

## Execution

When running the script, the user is prompted to enter a word or phrase, which is then processed according to the available options. Results are displayed in the console, indicating in which books the word or phrase is found, the number of occurrences, and the exact positions.

### Usage Example

```bash
$ python search_word.py
Enter a phrase or word: "love"
---------------------
('DANGEROUS LOVES - Walter Riso', 12)
---------------------
('IN LOVE OR ENSLAVED - Walter Riso', 10)
# ... more results ...

