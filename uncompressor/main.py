#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import tarfile
import zipfile
from . import Compressed


@click.command()
@click.argument('srcs', type=click.Path(exists=True), nargs=-1)
@click.option('--dist', '-d', default='', help='An optional directory to which extract files.')
def uncmprs(srcs, dist):
    for src in srcs:
        file = Compressed.Compressed(src)
        if file.is_available():
            print('available: ', end='')
        print('src:' + src)
    print('dist:' + dist)


def main():
    uncmprs()


if __name__ == '__main__':
    main()
