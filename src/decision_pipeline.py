"""
MacroLensAI decision pipeline.

The system is intentionally organized around decision quality rather than
around a specific AI technique.

Pipeline:
1. Frame the strategic question
2. Define hypotheses
3. Gather evidence
4. Map causal mechanisms
5. Quantify sensitivities
6. Build scenarios
7. Recommend an action
"""


def frame_question(question: str) -> dict:
    return {
        "question": question,
        "decision_owner": "Executive team",
        "time_horizon": "12-24 months",
        "decision_type": "Strategic",
    }


def build_hypotheses(question: str) -> list[str]:
    return [
        f"The external change materially affects economics related to: {question}",
        "The impact differs by segment, geography, or customer group",
        "A combined response is likely stronger than a single operational lever",
    ]


def structure_recommendation(options: list[str], key_risks: list[str]) -> dict:
    return {
        "recommended_actions": options,
        "key_risks": key_risks,
        "monitoring": [
            "Leading macro indicators",
            "Competitor actions",
            "Unit economics",
            "Demand response",
        ],
    }


if __name__ == "__main__":
    q = "What should an airline do if oil prices rise 30%?"
    print(frame_question(q))
    print(build_hypotheses(q))
