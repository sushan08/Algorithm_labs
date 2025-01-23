def get_strings(n):
    return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

def bruteforce_01knapsack(p, w, m):
    assert len(p)== len(w), "p and w do not have the same number of elements"
    n= len(p)
    bit_strings= get_strings(n)
    max_profit = 0
    solution = ''
    for s in bit_strings:
        weight=0
        profit=0
        for i in range (n):
            if s[i]=='1':
                weight += w[i]
                profit += p[i]
        if weight<=m and profit > max_profit:
            max_profit= profit
            solution = s
    return max_profit, solution


def bruteforce_fractional_knapsack(p, w, m):
    assert len(p) == len(w), "p and w differ"
    n = len(p)  
    max_profit = 0  
    total_weight = m 
    best_solution = []  
    
    for i in range(2**n):
        s = bin(i)[2:].rjust(n, '0')  
        profit = 0  
        weight = 0  
        fraction_solution = []  
        
        for j in range(n):
            if s[j] == '1': 
                profit += p[j]
                weight += w[j]
                fraction_solution.append(1)  
            else:  
                fraction_solution.append(0)  
        
        if weight > total_weight:
            continue
        

        remaining_capacity = total_weight - weight  
        fractional_items = [j for j in range(n) if s[j] == '0']  
        total_fractional_weight = sum(w[j] for j in fractional_items) 
        
        if total_fractional_weight > 0:
            fraction = remaining_capacity / total_fractional_weight
            for j in fractional_items:
                profit += fraction * p[j]
                weight += fraction * w[j]
                fraction_solution[j] = fraction 
        
        if profit > max_profit:
            max_profit = profit
            best_solution = fraction_solution 

    return max_profit, best_solution


def greedy_fractional_knapsack(p, w, m):
    assert len(p) == len(w), "p and w do not have the same number of elements"
    n = len(p)
    ratios = [(p[i] / w[i], p[i], w[i]) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_profit = 0
    weight_left = m
    solution = []
    
    for ratio, profit, weight in ratios:
        if weight_left <= 0:
            break
        if weight_left >= weight:
            total_profit += profit
            weight_left -= weight
            solution.append((1, profit, weight))  
        else:
            total_profit += profit * (weight_left / weight)
            solution.append((weight_left / weight, profit, weight))  
            weight_left = 0
    
    return total_profit


def dynamic_programming_knapsack(p, w, m):
    assert len(p) == len(w), "p and w do not have the same number of elements"
    n = len(p)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + p[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


#weights= [4, 2, 1, 3]
#profit= [15,6,3,6]
#capacity = 6
#maximum= dynamic_programming_knapsack(profit, weights, capacity)
#print("Maximum profit is", maximum)
