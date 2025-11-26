import os

def load_report_text(file_path: str = "data/분기보고서.txt") -> str:
    """
    분기보고서 txt 파일 내용을 전부 읽어서 하나의 문자열로 반환
    """
    if not os.path.exists(file_path):
        return "분기보고서 파일을 찾을 수 없습니다."

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return text
