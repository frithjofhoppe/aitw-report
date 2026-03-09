# quality_score.py

# Definition der Quality Attributes (Name: (weight, score))
# weight = w_quality(q)
# score  = s_quality(q)

quality_attributes = {
    "Q1_performance": (1, 5),
    "Q2_cost_effectiveness": (1, 5),
    "Q3_security": (1, 5),
    "Q4_portability": (1, 5),
    "Q5_architectural_sustainability": (1, 5),
    "Q6_auditability": (1, 5),
    "Q7_automatibility": (1, 5),
    "Q8_maintainability": (1, 5),
}

weighted_sum = 0
weight_sum = 0

for q, (weight, score) in quality_attributes.items():
    weighted_sum += weight * score
    weight_sum += weight

score_quality = weighted_sum / weight_sum

print("Weighted sum:", weighted_sum)
print("Total weight:", weight_sum)
print("Score_quality:", round(score_quality, 3))