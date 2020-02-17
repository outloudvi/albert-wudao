# -*- coding: utf-8 -*-

"""Wudao dict backend for albert"""

from albertv0 import *
from shutil import which
from subprocess import check_output
import re

__iid__ = "PythonInterface/v0.2"
__prettyname__ = "Wudao Dict"
__version__ = "1.1.1"
__trigger__ = "wd"
__author__ = "Outvi V"
__dependencies__ = []

if which("wd") is None:
    raise Exception("'wd' is not in $PATH.")
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')


def handleQuery(query):
    if query.isTriggered:
        keyword = query.string
        if keyword == "" or keyword[-1] != ".":
            return Item(
                id=__prettyname__,
                text=__prettyname__,
                subtext="Enter a word to search. End with \".\"."
            )
        keyword = keyword.rstrip(".")
        result = check_output([which("wd"), keyword]).decode()
        escaped = ansi_escape.sub('', result)
        lines = escaped.split("\n")

        return Item(
            id=__prettyname__,
            text=str(lines[1]),
            subtext=str("\n".join(lines[2:])),
            actions=[
                ClipAction(
                    "Copy word to clipboard", keyword)
            ]
        )
    else:
        return []
