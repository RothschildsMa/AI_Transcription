# ============================================================
# 機能説明:
#   正規化済み TXT 行に対して、セクション候補マーカーを付与する。
#   本クラスは「候補判定」のみを行い、意味解析や構造確定は行わない。
#
# マーカー例:
#   [PROFILE_CANDIDATE]
#   [WORK_ITEM_CANDIDATE]
#   [EDUCATION_CANDIDATE]
#
# 作成者:RothschildsMa
#
# 作成日:2025-12-24 
# ============================================================

from typing import List


class SectionMarker:
    """
    TXT v1.5 用 セクション候補マーカー付与クラス
    """

    PROFILE_KEYWORDS = [
        "氏名", "氏 名", "生年月", "年齢", "歳", "性別", "住所", "国籍", "フリガナ"
    ]

    EDUCATION_KEYWORDS = [
        "学歴", "卒業", "学校", "大学", "専攻"
    ]

    WORK_KEYWORDS = [
        "№", "No", "期間", "～", "プロジェクト", "作業"
    ]

    SKILL_KEYWORDS = [
        "OS", "言語", "DB", "技術", "ツール", "環境"
    ]

    NOTE_KEYWORDS = [
        "備考", "自己PR", "資格", "トレーニング"
    ]

    def mark(self, lines: List[str]) -> List[str]:
        """
        各行に対してセクション候補マーカーを付与する。

        :param lines: RowNormalizer 出力の文字列行リスト
        :return: マーカー付き行リスト
        """

        if lines is None:
            raise ValueError("入力 lines が None です")

        marked_lines: List[str] = []

        for line in lines:
            markers = self._detect_markers(line)

            if markers:
                marker_prefix = "[" + ", ".join(markers) + "]"
                marked_lines.append(f"{marker_prefix}\n{line}")
            else:
                marked_lines.append(line)

        return marked_lines

    def _detect_markers(self, line: str) -> List[str]:
        """
        1行に含まれるキーワードからマーカー候補を判定する。
        """

        markers: List[str] = []

        if self._contains_any(line, self.PROFILE_KEYWORDS):
            markers.append("PROFILE_CANDIDATE")

        if self._contains_any(line, self.EDUCATION_KEYWORDS):
            markers.append("EDUCATION_CANDIDATE")

        if self._contains_any(line, self.WORK_KEYWORDS):
            markers.append("WORK_ITEM_CANDIDATE")

        if self._contains_any(line, self.SKILL_KEYWORDS):
            markers.append("SKILL_CANDIDATE")

        if self._contains_any(line, self.NOTE_KEYWORDS):
            markers.append("NOTE_CANDIDATE")

        return markers

    @staticmethod
    def _contains_any(text: str, keywords: List[str]) -> bool:
        """
        テキストにキーワードのいずれかが含まれているか判定する。
        """

        for keyword in keywords:
            if keyword in text:
                return True
        return False
