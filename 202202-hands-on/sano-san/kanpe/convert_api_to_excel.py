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

    holiday_wb = Workbook()
    holiday_ws = holiday_wb.active
    holiday_ws.title = "日本の祝日一覧"

    # 祝日一覧を日付と曜日でExcelファイルへ書き出す

    # 列見出しを生成
    holiday_ws.cell(1, 1, "日付")
    holiday_ws.cell(1, 2, "祝日名")

    # enumerate: リストなどの連続データ:シーケンシャル を行番号をつけて出力してくれる。
    # enumerate(シーケンシャルなオブジェクト, 開始行番号)
    for row_index, jp_holiday_data in enumerate(jp_holiday_data_list.items(), 2):

        jp_holiday_date = jp_holiday_data[0]
        jp_holiday_name = jp_holiday_data[1]
        print(f"{row_index}, {jp_holiday_date}, {jp_holiday_name}")

        # 2列だけなので直接指定で入れてます
        holiday_ws.cell(column=1, row=row_index, value=f"{jp_holiday_date}")
        holiday_ws.cell(column=2, row=row_index, value=f"{jp_holiday_name}")

    # ファイルを保存する
    holiday_wb.save(filename=EXPORT_EXCEL_FILEPATH)


if __name__ == "__main__":
    main()
