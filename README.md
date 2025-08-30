# Pipeline IA - Troubleshooting Automático com ChatGPT

Este projeto implementa uma pipeline de CI/CD com falha intencional e troubleshooting automático usando ChatGPT para análise e sugestões de correção.

## 📋 Visão Geral

A pipeline é composta por dois jobs principais:
1. **Falha Intencional**: Simula diferentes tipos de erros comuns em deployments
2. **Troubleshooting com ChatGPT**: Analisa o erro e gera um relatório com sugestões de correção

## 🚀 Como Funciona

### Job 1: `failing-step`
Este job simula falhas reais que podem ocorrer em um ambiente de produção:

- **Database Connection Timeout**: Simula falha de conexão com banco de dados
- **Missing Environment Variable**: Simula variável de ambiente não configurada
- **Docker Build Failure**: Simula erro na construção de imagem Docker
- **Permission Denied**: Simula falha de autenticação SSH

O job sempre falha intencionalmente e captura informações detalhadas sobre o erro.

### Job 2: `chatgpt-troubleshooting`
Este job é executado apenas quando o primeiro job falha e:

1. Executa o script Python `chatgpt_troubleshoot.py`
2. Envia o contexto do erro para o ChatGPT
3. Gera um relatório de troubleshooting
4. Faz upload do relatório como artefato
5. Comenta no PR (se aplicável) com as sugestões

## 📁 Estrutura do Projeto

```
pipeline_ia/
├── .github/
│   └── workflows/
│       └── cd.yml              # Pipeline principal
├── scripts/
│   └── chatgpt_troubleshoot.py # Script de troubleshooting
├── README.md                   # Esta documentação
└── TECHNICAL_DOCS.md           # Documentação técnica
```

## 🔧 Configuração

### Pré-requisitos

1. **OpenAI API Key**: Necessária para usar o ChatGPT
   - Crie uma conta em [OpenAI](https://platform.openai.com/)
   - Gere uma API key
   - Adicione como secret `OPENAI_API_KEY` no repositório

### Configuração do Secret

1. Vá para o repositório no GitHub
2. Acesse `Settings` > `Secrets and variables` > `Actions`
3. Clique em `New repository secret`
4. Nome: `OPENAI_API_KEY`
5. Valor: Sua chave da API OpenAI

## 🐍 Script Python: `chatgpt_troubleshoot.py`

### Funcionalidades

O script Python é responsável por:

1. **Coleta de Contexto**: Captura informações do ambiente GitHub Actions
2. **Integração com OpenAI**: Envia dados para o modelo GPT-4
3. **Geração de Relatório**: Cria um arquivo markdown com análise detalhada
4. **Tratamento de Erros**: Gerencia falhas de API e conectividade

### Variáveis de Ambiente Utilizadas

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `OPENAI_API_KEY` | Chave da API OpenAI | `sk-...` |
| `ERROR_TYPE` | Tipo do erro capturado | `database_connection_timeout` |
| `WORKFLOW_NAME` | Nome do workflow | `Test Pipeline with ChatGPT` |
| `REPOSITORY` | Nome do repositório | `iesodias/pipeline_ia` |
| `BRANCH` | Branch atual | `main` |
| `COMMIT` | Hash do commit | `abc123...` |

## 📚 Referências

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python Requests Library](https://docs.python-requests.org/)

## 📄 Licença

Este projeto é apenas para fins educacionais e demonstração.
