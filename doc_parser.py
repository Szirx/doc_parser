import re
from typing import Tuple
from docx import Document
from io import StringIO


def split_by_regex(
        text: str,
        pattern: str
) -> Tuple[str, str]:
    matching = re.match(pattern, text)
    matched_part = matching.group(0)
    remaining_part = text[matching.end():].strip()
    return matched_part, remaining_part


def parse_docx_to_txt(
        docx_file: str
) -> StringIO:
    doc = Document(docx_file)
    output = StringIO()

    pattern = re.compile(r'^[А-Яа-яA-Za-z]+\s\d+\. *')

    for para in doc.paragraphs:
        text = para.text.strip()

        if pattern.match(text):
            matched_part, remaining_part = split_by_regex(text, pattern)
            output.write(f'Q:\n{matched_part}\nA:\n{remaining_part}\n\n')
        else:
            if text:
                output.write(f'{text}\n')

    return output.getvalue()
