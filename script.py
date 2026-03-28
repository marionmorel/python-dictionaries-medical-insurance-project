# Task 1
medical_costs = {}

# Task 2
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# Task 3
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

# Task 4
print(medical_costs)

# Task 5
medical_costs["Vinay"] = 3325.0
print(medical_costs)

# Task 6
total_cost = 0
for cost in medical_costs.values():
    total_cost += cost

# Task 7
average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))