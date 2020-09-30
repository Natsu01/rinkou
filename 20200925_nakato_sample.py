# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas as pd

def read_file(path):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [ln.strip(os.linesep) for ln in lines]

    return lines

def read_filepa(path):
    data = pd.read_table(path)
    lines = len(data)

    return plines

# change this function that uses pandas library
def count_lines(file_path):
    lines = read_file(file_path)
    return len(lines)

def count_entry(file_path):
    data = pd.read_table(file_path)
    data.columns = ['city','adress']
    counts = data['city'].value_counts()
    return counts             

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    nlines = args.number
    print('file: %s' % filename)
    print('number: %d' % nlines)

    len = count_lines(filename)

    print('length is {}'.format(len))

    count = count_entry(filename)

    print('Unique counts is {}' .format(count))
