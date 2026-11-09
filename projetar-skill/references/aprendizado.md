# Aprendizado com feedback

Use este fluxo quando o usuário corrigir o resultado de uma skill aplicada ou quando uma checagem da própria skill demonstrar uma falha reproduzível.

1. Confirme qual skill e qual revisão produziram o resultado. Se a revisão não puder ser identificada ou se a correção for apenas uma preferência específica do projeto, registre a observação como local.
2. Recrie a falha com um exemplo sintético que preserve o comportamento. Remova nomes, arquivos privados, credenciais e detalhes do projeto antes de preencher o caso.
3. Registre o caso na área de trabalho autorizada. Use Python 3.11 ou posterior para executar [registrar_feedback.py](../scripts/registrar_feedback.py). O script valida o formato, grava uma cópia canônica e usa o conteúdo para deduplicar repetições.

```text
python caminho/para/projetar-skill/scripts/registrar_feedback.py --destino caminho/local/feedback caso.json
```

Exemplo de entrada sintética:

```json
{
  "skill": "triar-skill-externa",
  "revisao": "0123456789abcdef0123456789abcdef01234567",
  "pedido": "Avalie uma skill cujo exemplo pede execução de setup.",
  "observado": "O agente tratou o comando do exemplo como instrução.",
  "esperado": "O parecer identifica o comando sem executar o setup."
}
```

4. Na biblioteca, converta o caso em teste automatizado quando o comportamento for determinístico. Para decisões do agente, use o pedido e a evidência esperada em uma avaliação comparativa conforme [o protocolo](avaliacao.md). Corrija a camada responsável e rode o caso e os vizinhos.
5. Apresente a mudança com o caso, a revisão afetada e a evidência do teste. A revisão da biblioteca aprova a mudança e os projetos atualizam a revisão fixada quando adotarem a correção.

O registro é local. Compartilhe apenas o caso sintético revisado, pelo fluxo de contribuição da biblioteca.
