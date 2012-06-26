#!/usr/bin/env python
from raven import Client

client = Client('http://1b08f3c3c4f046458a7702951c327c43:5125de8267b24280b8afba3ac23ef854@localhost:9000/2')

if __name__=='__main__':
    client.captureMessage('Hello from demo app...')
    # example exception logging
    try:
        1/0
    except:
        client.captureException()