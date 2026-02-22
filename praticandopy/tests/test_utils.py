"""
Testes unitários para as funções de prática
"""
import pytest
from utils import (
    calcular_tempo_total,
    verificar_acesso,
    validar_emprestimo,
    calcular_imc,
    calcular_media_escolar,
    verificar_orcamento,
    verificar_paridade,
    calcular_pedagio,
    comparar_vendas,
    verificar_temperatura,
)


# Testes do tempo total
def test_calcular_tempo_total_valido():
    assert calcular_tempo_total(5, 10, 15) == 30


def test_calcular_tempo_total_zeros():
    assert calcular_tempo_total(0, 0, 0) == 0


def test_calcular_tempo_total_negativo():
    with pytest.raises(ValueError):
        calcular_tempo_total(-1, 5, 10)


# Testes de acesso
def test_verificar_acesso_permitido():
    assert verificar_acesso(12) == "acesso permitido"


def test_verificar_acesso_negado_madrugada():
    assert verificar_acesso(3) == "acesso negado"


def test_verificar_acesso_negado_noite():
    assert verificar_acesso(20) == "acesso negado"


# Testes de empréstimo
def test_emprestimo_aprovado():
    assert validar_emprestimo(5000, 1000) == "empréstimo aprovado"


def test_emprestimo_renda_insuficiente():
    assert validar_emprestimo(1500, 300) == "empréstimo negado: renda mensal insuficiente"


def test_emprestimo_parcela_acima_limite():
    assert validar_emprestimo(3000, 1000) == "empréstimo negado: parcela acima de 30% da renda mensal"


# Testes de IMC
def test_imc_abaixo_peso():
    imc, classificacao = calcular_imc(50, 1.70)
    assert classificacao == "abaixo do peso"


def test_imc_peso_normal():
    imc, classificacao = calcular_imc(70, 1.70)
    assert classificacao == "peso normal"


def test_imc_acima_peso():
    imc, classificacao = calcular_imc(90, 1.70)
    assert classificacao == "acima do peso"


# Testes de média escolar
def test_media_escolar_aprovado():
    media, situacao = calcular_media_escolar(8, 9, 7)
    assert situacao == "aprovado"


def test_media_escolar_recuperacao():
    media, situacao = calcular_media_escolar(5, 6, 4)
    assert situacao == "recuperação"


def test_media_escolar_reprovado():
    media, situacao = calcular_media_escolar(3, 2, 3)
    assert situacao == "reprovado"


# Testes de orçamento
def test_orcamento_dentro_limite():
    assert "dentro do orçamento" in verificar_orcamento(2000)


def test_orcamento_acima_limite():
    assert "ultrapassou" in verificar_orcamento(4000)


# Testes de paridade
def test_numero_par():
    assert verificar_paridade(10) == "par"


def test_numero_impar():
    assert verificar_paridade(7) == "ímpar"


# Testes de pedágio
def test_pedagio_menos_100km():
    assert calcular_pedagio(50) == 10


def test_pedagio_entre_100_200km():
    assert calcular_pedagio(150) == 20


def test_pedagio_acima_200km():
    assert calcular_pedagio(250) == 30


# Testes de vendas
def test_vendas_mais_macas():
    assert "maçãs" in comparar_vendas(10, 5)


def test_vendas_mais_bananas():
    assert "bananas" in comparar_vendas(5, 10)


def test_vendas_iguais():
    assert "mesma quantidade" in comparar_vendas(5, 5)


# Testes de temperatura
def test_temperatura_dentro_limite():
    assert "dentro" in verificar_temperatura(20)


def test_temperatura_acima_limite():
    assert "alerta" in verificar_temperatura(30)
