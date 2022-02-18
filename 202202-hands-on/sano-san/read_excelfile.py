# PythonでExcelファイルを読み込んで、CSVファイルに書き出してみる
import json
from datetime import datetime
from pathlib import Path

from openpyxl import load_workbook

HANDSON_DIR = Path(__file__).parent
EXAMPLE_EXCEL_FILEPATH = HANDSON_DIR / "./example_tyohyo.xlsx"

EXPORT_JSON_FILEPATH = HANDSON_DIR / "export_tyohyo.json"


def main() -> None:
    # （Excelの数式はすでに計算された結果が入っていることを想定）
    ex_wb = load_workbook(filename=EXAMPLE_EXCEL_FILEPATH, data_only=True)



if __name__ == "__main__":
    main()
