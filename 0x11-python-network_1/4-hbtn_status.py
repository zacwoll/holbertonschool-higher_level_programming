#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == '__main__':
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
