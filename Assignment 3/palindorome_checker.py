# CMPR.X416 Python For Programmers
# Module 4: Palindrome Checker Programming Assignment


def filter_non_alphanumeric(s):
    '''
    Input: a string
    Output: a string which is the same as the input string without its non-alphanumeric characters
    '''
    # Note: Use isalnum() method.
    return ''.join([c for c in s if c.isalnum()])


def is_pal_no_loop_recur(s):
    '''
     Input: a string
     Output: returns True if the string is a palindrome, False otherwise.
    '''
    # No loops or recursion are allowed
    return s == s[::-1]


def is_pal_loop(s):
    '''
     Input: a string
     Output: returns True if the string is a palindrome, False otherwise.
    '''
    # No recursion allowed. One (for) loop should suffice. Code < 6 lines
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


def is_pal_recur(s):
    '''
     Input: a string
     Output: returns True if the given string is a palindrome, False otherwise.
    '''
    # Recursive version
    if len(s) == 1:
        return True
    if len(s) == 2:
        return s[0] == s[-1]
    return s[0] == s[-1] and is_pal_recur(s[1:len(s)-1])

#
# main body
#


# list of is_pal functions (that you are going to implement)
func_list = [is_pal_no_loop_recur, is_pal_loop, is_pal_recur]

phrase = ''
while phrase.lower() != 'exit':
    # Prompt the user to enter input
    phrase = input(
        "\nEnter a phrase on a single line. To exit, enter [Exit/exit/EXIT]: ")

    if phrase.strip().lower() == 'exit':  # remove leading/trailing whitespaces
        print("Exiting the program, bye.")
        exit(0)

    # Filter out non-alphanumeric characters
    alphanum_phrase = filter_non_alphanumeric(phrase)

    if len(alphanum_phrase) == 0:
        print("The phrase you entered did not have any alphanumeric characters in it...skipping it.")
        continue

    lower_case = alphanum_phrase.lower()  # make input case-insensitive

    for f in func_list:  # invoke each is_pal function listed in the list func_list
        if f(lower_case):
            print("{}: Phrase '{}' is a palindrome".format(f.__name__, phrase))
        else:
            print("{}: Phrase '{}' is NOT a palindrome".format(f.__name__, phrase))
