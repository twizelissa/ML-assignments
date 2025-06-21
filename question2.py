# Prior
P_Disease = 0.001
P_NoDisease = 1 - P_Disease

# Likelihood
P_Pos_given_Disease = 0.99
P_Pos_given_NoDisease = 0.01

# Evidence
P_Pos = (P_Pos_given_Disease * P_Disease) + (P_Pos_given_NoDisease * P_NoDisease)

# Posterior
P_Disease_given_Pos = (P_Pos_given_Disease * P_Disease) / P_Pos

print(f"P(Disease | Positive Test) = {P_Disease_given_Pos:.4f}")