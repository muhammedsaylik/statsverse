import os
from pathlib import Path
from .utils import create_module_dirs

class ROutputManager:
    def __init__(self, module_name=None):
        if module_name is None:
            # R Markdown için elle geçilecek veya dosya adı alınabilir
            module_name = "default_module"
        self.module_name = module_name
        self.base_path = Path("outputs") / self.module_name
        create_module_dirs(self.base_path)

    def save_plot(self, filename):
        return str(self.base_path / "figures" / filename)

    def save_table(self, filename):
        return str(self.base_path / "tables" / filename)


