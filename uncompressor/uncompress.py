#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import compressed


def uncompress(file: compressed):
    if file.get_ext() == '.tar':
        # tarの場合の処理
        print('tar')
    elif file.get_ext() == '.zip':
        # zipの場合の処理
        print('zip')
