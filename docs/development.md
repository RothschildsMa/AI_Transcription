# AI_Transcription チーム開発手順

このドキュメントは、AI_Transcription プロジェクトにおけるチーム開発用の開発環境、使用技術、ディレクトリ構成、環境構築手順、開発フローをまとめたものです。

---

## 1. 説明

### 1.1 使用技術
- **Python 3.10 以上**  
- **依存管理**: 仮想環境（venv）、pip、pyproject.toml  
- **UI**: Python GUI モジュール (将来拡張)  
- **データ処理**: pandas, openpyxl, python-docx など  
- **AI 情報抽出**: OpenAI API / 他 AI モジュール（拡張可能）  
- **コード品質**: Black, isort, flake8  
- **テスト**: pytest + coverage  
- **CI/CD**: GitHub Actions  

### 1.2 ディレクトリ構成
AI_Transcription/
├─.vscode/ # VS Code 設定
├─src/
│ └─ai_transcription/
│ ├─core/ # コア処理モジュール
│ ├─ui/ # GUI モジュール
│ └─data/ # データ格納用
├─tests/ # 単体テスト
├─docs/ # 開発手順・仕様書
├─.flake8 # flake8 設定
├─pyproject.toml # 依存関係定義
├─README.md # プロジェクト概要・環境構築概要
├─LICENSE
└─main.py # プロジェクト起動用メインスクリプト

## 2. 環境構築手順

### 2.1 リポジトリクローン

```bash
# GitHub リポジトリをクローン
git clone https://github.com/RothschildsMa/AI_Transcription.git

# クローンしたディレクトリへ移動
cd AI_Transcription
```

### 2.2 仮想環境作成

```bash
#仮想環境構築
python -m venv .venv

#仮想環境起動
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 2.3 依存パッケージのインストール

```bash
# pip を最新バージョンにアップグレード
python -m pip install --upgrade pip

# 現在のプロジェクトを editable モードでインストール
# 開発中にソースを変更しても再インストール不要
pip install -e .

# コード整形、静的解析、テスト、カバレッジ測定用パッケージをインストール
pip install black isort flake8 pytest coverage
```

## 3. Git操作手順

### 3.1 ブランチ管理

```bash
# main ブランチを最新に更新
git checkout main
git pull origin main

# 新しい作業ブランチを作成
git checkout -b feature/機能ID
```

### 3.2 コード変更・コミット

```bash
# 変更をステージング
git add .

# コミットメッセージを付けて保存
git commit -m "作業内容の説明"
```

### 3.3 コード変更・コミット

```bash
# リモートリポジトリにプッシュ
git push origin feature/機能ID

# GitHub で Pull Request を作成
```
### 3.4 マージ
テスト及び内部レビュー実施した上で、責任者よりPull Requestのマージを行う。