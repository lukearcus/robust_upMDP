# Probably Approximately Correct Robust Policy synthesis for uncertain parametric Markov Decision Processes

We provide a tool for the synthesis of a robust policy, and associated guarantee, for uncertain parametric Markov Decision Processes (upMDPs).
See our [associated paper](lukerickard.co.uk/pubs/RAM24.pdf) for details.

## Requirements

To install dependencies use:
> conda env create -f environment.yml

## Running

To run use
> python run.py

Options:

| Option | Arguments | Description |
| -------|-----------|-------------|
|--model | "test", "test2", "test3", "test4", "test5", "test6", "test7", "drone", "consensus", "hol", "robot", "expander", "brp", "sav", "zeroconf"| Choose model type (default test2)|
|-N | int > 1 | Number of samples (default 200) |
|-beta | Probability \[0,1\]| Confidence parameter (default 1e-5)|
|--MC | None | Run Monte-Carlo test|
|--MC\_p | None | Run Monte-Carlo test with perturbation|
|--MC\_samples| int > 1 | Number of samples for Monte-Carlo test (default 10,000)|
|--tol | float > 0 |Convergence tolerance (default 1e-5)| 
|--load | filename | Load stored samples | 
|--save | filename | Save samples after generation |
|--save\_res | filename | Sav results |
|--load\_res | filename | Load results (for hot starting)|
|--sg\_itt | int > 1 | Max. number of subgradient iterations (default 5000)| 
|--file\_out | filename | output for text |
|--output\_figs | None | Display figures | 
|--save\_figs | filename | File for saving figures |
|--init\_step | float > 0 | initial subgradient step size (default 10)|
|--step\_exp | float \[0,1\] | exponential for step size decay (deault 0.5)| 
|--to | int > 1 | max computation time in s (default 1hr) |
|--sg\_only | None | run subgradient method only |
| -v | None | Verbose debug level|
| -d | None | Debugging |
