from __future__ import annotations

import re

WORD_RE = re.compile(r"[A-Za-zÀ-ÿ0-9_-]+")


def words(text: str) -> set[str]:
    return {w.lower() for w in WORD_RE.findall(text) if len(w) > 2}


def estimate_tokens(text: str) -> int:
    # Transparent provider-agnostic approximation for budgeting.
    # Replace with the target model tokenizer when exact accounting matters.
    return (len(text) + 3) // 4


def keyword_relevance(query: str, title: str, tags: tuple[str, ...], text: str) -> float:
    q = words(query)
    if not q:
        return 0.0
    hay = words(" ".join([title, " ".join(tags), text[:4000]]))
    return len(q & hay) / len(q)


def compress_extractively(text: str, token_limit: int) -> tuple[str, bool]:
    if estimate_tokens(text) <= token_limit:
        return text, False
    if token_limit < 0:
        raise ValueError("token limit must be non-negative")
    marker = "\n\n[TRUNCATED BY CONTEXT BUDGET]"
    char_limit = token_limit * 4
    if char_limit < len(marker):
        return text[:char_limit], True
    clipped = text[:char_limit - len(marker)].rstrip()
    return clipped + marker, True
