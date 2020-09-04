# 1.C

import argparse
import csv
parser = argparse.ArgumentParser(description='Reading/Writing text files or reading csv files')

def print_file_content(file):
    with open(file,'r') as file_object:
        fileText = file_object.read()
        print(fileText)

def write_list_to_file(output_file, lst): 
    with open(output_file, 'w') as file_object:
        for i in range(len(lst)):
            file_object.write(str(lst[i]))
        
def read_file(input_file):
    with open(input_file) as file_object:
        reader = csv.reader(file_object)
        data = list(reader)
        print(data)


if __name__ == '__main__':
    parser.add_argument('file', help='Name of input file to read or output file to write.')
    parser.add_argument('-list', '--list', help='List to be written to the output file')
    args = parser.parse_args()


    if args.file is None:
        if ".csv" in str(args.file):
            read_file(args.file)
        else:
            print_file_content(args.file)
    else:
         write_list_to_file(args.file, args.list)
