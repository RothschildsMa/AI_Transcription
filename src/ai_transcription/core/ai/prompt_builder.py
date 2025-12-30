from typing import List

class PromptBuilder:
    @staticmethod
    def build(lines: List[str]) -> str:
        text = "\n".join(lines)

        return f"""
あなたは履歴書情報を構造化するアシスタントです。

以下は Excel から抽出された履歴書のテキストです。
内容は以下を含む可能性があります：
- 横向きの表
- 縦向きの表
- 混在したレイアウト

【履歴書テキスト開始】
{text}
【履歴書テキスト終了】

指示：
1. 履歴書情報を識別してください
2. 存在しない情報は推測しないでください
3. 不明な項目は null を設定してください
4. 期間は可能な限り「YYYY/MM - YYYY/MM」で統一
5. 表現は簡潔なビジネス日本語
6. 出力は JSON のみとしてください（説明文は禁止）

JSON 形式（厳守）：

{
  "basic_info": {
    "name": "",
    "experience_years": "",
    "nationality": "",
    "remarks": ""
  },
  "skills": {
    "languages": [],
    "os": [],
    "db": [],
    "frameworks": [],
    "tools": []
  },
  "career": [
    {
      "period": "",
      "project_overview": "",
      "role": "",
      "process": "",
      "environment": ""
    }
  ]
}

""".strip()