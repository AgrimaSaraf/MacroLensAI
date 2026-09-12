"""
Scenario-analysis template for MacroLensAI.

Purpose:
Convert a strategic question into explicit assumptions and compare
base, upside, and downside outcomes.

This is intentionally simple and explainable.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Scenario:
    name: str
    assumptions: Dict[str, float]
    implications: List[str]


def compare_scenarios(scenarios: List[Scenario]) -> None:
    for scenario in scenarios:
        print(f"\n=== {scenario.name.upper()} ===")
        print("Assumptions:")
        for key, value in scenario.assumptions.items():
            print(f"- {key}: {value}")

        print("Implications:")
        for item in scenario.implications:
            print(f"- {item}")


if __name__ == "__main__":
    scenarios = [
        Scenario(
            name="Base",
            assumptions={
                "oil_price_change_pct": 15,
                "demand_change_pct": 0,
                "fx_change_pct": 0,
            },
            implications=[
                "Moderate cost pressure",
                "Selective pricing actions",
                "Limited route changes",
            ],
        ),
        Scenario(
            name="Downside",
            assumptions={
                "oil_price_change_pct": 30,
                "demand_change_pct": -8,
                "fx_change_pct": -5,
            },
            implications=[
                "Severe margin pressure",
                "Capacity rationalization",
                "Greater need for hedging and cost action",
            ],
        ),
        Scenario(
            name="Upside",
            assumptions={
                "oil_price_change_pct": 10,
                "demand_change_pct": 6,
                "fx_change_pct": 1,
            },
            implications=[
                "Healthy demand offsets fuel pressure",
                "Pricing power improves",
                "Capacity can be preserved",
            ],
        ),
    ]

    compare_scenarios(scenarios)
