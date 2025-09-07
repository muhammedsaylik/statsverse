 import os
from pathlib import Path
from .utils import create_module_dirs
import inspect

class OutputManager:
    def __init__(self):
        # Çalışan notebook veya script ismini al
        frame = inspect.currentframe()
        module_file = inspect.getfile(frame.f_back)
        notebook_name = Path(module_file).stem  # örn: '01_basic_statistics'
        
        self.module_name = notebook_name
        self.base_path = Path("outputs") / self.module_name
        create_module_dirs(self.base_path)

    def save_figure(self, fig, name):
        """matplotlib figürü kaydeder"""
        fig_path = self.base_path / "figures" / f"{name}.png"
        fig.savefig(fig_path, bbox_inches='tight')
        print(f"Figure saved to {fig_path}")

    def save_table(self, df, name):
        """pandas dataframe kaydeder"""
        table_path = self.base_path / "tables" / f"{name}.csv"
        df.to_csv(table_path, index=False)
        print(f"Table saved to {table_path}")


