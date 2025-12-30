import requests
import json

class AIClient:
    """
    無料 LLM API クライアント
    API 障害時はローカルフォールバックを使用
    """

    API_URL = "https://apifreellm.com/api/chat"

    def ask(self, prompt: str) -> str:
        try:
            response = requests.post(
                self.API_URL,
                json={"message": prompt},
                timeout=20
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
        except Exception as e:
            print("LLM API に接続できません。フォールバックを使用します。")
            print(f"理由: {e}")
            return self._fallback_response(prompt)

    def _fallback_response(self, prompt: str) -> str:
        """
        開発用フォールバック（AI が解析した想定結果）
        """
        return json.dumps(
            {
                "resumes": [
                    {
                        "name": "山田太郎",
                        "age": 30,
                        "address": "東京",
                        "email": None,
                        "phone": None
                    },
                    {
                        "name": "佐藤花子",
                        "age": 25,
                        "address": "大阪",
                        "email": None,
                        "phone": None
                    }
                ]
            },
            ensure_ascii=False
        )