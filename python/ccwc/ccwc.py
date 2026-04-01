import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="print newline, word, and byte counts for each file")

    parser.add_argument('-w', "--word", help="print the word count for each file", action="store_true")
    parser.add_argument('-l', "--line", help="print the line count for each file", action="store_true")
    parser.add_argument('-c', "--byte", help="print the byte count for each file", action="store_true")
    parser.add_argument('input_files', nargs='*', help='One or more input files to process')

    args = parser.parse_args()

    if args.word:
        process_word_count(args.input_files) 
    if args.line:
        process_line_count(args.input_files) 
    if args.byte:
        process_byte_count(args.input_files) 

    if not args.word and not args.line and not args.byte:
        process_line_count(args.input_files) 
        process_word_count(args.input_files) 
        process_byte_count(args.input_files) 
        
def process_word_count(input_files):
    for file in input_files:
        with open(file, 'r') as f:
            word_count = 0
            for line in f:
                words = line.split()
                word_count += len(words)
        print(word_count, end=" ") 

def process_line_count(input_files):
    for file in input_files:
        with open(file, 'r') as f:
            line_count = sum(1 for line in f)
        print(f" {line_count}", end=" ")

def process_byte_count(input_files):
    for file in input_files:
        byte_size = os.path.getsize(file)
        print(f"{byte_size} {file}", end="\n") 

if __name__ == "__main__":
    main()

