# Import necessary libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Step 1: Define Fuzzy Variables
# Input Variables
soil_moisture = ctrl.Antecedent(np.arange(0, 101, 1), 'Soil Moisture')
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'Temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'Humidity')  # New input variable

# Output Variable
sprinkling = ctrl.Consequent(np.arange(0, 101, 1), 'Sprinkling')

# Step 2: Define Membership Functions

# Soil Moisture (0% - 100%)
soil_moisture['Dry'] = fuzz.trimf(soil_moisture.universe, [0, 0, 50])
soil_moisture['Moist'] = fuzz.trimf(soil_moisture.universe, [30, 50, 70])
soil_moisture['Wet'] = fuzz.trimf(soil_moisture.universe, [60, 100, 100])

# Temperature (0°C - 50°C)
temperature['Cold'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['Warm'] = fuzz.trimf(temperature.universe, [10, 25, 35])
temperature['Hot'] = fuzz.trimf(temperature.universe, [30, 50, 50])

# Humidity (0% - 100%) - New Membership Functions
humidity['Low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['Medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity['High'] = fuzz.trimf(humidity.universe, [60, 100, 100])

# Sprinkling Level (0 - 100)
sprinkling['Low'] = fuzz.trimf(sprinkling.universe, [0, 0, 40])
sprinkling['Medium'] = fuzz.trimf(sprinkling.universe, [30, 50, 70])
sprinkling['High'] = fuzz.trimf(sprinkling.universe, [60, 100, 100])

# Step 3: Define Fuzzy Rules (with Humidity Consideration)
rule1 = ctrl.Rule(soil_moisture['Dry'] & temperature['Hot'] & humidity['Low'], sprinkling['High'])
rule2 = ctrl.Rule(soil_moisture['Dry'] & temperature['Warm'] & humidity['Low'], sprinkling['Medium'])
rule3 = ctrl.Rule(soil_moisture['Moist'] & temperature['Warm'] & humidity['Medium'], sprinkling['Medium'])
rule4 = ctrl.Rule(soil_moisture['Moist'] & temperature['Cold'] & humidity['High'], sprinkling['Low'])
rule5 = ctrl.Rule(soil_moisture['Wet'], sprinkling['Low'])
rule6 = ctrl.Rule(humidity['High'] & soil_moisture['Dry'], sprinkling['Medium'])  # New rule
rule7 = ctrl.Rule(humidity['High'] & soil_moisture['Moist'], sprinkling['Low'])   # New rule

# Step 4: Create the Fuzzy Control System
sprinkling_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
sprinkling_simulation = ctrl.ControlSystemSimulation(sprinkling_ctrl)

# Step 5: Test Cases and Compute Output

# Test Case 1: Soil Moisture = 30%, Temperature = 35°C, Humidity = 20%
sprinkling_simulation.input['Soil Moisture'] = 30
sprinkling_simulation.input['Temperature'] = 35
sprinkling_simulation.input['Humidity'] = 20
sprinkling_simulation.compute()
print(f"Test Case 1 - Soil Moisture: 30%, Temperature: 35°C, Humidity: 20% → Sprinkling Level: {sprinkling_simulation.output['Sprinkling']}%")

# Test Case 2: Soil Moisture = 70%, Temperature = 20°C, Humidity = 80%
sprinkling_simulation.input['Soil Moisture'] = 70
sprinkling_simulation.input['Temperature'] = 20
sprinkling_simulation.input['Humidity'] = 80
sprinkling_simulation.compute()
print(f"Test Case 2 - Soil Moisture: 70%, Temperature: 20°C, Humidity: 80% → Sprinkling Level: {sprinkling_simulation.output['Sprinkling']}%")

# Step 6: Plot Membership Functions
fig, ax = plt.subplots(1, 4, figsize=(20, 5))

soil_moisture.view(ax=ax[0])
temperature.view(ax=ax[1])
humidity.view(ax=ax[2])
sprinkling.view(ax=ax[3])

plt.show()
