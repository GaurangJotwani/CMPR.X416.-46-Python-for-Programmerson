# Assignment 6: Counting line, words, characters Programming Assignment

import argparse
import os

version_str = '1.0'

parser = argparse.ArgumentParser(
    description='Counts the number of lines, words, and characters in file(s)')

parser.add_argument('-v', '--version', action='version', version=version_str)
parser.add_argument('-l', '--line', required=False,
                    action='store_true', help='If present, return the line count')
parser.add_argument('-w', '--word', required=False,
                    action='store_true', help='If present, return the word count')
parser.add_argument('-c', '--char', required=False,
                    action='store_true', help='If present, return the character count')
parser.add_argument(
    'path', help='string: path-name for a single file or directory', type=str,)
args = parser.parse_args()


def counter(file_path):
    '''
    Input is path to a FILE
    No output returned
    Will print line, char and word counts
    depending on arguements passed
    '''
    def line_count(file_path):
        '''
        INPUT: path to a FILE
        OUTPUT: returns number of lines
        '''
        with open(file_path) as data:
            count = 0
            for _ in data:
                count += 1
        return count

    def character_count(file_path):
        '''
          INPUT: path to a FILE
          OUTPUT: returns number of characters
          includes \n in character count
        '''
        with open(file_path) as data:
            count = 0
            for _ in data.read():
                count += 1  # \n is included in character count
        return count

    def word_count(file_path):
        '''
          INPUT: path to a FILE
          OUTPUT: returns number of words
        '''
        with open(file_path) as data:
            count = 0
            for line in data.readlines():
                if line == '\n':  # Empty line has no words hence not added
                    continue
                else:
                    count += len(line.split(' '))
        return count

    if not(args.line) and not(args.word) and not(args.char):
        # if no arguements were passed, print all three counts
        print(
            f"   line count = {line_count(file_path)}\n"
            f"   word count = {word_count(file_path)}\n"
            f"   char count = {character_count(file_path)}"
        )
    else:
        if args.line:
            print(f"   line count = {line_count(file_path)}")
        if args.word:
            print(f"   word count = {word_count(file_path)}")
        if args.char:
            print(f"   char count = {character_count(file_path)}")


if os.path.exists(args.path):  # check if valid path
    path = args.path
else:
    # if not a valid path, exit the program with code 1
    print(f'[ERROR] Invalid file/directory {args.path}, it does not exist\n')
    exit(1)

if os.path.isfile(path):
    print(f"{args.path}")
    counter(path)
    exit('')  # Exit the program with empty line
elif os.path.isdir(path):
    if len(os.listdir(path)) == 0:  # check if path is to empty directory
        print(f'[INFO] {args.path} is empty\n')
        exit(0)  # exit with code 0 if empty directory given
    else:
        for current_dir, its_dirs, its_files in os.walk(path):
            if len(its_files) > 0:
                for f in its_files:
                    print(f"{current_dir}/{f}")
                    counter(os.path.join(current_dir, f))
        exit('')  # Exit the program with empty line
