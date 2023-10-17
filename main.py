"""
    Python Job Batcher | RPINerd, 10/17/23

    A general purpose, thread aware launcher for python scripts or command line programs.
"""

import os
import sys


def run(function, args, items) -> None:
    # Validate that the function is installed (if it's a command line program) or that it exists (if it's a python script)
    if os.system(f"which {function}") != 0 and not os.path.exists(function):
        print(f"Error: {function} is not installed or does not exist")
        sys.exit(1)

    # Get the max machine threads
    max_threads = len(os.sched_getaffinity(0))

    return
