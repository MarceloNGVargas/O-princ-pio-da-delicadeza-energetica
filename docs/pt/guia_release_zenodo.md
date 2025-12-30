# Guia de Release v1.0 e DOI via Zenodo

## Pré-requisitos
- Repositório público no GitHub
- Branch principal: main
- Arquivos de licença: LICENSE-MIT e LICENSE-CC-BY-4.0
- Arquivo de citação: CITATION.cff
- Documentação organizada em docs/pt e docs/en; imagens em images/; script em examples/

## Criar o release v1.0 no GitHub
- Via CLI:
  - gh release create v1.0 --repo MarceloNGVargas/O-principio-da-delicadeza-energetica --generate-notes --title "v1.0"
- Via interface web:
  - Acesse o repositório → Releases → Draft a new release
  - Tag: v1.0, Target: main
  - Title: v1.0
  - Publish release

## Conectar com Zenodo e gerar DOI
- Acesse https://zenodo.org e faça login com GitHub
- Autorize acesso e vá em Settings → GitHub
- Habilite o repositório MarceloNGVargas/O-principio-da-delicadeza-energetica
- Ative a opção de arquivamento automático em releases
- Crie ou confirme o release v1.0 no GitHub
- Aguarde Zenodo arquivar o release e gerar o DOI
- Copie o DOI gerado (formato 10.5281/zenodo.xxxxxxx)

## Atualizar CITATION.cff e README com o DOI
- Editar CITATION.cff:
  - Adicionar:
    - doi: "10.5281/zenodo.xxxxxxx"
    - identifiers:
      - type: doi
        value: "10.5281/zenodo.xxxxxxx"
- Editar README.md:
  - Badge:
    - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg)](https://doi.org/10.5281/zenodo.xxxxxxx)

## Verificações finais
- README renderiza links relativos (docs/, images/)
- Release v1.0 visível e com notas
- DOI resolve para a página do Zenodo com artefatos
- Licenças e CITATION presentes na raiz

## Opcional
- Adicionar palavras-chave e comunidades no Zenodo
- Incluir arquivos extras como assets do release
