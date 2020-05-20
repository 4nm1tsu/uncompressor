#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from . import compressed
from . import uncompress


@click.command()
@click.argument('srcs', type=click.Path(exists=True), nargs=-1)
@click.option('--dist', '-d', default='', help='An optional directory to which extract files.')
def uncmprs(srcs, dist):
    if dist:
        compressed.Compressed.dist = dist
    with click.progressbar(srcs) as bar:
        for src in bar:
            file = compressed.Compressed(src)
            if file.is_available():
                # 解凍処理
                uncompress.uncompress(file)
            else:
                click.secho('{file} is not a valid type'.format(file=file.path), fg='red')


def main():
    uncmprs()


if __name__ == '__main__':
    main()
