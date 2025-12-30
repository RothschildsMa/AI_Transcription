# 業務経歴書 フィールド契約
（TXTv1.5 → TXTv2.x 用・最終出力テンプレート準拠）

---

## 0. 基本方針

- 本契約は最終出力 Excel テンプレートを唯一の正とする
- 出力不能な項目は空欄（null / 空文字）とする
- 推測・補完・要約は禁止
- 評価記号・レベルは原文準拠
- 構造が存在しない場合はセクション自体を出力しない

---

## 1. HEADER（ヘッダ情報）

| フィールド名 | 型 | 説明 |
|---|---|---|
| document_type | string | 固定値「業務経歴書」 |
| created_year | int | 作成年 |
| created_month | int | 作成月（1–12） |

---

## 2. 基本情報（PROFILE）

| フィールド名 | 型 | 説明 |
|---|---|---|
| furigana | string | フリガナ |
| name | string | 氏名 |
| gender | string | 性別 |
| nationality | string | 国籍 |
| marital_status | string | 既婚 / 未婚 |
| birth_year | int | 生年 |
| birth_month | int | 生月 |
| japan_arrival_year | int | 来日年 |
| japan_arrival_month | int | 来日月 |
| stay_years | int | 滞日年数 |
| work_experience_years | int | 実務年数 |
| nearest_station_line | string | 最寄駅 路線名 |
| nearest_station_name | string | 最寄駅 駅名 |
| address | string | 現住所 |

---

## 3. 学歴（EDUCATION）

| フィールド名 | 型 | 説明 |
|---|---|---|
| final_education | string | 最終学歴 |
| graduation_year | int | 卒業年 |
| graduation_month | int | 卒業月 |
| school_name | string | 学校名 |
| major | string | 専攻 |

---

## 4. 保有資格（CERTIFICATIONS）

複数の資格を保持できるセクション。

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| certifications | list | 保有資格の配列 |

---

### certifications 要素構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| name | string | 資格名 |
| acquired_year | int | 取得年 |
| acquired_month | int | 取得月 |

---

### 出力ルール

- 資格が存在しない場合は `certifications` 自体を出力しない
- 年月が不明な場合は該当フィールドを空欄とする
- 推測・補完は禁止

---

## 5. 語学能力（LANGUAGE）

複数言語に対する能力評価を表すセクション。

---

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| languages | list | 語学能力の配列 |

---

### languages 要素構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| language | string | 言語名 |
| overall_level | string | 総合レベル |
| spec_writing | string | 仕様書作成 |
| reading | string | 読み |
| technical_conversation | string | 専門会話 |
| daily_conversation | string | 日常会話 |

---

### 語学レベル定義（固定）

| 記号 | 意味 |
|---|---|
| A | ネイティブ同等 |
| B | 上級 |
| C | 実務レベル |
| D | 初級 |

---

### 出力ルール

- 原文に存在する評価のみを出力する
- 評価記号の変換・補完は禁止
- 不明な項目は空欄とする

---

## 6. 技術スキル（SKILLS）

技術スキルはカテゴリ別に分けて出力する。

---

### 技術レベル定義（共通・固定）

| 記号 | 定義 |
|---|---|
| A | スペシャリスト |
| B | 指導経験あり |
| C | 実務経験あり |
| D | 知識あり |

---

## 6.1 OS スキル

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| skills_os | list | OS スキル一覧 |

---

### skills_os 要素構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| name | string | OS 名 |
| level | string | 技術レベル（A/B/C/D） |

---

### 出力ルール

- レベルが明示されていない OS は出力しない
- 「未経験」「記号なし」は対象外とする

---

## 6.2 Database スキル

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| skills_database | list | DB スキル一覧 |

---

### skills_database 要素構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| name | string | DB 名 |
| level | string | 技術レベル（A/B/C/D） |

## 6.3 開発言語スキル（PROGRAMMING LANGUAGES）

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| skills_programming | list | 開発言語スキル一覧 |

---

### skills_programming 要素構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| name | string | 言語名 |
| level | string | 技術レベル（A/B/C/D） |

---

### 出力ルール

- 評価記号が明示されている言語のみ出力
- 記号が存在しない場合は出力しない
- レベル変換・推測は禁止

---

## 6.4 その他スキル（OTHER SKILLS）

サーバ構築、クラウド、フレームワーク、ツール等を含む。

---

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| skills_other | list | その他スキル一覧 |

---

### skills_other 要素構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| category | string | 分類（例：Server構築、Framework、Tool 等） |
| name | string | スキル名 |
| level | string | 技術レベル（A/B/C/D） |

---

### 出力ルール

- カテゴリは原文の表現を尊重する
- レベル不明な場合は出力しない
- 推測禁止

---

## 7. 業務知識（BUSINESS KNOWLEDGE）

---

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| business_knowledge | list | 業務知識一覧 |

---

### business_knowledge 要素構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| domain | string | 業務分野名 |
| level | string | 技術レベル（A/B/C/D） |

---

### 出力ルール

- 評価が存在する分野のみ出力
- 分野名は原文表記を保持する

---

## 8. 管理経験（MANAGEMENT EXPERIENCE）

---

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| management_experience | object | 管理経験情報 |

---

### management_experience 構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| member_count | string | メンバー人数 |
| total_management_months | int | 累計管理月数 |
| pm_roles | list | 担当 PM/PL 等の役割 |

---

### 出力ルール

- 数値が不明な場合は空欄
- 推測・計算は禁止

---

## 9. 業務経歴（WORK HISTORY）

業務経歴は **配列として順序を保持** する。

---

### フィールド定義

| フィールド名 | 型 | 説明 |
|---|---|---|
| work_history | list | 業務経歴一覧 |

---

### work_history 要素構造

| フィールド名 | 型 | 説明 |
|---|---|---|
| index | int | 項番 |
| period_start | string | 開始年月（YYYY-MM） |
| period_end | string | 終了年月（YYYY-MM または 現在） |
| project_name | string | プロジェクト概要 |
| work_location | string | 作業場所 |
| role | string | 役割（SE / PG / PM 等） |
| technical_area | string | 技術エリア |
| summary | string | プロジェクト概要 |
| responsibilities | list | 担当作業一覧 |
| environment_os | list | 使用 OS |
| environment_languages | list | 使用言語 |
| environment_framework | list | フレームワーク |
| environment_db | list | DB |
| environment_tools | list | ツール |
| process_requirements | boolean | 要件定義 |
| process_basic_design | boolean | 基本設計 |
| process_detail_design | boolean | 詳細設計 |
| process_implementation | boolean | 製造 |
| process_unit_test | boolean | 単体テスト |
| process_integration_test | boolean | 結合テスト |
| process_system_test | boolean | 総合テスト |
| process_operation | boolean | 運用保守 |

---

### 出力ルール（業務経歴）

- 各項目は **原文に存在する内容のみ出力**
- チェックマーク（●）がある工程のみ `true`
- 存在しない工程は `false`
- 項番順を必ず保持する
- 要約・省略・統合は禁止

---

## 10. 共通厳守ルール（GLOBAL CONSTRAINTS）

- 推測・補完・一般化は禁止
- 原文に存在しない情報は出力しない
- フォーマットは本契約に完全準拠すること
- 出力テンプレート以外のフィールドは禁止
