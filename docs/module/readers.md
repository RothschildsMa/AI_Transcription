# AI_Transcription：Reader モジュール処理説明

## 1. 概要

Reader モジュールは、**ユーザーがアップロードした履歴書ファイル**（Excel / Word）から内容を読み取り、**テキスト行のリスト**として出力します。  
このモジュールの目的は以下の通りです：

- Excel および Word ファイルに対応
- 標準化されたテキストリストを出力
- 空行や無効データを無視

---

## 2. モジュールパス

```text
src/
└─ ai_transcription/
   └─ core/
      └─ readers/
         ├─ __init__.py
         ├─ excel_reader.py
         └─ word_reader.py
```

## 3. ExcelReader の処理

### 3.1 機能

- Excel ファイルを読み込む  
- 各行を文字列として結合  
- 空値や空行を除外

### 3.2 処理フロー

```text
Excel ファイル → pandas で読み込み → 各行をループ → セルを結合して1行の文字列に → 空値を除外 → テキストリスト生成
```

## 4. WordReader の処理

### 4.1 機能

- Word ファイル（.docx）を読み込む  
- 各段落を取得  
- 空段落を除外

### 4.2 処理フロー

```text
Word ファイル → python-docx で読み込み → 段落をループ → 空段落を除外 → テキストリスト生成
```