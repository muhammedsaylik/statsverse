from pathlib import Path

def create_module_dirs(base_path):
    """figures, tables, reports klasörlerini oluşturur"""
    for folder in ["figures", "tables", "reports"]:
        (base_path / folder).mkdir(parents=True, exist_ok=True)


