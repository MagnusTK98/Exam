# Flow 29
# Task 4
# Instead of making a whole new code with the cost of 5, it can easily be changed at the bottom.
# Quick analysis: Intuitively, it could make sense to produce fewer ice creams with higher costs.
# However, two things do count the opposite:
# 1. There is still a higher penalty fee for missing out on sales. Thus, it will still make more sense to over produce
# 2. This is the bigger reason. Empirically, we see an average demand of 800. Thus, the optimal production level is 800
# So, optimal production quantity should stay the same, but we have lower profits as a result

import numpy as np
import matplotlib.pyplot as plt
def simulate_demand(poisson):
    demand=round(np.random.poisson(poisson))
    return demand


def get_daily_profit(cost, penaltyfee, price, maxunits, poisson):
    demand = simulate_demand(poisson)
    producedUnits = []
    profits = []
    for i in range(maxunits):
        production = i
        production_cost = production * cost
        sales = min(demand, production)
        excess_demand=max(0,demand-production)
        revenue = sales * price
        penalty = excess_demand * penaltyfee
        # print(revenue, production_cost, penalty)
        profit = revenue - production_cost - penalty
        # print(profit)
        profits.append(profit)
        producedUnits.append(i)

    best_profit = np.max(profits)
    best_production = profits.index(max(profits))
 
    return best_profit, best_production, profits, producedUnits

def optimal_production(n, cost, penalty, price, maxunits, poisson):
        icecreams=[]
        for i in range(n):
            best_profit, best_production, profits, producedUnits = get_daily_profit(cost, penaltyfee, price, maxunits, poisson)
            icecreams.append(best_production)
        print(round(np.mean(icecreams)))
        print(best_profit)
        plt.figure()
        plt.plot(producedUnits, profits)
        plt.savefig("Task4.png")


n = 1000
cost = 4
penaltyfee = 10
price = 15
maxunits = 1200
poisson = 800
optimal_production(n, cost, penaltyfee, price, maxunits, poisson)

