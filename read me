Deliverable 3: Backtrack Performance Analysis

1. Easy Board 

Backtrack Calls: [1]

Failures: [0]

Comment: The easy board was solved with minimal backtrack calls and zero failures. Because the board starts with a high density of pre-filled numbers, AC-3 and forward checking were able to prune the domains rapidly, allowing the search to navigate straight down to the solution without guessing incorrectly.

2. Medium Board 

Backtrack Calls: [26]

Failures: [0]

Comment: The medium board performed similarly to the easy board. The combination of arc consistency maintaining domain restrictions and the Minimum Remaining Values (MRV) heuristic selecting optimal variables kept the failure rate at zero, proving that standard propagation is sufficient to solve this level without blind guessing.

3. Hard Board 

Backtrack Calls: [62]

Failures: [8]

Comment: The hard board required slightly more backtrack calls. With fewer initial clues, the propagation algorithms (AC-3 and Forward Checking) eventually exhausted their immediate logical deductions. The algorithm had to assign values to variables with domains greater than 1, leading to a small number of failures and subsequent backtracks before correcting the path.

4. Very Hard Board 

Backtrack Calls: [153]

Failures: [97]

Comment: This board demonstrated the highest number of calls and failures. The extreme sparseness of the initial state meant that AC-3 could not reduce many domains to a single value initially. The search tree was significantly wider and deeper, forcing the backtracking algorithm to make multiple assumptions, hit dead-ends, and reverse its decisions frequently before finalizing the valid matrix.




