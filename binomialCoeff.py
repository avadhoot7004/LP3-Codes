def binomial_coeff(n):
    # DP table to store binomial coefficients
    C = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Build Pascal's Triangle
    for i in range(n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                C[i][j] = 1  # Base case: C(n,0)=C(n,n)=1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]  # Recurrence: C(n,k)=C(n-1,k-1)+C(n-1,k)

    return C


# Example usage
n = 6
coeff = binomial_coeff(n)

print(f"Binomial Coefficients (Pascal's Triangle) for n = {n}:\n")
for i in range(n+1):
    for j in range(i+1):
        print(coeff[i][j], end=" ")
    print()
