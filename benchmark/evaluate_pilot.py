from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "benchmark/outputs"
RESULT = ROOT / "benchmark/results.csv"
CONDITIONS = ["A", "B", "C", "D"]

FORBIDDEN = [
    "guaranteed roi",
    "guaranteed return",
    "future-proof",
    "future proof",
    "unmatched speed",
    "revolutionary digital transformation partner",
]

AUDIENCE_TERMS = [
    "audit", "authorization", "identity", "integration", "production",
    "reliability", "runtime", "permission", "operating model",
]

SUPPORTED_CONCEPTS = [
    "context", "tool", "permission", "deterministic", "semantic", "evaluation", "governance",
]


def count_any(text, terms):
    t = text.lower()
    return sum(1 for term in terms if term in t)


def word_count(text):
    return len(re.findall(r"\b\w+\b", text, flags=re.UNICODE))


def main():
    missing = [c for c in CONDITIONS if not (OUTDIR / f"{c}.md").exists()]
    if missing:
        print("Pilot outputs missing:", ", ".join(missing))
        print("Run the same model/settings on benchmark/generated/A..D and save outputs in benchmark/outputs/.")
        return 2

    rows = []
    for c in CONDITIONS:
        text = (OUTDIR / f"{c}.md").read_text(encoding="utf-8")
        wc = word_count(text)
        rows.append({
            "condition": c,
            "word_count": wc,
            "length_in_range": int(500 <= wc <= 700),
            "forbidden_claim_hits": count_any(text, FORBIDDEN),
            "audience_signal_terms": count_any(text, AUDIENCE_TERMS),
            "supported_concept_terms": count_any(text, SUPPORTED_CONCEPTS),
            "human_positioning_fit_0_2": "",
            "human_audience_relevance_0_2": "",
            "human_evidence_discipline_0_2": "",
            "human_specificity_0_2": "",
            "human_decision_usefulness_0_2": "",
            "notes": "",
        })

    with RESULT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {RESULT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
