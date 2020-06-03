#!/usr/bin/python3
""" 101-stats is a log parsing script """
import sys

if __name__ == "__main__":
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def log(line):
        """ logs line code and size """
        try:
            terms = line[:-1].split(' ')
            size[0] += int(terms[-1])
            code = int(terms[-2])
            if code in codes:
                codes[code] += 1
        except:
            pass

    def print_stats():
        """ prints accumulated stats """
        print("File size: {}".format(size[0]))
        for k in sorted(codes.keys()):
            if codes[k]:
                print("{}: {}".format(k, codes[k]))

    i = 1
    try:
        for line in sys.stdin:
            log(line)
            if i % 10 is 0:
                print_stats()
            i += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
