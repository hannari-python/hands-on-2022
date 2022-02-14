# 佐野さんハンズオン格納用

PythonでExcelファイルを読んだり書いたりしてみるハンズオン

## 必要環境

- Python (3.8<=)3.10
  - win: 公式のインストーラーをおすすめ
  - mac: 公式インストーラー or homebrewをおすすめ
- openpyxl: [openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files — openpyxl 3.0.9 documentation](https://openpyxl.readthedocs.io/en/stable/)
  - PythonでExcelファイル（xlsx）を読み書きするソフトウェア
- エディタ: VSCodeをおすすめ（もしくはpycharm）

## 環境作成

※pythonコマンドは各環境によって異なる可能性があります。`python`コマンドでpython3.10が起動しない場合（MacやLinux系にあります）

- venvで仮想環境作成
  - win `python -m venv .venv`
  - mac `python3 -m venv .venv`
- venvへ入ります
  - win `.venv/Scripts/activate`
  - mac `source .venv/bin/activate`
- pipで`openpyxl`をインストールします
  - all `python -m pip install openpyxl`

## ハンズオンで行うこと

- PythonでExeclファイルを読み込んで値を操作してみます。
- Pythonでなんらかの情報を作ってExcelファイルを書き出してみます。
- （Python3.10で使える何かを使ってみる？）
