# Relatório de Justificativa da Abordagem

## Introdução
O problema proposto consiste em encontrar o menor subconjunto de apostas de 15 números (S15) que cubra todas as combinações possíveis de 11, 12, 13 e 14 números (S11, S12, S13, S14) a partir de um universo de 25 números, conforme exigido no trabalho de Complexidade de Algoritmos.

## Análise das Possíveis Abordagens

### 1. Força Bruta
A abordagem por força bruta exigiria testar todas as possíveis seleções de subconjuntos de S15 para verificar quais cobrem todos os subconjuntos menores. O número de combinações possíveis é astronômico (por exemplo, existem mais de 3 milhões de apostas possíveis apenas para S15), tornando essa abordagem absolutamente inviável em termos de tempo e memória, mesmo com computadores modernos. Portanto, a força bruta é impraticável para este problema.

### 2. Algoritmos Exatos (Otimização)
Algoritmos exatos, como programação inteira ou branch-and-bound, também são inviáveis para instâncias desse porte, pois o problema de cobertura de conjuntos é NP-difícil. O tempo de execução cresce exponencialmente com o tamanho do universo, tornando impossível obter a solução ótima em tempo razoável.

### 3. Algoritmos Randômicos/Probabilísticos
Abordagens randômicas podem gerar subconjuntos de S15 aleatoriamente até cobrir todos os subconjuntos menores. No entanto, não há garantia de encontrar uma solução mínima, e o número de apostas geradas tende a ser muito maior do que o necessário. Além disso, o tempo para encontrar uma cobertura completa pode ser imprevisível e, em muitos casos, não atinge a cobertura total dentro de um número razoável de tentativas.

### 4. Algoritmos Metaheurísticos
Técnicas como algoritmos genéticos, simulated annealing e GRASP podem ser aplicadas, mas exigem parametrização cuidadosa, são mais complexas de implementar e, na prática, raramente superam a heurística gulosa para problemas de cobertura de conjuntos grandes. Além disso, não garantem solução ótima e podem demandar muito tempo de execução.

### 5. Algoritmo Guloso (Heurística)
O algoritmo guloso seleciona, a cada passo, a aposta de 15 números que cobre o maior número de subconjuntos ainda não cobertos. Embora não garanta a solução ótima, é a abordagem mais eficiente e prática para problemas de cobertura de conjuntos de grande porte. É simples de implementar, fácil de justificar teoricamente e apresenta resultados próximos do ótimo em tempo viável. Por isso, é amplamente recomendado na literatura para esse tipo de problema.

## Justificativa da Escolha
A heurística gulosa foi escolhida por ser a única abordagem viável e eficiente para o problema proposto, considerando o tamanho do universo e as restrições computacionais. Ela permite obter soluções de boa qualidade em tempo razoável, enquanto outras abordagens são inviáveis, imprevisíveis ou excessivamente complexas para o contexto do trabalho.

## Conclusão
A escolha do algoritmo guloso é a mais sensata e justificável para o problema de cobertura de conjuntos apresentado, sendo reconhecida como a principal heurística para esse tipo de desafio em livros e artigos científicos. Outras abordagens foram consideradas, mas se mostraram impraticáveis ou ineficazes para o escopo do trabalho.

---

*Este relatório pode ser anexado ao trabalho para justificar a escolha da abordagem e demonstrar conhecimento sobre alternativas e suas limitações.*
