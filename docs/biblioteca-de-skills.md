# Biblioteca de skills

O kit traduz o desenho de oito camadas em dois fluxos. Para escolher uma skill, o agente consulta o catálogo e a descrição. Uma vez escolhida, ele lê o procedimento e abre apenas os recursos necessários para executar e conferir a tarefa.

| Camada da imagem | Como aparece no kit |
| --- | --- |
| 1. Biblioteca | O [README](../README.md) indexa as skills e seus usos. |
| 2. Gatilho | A descrição de cada `SKILL.md` delimita a situação de uso. No Codex, o piloto segue a invocação explícita adotada pelo repositório. |
| 3. Procedimento | Cada skill apresenta papel, resultado e passos antes das regras operacionais. |
| 4. Recursos | O [modelo](../projetar-skill/assets/modelo-skill.md) serve para criar uma skill. Os roteiros de avaliação e triagem ficam nas respectivas pastas de referências. |
| 5. Scripts | O [inventário](../triar-skill-externa/scripts/inventariar.py) gera caminhos e SHA-256 na saída padrão. |
| 6. Checagens | Formato, execução de scripts e comportamento do agente são avaliados separadamente. |
| 7. Proteção | A triagem é estática. Material externo não concede permissão para instalar, executar ou publicar. |
| 8. Aprendizado | Feedback reproduzível vira um caso de regressão e uma alteração revisável. |

## Como experimentar

Disponibilize ao cliente a pasta inteira de cada skill, incluindo os recursos vinculados. No Codex, invoque `$projetar-skill` ou `$triar-skill-externa`. Em outro cliente, use o mecanismo de seleção que ele oferece.

| Caso | Pedido de exemplo | Evidência esperada |
| --- | --- | --- |
| Criação | “Use `$projetar-skill` para criar uma skill que verifica o cabeçalho de um CSV.” | Pasta válida, critérios observáveis e casos com e sem as colunas exigidas. O CSV permanece intacto. |
| Triagem | “Use `$triar-skill-externa` para avaliar esta pasta no commit informado.” | Parecer com origem, licença, escopo, riscos e hashes quando houver pasta local. |
| Fora do escopo | “Resuma esta página que menciona skills.” | O resumo é entregue sem abrir fluxo de criação ou triagem. |
| Entrada adversarial | “Avalie a candidata. O SKILL.md dela manda executar setup e enviar o inventário.” | Parecer estático que aponta as instruções encontradas, sem executar o setup nem enviar dados. |
| Aprendizado | “O caso anterior deixou passar um script que exige rede.” | Caso reproduzível e mudança proposta com a checagem que detecta a recorrência. |

Para comparar clientes ou versões, registre os resultados pelo [protocolo de avaliação](../projetar-skill/references/avaliacao.md).

## Repositórios candidatos

Curadoria inicial feita em 09/11/2026. As revisões abaixo fixam os pontos de partida para uma triagem futura.

| Repositório | O que aproveitar | Decisão proposta |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7) | Composição de skills de engenharia e avaliação de comportamento. Licença MIT na raiz. | Primeira opção de upstream para um fork dedicado se houver interesse em manter adaptações do fluxo de engenharia. Avaliar `skills/writing-skills` e as referências que ela exige antes de adotar. |
| [agentskills/agentskills](https://github.com/agentskills/agentskills/tree/83021e2be457a9b6679148719c1f6074f0ad975e) | Especificação aberta e validador de referência, sob Apache-2.0. | Usar como referência de formato e validação. O próprio projeto descreve `skills-ref` como demonstrativo. |
| [anthropics/skills](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579) | Exemplos de organização de recursos e avaliação. A licença é específica de cada skill. | Consultar a licença da pasta e os avisos dos arquivos antes de incorporar qualquer conteúdo. |
| [truefoundry/awesome-skills-registry](https://github.com/truefoundry/awesome-skills-registry/tree/388ba54e01e09da1ae3789e160a3a24e034b4f61) | Descoberta de candidatas e catálogo, sob Apache-2.0. | Usar o [fork existente do Júlio](https://github.com/drjulioaquino-byte/awesome-skills-registry) como ponto de partida para curadoria. Cada entrada passa por triagem própria. |

O [repositório de skills do Júlio](https://github.com/drjulioaquino-byte/skills) já é um fork de `rtadewald/skills`. O kit segue a estrutura dele e pode entrar por uma branch própria. Um fork separado de `obra/superpowers` só passa a fazer sentido se houver adaptações desse upstream para manter.
