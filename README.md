# AI_Transcription

## プロジェクト構築説明

このプロジェクトでは、以下の観点で開発環境とチーム開発基盤を整備しています。

### 1. IDE
- 推奨 IDE: VS Code  
- 保存時の自動整形や import 整理など、チームで統一した設定を適用

### 2. プロジェクト構造
- コード、テスト、データ、UI モジュールなどを整理したディレクトリ構造  
- 各ディレクトリは Python パッケージとして管理

### 3. 依存管理
- 仮想環境を利用して Python 依存パッケージを隔離  
- `pyproject.toml` などで依存関係を明示

### 4. コードスタイルと品質
- Black, isort による自動整形  
- flake8 による静的解析でコード品質チェック  
- チーム全員で統一したスタイルを維持

### 5. CI/CD
- GitHub Actions で PR / Push ごとに自動で lint、テスト、カバレッジ確認  
- チーム開発時の品質保証と自動化フローを構築

### 6. ドキュメント
- 開発手順、モジュール構造、使用方法などを Markdown 形式で管理  
- `docs/` 配下にチーム開発手順や API 仕様をまとめる
---

## プロジェクト全体フロー（総覧）

```mermaid
flowchart LR
    A["GitHub リポジトリクローン"]
    B["仮想環境作成・依存インストール"]
    C["VS Code でコード作業"]
    D["Black / isort 整形"]
    E["flake8 チェック"]
    F["Git commit & push"]
    G["GitHub Actions CI/CD"]
    H["Lint / Test / Coverage"]
    I["PR レビュー & main ブランチにマージ"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I