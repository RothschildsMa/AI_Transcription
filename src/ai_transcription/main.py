# ============================================================
# ファイル名: main.py
#
# 機能説明:
#   Excel 履歴書を読み込み、
#   TXT v1.x → TXT v1.5 までの前処理パイプラインを実行する。
#
# 作成者:RothschildsMa
#
# 作成日:2025-12-24 
# ============================================================

from pathlib import Path

from ai_transcription.core.pipeline.section_marker import SectionMarker
from ai_transcription.core.pipeline.row_normalizer import RowNormalizer
from ai_transcription.core.readers.excel_reader import ExcelReader
from ai_transcription.core.writer.debug_txt_writer import DebugTxtWriter
from ai_transcription.core.ai.llm_txt_v2_converter import LlmTxtV2Converter


def main() -> None:
    # ==========================================
    # 入出力パス設定
    # ==========================================
    input_excel_path = "data/input/sample3.xlsx"
    output_debug_txtv15_path = "data/output/output_v1_5_debug.txt"
    output_debug_txtv2_path = "data/output/output_v2_debug.txt"

    # ==========================================
    # 1. Excel 読み込み
    # ==========================================
    excel_reader = ExcelReader()
    table = excel_reader.read(input_excel_path)

    # ==========================================
    # 2. Row 正規化（TXT v1.x）
    # ==========================================
    normalizer = RowNormalizer()
    normalized_lines = normalizer.normalize_rows(table)

    # ==========================================
    # 3. SectionMarker v1.5
    # ==========================================
    marker = SectionMarker()
    marked_lines = marker.mark(normalized_lines)

    # ==========================================
    # 4. デバッグ用 TXT 出力
    # ==========================================
    writer = DebugTxtWriter()
    writer.write(marked_lines, output_debug_txtv15_path)

    print("✔ TXT v1.5 デバッグ出力が完了しました")
    print(f"   出力先: {Path(output_debug_txtv15_path).resolve()}")

    with open(output_debug_txtv15_path,"r",encoding="utf-8") as f:
        txt_v1_5 = f.read()

    converter = LlmTxtV2Converter(model="llama3.1:8b")
    txt_v2 = converter.convert(txt_v1_5)

    with open(output_debug_txtv2_path, "w", encoding="utf-8") as f:
        f.write(txt_v2)

if __name__ == "__main__":
    main()
