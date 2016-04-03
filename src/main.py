#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

from api import Device, Flags, Location, Jodel


def main(args):
    device = Device.from_user("loluser", "omgpassword")

    print("UID: {0}".format(device.uid))

    jodel = Jodel(device)

    print(jodel.get_request_token())

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main(sys.argv))

