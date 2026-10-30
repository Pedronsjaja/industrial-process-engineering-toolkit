# Caso de aplicação: organização do estoque técnico do GAIA

Caso didático inspirado no contexto de um projeto de extensão de robótica fornecido pelo mantenedor. Os CSVs desta pasta são **fictícios**: não reproduzem o inventário, quantidades, pessoas ou patrimônio do GAIA. O diagnóstico real é mantido separadamente no ambiente local. Nenhum ganho operacional foi medido ou comprovado por estes arquivos.

## Problema e objetivo

Um estoque pode conter contagens e categorias, mas ainda ser difícil de usar quando localização, condição, responsável e alocação não estão definidos. Objetivo proposto: selecionar uma bancada/armário piloto, confirmar sua situação física e estabelecer rastreabilidade até o empréstimo/devolução e a reposição.

Não pressupor que o robô, a oficina ou todos os componentes estão disponíveis. A planilha é uma fonte de registros; quantidades atuais e condição exigem conferência física.

## Primeiro ciclo aplicável

| Etapa | Ação proposta | Evidência para avançar |
|---|---|---|
| Diagnóstico | Escolher área, registrar itens e medir tempo de localização com procedimento definido | Linha de base com data, amostra, unidade e observador |
| Seiri | Avaliar necessidade por projeto; separar quarentena, patrimônio, material didático e estoque técnico | Decisão aprovada por item; sem descarte automático |
| Seiton | Definir endereços de armazenamento e identificação estável de item/lote | Localização observada e etiqueta correspondente |
| Seiso | Limpeza/inspeção com procedimento compatível com equipamentos e eletrônica | Condição registrada, sem presumir teste elétrico ou funcionamento |
| Seiketsu | Definir campos obrigatórios, rotina de retirada/devolução e responsável | Registro consistente e procedimento usado pela equipe |
| Shitsuke | Verificações periódicas e integração de novos membros | Registros de execução e revisão das pendências |

Destinos de material defeituoso, obsoleto ou sem uso claro exigem avaliação técnica e patrimonial. Uma bola pode ser necessária a testes de futebol robótico; um livro pode ser material de extensão. “Não é componente eletrônico” não significa “descartar”. Quantidades mínimas sugeridas automaticamente precisam de demanda, prazo de reposição e aprovação; não são autorização de compra.

## Exercício executável

Da raiz do toolkit:

```text
python automation/validate_inventory.py examples/gaia-extension-case/inventory-incomplete.csv --as-of 2026-10-30
python automation/validate_inventory.py examples/gaia-extension-case/inventory-demo-valid.csv --as-of 2026-10-30
```

O primeiro retorna código **1**, com quatro pendências (localização e condição de duas linhas). O segundo retorna código **0** e duas linhas válidas. Os locais e condições do segundo arquivo são inventados apenas para demonstrar o formato; não autorizam preencher esses dados na planilha real.

Não calcule o KPI existente de disponibilidade para concluir que material sem condição informada está indisponível: o script considera apenas os status específicos de sua [definição](../../docs/kpi-definitions.md). O caso exige primeiro medir a completude dos dados. Não gere nota 5S a partir do inventário: use critérios observados e o [roteiro de entrevista](../../quality/5s/roteiro-entrevista.md).

## Integração com a planilha existente

| Campo da planilha | Campo do toolkit | Regra |
|---|---|---|
| Item | item | Preservar nome original e confirmar identidade/modelo quando ambíguo |
| Categoria | category | Taxonomia revista pela equipe |
| Quantidade | quantity | Registrar unidade de contagem; conferir fisicamente |
| Localização | location | Não preencher com local presumido |
| Alocação/Projeto | project | Separar reserva, uso e propriedade |
| Status/Condição | status | Mapear somente após definir critérios; não transformar vazio em available |
| Responsável | owner | Manter dado pessoal apenas em ambiente autorizado |
| Estoque Mínimo | Sem campo equivalente no validador atual | Manter no sistema de origem; não perder na exportação |
| Abaixo do Mínimo? | Campo derivado na origem | Preservar fórmula; não editar manualmente |
| Link de referência | supplier/notes conforme conteúdo | Link de busca não identifica fornecedor, produto ou cotação confirmada |

`asset_id` não existe necessariamente na origem: definir IDs estáveis de item/lote em mapeamento separado; não usar número da linha como identidade permanente. Datas de inspeção ficam vazias quando não disponíveis, conforme o esquema; nunca inventar datas. Não sincronizar escrevendo sobre a origem antes de revisar o mapeamento e as permissões. Os scripts atuais não fazem sincronização automática com Google Sheets.

## Acompanhamento e Definition of Done

Proposta: medir fração dos registros com identidade, localização, condição e responsabilidade confirmadas; registrar divergências de contagem e pendências de triagem; comparar tempo de busca antes/depois em condições equivalentes. Meta, período, equipe e orçamento: **a definir**, não resultados reais.

Concluído o piloto quando a área escolhida tiver conferência física documentada, decisões de triagem autorizadas, registros rastreáveis e uma verificação posterior. Use [5W2H](../../process-management/5w2h/README.md) para responsabilidades e prazos e [PDCA](../../process-management/pdca/README.md) para verificar eficácia. Uma tabela preenchida ou software aprovado não demonstra implantação física.

## Uso por assistentes

Consultar este caso apenas para tarefas de estoque/oficina/5S. Recuperar os dados reais autorizados sob demanda; não copiar o Drive inteiro nem usar dados pessoais em exemplos públicos. Classificar RELATADO, OBSERVADO, MEDIDO e CALCULADO; manter UNKNOWN/NOT_MEASURED quando faltar evidência. Não recomendar compras, descarte ou alteração de segurança com base só em mínimos automáticos e nomes de itens.
