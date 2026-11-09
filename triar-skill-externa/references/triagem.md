# Roteiro de triagem

## Inventário local

Execute o script confiável do kit com o caminho da candidata. A partir da raiz do repositório, por exemplo:

```text
python triar-skill-externa/scripts/inventariar.py "caminho/da/skill"
```

O script lê arquivos regulares e emite JSON na saída padrão. Em caso de caminho inválido, link, arquivo especial ou erro de leitura, retorna código diferente de zero e não emite inventário parcial. Registre o commit da origem separadamente.

## Revisão

- **Origem.** URL, commit, caminho e arquivos relacionados que o procedimento usa fora da pasta.
- **Licença.** Localize os termos aplicáveis à pasta, aos recursos incorporados e às dependências que seriam redistribuídas. Registre avisos e atribuições exigidos pela licença identificada.
- **Comportamento.** Registre gatilho, resultado, sobreposição com a biblioteca, dependências e efeitos. Procure rede, gravação fora do escopo, uso de credenciais, instalação, publicação e execução de código externo.
- **Checagens.** Aponte ao menos um pedido típico, um pedido fora de escopo e uma entrada adversarial. Descreva o resultado esperado de cada um.

## Parecer

| Estado | Quando usar |
| --- | --- |
| `candidata-a-piloto` | Origem e termos aplicáveis identificados, escopo útil e riscos conhecidos que podem ser contidos em uma avaliação isolada. |
| `pendente` | Falta informação necessária sobre origem, licença, dependência ou comportamento. |
| `rejeitada` | Há incompatibilidade demonstrada com o objetivo, a licença exigida ou o limite de execução. |

Registre estado, commit, caminho, evidências e próximo teste. Use evidências locais sem divulgar segredos nem transferir arquivos privados.
