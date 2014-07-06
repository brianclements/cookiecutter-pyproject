#!/usr/bin/env python3
'''
The main entrypoint. Invoke as `{{cookiecutter.repo_name}}` or `python -m {{cookiecutter.repo_name}}`.
'''

import sys
from . core import main

if __name__ == '__main__':
    sys.exit(main())
