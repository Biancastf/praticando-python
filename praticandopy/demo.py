"""
Demonstração das funções disponíveis no projeto praticando-python
"""

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


def main():
    """Executa exemplos de todas as funções"""
    
    print("=" * 60)
    print("🐍 DEMONSTRAÇÃO - Praticando Python")
    print("=" * 60)
    
    # 1. Tempo Total
    print("\n1️⃣  Cálculo de Tempo Total")
    print("-" * 60)
    tempo = calcular_tempo_total(5, 10, 15)
    print(f"   Tempo total: {tempo} dias")
    
    # 2. Acesso
    print("\n2️⃣  Controle de Acesso")
    print("-" * 60)
    acesso = verificar_acesso(14)
    print(f"   Acesso às 14h: {acesso}")
    
    # 3. Empréstimo
    print("\n3️⃣  Validação de Empréstimo")
    print("-" * 60)
    emprestimo = validar_emprestimo(5000, 1200)
    print(f"   Resultado: {emprestimo}")
    
    # 4. IMC
    print("\n4️⃣  Cálculo de IMC")
    print("-" * 60)
    imc_valor, imc_class = calcular_imc(75, 1.75)
    print(f"   IMC: {imc_valor} - {imc_class}")
    
    # 5. Média Escolar
    print("\n5️⃣  Cálculo de Média Escolar")
    print("-" * 60)
    media, situacao = calcular_media_escolar(8, 7, 9)
    print(f"   Média: {media} - Situação: {situacao}")
    
    # 6. Orçamento
    print("\n6️⃣  Verificação de Orçamento")
    print("-" * 60)
    orcamento = verificar_orcamento(2500)
    print(f"   Status: {orcamento}")
    
    # 7. Paridade
    print("\n7️⃣  Verificação de Paridade")
    print("-" * 60)
    paridade = verificar_paridade(42)
    print(f"   O número 42 é: {paridade}")
    
    # 8. Pedágio
    print("\n8️⃣  Cálculo de Pedágio")
    print("-" * 60)
    valor_pedagio = calcular_pedagio(150)
    print(f"   Valor do pedágio para 150 km: R$ {valor_pedagio}")
    
    # 9. Vendas
    print("\n9️⃣  Comparação de Vendas")
    print("-" * 60)
    vendas = comparar_vendas(20, 15)
    print(f"   Resultado: {vendas}")
    
    # 10. Temperatura
    print("\n🔟 Verificação de Temperatura")
    print("-" * 60)
    temp = verificar_temperatura(22)
    print(f"   Status: {temp}")
    
    print("\n" + "=" * 60)
    print("✅ Demonstração concluída!")
    print("=" * 60)


if __name__ == "__main__":
    main()
