# Wordle-Solver

A simple python program to assist in solving the daily wordle.

# How to Run

To run, simply navigate to the directory where you have it saved and run the main.py file. There will be instructions printed along side it that explain what to do. But as an overview, you'll be asked to input all green letters and their indices, followed by yellow, and grey. Make sure you follow proper formatting!

After you input all your letters, a list will be printed of all the words that could work given the letters you know. All the letters you know are in the word will be in all of the words in this list. Additionally, this list is sorted based on letter frequency. Once the list is generated, the solver counts how many times each letter appears in the list, and then each word is given a score equal to the sum of it's letter frequencies. The list is then sorted based on that score. This way you can guarantee that the first word in the list will get information about as many words as possible.

There is now also a second main file, titled "newMain.py" which includes a new user interface, and potentially faster solver. The solver works very similarly, but there is a new text interface to input words and the feedback. You now enter entire words, instead of individual letters with their positions. The program will first ask you for the entire word, which you can print normally. Then, it will ask you for a string of 5 characters corresponding to the colors of the letters. For green letters, type 'g'. For yellow letters, type 'y'. And for grey letters type 'r'. So, an example entry could be: 'blind', which yielded the colors "grey, yellow, grey, grey, green". So you would then type 'ryrrg' to represent that response. Other than that, the solver works the same and is largely interchangable with the original main.py file!

# Formatting

For any entry, the correct formatting follows the form "Letter,index". The program reads in 1 based indexing, so the "A" in "Apple" is index one. Make sure you submit indices for all of the colors, not just green! When you have finished entering all letters of a color, simply press return to move on to the next step

# Exiting

At any time you can end the program by typing "quit" instead of entering your letters. It will finish the current iteration and then quit out.

# Settings:

There is a settings section at the top of the "main.py" file. Currently the settings section only has support for enabling and disabling easyMode. By default easyMode is on and thus set to True, but to turn it off just change that value to False.

At the top of "realWordleList" there is also an option to switch between using the list of accepted guesses and the list of accepted solutions. The accepted solutions has 2315 words, while the accepted guesses has 12972 words. This large uptick in words may slow down the execution of the program. If you want to switch to use the guesses list, simply change "allowGuesses" to true.

# EasyMode

EasyMode is a mode of playing wordle where you do not have to use the letters you know in each guess. So for example if you had guessed "Apple" and knew the A to be correct, playing under normal/hard rules you would have to use the "A" in your next guess. EasyMode has no such restriction. With easyMode on you'll see two word lists printed. The first will be the standard list you'll always get, and the second will be a list of words that use none of the letters you already know about. The second list will be ranked the same as the first.
