# Python


**Working with files**

- [Count words](https://github.com/szyymek/Python-scripts/blob/master/Count_words.py) - takes words from column in one excel file and counts occurrences of them in another file. Final file with numbers of occurrences is saved on disc.
- [Simple supplier recomendation]() - takes ID of part and checks if the part was bought in the past. Returns recomendations of suppliers based on past orders
- [Supplier recomendation](https://github.com/szyymek/Python-scripts/blob/master/rekomendations.py) - takes name and part number of new part from one xls file and, using Levenstein distance, is looking for most similar names and part numbers in purchase history, then recomendes best suppliers, based on purchasing history of similar parts.

**Math and numeric libraries**

- [Numpy](https://github.com/szyymek/Python-scripts/blob/master/numpy_examples.py) - basic vectors, matrixes and linear algebra operations with Numpy library
- [Closest pair problem](https://github.com/szyymek/Python-scripts/blob/master/closest_pair.py) - find a pair of points with the smallest distance between them, using brute force algorithm
- [Collatz conjecture](https://github.com/szyymek/Python-scripts/blob/master/collatz.py) - checks how many steps we need to resolve Collatz conjecture and creates visualization of it on graph
- [Sympy math](https://github.com/szyymek/Python-scripts/blob/master/Sympy_examples.py) - symbolic mathematics in python using SymPy

**Networking**

- [Send an e-mail](https://github.com/szyymek/Python-scripts/blob/master/send_email.py) - send an e-mail from outlook mailbox, with attachment

**Strings**
- [Valid parentheses](https://github.com/szyymek/Python-scripts/blob/master/Valid_Parentheses.py) - function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function return true if the string is valid, and false if it's invalid
- [String transformer](https://github.com/szyymek/Python-codewars/blob/master/String_transformer.py) - Given a string, return a new string that has transformed based on the input - rules: change case of every character, ie. lower case to upper case, upper case to lower case, reverse the order of words from the input, handle multiple spaces.
- [Exes_and_Ohs](https://github.com/szyymek/Python-scripts/blob/master/Exes_and_Ohs.py) - Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char. Excersise from codewars
- [Counting duplicates](https://github.com/szyymek/Python-scripts/blob/master/Counting_duplicates.py) - Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits. Example: "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`).
- [Strip comments](https://github.com/szyymek/Python-scripts/blob/master/Strip_comments.py) - it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out. Example: string = ("apples, pears # and bananas\ngrapes\nbananas !apples",markers =  ["#", "!"]) ; result should == "apples, pears\ngrapes\nbananas".
- [Human Readable Time](https://github.com/szyymek/Python-scripts/blob/master/Human_Readable_Time.py) - Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS), The maximum time never exceeds 359999 -- 99:59:59. From codewars
- [Text align justify](https://github.com/szyymek/Python-scripts/blob/master/Text_align_justify.py) - task is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width. Rules: Use spaces to fill in the gaps between words.Each line should contain as many words as possible.Use '\n' to separate lines.Gap between words can't differ by more than one space.Lines should end with a word not a space.'\n' is not included in the length of a line.Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).Last line should not be justified, use only one space between words.Last line should not contain '\n'Strings with one word do not need gaps ('somelongword\n'). Excersise from codewars
- [Levenstein](https://github.com/szyymek/Python-scripts/blob/master/Levenstein.py) - check similarity of 2 strings using Levenstein distance
- [Add commas to number](https://github.com/szyymek/Python-scripts/blob/master/Add_commas.py) - task is to convert a given number into a string with commas added for easier readability. The number should be rounded to 3 decimal places and the commas should be added at intervals of three digits before the decimal point. There does not need to be a comma at the end of the number. Example - commas(-1000000.123) == "-1,000,000.123" 

**Python basics**

- [Print formatting](https://github.com/szyymek/Python/blob/master/print_formatting.py) 
- [Lists](https://github.com/szyymek/Python/blob/master/lists.py)
- [Tuples](https://github.com/szyymek/Python/blob/master/tuples.py)

**Sorting**

- [Mergesort](https://github.com/szyymek/Python-scripts/blob/master/merge_sort.py)
- [Bubble sort optimized](https://github.com/szyymek/Python-scripts/blob/master/bubble_sort.py)
- [numpy.sort() function](https://github.com/szyymek/Python-scripts/blob/master/np-Sort.py) - generates list of random ints and using time module checks the time of executions of nupy.sort() with different kind of algorithms - mergesort, quicksort and heapsort

**Recursion**

- [Fibonacci number](https://github.com/szyymek/Python-scripts/blob/master/fibonacci.py)
- [Recursive exponent](https://github.com/szyymek/Python-scripts/blob/master/recursive_exponent.py)
- [Mergesort](https://github.com/szyymek/Python-scripts/blob/master/merge_sort.py)
- [Factorial](https://github.com/szyymek/Python-scripts/blob/master/factorial.py)
- [Greatest common divisor](https://github.com/szyymek/Python-scripts/blob/master/Greatest_common_divisor.py) - find greatest common divisor using Euclidean Algorithm

**Cryptography**

- [Decode morse code](https://github.com/szyymek/Python-scripts/blob/master/Decode_the_Morse_code.py)
