# Trabalho de Complexidade de Algoritmos - Lotofácil

## Descrição Geral
Este projeto resolve o problema de cobertura de subconjuntos para a Lotofácil, conforme proposto na disciplina de Complexidade de Algoritmos. O objetivo é gerar todas as combinações possíveis de apostas e, a partir delas, encontrar subconjuntos mínimos de apostas de 15 números que cubram todas as combinações menores (de 11 a 14 números), além de analisar a complexidade e o custo financeiro dessas soluções.

## Estrutura dos Arquivos

- **main.py**: Arquivo principal. Apresenta um menu interativo para o usuário escolher qual etapa executar. Centraliza a chamada das funções dos demais módulos.
- **combinacoes.py**: Responsável pela geração e salvamento de todas as combinações possíveis de 11 a 15 números (PROGRAMA 1). Gera arquivos S11.txt, S12.txt, S13.txt, S14.txt e S15.txt.
- **cobertura.py**: Implementa a heurística gulosa para encontrar subconjuntos de apostas de 15 números que cubram todas as combinações de 11, 12, 13 ou 14 números (PROGRAMAS 2 a 5). Gera arquivos SB15_11.txt, SB15_12.txt, SB15_13.txt e SB15_14.txt.
- **analise.py**: Apresenta a análise de complexidade de tempo do algoritmo guloso utilizado para a cobertura dos subconjuntos (ITEM 6).
- **custo.py**: Calcula o custo financeiro para jogar todos os subconjuntos de apostas encontrados, considerando o valor de R$ 3,00 por aposta (ITEM 7).
- **randomico.py**: Implementa uma abordagem randômica alternativa para o problema de cobertura, utilizada para comparação e justificativa da escolha da heurística gulosa.
- **relatorio_justificativa.md**: Relatório formal justificando a escolha do algoritmo guloso e explicando por que outras abordagens não são viáveis ou eficientes para o problema.

## Funcionamento do Projeto

1. **Geração das Combinações**
   - O usuário pode gerar todas as combinações possíveis de 11 a 15 números, que são salvas em arquivos de texto. Cada linha representa uma combinação distinta.

2. **Cobertura dos Subconjuntos**
   - Utilizando uma heurística gulosa, o programa encontra subconjuntos de apostas de 15 números que cobrem todas as combinações menores (S11, S12, S13, S14). O processo é computacionalmente intensivo e pode levar horas ou dias para grandes valores de t.

3. **Análise de Complexidade**
   - O projeto apresenta uma análise formal da complexidade de tempo do algoritmo guloso, detalhando as etapas e justificando a escolha da abordagem.

4. **Cálculo do Custo Financeiro**
   - O programa calcula o custo total para jogar todos os subconjuntos de apostas gerados, multiplicando o número de apostas pelo valor unitário do cartão.

5. **Abordagem Randômica (Opcional)**
   - O arquivo `randomico.py` demonstra uma abordagem alternativa baseada em sorteio aleatório de apostas, servindo para comparação e justificativa teórica.

## Como Executar

1. Execute o arquivo `main.py`.
2. Siga o menu interativo para escolher a etapa desejada.
3. Os arquivos gerados estarão na mesma pasta do projeto.

> **Atenção:** As etapas de cobertura (PROGRAMAS 2 a 5) podem demandar muito tempo e memória, dependendo do tamanho do subconjunto a ser coberto.

## Observações Finais
- O projeto está modularizado para facilitar a compreensão, manutenção e apresentação.
- Comentários detalhados foram adicionados em todos os arquivos para explicar o funcionamento das funções e a lógica dos algoritmos.
- O relatório de justificativa pode ser utilizado para fundamentar a escolha da abordagem no contexto acadêmico.

---

Desenvolvido para a disciplina de Complexidade de Algoritmos - 2025/1
Professor: Edson Emílio Scalabrin
