## 💡 Por que utilizamos uma heurística?

O problema de encontrar o menor número de apostas de 15 números que cubra todas as combinações possíveis de 11 (ou 12, 13, 14) números é uma aplicação direta do **Problema de Cobertura de Conjuntos (Set Cover Problem)** — um problema clássico da Ciência da Computação, conhecido por ser **NP-difícil**.

---

### ❌ Por que não usar uma abordagem exata?

Uma abordagem exata exigiria:

- 🧮 Gerar todas as apostas possíveis de 15 números:  
  \[
  \binom{25}{15} = 3.268.760 \text{ apostas}
  \]

- 🔍 Testar todos os subconjuntos possíveis dessas apostas para cobrir todas as combinações de 11 números:  
  \[
  \binom{25}{11} = 4.457.400 \text{ combinações}
  \]

Mesmo limitando a busca a subconjuntos com **até 50 apostas** dentro de um universo de 100 mil apostas, o número de combinações seria:

\[
\sum_{k=1}^{50} \binom{100000}{k}
\]

❗ Só o termo \( \binom{100000}{20} \) já ultrapassa \( 10^{90} \) combinações.  
💥 Considerar todos os subconjuntos possíveis entre as 3 milhões de apostas levaria a \( 2^{3.268.760} \) combinações — **completamente inviável**, mesmo com supercomputadores.

---

### ✅ Por que escolhemos a heurística gulosa?

A **heurística gulosa** funciona da seguinte forma:

1. Seleciona a cada passo a aposta de 15 números que **cobre mais subconjuntos ainda não cobertos**.
2. Repete o processo até que **todas as combinações menores (S11 a S14)** estejam cobertas.
3. Garante **resultados bons o suficiente** em tempo viável.

⚡ Mesmo sem garantir a solução ótima, a heurística entrega um **equilíbrio entre qualidade e desempenho**, resolvendo o problema em **horas ou dias**, em vez de séculos.

---

### 🧠 Conclusão

> O uso de heurística não é apenas uma decisão de otimização — é **uma exigência prática**.

🔒 A força bruta é computacionalmente impossível para o tamanho real do problema.  
🧭 A heurística gulosa é a **única alternativa viável e eficaz** para resolver o problema de cobertura de subconjuntos no contexto da Lotofácil.

---
