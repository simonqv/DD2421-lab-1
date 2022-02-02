# Report

## Assignment 0
MONK-2 is the hardest to learn because it has the most complex `true` condition with the most different cases. This will lead to lost of "questions".

## Assignment 1
|Dataset|Entropy           |
|-------|------------------|
|MONK-1 |1.0               |
|MONK-2 |0.957117428264771 |
|MONK-3 |0.9998061328047111|

## Assignment 2
A uniform distribution should have a high entropy because there is more uncertainty about the outcome.
A non-uniform distribution should have a lower entropy because the there is less uncertainty about the outcome.

### Examples
- Coin toss: Uniformly distributed (high entropy), either *head* or *tail*. Each side has the same probability of `1/2`.
- Biased coin toss: Non-uniform distribution (low entropy), either *head* or *tail*. But one side is more likely than the other. Lowest entropy is when one side has a probability of 1, which results in entropy of 0.

## Assignment 3
|Dataset|a₁           |a₂           |a₃           |a₄           |a₅           |a₆           |
|-------|-------------|-------------|-------------|-------------|-------------|-------------|
|MONK-1 | 0.07527255560831925| 0.005838429962909286| 0.00470756661729721| 0.02631169650768228| 0.28703074971578435| 0.0007578557158638421|
|MONK-2 | 0.0037561773775118823| 0.0024584986660830532| 0.0010561477158920196| 0.015664247292643818| 0.01727717693791797| 0.006247622236881467|
|MONK-3 | 0.007120868396071844| 0.29373617350838865| 0.0008311140445336207| 0.002891817288654397| 0.25591172461972755| 0.007077026074097326|

- MONK-1: a₅
- MONK-2: a₅
- MONK-3: a₂

## Assignment 4
If we look at the equation we can see that if the information gain is maximized, then the entropy of the subsets Sₖ is low.

To get smaller, and therefore maybe more generalized, trees we want to take "steps" that gives us the most information gain in each step. Therefore it's quite reasonable to use the gain as a heuristic for choosing an attribute for splitting. If we pick an attribute with more gain, we are left with less "surprise".

## Assignment 5
|       |E\_train     | E\_test           |
|-------|-------------|-------------------|
|MONK-1 |1.0          | 0.8287037037037037|
|MONK-2 |1.0          | 0.6921296296296297|
|MONK-3 |1.0          | 0.9444444444444444|

## Assignment 6
The more we prune, the higher the bias of the tree gets and the variance gets lower.
If we don't prune, we'll have high variance and low bias.

## Assignment 7
See Figure\_1.png




















