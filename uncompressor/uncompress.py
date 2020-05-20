#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import compressed
import tarfile
import zipfile


class UndefinedExtError(Exception):
    "定義されていない拡張子が渡されたことを知らせる例外クラス"
    pass


def uncompress(file: compressed):
    if file.get_ext() == '.tar':
        with tarfile.open(file.path) as mytar:
            mytar.extractall(compressed.Compressed.dist)
    elif file.get_ext() == '.zip':
        with zipfile.ZipFile(file.path, 'r') as myzip:
            myzip.extractall(compressed.Compressed.dist)
    else:
        raise UndefinedExtError('{ext} is not defined.'.format(ext=file.ext))
