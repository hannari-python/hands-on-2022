# PythonでAPIにアクセスしてきて取得したデータをExcelファイルに書き出してみる
from pathlib import Path

import requests
from openpyxl import Workbook

JP_HOLIDAY_API_URL = "https://holidays-jp.github.io/api/v1/date.json"

HANDSON_DIR = Path(__file__).parent
EXPORT_EXCEL_FILEPATH = HANDSON_DIR / "export_jp_holiday_list.xlsx"


def get_api_data(api_url: str) -> dict:
    return requests.get(api_url).json()


def main() -> None:
    # jp.holiday apiからデータを生成
    jp_holiday_data_list = get_api_data(JP_HOLIDAY_API_URL)
    print(jp_holiday_data_list)



if __name__ == "__main__":
    main()
