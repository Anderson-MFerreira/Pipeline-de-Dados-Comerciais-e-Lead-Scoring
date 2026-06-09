# IT Contract Auditor & Data Extractor

## Descrição
Automação em Python desenvolvida para auditar e extrair dados críticos de contratos de prestação de serviços de TI e licenças de softwares. O script lê arquivos PDF em lote e utiliza Expressões Regulares (Regex) para identificar e capturar automaticamente CNPJs, Valores Mensais e métricas de SLA (Uptime), gerando um relatório consolidado em Excel. Elimina a necessidade de leitura manual de dezenas de páginas.

## Funcionalidades
* **Processamento em Lote:** Lê múltiplos arquivos `.pdf` contidos em um diretório específico.
* **Extração via Regex:** Captura inteligente de padrões textuais para extrair dados financeiros e identificadores fiscais.
* **Consolidação B2B:** Exporta uma planilha pronta para análise de redução de custos e controle de fornecedores de tecnologia.

## Tecnologias Utilizadas
* Python 3
* PDFPlumber (Leitura e conversão de PDFs)
* Expressões Regulares / Regex (Mapeamento de padrões)
* Pandas & Openpyxl (Geração do relatório Excel)

## Como Executar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
