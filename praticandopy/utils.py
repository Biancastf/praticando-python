"""
Utilitários com funções reutilizáveis das atividades de prática
"""

def calcular_tempo_total(at_a, at_b, at_c):
    """Calcula o tempo total do projeto validando se os dias são não-negativos"""
    if at_a >= 0 and at_b >= 0 and at_c >= 0:
        return at_a + at_b + at_c
    else:
        raise ValueError("Os dias não podem ser negativos.")


def verificar_acesso(hora_atual):
    """Verifica se o acesso é permitido baseado na hora (formato 24h)"""
    if 8 <= hora_atual < 18:
        return "acesso permitido"
    else:
        return "acesso negado"


def validar_emprestimo(renda_mensal, parcela):
    """Valida a aprovação de um empréstimo"""
    if renda_mensal > 2000 and parcela <= 0.3 * renda_mensal:
        return "empréstimo aprovado"
    elif renda_mensal <= 2000:
        return "empréstimo negado: renda mensal insuficiente"
    else:
        return "empréstimo negado: parcela acima de 30% da renda mensal"


def calcular_imc(peso, altura):
    """Calcula o IMC e retorna o valor e a classificação"""
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        classificacao = "peso normal"
    else:
        classificacao = "acima do peso"
    return round(imc, 2), classificacao


def calcular_media_escolar(nota1, nota2, nota3):
    """Calcula a média escolar e determina a situação do aluno"""
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        situacao = "aprovado"
    elif 5 <= media < 7:
        situacao = "recuperação"
    else:
        situacao = "reprovado"
    return round(media, 2), situacao


def verificar_orcamento(despesas, limite=3000):
    """Verifica se as despesas ultrapassam o limite de orçamento"""
    if despesas > limite:
        return f"atenção! você ultrapassou o limite do orçamento (R$ {limite})"
    else:
        return "você está dentro do orçamento"


def verificar_paridade(numero):
    """Verifica se um número é par ou ímpar"""
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def calcular_pedagio(distancia):
    """Calcula o valor do pedágio de acordo com a distância"""
    if distancia < 100:
        return 10
    elif 100 <= distancia <= 200:
        return 20
    else:
        return 30


def comparar_vendas(maca, banana):
    """Compara o volume de vendas entre maçãs e bananas"""
    if maca > banana:
        return "você vendeu mais maçãs que bananas"
    elif banana > maca:
        return "você vendeu mais bananas que maçãs"
    else:
        return "você vendeu a mesma quantidade de maçãs e bananas"


def verificar_temperatura(temperatura, limite=25):
    """Verifica se a temperatura está dentro do limite permitido"""
    if temperatura > limite:
        return f"alerta! temperatura acima do limite permitido ({limite}°C)"
    else:
        return "temperatura dentro do limite permitido"
