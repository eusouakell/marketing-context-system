"""Offline fixture check; does not call or evaluate a model."""
import json
from pathlib import Path

REQUIRED = ("brand", "audience", "editorial-policy")


def prepare(corpus, brief, encode):
    items = corpus["items"]
    by_id = {item["id"]: item for item in items}
    if len(by_id) != len(items):
        raise ValueError("duplicate source IDs")
    selected = []
    for source_id in REQUIRED:
        item = by_id[source_id]
        if item["status"] != "current" or item["authority"] not in {"canonical", "approved"}:
            raise ValueError("required source unavailable")
        selected.append({"id": source_id, "reason": "required for the synthetic briefing", "source": item})
    excluded = [{"id": i["id"], "reason": "superseded" if i["status"] == "superseded" else "not required"}
                for i in items if i["id"] not in REQUIRED]
    if not brief["synthetic"] or not all(i["synthetic"] for i in items):
        raise ValueError("non-synthetic input")
    if brief["external_evidence"]:
        raise ValueError("fixture cannot supply external evidence")
    if brief["publication_status"] != "HOLD" or brief["human_approval"] is not None:
        raise ValueError("human gate must remain closed")
    if "Usar IA dobra o ROI" not in brief["unsupported_claims"]:
        raise ValueError("unsupported ROI claim missing")
    for section in brief["outline"]:
        if not section["source_ids"] or not set(section["source_ids"]).issubset(REQUIRED):
            raise ValueError("untraceable section")
    text = "\n\n".join(i["source"]["text"] for i in selected)
    tokens = len(encode(text))
    if tokens > 1500:
        raise ValueError("knowledge budget exceeded; no truncation")
    return {"selected": selected, "excluded": excluded, "publication_status": "HOLD",
            "token_report": {"encoding": "o200k_base", "selected_knowledge_tokens": tokens,
                             "budget_tokens": 1500, "within_budget": True,
                             "skill_instruction_tokens": 3783,
                             "session_total_tokens": None, "api_calls": 0}}


if __name__ == "__main__":
    import tiktoken
    import tiktoken.load
    # Cache is prepared separately. Never fetch a tokenizer table in this pilot.
    def deny_download(path):
        raise RuntimeError("tokenizer cache required; network disabled")
    tiktoken.load.read_file = deny_download
    root = Path(__file__).resolve().parent
    encoder = tiktoken.get_encoding("o200k_base")
    report = prepare(json.loads((root / "corpus.json").read_text(encoding="utf-8")),
                     json.loads((root / "brief.json").read_text(encoding="utf-8")), encoder.encode)
    (root / "manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["token_report"]))
