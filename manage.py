#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if (os.uname()[1] == "Hunters-MacBook-Pro.local"):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storieshouse.debug")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storieshouse.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
