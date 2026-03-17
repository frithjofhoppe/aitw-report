# quality_score.py

# Definition der Quality Attributes (Name: (weight, score))
# weight = w_quality(q)
# score  = s_quality(q)

quality_attributes = {
    "Performance": (0.3, 4),
    "Portability": (1, 1),
    "Auditability": (0.6, 2),
    "Automatability": (1, 4),
    "Maintainability": (0.8, 2),
    "Adaptability": (0.6, 1),
    "Complexity": (0.8, 4),
    "Traceability Strength": (1, 3),
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