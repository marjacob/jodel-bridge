#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import os
import sys


def unix_time_millis(dt):
    """
    http://stackoverflow.com/a/11111177
    """
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0


def hmac():
    now = unix_time_millis(datetime.datetime.utcnow())


def main(args):

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main(sys.argv))

