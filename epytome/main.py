"""
EpyTome is a plain text parser for generating LaTeX and BibTeX documents,
mainly for typesetting academic publications.
"""
import click


@click.group()
def cli():
    pass


if __name__ == '__main__':
    cli()
