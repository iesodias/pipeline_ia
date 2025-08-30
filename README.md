# Pipeline IA

[![CI Pipeline](https://github.com/iesodias/pipeline_ia/actions/workflows/ci.yml/badge.svg)](https://github.com/iesodias/pipeline_ia/actions/workflows/ci.yml)
[![CD Pipeline](https://github.com/iesodias/pipeline_ia/actions/workflows/cd.yml/badge.svg)](https://github.com/iesodias/pipeline_ia/actions/workflows/cd.yml)
[![Code Quality](https://github.com/iesodias/pipeline_ia/actions/workflows/code-quality.yml/badge.svg)](https://github.com/iesodias/pipeline_ia/actions/workflows/code-quality.yml)

Uma pipeline de Inteligência Artificial com integração completa ao GitHub Actions para CI/CD.

## 🚀 Características

- **Pipeline CI/CD Completa**: Integração e deployment automatizados
- **Qualidade de Código**: Linting, formatação e análise de segurança
- **Testes Automatizados**: Cobertura de testes unitários e de integração
- **Containerização**: Suporte completo ao Docker
- **Segurança**: Verificações automáticas de vulnerabilidades
- **Documentação**: Documentação automática e templates

## 📁 Estrutura do Projeto

```
pipeline_ia/
├── .github/
│   ├── workflows/          # GitHub Actions workflows
│   ├── ISSUE_TEMPLATE/     # Templates para issues
│   └── pull_request_template.md
├── src/                    # Código fonte principal
│   ├── core/              # Módulos principais
│   ├── config.py          # Configurações
│   └── __init__.py
├── tests/                  # Testes unitários
├── scripts/               # Scripts de build e deploy
├── docs/                  # Documentação
├── requirements.in        # Dependências principais
├── requirements-dev.in    # Dependências de desenvolvimento
├── pyproject.toml         # Configuração do projeto
├── Dockerfile             # Container Docker
├── docker-compose.yml     # Orquestração de containers
└── README.md
```

## 🛠️ Configuração do Ambiente

### Pré-requisitos

- Python 3.9+
- Git
- Docker (opcional)

### Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/iesodias/pipeline_ia.git
cd pipeline_ia

# Execute o script de setup
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### Instalação Manual

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Instalar hooks de pre-commit
pre-commit install
```

## 🚀 Como Usar

### Executar a Pipeline

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar a aplicação
python -m src
```

### Executar Testes

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=src/

# Apenas testes unitários
pytest tests/ -m unit
```

### Verificações de Qualidade

```bash
# Executar todas as verificações
./scripts/lint.sh

# Formatação do código
black src/ tests/
isort src/ tests/

# Linting
flake8 src/ tests/
mypy src/
```

## 🐳 Docker

### Build e Execução

```bash
# Build da imagem
docker build -t pipeline-ia .

# Executar container
docker run -p 8000:8000 pipeline-ia

# Usando docker-compose
docker-compose up -d
```

## 🔄 GitHub Actions

### Workflows Disponíveis

1. **CI Pipeline** (`.github/workflows/ci.yml`)
   - Testes em múltiplas versões do Python
   - Verificações de qualidade de código
   - Análise de segurança
   - Relatórios de cobertura

2. **CD Pipeline** (`.github/workflows/cd.yml`)
   - Deploy automático para staging
   - Build e push de imagens Docker
   - Deploy para produção com tags

3. **Code Quality** (`.github/workflows/code-quality.yml`)
   - Verificações em Pull Requests
   - Formatação e linting
   - Análise estática

4. **Dependency Update** (`.github/workflows/dependency-update.yml`)
   - Atualização automática de dependências
   - Criação de PRs automáticos

### Configuração de Secrets

Configure os seguintes secrets no GitHub:

```
GITHUB_TOKEN          # Token para operações no GitHub
```

Para deploy em produção, adicione também:

```
PRODUCTION_API_KEY    # Chave da API de produção
PRODUCTION_URL        # URL do ambiente de produção
```

## 📊 Monitoramento e Logs

### Estrutura de Logs

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Pipeline executada com sucesso")
```

### Métricas

- Cobertura de testes
- Tempo de execução da pipeline
- Análise de qualidade de código
- Vulnerabilidades de segurança

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código

- Use Black para formatação
- Siga PEP 8
- Adicione testes para novas funcionalidades
- Mantenha cobertura de testes acima de 80%

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🔗 Links Úteis

- [Documentação](docs/)
- [Issues](https://github.com/iesodias/pipeline_ia/issues)
- [Pull Requests](https://github.com/iesodias/pipeline_ia/pulls)
- [Releases](https://github.com/iesodias/pipeline_ia/releases)

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique as [Issues existentes](https://github.com/iesodias/pipeline_ia/issues)
2. Crie uma nova issue usando os templates disponíveis
3. Para bugs, inclua informações detalhadas sobre o ambiente

---

Desenvolvido com ❤️ para facilitar o desenvolvimento de pipelines de IA com CI/CD robusta.
