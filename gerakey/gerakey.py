from random import choices
from string import ascii_letters, digits, punctuation


def gerador_keys(
    pontuacao: bool = True,
    numeros: bool = True,
    salvar: bool = False,
    tamanho: int = 8,
    remdigito: str = None,
    rempontuacao: str = None,
) -> str:

    p = d = ''
    if pontuacao:
        p = punctuation
        if rempontuacao != None:
            if rempontuacao.isalnum():
                return "Typer error: 'rempontuacao' não aceita números ou letras do alfabeto!"
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
                return "Typer error: 'remdigito' aceita apenas números!"

    senha: str = f"{''.join(choices(ascii_letters + p + d, k=tamanho))[::-1]}"
    if salvar:
        with open('password.guf', 'at', encoding='utf-8') as arquivo:
            print('Key:', senha, file=arquivo)
            print(
                "O seu token foi salvo no arquivo 'password.guf' com sucesso!\n"
            )

    return f'Key: {senha}\n' + '-' * 47


if __name__ == '__main__':
    senha: str = gerador_keys(remdigito='09', pontuacao=False, salvar=True, tamanho=15)
    print(senha)
