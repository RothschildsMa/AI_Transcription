 # AI_Transcription チーム開発手順

このドキュメントは、AI_Transcription プロジェクトにおけるチーム開発用の開発環境、使用技術、ディレクトリ構成、環境構築手順、開発フローをまとめたものです。

---

# 1. 説明

## 1.1. 使用技術
- **Python 3.10 以上**  
- **依存管理**: 仮想環境（venv）、pip、pyproject.toml  
- **UI**: Python GUI モジュール (将来拡張)  
- **データ処理**: pandas, openpyxl, python-docx など  
- **AI 情報抽出**: AI API
- **コード品質**: Black, isort, flake8  
- **テスト**: pytest + coverage  
- **CI/CD**: GitHub Actions  

## 1.2. ディレクトリ構成

```text
AI_Transcription/
├─.vscode/        # VS Code 設定
├─src/
│  └─ai_transcription/
│      ├─core/    # コア処理モジュール
│      ├─ui/      # GUI モジュール
│      └─data/    # データ格納用
├─tests/          # 単体テスト
├─docs/           # 開発手順・システム説明・機能単位説明
├─htmlcov/        # 単体テスト結果(カバレッジ)
├─.flake8         # flake8 設定
├─pyproject.toml  # 依存関係定義
├─README.md       # プロジェクト概要・環境構築概要
├─LICENSE         # ライセンス
└─main.py         # プロジェクト起動用メインスクリプト
```

# 2. 環境構築手順

## 2.1. リポジトリクローン

```bash
# GitHub リポジトリをクローン
git clone https://github.com/RothschildsMa/AI_Transcription.git

# クローンしたディレクトリへ移動
cd AI_Transcription
```
## 2.2. AI modelを準備する
### 2.2.1. OllamaをローカルにDownloadする
https://ollama.com

### 2.2.2. モデル準備及び動作確認
```bash
# モデルを用意する
ollama pull llama3.1:8b

# モデル一覧を取得、llama3が存在することを確認
ollama list

# ローカルAI APIのステータスを確認、StatusCodeが200であること
curl http://localhost:11434/api/tags
```

## 2.3. 仮想環境作成

```bash
#仮想環境構築
python -m venv .venv

#仮想環境起動
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

## 2.4. 依存パッケージのインストール

```bash
# pip を最新バージョンにアップグレード
python -m pip install --upgrade pip

# 現在のプロジェクトを editable モードでインストール
# 開発中にソースを変更しても再インストール不要
pip install -e .

# コード整形、静的解析、テスト、カバレッジ測定用パッケージをインストール
pip install black isort flake8 pytest coverage

# xls対応のため、xlrdをインストール
pip install xlrd requests

# インストール済みパッケージ一覧
pip list
```
# 3. コード整形・静的解析・テスト手順

## 3.1. Black（自動コード整形）

```bash
# プロジェクト全体の Python ファイルを整形
black src tests

# 整形結果を確認のみしたい場合（変更は加えない）
black --check src tests
```

## 3.2. flake8（静的解析）

```bash
# 静的解析でコード品質をチェック
flake8 src tests
```

## 3.3. isort（import 整理）

```bash
# import 文を自動で整理
isort src tests

# 整理結果の確認のみ
isort --check-only src tests
```

## 3.4. pytest（単体テスト）

```bash
# tests フォルダ配下のテストを実行
pytest tests

# 詳細なテスト結果を表示
pytest -v tests

# テスト実行とカバレッジ測定
coverage run -m pytest tests

# ターミナル上でカバレッジ結果を表示
coverage report -m

# HTML レポート生成
coverage html
```

# 4. Git操作手順

## 4.1. ブランチ管理

```bash
# main ブランチを最新に更新
git checkout main
git pull origin main

# 新しい作業ブランチを作成
git checkout -b feature/機能ID
```

## 4.2. コード変更・コミット

> [!IMPORTANT]
> ## ⚠ 注意事項↓↓↓
> - コミット前に、必ずblackとflake8のテストを実施する！！！
> - pytestを実施して、カバレッジが60%以上であること
> - 上記二つの条件を達成しない場合は、CIの動作により、ビルドエラーになります。

```bash
# 変更をステージング
git add .

# コミットメッセージを付けて保存
git commit -m "作業内容の説明"
```

## 4.3. コード変更・コミット

```bash
# リモートリポジトリにプッシュ
git push origin feature/機能ID
```
## 4.4. ci.yml動作確認
- GitHubのActionsでコード変更の自動検証結果を確認する
- buildが成功してから手順の4.5を実施する
- 失敗した場合はPull Requestの作成は禁止。エラーログを確認して、解消した場合は4.2から実施
![github action](images/gitaction.png)

## 4.5. Pull Request を作成

## 4.6. マージ
テスト及びPRレビュー実施した上で、責任者よりPull Requestのマージを行う。