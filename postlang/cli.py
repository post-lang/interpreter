#!/usr/bin/python3
import argparse

import postlang.tests


def main():
    """ Entry point of the POST interpreter """
    parser = argparse.ArgumentParser()
    parser.add_argument('--test',
                        help='Execute unit tests',
                        dest='unit_tests',
                        action='store_true')
    args = parser.parse_args()

    # Run unit tests
    if args.unit_tests:
        postlang.tests.run()
