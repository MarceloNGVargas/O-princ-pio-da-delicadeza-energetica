# Do Macro ao Micro: Princípio da Resolução por Energia Mínima
### Marcelo Vargas

Este repositório organiza a teoria, artigos e materiais de apoio do princípio de que a resolução espacial mínima é otimizada por energia mínima, maior coerência e baixo ruído térmico.

## Fórmula

\\[
\\delta x_{\\min} = \\frac{C}{\\alpha} \\cdot \\frac{\\sqrt{k_B T + \\gamma \\varepsilon}}{\\sqrt{N \\cdot \\tau}}
\\]

## Estrutura
- docs/pt: artigo completo, abstract, originalidade, resultados e discussão
- docs/en: artigo completo em inglês
- examples: script de simulação para reproduzir gráficos
- images: gráficos gerados e figuras ilustrativas

## Como reproduzir
- Executar o script em examples/simulation.py para gerar gráficos de dependência de \\(\\delta x_{\\min}\\).
- Os gráficos serão salvos em images/.

## Documentação
- Português:
  - [Abstract](docs/pt/abstract.md)
  - [Artigo completo](docs/pt/preprint.md)
  - [Originalidade e Inovação](docs/pt/originalidade_inovacao.md)
  - [Resultados e Discussão](docs/pt/resultados_discussao.md)
- English:
  - [Full paper](docs/en/preprint.md)

## Imagens
- Gráficos: [dx_vs_t.png](images/dx_vs_t.png), [dx_vs_epsilon.png](images/dx_vs_epsilon.png), [dx_vs_n.png](images/dx_vs_n.png), [dx_vs_tau.png](images/dx_vs_tau.png), [dx_surface_t_epsilon.png](images/dx_surface_t_epsilon.png)
- Fórmula e metáfora: [formula.png](images/formula.png), [sintese_formula.png](images/sintese_formula.png), [descricao_formula.png](images/descricao_formula.png), [principio_delicadeza_energetica.png](images/principio_delicadeza_energetica.png)

## Licença
- Código: MIT License (ver LICENSE-MIT)
- Textos e imagens: CC-BY 4.0 (ver LICENSE-CC-BY-4.0)

## Citação
- Consulte CITATION.cff para citar este trabalho em gerenciadores de referência.

