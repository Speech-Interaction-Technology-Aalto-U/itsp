"""Draw the figure of evaluation over the product life-cycle.

Writes attachments/evaluation_lifecycle.svg next to this script.
Only needs matplotlib.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

# Stages in order. Gates are drawn as narrow vertical bars.
stages = [
    ("Algorithm\ndevelopment", False),
    ("Gate:\nalgorithm\nmilestone", True),
    ("Product\ndevelopment", False),
    ("Gate:\nproduct\nmilestone", True),
    ("Monitoring after\ndeployment", False),
]

# Per stage: (relative scale of the test, label), or None if not used.
# Scale is drawn as the marker area.
subjective = [
    (1, "Informal listening\n1 expert"),
    (4, "Small expert test\n~6–10 colleagues"),
    None,
    (12, "Large naïve test\n(lab or crowd)"),
    (3, "Periodic tests,\nuser feedback"),
]
objective = [
    (3, "Development set"),
    (5, "Held-out test set"),
    (6, "Nightly\nregression tests"),
    (12, "Large-scale\nmetrics"),
    (4, "Continuous,\nno reference"),
]
feedback = ["minutes–hours", "days", "overnight", "weeks", "continuous"]

x = [0, 1.6, 3.2, 4.8, 6.4]
y_sub, y_obj = 2.0, 0.8
gate_colour = "#46A5FF"
sub_colour = "#FD6360"
obj_colour = "#555555"

fig, ax = plt.subplots(figsize=(11, 4.8))

for (name, is_gate), xi in zip(stages, x):
    if is_gate:
        ax.add_patch(Rectangle((xi - 0.12, -0.3), 0.24, 2.85,
                               color=gate_colour, alpha=0.35, lw=0))
    ax.text(xi, 2.65, name, ha="center", va="bottom", fontsize=10,
            fontweight="bold" if is_gate else "normal")

for lane, y, colour in [(subjective, y_sub, sub_colour),
                        (objective, y_obj, obj_colour)]:
    for item, xi in zip(lane, x):
        if item is None:
            ax.text(xi, y, "rarely", ha="center", va="center",
                    fontsize=9, color="#888888", style="italic")
            continue
        scale, label = item
        ax.scatter([xi], [y], s=90 * scale, color=colour, alpha=0.85,
                   edgecolors="none", zorder=3)
        ax.text(xi, y - 0.42, label, ha="center", va="top", fontsize=8.5)

ax.text(-0.95, y_sub, "Subjective", ha="right", va="center",
        fontsize=11, color=sub_colour, fontweight="bold")
ax.text(-0.95, y_obj, "Objective", ha="right", va="center",
        fontsize=11, color=obj_colour, fontweight="bold")

for xi, t in zip(x, feedback):
    ax.text(xi, -0.55, t, ha="center", va="center", fontsize=8.5,
            color="#333333")
ax.text(-0.95, -0.55, "Feedback time", ha="right", va="center",
        fontsize=9, color="#333333")

# Trend from fast and biased to slow and representative.
ax.add_patch(FancyArrowPatch((0, 3.55), (4.8, 3.55), arrowstyle="-|>",
                             mutation_scale=14, color="#333333", lw=1))
ax.text(0, 3.65, "fast, cheap, biased", ha="left", va="bottom", fontsize=9)
ax.text(4.8, 3.65, "slow, costly, close to real users", ha="right",
        va="bottom", fontsize=9)

ax.set_xlim(-2.4, 7.3)
ax.set_ylim(-0.85, 4.0)
ax.axis("off")
fig.tight_layout()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "attachments", "evaluation_lifecycle.svg")
fig.savefig(out, bbox_inches="tight")
print("Wrote", out)
