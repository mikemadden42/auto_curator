#!/usr/bin/env python
"""Process Elastic indices"""

import csv


def get_indices(file):
    """Create dict of indices"""
    with open(file, 'rt') as fin:
        cin = csv.DictReader(fin, fieldnames=['index', 'age'])
        indices = [row for row in cin]
    return indices


def print_indices(indices):
    """Print indices"""
    for i in indices:
        print(i['index'], i['age'])


def main():
    """Process indices"""
    i = get_indices('indices.csv')
    print_indices(i)


if __name__ == '__main__':
    main()
