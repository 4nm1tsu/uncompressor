#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mimetypes


class Compressed():
    available_ext = ['.tar', '.zip']
    dist = './'

    def __init__(self, path):
        self.path = path
        self.dist = self.dist + self.path
        self.type = mimetypes.guess_type(path)[0]

    def is_available(self) -> bool:
        if self.type is not None:
            self.ext = mimetypes.guess_extension(self.type)
            if self.ext in self.__class__.available_ext:
                return True
        return False

    def get_ext(self) -> str:
        if self.type is not None:
            ext = mimetypes.guess_extension(self.type)
            return ext
        return ''
