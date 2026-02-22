# 🚀 Guia Rápido (Quick Start)

Comece a usar o projeto em 5 minutos!

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Git (opcional)

## ⚡ Instalação Rápida

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/praticando-python.git
cd praticando-python
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv

# Ative o ambiente
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

## 🎯 Uso Básico

### Executar um script individual
```bash
python imc.py
python media.py
python emprestimo.py
```

### Executar a demonstração
```bash
python demo.py
```

### Executar os testes
```bash
python run_tests.py

# Com cobertura de código
python run_tests.py --coverage
```

## 🧪 Usar as funções no seu código

```python
from utils import calcular_imc, calcular_media_escolar

# Calcular IMC
imc_valor, classificacao = calcular_imc(70, 1.75)
print(f"Seu IMC é: {imc_valor} ({classificacao})")

# Calcular média
media, situacao = calcular_media_escolar(8, 7, 9)
print(f"Média: {media} - {situacao}")
```

## 📚 Documentação Completa

- [README.md](README.md) - Documentação detalhada de todas as atividades
- [CONTRIBUTING.md](CONTRIBUTING.md) - Como contribuir com o projeto
- [CHANGELOG.md](CHANGELOG.md) - Histórico de mudanças

## 🤔 Dúvidas Comuns

**P: Como executo um teste específico?**
```bash
pytest tests/test_utils.py::test_imc_peso_normal -v
```

**P: Como vejo a cobertura de código?**
```bash
python run_tests.py --coverage
# Abra: htmlcov/index.html
```

**P: Posso usar essas funções em outro projeto?**
Sim! Copie o arquivo `utils.py` para seu projeto:
```python
from utils import calcular_imc
```

**P: Como contribuo com novos exercícios?**
Veja [CONTRIBUTING.md](CONTRIBUTING.md) para instruções detalhadas.

## 📞 Suporte

- ❓ Dúvidas? Abra uma [issue](../../issues)
- 💡 Sugestões? Abra uma [discussão](../../discussions)
- 🐛 Bug encontrado? Reporte em [issues](../../issues)

## 📝 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para detalhes.

---

**Pronto para começar? Execute:**
```bash
python demo.py
```

**Happy Coding! 🎉**
