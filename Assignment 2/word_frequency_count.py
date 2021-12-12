# CMPR.X416 Python For Programmers
# Module 3: Word Frequency Count Programming

MOVIE_DATABASE = ["Love Actually", "STAR WARS", "From Russia With love",
                  "Dr. Strangelove", "Bourne Ultimatum", "The fault in our stars",
                  "Bourne supremacy", "A star is born", "Starsky and Hutch", "Dr No",
                  "Star Trek", "Lover's Paradise", "A Christmas Star", "Seven brides for seven brothers",
                  "Ernest Saves Christmas", "A CHRISTMAS CAROL", "The Muppet Christmas Carol", "White Christmas", "Fahrenheit 451"]

# Create List with each element being a list of words for each movie title i.e. [['love','actually'],['star','wars']...]
words = []
for movie in MOVIE_DATABASE:
    # make list of list of words for each movie title with no whitespace and lowercase
    words.append(movie.strip().lower().split())

# get user input of words to find in the words list
# make list of user_input_words with no whitespace and lowercase
word_user_input_list = input(
    'Enter your search word(s), separated by one or more whitespaces: ').strip().lower().split()
if len(word_user_input_list) > 0:
    # if user entered a word
    # initialzing empty dictionary to store frequency of words
    frequency_dict = {}
    for word in word_user_input_list:
        for movie_words in words:
            if word in movie_words:
                if word in frequency_dict:
                    # add 1 if word already in frequency_dict
                    frequency_dict[word] += 1
                else:
                    # make the value 1 if word not in frequency_dict
                    frequency_dict[word] = 1
    if len(frequency_dict.keys()) == 0:
        # if no words found...
        # make every element in the list title_format
        word_user_input_title_format = []
        for word in word_user_input_list:
            word_user_input_title_format.append(word.title())
        exit(
            f'\n\033[1mNone of your search words "{",".join(word_user_input_title_format)}" were found in the movie title database.\033[0m\n')
    else:
        # if words were found
        print(
            "\n\033[1mThe following word(s) were found in our movie title database!\033[0m\U0001F44D\n")
        # Make sorted list of the words that were found
        words_found_sorted = []
        for key in frequency_dict.keys():
            words_found_sorted.append(key)
        # Sort the list in alphabetically ascending order
        words_found_sorted.sort()
        for word in words_found_sorted:
            print(
                f"\033[1m{word.title()}\033[0m \033[91m{'*' * frequency_dict[word] }\033[0m")
        exit('')
else:
    # if no words or a blank line was entered by user
    exit("\033[1mNo words were entered...exiting the program.\033[0m\U0001F61E\n")
