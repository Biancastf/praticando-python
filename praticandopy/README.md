# Atividades de Prática Python 🐍

Este repositório contém uma coleção de scripts Python para praticar conceitos básicos de programação, como condicionais e operações matemáticas.

---

## 📋 Descrição das Atividades

### 1. **calctempo.py** - Cálculo de Tempo Total do Projeto
Calcula o tempo total necessário para um projeto somando os dias de três atividades diferentes.

**Entrada:**
- Dias para a atividade A
- Dias para a atividade B
- Dias para a atividade C

**Saída:**
- Tempo total do projeto em dias

**Validação:** Verifica se os valores são não-negativos

---

### 2. **controleac.py** - Controle de Acesso por Horário
Verifica se o acesso é permitido baseado na hora atual (formato 24 horas).

**Entrada:**
- Hora atual (0-23)

**Saída:**
- "acesso permitido" se entre 8h e 18h
- "acesso negado" caso contrário

---

### 3. **emprestimo.py** - Aprovação de Empréstimo
Valida a aprovação de um empréstimo com base na renda mensal e no valor da parcela.

**Entrada:**
- Renda mensal
- Valor da parcela desejada

**Critérios de Aprovação:**
- ✅ Renda > R$ 2.000
- ✅ Parcela ≤ 30% da renda mensal

---

### 4. **imc.py** - Cálculo de Índice de Massa Corporal
Calcula o IMC (Índice de Massa Corporal) e classifica o resultado em categorias.

**Entrada:**
- Peso (em kg)
- Altura (em metros)

**Fórmula:** IMC = peso / altura²

**Classificação:**
- IMC < 18,5 → Abaixo do peso
- 18,5 ≤ IMC < 25 → Peso normal
- IMC ≥ 25 → Acima do peso

---

### 5. **media.py** - Cálculo de Média Escolar
Calcula a média de três notas e determina a situação do aluno.

**Entrada:**
- Primeira nota
- Segunda nota
- Terceira nota

**Situação:**
- Média ≥ 7 → Aprovado
- 5 ≤ Média < 7 → Recuperação
- Média < 5 → Reprovado

---

### 6. **orcamento.py** - Controle de Orçamento
Verifica se as despesas do mês ultrapassam o limite de orçamento.

**Entrada:**
- Total de despesas do mês

**Limite:** R$ 3.000

**Saída:**
- Alerta se ultrapassar o limite
- Confirmação se dentro da meta

---

### 7. **paridade.py** - Verificação de Paridade
Verifica se um número é par ou ímpar.

**Entrada:**
- Um número inteiro

**Saída:**
- "o número é par" ou "o número é ímpar"

---

### 8. **pedagio.py** - Cálculo de Valor de Pedágio
Calcula o valor do pedágio de acordo com a distância percorrida.

**Entrada:**
- Distância percorrida (em km)

**Tabela de Preços:**
- Distância < 100 km → R$ 10
- 100 ≤ Distância ≤ 200 km → R$ 20
- Distância > 200 km → R$ 30

---

### 9. **temperatura.py** - Monitoramento de Temperatura
Verifica se a temperatura está dentro do limite permitido.

**Entrada:**
- Temperatura atual (em graus)

**Limite:** 25°C

**Saída:**
- Alerta se acima do limite
- Confirmação se dentro do limite

---

### 10. **vendasc.py** - Comparação de Vendas
Compara o volume de vendas entre maçãs e bananas.

**Entrada:**
- Quantidade de maçãs vendidas
- Quantidade de bananas vendidas

**Saída:**
- Qual fruta foi mais vendida
- Ou se as quantidades foram iguais

---

## 🚀 Como Executar

Para executar qualquer script, use o comando:

```bash
python nome_do_arquivo.py
```

**Exemplo:**
```bash
python imc.py
```

---

## 💡 Conceitos Praticados

- ✅ Estruturas condicionais (`if`, `elif`, `else`)
- ✅ Operadores de comparação (`>`, `<`, `==`, `<=`, `>=`)
- ✅ Operadores lógicos (`and`, `or`)
- ✅ Entrada de dados (`input()`)
- ✅ Saída de dados (`print()`)
- ✅ Operações matemáticas
- ✅ Formatação de strings (`f-strings`)
- ✅ Validação de dados

---

## 📝 Notas

Todos os scripts utilizam entrada interativa via teclado. Certifique-se de inserir os dados no formato solicitado (inteiros ou decimais conforme indicado).

---

**Desenvolvido como prática de programação Python básica** 🎓
