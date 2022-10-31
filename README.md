# Gerakey: Gerador de senha e token acesso!

#### Script feito com python para gerar senhas aleatórias e tokens de acesso bastante personalizáveis!

### Bibliotecas usadas:

```string```
```random```

### Uso na prática:

#### Parâmetros:

- **pontuacao: bool** = Ative ou desative a pontuação! (por padrão "True")
- **numeros: bool** = Ative ou desative os números! (por padrão "True")
- **salvar: bool** = Salva os seus tokens em um arquivo '.guf'! (por padrão "False")
- **tamanho: int** = Defina o tamanho do seu token! (por padrão "8")
- **remdigito: str** = Remover algum digito específico! 
- **rempontuacao: str** = Remover alguma pontuação específica!


#### Entrada dos dados e chamando a função!
```
senha: str = gerador_keys(remdigito='09', pontuacao=False, salvar=True, tamanho=15)
print(senha)
```

#### Ouput:
```
O seu token foi salvo no arquivo 'senha.guf' com sucesso!

Key: CEv6WpTxa8vOOJe
---------------------------------------------------------
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