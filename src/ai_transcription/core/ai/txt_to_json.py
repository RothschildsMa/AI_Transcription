import json
from typing import List, Dict, Any
from ai_transcription.core.ai.prompt_builder import PromptBuilder
from ai_transcription.core.ai.ai_client import AIClient


class TxtToJsonParser:
    """
    履歴書テキストを AI で JSON 化する
    """

    def __init__(self):
        self.client = AIClient()

    def parse(self, lines: List[str]) -> Dict[str, Any]:
        prompt = PromptBuilder.build(lines)
        response_text = self.client.ask(prompt)

        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            raise ValueError("AIの返却結果が正しいJSONではありません")