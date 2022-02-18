---
marp: true
# header: "**ラズパイとDashで環境ダッシュボードを作ろう** PyCon JP 2021 2021/10/16"
backgroundColor: #eee
---

## PythonでExcelファイルを読んだり書いたりするハンズオン

はんなりPython
2022/02/18

---

## お前誰よ

- 佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)
  - 🏠:静岡県の富士市🗻
- Job💼
  - [株式会社佐野設計事務所](https://sano-design.info)
    - 自動車向けプレス金型機械の設計事務所
      - 最近は3Dデータの製作/モデリングもやってます！
  - 米農家🌾
- Community🙋
  - 静岡Pythonコミュニティ: Python駿河、PyCon mini Shizuokaスタッフ
  - Code for ふじのくに

---

## FYI

- 静岡Pythonコミュニティの勉強会 Python駿河/Unagi.py
  - 2月は明日開催です！
  - 詳しくはこちら: https://py-suruga.connpass.com/event/238467/

---

## 今日のハンズオンでやること

- Pythonで（ライブラリ）パッケージをインストールする
- ExcelなファイルをPythonで読み込む
- Pythonで作った情報をExcelファイルに書き出す

---

## 今日のハンズオンのモチベーション

- 普段手作業でやっていることをPythonでやらせてみる
  - 退屈なことはPy...（以下 オライリーで見てね
- Excelを頑張るのはもうつらい
  - （はずなのにlambda関数なんか入ったりするので楽しさはあるけど）
- 手作業によるミスやヒューマンエラーを防ぐ
  - 3日前にしくじったので二度とやりたくない

---

## しくじり先生: 公開したくないExcelファイルをメールで送る

↑の文章だけで戦慄する

詳しいことは言わない（言えない）

- Excelで計算したものをPDF化変換してメール送付
- 変換作業は自動化していた:
メール送付時に不用意にExcelファイルは触らなくていい
- 一部不備があったExcelファイルをメール送付前に編集
→ **手作業してしまう（魔が差した**
- 後はわかるな...

しかもこれ3日前やったんですね...

<!-- _footer: もはやネタにするしかねえ -->

---

一度や二度はあると思いますが、本題に戻ります

![irasutoya](https://4.bp.blogspot.com/-L8kmjYNX064/VsGsN2ctx1I/AAAAAAAA39o/NHU8Gnym2GE/s400/kaisya_samui_man.png)

<!-- _footer: 俺みたいになるなよ！ -->

---

## ライブラリをインストールしましょう

- Pythonはバッテリーインクルードな言語
- 個人/コミュニティ/企業がサードパーティなライブラリをパッケージ公開する
  - `pip`でインストール, pypiにて公開される
  - パッケージはとっても豊富→エコシステムとして成熟している環境

今日はxlsxを読み書きできる `openpyxl` を使います

（そのほか標準ライブラリも使いますが、適時解説します）

---

## 確認すること

- Python 3.10は入ってる？
- pip install openpyxl
- 今日利用する資料のDL先
  - git clone <https://github.com/hrsano645/hands-on-2022.git>
  - <https://github.com/hrsano645/hands-on-2022> から zip ダウンロード

---

## PythonでExcelファイルを読み込む

---

やること

- 帳票的なExcelファイルを読み込む: 架空の業務っぽいファイルを使います
- 読み込んだ帳票データをjsonファイルに書き出す

---

## PythonでExcelファイルを書き出す

---

やること

- 日本の祝日APIからデータを取得する
  - <https://holidays-jp.github.io>
- 集めたデータをExcelファイルへ書き出す

---

## 付録

---

## Excelを扱うほかの方法

- pandas: バックエンドはopenpyxl
- そのほか: こちらに載ってます -> <https://www.python-excel.org>
  - 現在はopenpyxlをおすすめされることが多くなりました
