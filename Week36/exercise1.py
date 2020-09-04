# 1.A 

import argparse
parser = argparse.ArgumentParser(description='A program to read from an input file, and either write it out in the console, or to an output file')

if __name__ == '__main__':
    parser.add_argument('inputFile', help='Name of input file.')
    parser.add_argument('-o', '--outputFile', help='Name of the output file.')
    args = parser.parse_args()

    
    with open(args.inputFile,'r') as file_object:
        inputFileText = file_object.read()

    if args.outputFile:
        with open(args.outputFile, 'w') as file_object:
            file_object.write(inputFileText)

    else:
        print(inputFileText)
        
