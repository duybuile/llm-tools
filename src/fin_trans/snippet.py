from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, ValidationError


class CleanSnippet(BaseModel):
    sequence_id: int
    content: str = Field(..., min_length=10)
    processed_at: datetime = Field(default_factory=datetime.now)

def _clean_content(content: str) -> str:
    # Remove white space
    return content.strip()


def process_snippets(raw_list: List[str]) -> List[CleanSnippet]:
    clean_snippets = []
    seen_snippets = set()
    for i, raw_content in enumerate(raw_list):
        cleaned = _clean_content(raw_content)
        if cleaned in seen_snippets:
            continue
        try:
            snippet = CleanSnippet(
                sequence_id=i,
                content=cleaned,
            )
            clean_snippets.append(snippet)
            seen_snippets.add(cleaned)
        except ValidationError as e:
            print(f"Validation error: {e}")
            continue

    return clean_snippets

# Mock Input
test_data = ["  Talked about Pension  ", "", "Short", "Talked about Pension", "Invested £10k in ISA"]

print(process_snippets(test_data))