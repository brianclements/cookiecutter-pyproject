'''
This module provides the main functionality of {{cookiecutter.repo_name}}.

Invocation flow:

    1. Read, validate and process the input (args, `stdin`).
    2. stuff
    3. Exit.
'''

import sys


def main(args=None):
    from {{cookiecutter.repo_name}}.cli import parser

    parser.parse_args()
