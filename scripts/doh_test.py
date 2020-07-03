#!/bin/python3

import client
import argparse

parser = argparse.ArgumentParser(description = 'Get domain IP')
parser.add_argument('domains', metavar='Domains', nargs="+", help='Target domain names')

args = parser.parse_args()
for domain in args.domains:
	print(client.query(domain, "A"))
