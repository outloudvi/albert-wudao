# -*- coding: utf-8 -*-

"""Wudao dict backend for albert"""

from albert import *
from shutil import which
from subprocess import check_output
import re

__title__ = "Wudao Dict"
__version__ = "0.2.0"
__triggers__ = "wd "
__authors__ = "Outvi V"

if which("wd") is None:
    raise Exception("'wd' is not in $PATH.")
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')


def handleQuery(query):
    if query.isTriggered:
        keyword = query.string
        if keyword == "" or keyword[-1] != ".":
            return Item(
                id=__title__,
                text=__title__,
                subtext="Enter a word to search. End with \".\"."
            )
        keyword = keyword.rstrip(".").strip()
        result = check_output([which("wd"), keyword]).decode()
        escaped = ansi_escape.sub('', result)
        lines = escaped.split("\n")

        return Item(
            id=__title__,
            text=str(lines[1]),
            subtext=str("\n".join(lines[2:])),
            actions=[
                ClipAction(
                    "Copy word to clipboard", keyword)
            ]
        )
    else:
        return []
