#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if "MacBook-Pro" in os.uname()[1] or "virginia.edu" in os.uname()[1]:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storieshouse.debug")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storieshouse.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
