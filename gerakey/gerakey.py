from random import choices
from string import ascii_letters, digits, punctuation
from datetime import datetime
from rich.console import Console
from rich import print
from time import sleep


def gerador_keys(
    pontuacao: bool = True,
    numeros: bool = True,
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
                return "[red]TypeError:[/] 'rempontuacao' não aceita números ou letras do alfabeto!"
            else:
                for remover in rempontuacao:
                    p = p.replace(f'{remover}', '')

    if numeros:
        d = digits
        if remdigito != None:
            if remdigito.isdigit():
                for remover in remdigito:
                    d = d.replace(f'{remover}', '')
            else:
                return "[red]TypeError:[/] 'remdigito' aceita apenas números de 0-9!"

    senha: str = f"{''.join(choices(ascii_letters + p + d, k=tamanho))[::-1]}"
    # Salva em um arquivo '.gpuf'(General Purpose File)
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
        return f'\n[bold]Key/Token:[/] [yellow]{senha}[/]\n' + '-' * 61
        

if __name__ == '__main__':
    senha: str = gerador_keys(pontuacao=False, salvar=False, tamanho=15)
    print(senha)
