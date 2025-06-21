import matplotlib.pyplot as plt

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def binomial_pmf(n, p):
    return [nCr(n, k) * (p**k) * ((1 - p)**(n - k)) for k in range(n + 1)]

# Parameters
n = 5        # Number of matches
p = 0.7      # Probability of winning each match

# Compute binomial probabilities
pmf = binomial_pmf(n, p)

# Plot
plt.bar(range(n + 1), pmf, color='green')
plt.xlabel('Number of Wins in 5 Matches')
plt.ylabel('Probability')
plt.title('Binomial Distribution: Arsenal Wins')
plt.grid(True)
plt.show()