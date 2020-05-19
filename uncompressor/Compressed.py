#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mimetypes


class Compressed():
    availableExt = ['.tar', '.zip']

    def __init__(self, path):
        self.path = path
        self.ext = mimetypes.guess_extension(mimetypes.guess_type(path)[0])

    def is_available(self) -> bool:
        ext = mimetypes.guess_extension(mimetypes.guess_type(self.path)[0])
        if ext in self.__class__.availableExt:
            return True
        else:
            return False
