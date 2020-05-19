#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import tarfile
import zipfile
from . import compressed
from . import uncompress


@click.command()
@click.argument('srcs', type=click.Path(exists=True), nargs=-1)
@click.option('--dist', '-d', default='', help='An optional directory to which extract files.')
def uncmprs(srcs, dist):
    if dist:
        compressed.Compressed.set_dist(dist)
    for src in srcs:
        file = compressed.Compressed(src)
        if file.is_available():
            # 解凍処理
            uncompress.uncompress(file)


def main():
    uncmprs()


if __name__ == '__main__':
    main()
