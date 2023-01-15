from string import ascii_letters, digits, punctuation
from rich.console import Console
from datetime import datetime
from random import choices
from rich import print
from time import sleep
import click


@click.command()
@click.option('-p', '--pontuacao', 'pontuacao', is_flag=True,  default=False, type=click.BOOL, help='Adiciona ou remove pontuações.')
@click.option('-d', '--digitos', 'digitos', is_flag=True, default=False, type=click.BOOL, help='Adiciona ou remove os números.')
@click.option('-s', '--salvar', 'salvar', is_flag=True, default=False, type=click.BOOL, help='Salva a key/token em um arquivo ".gpuf"!')
@click.option('-t', '--tamanho', 'tamanho', default=12, type=click.INT, help='Define o tamanho da sua key/token. (default 12)')
@click.option('-rd', '--remdigito', 'remdigito', type=click.STRING, help='Remove digitos. Ex: 0..9!')
@click.option('-rp', '--rempontuacao', 'rempontuacao', type=click.STRING, help='Remove pontuações. Ex: "#%&*@<>"')
def gerador_keys(
    pontuacao: bool = False,
    digitos: bool = False,
    salvar: bool = False,
    tamanho: int = 12,
    remdigito: str = None,
    rempontuacao: str = None,
) -> str:

    p = d = ''
    if pontuacao:
        p = punctuation
        if rempontuacao != None:
            if rempontuacao.isalnum():
                print("[red]TypeError:[/] 'rempontuacao' não aceita números ou letras do alfabeto!")
                return ''
            else:
                for remover in rempontuacao:
                    p = p.replace(f'{remover}', '')

    if digitos:
        d = digits
        if remdigito != None:
            if remdigito.isdigit():
                for remover in remdigito:
                    d = d.replace(f'{remover}', '')
            else:
                print("[red]TypeError:[/] 'remdigito' aceita apenas números de 0-9!")
                return ''

    senha: str = f"{''.join(choices(ascii_letters + p + d, k=tamanho))[::-1]}"
    if salvar:
        data_atual = datetime.now().strftime(r"%d/%m/%Y %X.%f")
        with open('password.gpuf', 'at', encoding='utf-8') as arquivo:
            arquivo.write('[Token]:\n')
            arquivo.write(f'\t"date/time": "{data_atual}";\n')
            arquivo.write(f'\t"key": "{senha}";\n\n')
            print("O seu [bold]token[/] foi salvo no arquivo [yellow]'password.gpuf'[/] com sucesso!")

    console = Console()
    with console.status('Gerando sua [bold]key/token[/], aguarde...'):
        sleep(1.5)
    print(f'\n[bold]Key/Token:[/] [yellow]{senha}[/]')
    