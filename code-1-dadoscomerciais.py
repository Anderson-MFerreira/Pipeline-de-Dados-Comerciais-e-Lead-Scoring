import os
import re
import pandas as pd
import pdfplumber

def extract_contract_data(pdf_path):
    data = {
        "Arquivo": os.path.basename(pdf_path),
        "CNPJ_Fornecedor": "Não encontrado",
        "Valor_Mensal": "Não encontrado",
        "SLA_Uptime": "Não encontrado"
    }
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
                
            cnpj_match = re.search(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', text)
            if cnpj_match:
                data["CNPJ_Fornecedor"] = cnpj_match.group(0)
                
            valor_match = re.search(r'R\$\s?(\d{1,3}(?:\.\d{3})*,\d{2})', text)
            if valor_match:
                data["Valor_Mensal"] = valor_match.group(0)
                
            sla_match = re.search(r'(9[0-9](?:\.[0-9]+)?%)', text)
            if sla_match:
                data["SLA_Uptime"] = sla_match.group(0)
                
    except Exception as e:
        print(f"Erro ao processar {pdf_path}: {e}")
        
    return data

def process_all_contracts(input_folder, output_file):
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        with open(os.path.join(input_folder, "dummy.txt"), "w") as f:
            f.write("Adicione seus contratos em PDF nesta pasta.")
        return

    all_data = []
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            filepath = os.path.join(input_folder, filename)
            all_data.append(extract_contract_data(filepath))
            
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_excel(output_file, index=False)

if __name__ == "__main__":
    input_dir = "contratos_ti_pdf"
    output_report = "auditoria_contratos_automatizada.xlsx"
    process_all_contracts(input_dir, output_report)