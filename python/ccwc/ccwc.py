import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="print newline, word, and byte counts for each file")

    parser.add_argument('-w', "--word", help="print the word count for each file", action="store_true")
    parser.add_argument('-l', "--line", help="print the line count for each file", action="store_true")
    parser.add_argument('-c', "--byte", help="print the byte count for each file", action="store_true")
    parser.add_argument('input_files', nargs='*', help='One or more input files to process')

    args = parser.parse_args()

    total_words, total_lines, total_bytes = 0, 0, 0
    
    for input_file in args.input_files:
        if args.word:
            total_words += process_word_count(input_file) 
        if args.line:
            total_lines += process_line_count(input_file) 
        if args.byte:
            total_bytes += process_byte_count(input_file) 
        
        print("", input_file)

        """
        if not args.word and not args.line and not args.byte:
            process_line_count(args.input_files) 
            process_word_count(args.input_files) 
            process_byte_count(args.input_files) 
            """
        
def process_word_count(file):
    print("  ", end="")
    word_count = 0
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            word_count += len(words)
    print(f"{word_count}", end="")
    return word_count   

def process_line_count(file):
    print("  ", end="")
    line_count = 0
    with open(file, 'r') as f:
        line_count += sum(1 for line in f)
    print(f"{line_count}", end="")
    return line_count

def process_byte_count(file):
    print("  ", end="")
    byte_size = os.path.getsize(file)
    print(f"{byte_size}", end="")
    return byte_size

if __name__ == "__main__":
    main()

