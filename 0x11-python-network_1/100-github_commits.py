#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of the repository argv[1]
by the user argv[2] """
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[1], argv[2]))
    for commit in r.json()[0:10]:
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
