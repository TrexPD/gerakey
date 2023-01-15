# Gerakey: Gerador de keys e tokens de acesso!

#### O gerakey é um app CLI feito com python com a lib click, pode ser usado para gerar keys e tokens de acesso aleatórias bastante personalizáveis!

### Bibliotecas usadas:

```string```
```click```
```rich```
```date/time```
```random```
```time```

### Instalação:

#### Entre na pasta/diretório gerakey e digite o comando abaixo como ADM no windows ou root no linux e afins.

<!-- <div style="background-color: black; color:white; padding: 15px; border-radius: 5px; text-align: left; font-size: 13px">python setup.py install</div>  -->

```python setup.py install```

### Uso na prática:

#### Parâmetros opcionais:

```
-p, --pontuacao      BOLL     Adiciona ou remove pontuações. (por padrão "False")
-d, --digitos        BOLL     Adiciona ou remove os números. (por padrão "False")
-s, --salvar         BOLL     Salva a key/token em um arquivo ".gpuf"! (por padrão "False")
-t, --tamanho        INTEGER  Define o tamanho da sua key/token. (por padrão 12)
-rd, --remdigito     TEXT     Remove digitos. Ex: 0..9!
-rp, --rempontuacao  TEXT     Remove pontuações. Ex: "#%&*@<>"
--help                        Show this message and exit.
```

#### Entrada dos dados e chamando a função!
<!-- 
<div style="background-color: black; color:white; padding: 15px; border-radius: 5px; text-align: left; font-size: 13px">gerakey -d -s -t 20</div> -->

```gerakey -d -s -t 20```

#### Ouput:
```
O seu token foi salvo no arquivo 'password.gpuf' com sucesso!

Key/Token: Viu8eTW9Q85tdY60o34M
```


<h2 align="center">
    <strong>🌟
        Favorite este repositório 
    </strong>🌟
</h2>


<p align="center">
    Criado com ❤️ e python por
        <a href="https://github.com/TrexPD">
            Paulo Daniel (TrexPD)!
        </a>
</p> 