"""
Simple strategic-option scorecard.

Scores options across:
- impact
- feasibility
- speed
- resilience
- downside risk

Scale: 1 to 5
"""

OPTIONS = {
    "Selective fare increases": {
        "impact": 4,
        "feasibility": 5,
        "speed": 5,
        "resilience": 3,
        "downside_risk": 3,
    },
    "Increase fuel hedging": {
        "impact": 4,
        "feasibility": 4,
        "speed": 3,
        "resilience": 5,
        "downside_risk": 3,
    },
    "Reduce weak-route capacity": {
        "impact": 4,
        "feasibility": 4,
        "speed": 3,
        "resilience": 4,
        "downside_risk": 3,
    },
    "Expand ancillary revenue": {
        "impact": 3,
        "feasibility": 4,
        "speed": 3,
        "resilience": 4,
        "downside_risk": 5,
    },
}


def weighted_score(scores):
    weights = {
        "impact": 0.30,
        "feasibility": 0.20,
        "speed": 0.15,
        "resilience": 0.25,
        "downside_risk": 0.10,
    }
    return sum(scores[k] * weights[k] for k in weights)


if __name__ == "__main__":
    ranked = sorted(
        ((name, weighted_score(scores)) for name, scores in OPTIONS.items()),
        key=lambda x: x[1],
        reverse=True,
    )

    for name, score in ranked:
        print(f"{name}: {score:.2f}")
