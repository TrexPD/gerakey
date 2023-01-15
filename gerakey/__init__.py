from gerakey.gerakey import gerador_keys
from click import group


@group('cli')
def cli():
    pass


cli.add_command(gerador_keys())
cli()