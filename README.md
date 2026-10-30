# Ferramentas de Engenharia de Processos Industriais

[![Testes](https://github.com/Pedronsjaja/industrial-process-engineering-toolkit/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Pedronsjaja/industrial-process-engineering-toolkit/actions/workflows/tests.yml)
[![Licença MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

Conjunto modular de ferramentas abertas para engenharia de processos industriais, gestão de processos, melhoria contínua, qualidade, documentação de engenharia, estoque, análise de dados e automação leve.

Destinado a pequenas empresas, equipes de engenharia, projetos universitários e de extensão, laboratórios, consultorias, estudantes e profissionais. Utiliza arquivos CSV e orientações práticas. A aplicação em uma fábrica exige critérios locais, dados reais e análise profissional; o toolkit não constitui um sistema de gestão certificado.

<a id="project-status"></a>
## Estado do projeto

**IMPLEMENTADO:** existe código funcional. **DOCUMENTADO:** existe orientação ou esquema, sem implicar automação. **EXEMPLO:** dados fictícios. **PLANEJADO:** desenvolvimento futuro. Nenhum recurso atual está classificado como experimental.

<a id="capabilities"></a>
## Recursos

| Área | Recurso | Estado |
|---|---|---|
| 5S | Validação de notas e médias por senso e geral | IMPLEMENTADO |
| 5S | Base fictícia de auditoria de oficina | EXEMPLO |
| PDCA / 5W2H | Método, esquemas e rastreabilidade das ações a partir de achados 5S | DOCUMENTADO |
| 5W2H | Ações preenchidas fictícias | EXEMPLO |
| FMEA | Validação de notas 1–10, cálculo e ordenação do RPN | IMPLEMENTADO |
| FMEA | Base fictícia de engenharia | EXEMPLO |
| Estoque | Validação de campos, IDs duplicados, quantidades e datas de inspeção | IMPLEMENTADO |
| Estoque | Modelo CSV com cabeçalho | DOCUMENTADO |
| Controle documental | Registro, nomenclatura e revisão de documentos | DOCUMENTADO |
| Controle documental | Validador de nomes e datas de calendário | IMPLEMENTADO |
| Estrutura de projetos | Criação das pastas predefinidas e simulação com --dry-run | IMPLEMENTADO |
| Governança de Drive | Orientações de pastas, arquivo, permissões e integração de membros | DOCUMENTADO |
| Análise de dados | Geração dos KPIs suportados a partir de CSVs | IMPLEMENTADO |
| Análise de dados | Dicionário de dados | DOCUMENTADO |
| Normas | Índices de referência e links para fontes oficiais | DOCUMENTADO |

Os limites e próximos desenvolvimentos estão no [ROADMAP.md](ROADMAP.md).

## Aplicação em empresas e indústrias

Exemplo implementável: [estoque e 5S no projeto de extensão GAIA](examples/gaia-extension-case/README.md), com roteiro de implantação, mapeamento de dados e exercício executável com dados fictícios.

O material pode apoiar organização de oficinas, almoxarifados, manutenção, fabricação e controle documental. Adapte cada critério ao processo e às responsabilidades da empresa. Registre a condição inicial, execute uma melhoria e compare resultados com evidências; não atribua ganhos industriais aos exemplos fictícios.

Para estudar 5S com entrevistas, use o [roteiro de diagnóstico e acompanhamento](quality/5s/roteiro-entrevista.md). Ele relaciona organização, implantação, resultados e sustentação a observações e medições. Respostas de percepção não devem ser convertidas automaticamente em notas de auditoria ou ganhos percentuais.

Este repositório fornece material e automações determinísticas; não contém um agente de IA executável nem atualiza automaticamente agentes de outros projetos. [AGENTS.md](AGENTS.md) orienta assistentes que trabalham neste acervo a consultar as fontes pertinentes.

<a id="quick-start"></a>
## Início rápido

Requer Python 3.10 ou superior. Os scripts usam a biblioteca padrão; instale a dependência de testes uma vez:

```text
python -m pip install pytest
```

Execute na raiz do repositório. As datas fixas em `--as-of` tornam os exemplos reproduzíveis:

```text
python automation/calculate_fmea.py examples/engineering-project-case/fmea.csv --output fmea-ranked.csv
python automation/validate_inventory.py examples/inventory-case/inventory.csv --as-of 2026-10-26
python automation/generate_5s_report.py examples/5s-workshop-case/audit.csv --output 5s-scores.csv
python automation/generate_kpis.py --inventory examples/inventory-case/inventory.csv --actions examples/5s-workshop-case/actions.csv --fmea examples/engineering-project-case/fmea.csv --audit examples/5s-workshop-case/audit.csv --as-of 2026-10-26 --output kpis.csv
python -m pytest -q
```

Caminhos com barras normais funcionam em Python no Windows, macOS e Linux. Consulte [primeiros passos e convenções CSV](docs/getting-started.md).

<a id="implemented-automation"></a>
## Automações implementadas

| Script | Finalidade |
|---|---|
| [calculate_fmea.py](automation/calculate_fmea.py) | Valida notas inteiras de 1 a 10, calcula RPN e ordena o resultado. |
| [generate_5s_report.py](automation/generate_5s_report.py) | Valida notas de 0 a 5 e calcula médias por senso e geral. |
| [generate_kpis.py](automation/generate_kpis.py) | Calcula os indicadores suportados de ações, estoque, FMEA e 5S. |
| [validate_inventory.py](automation/validate_inventory.py) | Verifica campos obrigatórios, IDs, quantidades não negativas e inspeções. |
| [check_file_names.py](automation/check_file_names.py) | Confere recursivamente o padrão dos nomes e a validade das datas. |
| [generate_project_structure.py](automation/generate_project_structure.py) | Cria pastas predefinidas ou apresenta o plano com --dry-run. |

As escalas numéricas do código são fixas: FMEA 1–10 e 5S 0–5. Os critérios locais definem o significado de cada nota, sem alterar esses limites. Consulte [fórmulas e limitações dos KPIs](docs/kpi-definitions.md).

<a id="example-datasets"></a>
## Dados de exemplo

[examples/](examples/) contém registros fictícios de oficina 5S, estoque e FMEA de engenharia. Eles não representam empresas reais, desempenho industrial medido, registros certificados ou evidência de conformidade.

Os CSVs usam UTF-8, vírgula como delimitador e ponto como separador decimal. No Excel brasileiro, confira as opções de importação/exportação antes de executar os scripts.

<a id="repository-structure"></a>
## Estrutura do repositório

```text
automation/  data-analytics/  docs/  document-control/
drive-governance/  examples/  inventory/  process-management/
quality/  standards/  tests/  .github/workflows/
```

<a id="documentation"></a>
## Documentação

- [Primeiros passos](docs/getting-started.md), [arquitetura e fluxo de dados](docs/architecture.md), [metodologia de engenharia](docs/methodology.md), [KPIs](docs/kpi-definitions.md) e [terminologia](docs/terminology.md).
- [Qualidade](quality/README.md), [gestão de processos](process-management/README.md), [estoque](inventory/README.md), [controle documental](document-control/README.md), [governança de Drive](drive-governance/README.md) e [normas](standards/README.md).
- [Roadmap](ROADMAP.md), [histórico de alterações](CHANGELOG.md), [contribuição](CONTRIBUTING.md) e [créditos de terceiros](THIRD_PARTY_CREDITS.md).

Documentos complementares podem permanecer em inglês durante a tradução. Os índices de normas são referências limitadas, sem reprodução do conteúdo protegido ou determinação de conformidade. Existem três entradas ISO e duas NR; o índice ABNT e a matriz de normas possuem apenas cabeçalhos. Confira edições e aplicabilidade nas fontes oficiais.

<a id="license-and-attribution"></a>
## Licença e autoria

Distribuído sob a [licença MIT](LICENSE). Trabalho original mantido por Pedro Henrique Barbosa de Freitas Soares. Materiais de terceiros devem ser registrados em [THIRD_PARTY_CREDITS.md](THIRD_PARTY_CREDITS.md), com fonte e licença.

<a id="maintainer"></a>
## Mantenedor

Pedro Henrique Barbosa De Freitas Soares — estudante de Engenharia Mecânica, UFTM.

GitHub: [@Pedronsjaja](https://github.com/Pedronsjaja)
