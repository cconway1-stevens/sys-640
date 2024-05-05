
# Martin-Beck Company Plant Location and Distribution Model

## Problem Statement

The Martin-Beck Company is assessing options for expanding its production facilities and streamlining its distribution network to better meet rising customer demand. Their current operation, based in St. Louis, has a production limit of 30,000 units, which is no longer sufficient. The company is evaluating four new potential sites for plant development: Detroit, Denver, Toledo, and Kansas City. The primary goal is to minimize the combined costs of establishing new plants and distributing products to various markets.

## Part a) Linear Programming Model Development

**Decision Variables:**
- $x_{ij}$: the number of units shipped from plant $i$ to destination $j$.
- $y_i$: binary variable where $y_i = 1$ if plant $i$ is built, $y_i = 0$ otherwise.

**Objective Function:**
- Minimize $Z = \sum_{i} F_i y_i + \sum_{i} \sum_{j} C_{ij} x_{ij}$
  - $F_i$: fixed construction cost of plant $i$
  - $C_{ij}$: shipping cost per unit from plant $i$ to destination $j$

**Constraints:**
1. Supply Constraint: $ \sum_{j} x_{ij} \leq Q_i y_i $ for all $i$
   - $Q_i$: capacity of plant $i$
2. Demand Constraint: $ \sum_{i} x_{ij} = D_j $ for all $j$
   - $D_j$: demand at destination $j$
3. Non-Negativity and Binary Constraints: $ x_{ij} \geq 0 $ for all $i,j$ and $ y_i \in \{0, 1\} $ for all $i$

This part of the model lays the groundwork for determining the optimal distribution and production strategy for Martin-Beck Company. It combines linear programming techniques with strategic planning to analyze and minimize total costs.

## Part b) Modification for Policy Restriction: Detroit or Toledo

**Additional Constraint:**
- $y_{	ext{Detroit}} + y_{	ext{Toledo}} = 1$

To comply with internal policies or local regulatory requirements, the company considers an additional constraint. The decision mandates that between Detroit and Toledo, only one plant can be operational. This constraint ensures that strategic decisions align with broader company policies or regulatory frameworks.

## Part c) Modification for Policy Restriction: Denver, Kansas City, and St. Louis

**Additional Constraint:**
- $y_{	ext{Denver}} + y_{	ext{Kansas City}} + y_{	ext{St. Louis}} \leq 2$

This modification to the model accounts for another strategic decision that limits the operational scope within Denver, Kansas City, and St. Louis to two operational plants at most. This policy could be motivated by investment limitations, risk management strategies, or logistical efficiencies.

## Part d) Modification for Dual Capacity in Denver

**New Decision Variables:**
- $y_{	ext{Denver-small}}$ and $y_{	ext{Denver-large}}$: binary variables for the small and large capacities, respectively.

**Modified Constraints and Objective Function:**
- Capacity for Denver: $ \sum_{j} x_{	ext{Denver}, j} \leq 30000 y_{	ext{Denver-small}} + 60000 y_{	ext{Denver-large}} $
- Objective Function Update: Include costs for both sizes: $375000 y_{	ext{Denver-small}} + 550000 y_{	ext{Denver-large}}$

This part explores the flexibility of Denver's plant capacity, where the company considers two potential sizes—small and large. This choice allows the company to adapt more dynamically to market demands and production scalability, integrating varying costs and capacities into their strategic planning.