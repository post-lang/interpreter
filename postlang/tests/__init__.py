#!/usr/bin/python3
import unittest


def make_suite():
    """ Make the unit testing suite """
    suite = unittest.TestSuite()
    return suite


def run():
    """ Run unit tests """
    suite = make_suite()

    # Run unit tests with the default runner
    runner = unittest.TextTestRunner()
    runner.run(suite)
