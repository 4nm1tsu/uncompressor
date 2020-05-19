#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.argument('name')
def command(name):
    click.echo("hogehoge:{}".format(name))


def main():
    command()


if __name__ == '__main__':
    main()
