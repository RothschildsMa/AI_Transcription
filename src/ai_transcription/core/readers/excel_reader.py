# ============================================
# 機能説明:
#   Excelファイル（.xlsx / .xls / .xlsm）を読み込み、
#   セル構造を保持した二次元配列（List[List[str]]）として返却する。
#
#   ・行・列の境界情報を保持することを最優先とする
#   ・空セルは空文字列 "" として扱う
#   ・このクラスでは正規化・意味解析は一切行わない
#
# 作成者:RothschildsMa
#
# 作成日:2025-12-24 
# ============================================================

from typing import List
from pathlib import Path

import openpyxl
import xlrd


class ExcelReader:
    """
    Excelを読み込み、セル構造を保持した二次元配列として返却する Reader クラス。
    """

    @staticmethod
    def read(file_path: str) -> List[List[str]]:
        """
        Excelファイルを読み込み、二次元配列として返却する。

        :param file_path: Excelファイルパス
        :return: List[List[str]]
        :raises ValueError: 未対応フォーマットの場合
        :raises FileNotFoundError: ファイルが存在しない場合
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"ファイルが存在しません: {file_path}")

        suffix = path.suffix.lower()

        if suffix in [".xlsx", ".xlsm"]:
            return ExcelReader._read_xlsx(file_path)
        elif suffix == ".xls":
            return ExcelReader._read_xls(file_path)
        else:
            raise ValueError(f"未対応のExcel形式です: {suffix}")

    # -----------------------------
    # private methods
    # -----------------------------

    @staticmethod
    def _read_xlsx(file_path: str) -> List[List[str]]:
        """
        .xlsx / .xlsm 用 Reader（openpyxl）
        """
        workbook = openpyxl.load_workbook(
            file_path,
            data_only=True
        )

        sheet = workbook.active
        if sheet is None:
            raise RuntimeError("有効なシートが見つかりません")

        rows: List[List[str]] = []

        for row in sheet.iter_rows():
            row_values: List[str] = []
            for cell in row:
                value = cell.value
                row_values.append("" if value is None else str(value).strip())
            rows.append(row_values)

        return rows

    @staticmethod
    def _read_xls(file_path: str) -> List[List[str]]:
        """
        .xls 用 Reader（xlrd）
        """
        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_index(0)

        rows: List[List[str]] = []

        for r in range(sheet.nrows):
            row_values: List[str] = []
            for c in range(sheet.ncols):
                value = sheet.cell_value(r, c)
                row_values.append("" if value in (None, "") else str(value).strip())
            rows.append(row_values)

        return rows
