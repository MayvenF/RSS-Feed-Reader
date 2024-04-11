# Author: Maeven Fanebust
# Created: 11/04/2021
# Description: Script that reads RSS urls, parses the xml file and displays relevant information
import feedparser
import sys


def display(item):
    print("\tTitle: " + item.title)
    print("\tDesc: " + item.description)
    print("\tLink: " + item.link)


# arguments can either be:
# 1) -x which means to display the top x items
# 2) list of urls
def parse_command(args):
    if len(args) >= 2:
        first = args[1]
        if first.startswith('-'):
            z = first[1:]  # gets number
            if z.isdigit():
                return int(z), args[2:]
            else:
                print("Incorrect flag")
                return -1, args[2:]
        return -1, args[1:]
    return -1, []


def main():
    n, urls = parse_command(sys.argv)
    flag = True
    for url in urls:
        file = feedparser.parse(url)
        if not file['bozo']:
            items = file.entries
            print(file.feed.title + "\n")

            # if either no flag or flag is bigger than number of items
            if n >= len(items) or n == -1:
                n = len(items)
            for i in range(n):
                display(items[i])
                print("\n")
        else:
            flag = False
    if not flag:
        print("Could not process all urls")


if __name__ == '__main__':
    main()




