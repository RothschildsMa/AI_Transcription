# ============================================================
# 機能説明 : Excel から読み込んだ二次元配列を
#            正規化されたテキスト行（List[str]）へ変換する
#
# 作成者:RothschildsMa
#
# 作成日:2025-12-24 
# ============================================================


from typing import Any, List


class RowNormalizer:
    """
    Excel Reader が返却する二次元配列（行×列）を受け取り、
    各行を 1 行の文字列として正規化するクラス。
    """

    def normalize_rows(self, rows: List[List[Any]]) -> List[str]:
        """
        二次元配列を正規化されたテキスト行の配列へ変換する。

        :param rows: Excel Reader からの出力（List[List[Any]]）
        :return: 正規化された行リスト（List[str]）
        """
        normalized_lines: List[str] = []

        for row in rows:
            line = self._normalize_single_row(row)
            if line:
                normalized_lines.append(line)

        return normalized_lines

    # --------------------------------------------------------

    def _normalize_single_row(self, row: List[Any]) -> str:
        """
        1 行分のセル配列を文字列へ正規化する。

        正規化ルール：
        - None は無視
        - 前後空白を除去
        - セル同士は半角スペースで結合
        - 全体が空になる場合は空文字を返す
        """
        parts: List[str] = []

        for cell in row:
            if cell is None:
                continue

            text = str(cell).strip()
            if text:
                parts.append(text)

        return " ".join(parts)
