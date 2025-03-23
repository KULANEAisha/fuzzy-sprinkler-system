# Fuzzy Logic-Based Sprinkler System
This project implements a fuzzy logic-based decision system to control a sprinkler system based on environmental factors such as soil moisture, temperature, and humidity. Using scikit-fuzzy, the system determines the optimal sprinkling level to maintain ideal soil conditions while conserving water.

#Features

-Uses fuzzy logic for intelligent decision-making.
-Considers three inputs: Soil Moisture, Temperature, and Humidity.
-Provides an adjustable sprinkling level (0% - 100%).
- Visualizes membership functions and fuzzy inference.
-Implements test cases to demonstrate real-world behavior.


#How It Works
This system follows these steps:

Fuzzy Input Variables

-Soil Moisture (Dry, Moist, Wet)
-Temperature (Cold, Warm, Hot)
-Humidity (Low, Medium, High)

Fuzzy Output Variable

-Sprinkling Level (Low, Medium, High)

Fuzzy Rules

If soil is dry and temperature is hot and humidity is low, sprinkling should be high
If soil is moist and temperature is warm, sprinkling should be medium
If soil is wet, sprinkling should be low


#Installation & Usage

-Clone the repository: git clone https://github.com/KULANEAisha/fuzzy-sprinkler-system.git
cd fuzzy-sprinkler-system

-Install dependencies: pip install numpy matplotlib scikit-fuzzy  

-Run the script:python sprinkler.py  

#Example Output

Test Case 1 - Soil Moisture: 30%, Temperature: 35°C, Humidity: 20% → Sprinkling Level: 72.35%

Test Case 2 - Soil Moisture: 70%, Temperature: 20°C, Humidity: 80% → Sprinkling Level: 20.5%

#Visualizations

The script plots membership functions for each variable to illustrate how fuzzy sets are defined.
