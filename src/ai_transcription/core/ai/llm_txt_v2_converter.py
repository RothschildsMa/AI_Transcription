# ============================================================
# ファイル名: llm_txt_v2_converter.py
#
# 機能説明:
#   TXT v1.5（SectionMarker 済み）を入力として受け取り、
#   LLM（Ollama + llama3）を使用して TXT v2.x 形式へ変換する。
#
#   ・Prompt は固定仕様
#   ・JSON / Markdown は使用しない
#   ・TXT v2.x のみを出力する
#
# 作成者: RothschildsMa
# 作成日: 2025-12-26
# ============================================================

from typing import Optional
import requests


class LlmTxtV2Converter:
    """
    TXT v1.5 → TXT v2.x 変換クラス（LLM 使用）
    """

    def __init__(
        self,
        model: str = "llama3",
        ollama_url: str = "http://localhost:11434/api/generate",
        timeout: int = 120,
    ):
        """
        :param model: 使用する Ollama モデル名
        :param ollama_url: Ollama API エンドポイント
        :param timeout: 通信タイムアウト（秒）
        """
        self.model = model
        self.ollama_url = ollama_url
        self.timeout = timeout

    def convert(self, txt_v1_5: str) -> str:
        """
        TXT v1.5 テキストを TXT v2.x に変換する。

        :param txt_v1_5: TXT v1.5 文字列
        :return: TXT v2.x 文字列
        """

        if not txt_v1_5 or not txt_v1_5.strip():
            raise ValueError("TXT v1.5 の入力が空です")

        prompt = self._build_prompt(txt_v1_5)

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        try:
            response = requests.post(
                self.ollama_url,
                json=payload,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama API への接続に失敗しました: {e}")

        if response.status_code != 200:
            raise RuntimeError(
                f"Ollama API エラー: status={response.status_code}, body={response.text}"
            )

        data = response.json()

        result = data.get("response")
        if not result:
            raise RuntimeError("LLM からの応答が空です")

        return result.strip()

    def _build_prompt(self, txt_v1_5: str) -> str:
        """
        工業級 TXT v1.5 → v2.x 用 Prompt を構築する。
        """

        return f"""
あなたは「業務経歴書変換専用・原子抽取エンジン」である。
これは自然言語生成タスクではない。
説明・要約・補完・推測・再構成は禁止されている。

━━━━━━━━━━━━━━━━━━━━
【唯一の出力仕様（これ以外出力禁止）】

以下に示すフォーマットが
「出力可能フィールドの完全な定義」であり、
同時に「出力フォーマットの唯一の正」である。

このブロック以外の文字を1文字でも出力してはならない。

━━━━━━━━━━━━━━━━━━━━
【出力フォーマット（完全固定・変更不可）】

[WORK_HISTORY_ITEM]
index =
period_start =
period_end =
project_name =
work_location =
role =
technical_area =
summary =
responsibilities[] =
environment_os[] =
environment_languages[] =
environment_framework[] =
environment_db[] =
environment_tools[] =
process_requirements =
process_basic_design =
process_detail_design =
process_implementation =
process_unit_test =
process_integration_test =
process_system_test =
process_operation =

※ このフォーマット以外の行を1行でも出力してはならない
※ 見出し説明・前置き・後書きは禁止

━━━━━━━━━━━━━━━━━━━━
【絶対禁止事項】

・上記に存在しない行の出力
・行順の変更
・フィールド名の変更
・JSON / Markdown / 説明文の出力
・推測・補完・要約・再構成
・原文に存在しない情報の生成

━━━━━━━━━━━━━━━━━━━━
【抽出ルール（厳守）】

■ period_start / period_end
・原文に存在する年月のみ
・形式は YYYY-MM
・「現在」「現行」等はそのまま「現在」と出力
・推測禁止

■ responsibilities[]
・原文に明示的に列挙されている作業内容のみ
・要約・統合・書き換え禁止
・1作業 = 1行

■ environment_xxx[]
・原文に明示的に記載された名称のみ
・用途推測による分類は禁止
・不明な場合は出力しない

■ process_xxx
・チェックマーク（●）が明示されている場合のみ true
・存在しない工程は false
・推測・補完は禁止

■ summary / technical_area
・原文に該当文言が存在する場合のみ転写
・存在しない場合は空欄

────────────────────
【変換対象 TXT v1.5】

{txt_v1_5}

====================
【出力開始】
""".strip()