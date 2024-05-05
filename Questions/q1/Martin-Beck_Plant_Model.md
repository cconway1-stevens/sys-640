# Martin-Beck Company Plant Location and Distribution Model

## Problem Statement

Martin-Beck Company aims to enhance its production capabilities and streamline distribution networks to meet increasing customer demands effectively. Currently based in St. Louis with a production limit of 30,000 units, the company seeks to expand. Four potential new plant locations are under evaluation: Detroit, Denver, Toledo, and Kansas City. The primary objective is to minimize costs associated with establishing new plants and distributing products to diverse markets.

## Part a) Linear Programming Model Development

**Decision Variables:**
- $x_{ij}$: units shipped from plant $i$ to destination $j$.
- $y_i$: binary variable indicating if plant $i$ is built.

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

This model forms the basis for optimizing Martin-Beck Company's distribution and production strategy, blending linear programming with strategic planning to minimize overall costs.

## Part b) Modification for Policy Restriction: Detroit or Toledo

**Additional Constraint:**
- $y_{\text{Detroit}} + y_{\text{Toledo}} = 1$

To adhere to internal policies or regulatory requirements, the company imposes a constraint: either Detroit or Toledo can operate, but not both. This ensures strategic decisions align with broader company policies or regulations.

## Part c) Modification for Policy Restriction: Denver, Kansas City, and St. Louis

**Additional Constraint:**
- $y_{\text{Denver}} + y_{\text{Kansas City}} + y_{\text{St. Louis}} \leq 2$

Another strategic decision restricts operational plants in Denver, Kansas City, and St. Louis to a maximum of two. This could result from investment limitations, risk management strategies, or logistical efficiencies.

## Part d) Modification for Dual Capacity in Denver

**New Decision Variables:**
- $y_{\text{Denver-small}}$ and $y_{\text{Denver-large}}$: binary variables for small and large capacities.

**Modified Constraints and Objective Function:**
- Capacity for Denver: $ \sum_{j} x_{\text{Denver}, j} \leq 30000 y_{\text{Denver-small}} + 60000 y_{\text{Denver-large}} $
- Objective Function Update: Includes costs for both sizes: $375000 y_{\text{Denver-small}} + 550000 y_{\text{Denver-large}}$

Exploring Denver's plant capacity flexibility, the company considers two potential sizes—small and large. This choice enables dynamic market adaptation and production scalability, integrating varied costs and capacities into strategic planning.