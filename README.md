# Do Macro ao Micro: Princípio da Resolução por Energia Mínima
### Marcelo Vargas

Este repositório organiza a teoria, artigos e materiais de apoio do princípio de que a resolução espacial mínima é otimizada por energia mínima, maior coerência e baixo ruído térmico.

## Fórmula

\\[
\\delta x_{\\min} = \\frac{C}{\\alpha} \\cdot \\frac{\\sqrt{k_B T + \\gamma \\varepsilon}}{\\sqrt{N \\cdot \\tau}}
\\]

## Estrutura
- conteudo: resumo claro com fórmula, gráficos e links essenciais
- docs/pt e docs/en: artigos completos e materiais de referência
- examples: script de simulação para reproduzir gráficos
- images: gráficos gerados e figuras ilustrativas
 
## Visão rápida
- Conteúdo essencial: [conteudo/README.md](conteudo/README.md)
- Preprint (PT): [docs/pt/preprint.md](docs/pt/preprint.md)
- Full paper (EN): [docs/en/preprint.md](docs/en/preprint.md)

## Como reproduzir
- Executar o script em examples/simulation.py para gerar gráficos de dependência de \\(\\delta x_{\\min}\\).
- Os gráficos serão salvos em images/.

## Documentação
- Português: [docs/pt/](docs/pt/)
- English: [docs/en/](docs/en/)

## Imagens
- Gráficos: [dx_vs_t.png](images/dx_vs_t.png), [dx_vs_epsilon.png](images/dx_vs_epsilon.png), [dx_vs_n.png](images/dx_vs_n.png), [dx_vs_tau.png](images/dx_vs_tau.png), [dx_surface_t_epsilon.png](images/dx_surface_t_epsilon.png)
- Fórmula e metáfora: [formula.png](images/formula.png), [sintese_formula.png](images/sintese_formula.png), [descricao_formula.png](images/descricao_formula.png), [principio_delicadeza_energetica.png](images/principio_delicadeza_energetica.png)
- Diagrama conceitual: [diagram_macro_micro_resolucao.png](images/diagram_macro_micro_resolucao.png)

## Licença
- Código: MIT License (ver LICENSE-MIT)
- Textos e imagens: CC-BY 4.0 (ver LICENSE-CC-BY-4.0)
- Aviso de royalties e autoria: [IP-ROYALTY-NOTICE.md](IP-ROYALTY-NOTICE.md)
- Licença Comercial (termos e percentuais): [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)
- Modelo de acordo comercial: [docs/pt/acordo_licenca_comercial_template.md](docs/pt/acordo_licenca_comercial_template.md)

## Citação
- Consulte CITATION.cff para citar este trabalho em gerenciadores de referência.

