### Part (a): Linear Programming Model Formulation

To create a linear programming model for the Martin-Beck Company's problem, we need to consider both the distribution costs and the construction costs of potential new plants.

**Decision Variables:**
- Let $x_{ij}$ be the number of units shipped from plant $i$ to destination $j$.
- Let $y_i$ be a binary variable where $y_i = 1$ if plant $i$ is built and $y_i = 0$ otherwise, for $i \in \{Detroit, Toledo, Denver, Kansas City, St. Louis\}$.

**Objective Function:**
- Minimize the total cost, which includes both shipping and construction costs.
  $$
  \text{Minimize} \quad Z = \sum_{i,j} c_{ij} x_{ij} + 175000 y_{\text{Detroit}} + 300000 y_{\text{Toledo}} + 375000 y_{\text{Denver}} + 500000 y_{\text{Kansas City}} + 0 y_{\text{St. Louis}}
  $$
  where $c_{ij}$ represents the cost of shipping from plant $i$ to destination $j$.

**Constraints:**
1. **Supply Constraints:** Each plant can supply up to its capacity only if it is built.
   $$
   \sum_j x_{ij} \leq \text{Capacity of } i \times y_i \quad \forall i
   $$
2. **Demand Constraints:** Each destination's demand must be met.
   $$
   \sum_i x_{ij} = \text{Demand at } j \quad \forall j
   $$
3. **Binary and Non-Negativity Constraints:**
   $$
   y_i \in \{0,1\} \quad \forall i
   $$
   $$
   x_{ij} \geq 0 \quad \forall i,j
   $$

### Part (b): One Plant in Either Detroit or Toledo

To modify the original formulation to ensure that exactly one plant among Detroit and Toledo is built:

**Additional Constraint:**
- Ensure that exactly one of the two plants is built.
  $$
  y_{\text{Detroit}} + y_{\text{Toledo}} = 1
  $$

### Part (c): At Most Two Plants among Denver, Kansas City, and St. Louis

To modify the original formulation to limit the construction to at most two plants among Denver, Kansas City, and St. Louis:

**Additional Constraint:**
- At most two of these plants can be built.
  $$
  y_{\text{Denver}} + y_{\text{Kansas City}} + y_{\text{St. Louis}} \leq 2
  $$

### Part (d): Two Possible Sizes for the Denver Plant

To account for two possible sizes for the Denver plant, introduce a new decision variable and adjust the costs and capacities accordingly.

**New Decision Variables:**
- Let $z_{\text{Denver}}$ be a binary variable where $z_{\text{Denver}} = 1$ if the larger Denver plant is built and $z_{\text{Denver}} = 0$ otherwise.

**Modified Objective Function and Constraints:**
- Adjust the Denver-related terms in the objective function:
  $$
  Z = \sum_{i,j} c_{ij} x_{ij} + 175000 y_{\text{Detroit}} + 300000 y_{\text{Toledo}} + 375000 y_{\text{Denver}} + 550000 z_{\text{Denver}} + 500000 y_{\text{Kansas City}} + 0 y_{\text{St. Louis}}
  $$
- Modify the capacity constraint for Denver to consider the two possible capacities.
  $$
  \sum_j x_{\text{Denver}, j} \leq 30000 y_{\text{Denver}} + 60000 z_{\text{Denver}}
  $$
- Ensure that at most one version of the Denver plant is built:
  $$
  y_{\text{Denver}} + z_{\text{Denver}} \leq 1
  $$

**Discussion:**
These modifications add complexity to the model by introducing additional binary variables and constraints that must be managed carefully to ensure the model remains solvable and accurately represents the decision space. Each modification has implications for the feasibility and optimality of the solutions, potentially increasing computational requirements.
