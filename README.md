# Constante de Kaprekar

Este repositório contém a implementação, em Python, de um algoritmo que executa a **Constante de Kaprekar**, conforme proposto na disciplina de Programação de Computadores do curso de Análise e Desenvolvimento de Sistemas.

O objetivo é demonstrar, de forma iterativa, como números de quatro dígitos convergem para a constante **6174**.

---

## Contextualização

Em 1949, o matemático indiano Dattatreya Ramchandra Kaprekar descreveu uma propriedade interessante:

Ao reorganizar os dígitos de um número de 4 dígitos em ordem crescente e decrescente, e subtrair o menor do maior, o processo sempre converge para **6174**, exceto em casos inválidos.

Esse processo é chamado de **Rotina de Kaprekar**.

---

## Objetivo

Desenvolver um algoritmo que:

- Receba um número de 4 dígitos
- Execute a Rotina de Kaprekar
- Mostre todas as iterações
- Valide corretamente os dados de entrada
- Encerre ao atingir **6174**

---

## Funcionamento do Algoritmo

O programa segue as seguintes etapas:

1. **Validação de tipo**
   - O número deve ser inteiro e positivo

2. **Validação de faixa**
   - Deve estar entre `0000` e `9999`

3. **Validação de dígitos**
   - Não pode ter 3 ou mais dígitos iguais

4. **Processamento**
   - Organiza os dígitos em:
     - Ordem crescente (NDC)
     - Ordem decrescente (NDD)
   - Realiza:
     ```
     NDD - NDC
     ```

5. **Iteração**
   - Repete o processo com o resultado

6. **Parada**
   - Quando atingir:
     ```
     6174
     ```

---
