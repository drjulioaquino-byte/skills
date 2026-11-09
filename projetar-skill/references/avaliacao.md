# Avaliação e aprendizado

## Antes de executar

| Caso | O que observar |
| --- | --- |
| Pedido típico | A skill adequada é escolhida ou invocada conforme a política do cliente e entrega o artefato esperado. |
| Entrada incompleta ou adversarial | O agente identifica a condição, preserva o estado e para ou conclui a parte que tem evidência suficiente. |
| Pedido semelhante fora do escopo | A skill fica fora do fluxo. Se for invocada explicitamente, identifica a incompatibilidade. |

Para cada caso, registre o pedido, as entradas, os efeitos permitidos e um critério verificável. Salve dados sintéticos ou anonimizados junto do caso quando a reprodução exigir arquivos.

## Durante a avaliação

1. Valide frontmatter, nome da pasta, links e metadados exigidos pelo repositório. O [validador de referência](https://github.com/agentskills/agentskills/tree/main/skills-ref) cobre o formato base.
2. Execute scripts próprios com uma entrada válida e outra que deva falhar. Verifique código de saída, resultado e arquivos afetados.
3. Compare sessões novas com as mesmas entradas e permissões. Use a versão anterior ou uma sessão sem a skill como controle. Em um cliente configurado para invocação explícita, teste o comportamento após a invocação e registre essa condição.
4. Anote versão, cliente, modelo, resultado por caso e caminho das evidências. Um teste de formato ou de script não comprova a seleção nem a qualidade do comportamento. Se alguma etapa não puder ser executada, marque-a como pendente.

## Ao receber uma correção

Registre a falha observada e o resultado esperado. Reproduza em um caso mínimo e ajuste a descrição, o procedimento ou o script na camada responsável. Rode novamente o caso e os vizinhos que podem sofrer regressão. Submeta a mudança com a evidência pelo fluxo de revisão do repositório.
