import argparse
from collections import Counter

def count_words(fname):

    with open(fname,'r') as f:
        count = Counter(word for line in f
                             for word in line.split())
    return count.most_common(1)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Give the file name")
    args = parser.parse_args()
    
    print(count_words(args.filename))
