"""
src/priority_engine/rules.py
──────────────────────────────
Deterministic threshold rules.
Returns a list of PriorityItem-shaped dicts for modules that breach thresholds.
The LLM engine uses these as hard constraints.
"""

SLEEP_WARN_HOURS = 6.0
FITNESS_NO_WORKOUT_DAYS = 4
FINANCIAL_SAVINGS_GAP_PCT = 12


def apply_rules(summaries: list[dict]) -> list[dict]:
    """
    summaries: list of ModuleSummary dicts from the backend.
    Returns: list of high-urgency PriorityItem dicts.
    """
    flags = []

    for s in summaries:
        module = s.get("module", "")
        data = s.get("summary_data", {})

        if module == "sleep":
            avg_hours = data.get("avg_hours_last_3_days")
            if avg_hours is not None and avg_hours < SLEEP_WARN_HOURS:
                flags.append({
                    "module": "sleep",
                    "title": "Sleep Deficit Alert",
                    "description": f"Average sleep is {avg_hours:.1f}h over the last 3 days (threshold: {SLEEP_WARN_HOURS}h)",
                    "urgency": "high",
                    "impact": "high",
                    "score": 90,
                })

        if module == "financial":
            savings_gap = data.get("savings_gap_percent")
            if savings_gap is not None and savings_gap > FINANCIAL_SAVINGS_GAP_PCT:
                flags.append({
                    "module": "financial",
                    "title": "Savings Gap",
                    "description": f"Savings are {savings_gap:.0f}% below target",
                    "urgency": "high",
                    "impact": "high",
                    "score": 85,
                })

        if module == "fitness":
            days_no_workout = data.get("days_since_last_workout")
            if days_no_workout is not None and days_no_workout >= FITNESS_NO_WORKOUT_DAYS:
                flags.append({
                    "module": "fitness",
                    "title": "No Recent Workout",
                    "description": f"{days_no_workout} days since last workout",
                    "urgency": "medium",
                    "impact": "medium",
                    "score": 60,
                })

    return flags
