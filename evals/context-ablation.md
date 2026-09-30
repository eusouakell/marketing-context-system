# Experiment — Context ablation

**Status: proposed protocol; results have not been published.**

## Question

Which context layers materially improve the output, and which merely make the input larger?

## Conditions

Run the same task with the same model under:

A. Prompt only  
B. Prompt + brand context  
C. B + audience context  
D. C + evidence context  
E. D + task skill  
F. E + verification harness

## Measures

- factual accuracy;
- unsupported claims;
- brand consistency;
- audience fit;
- evidence quality;
- revision count;
- context size / token cost.

## Interpretation

The target is not "full context wins."

The target is identifying the **minimum sufficient context configuration** for the task.
