## Problem Description
Trick E. Dingo is trying, as usual, to catch his nemesis the Street Sprinter. His past attempts
using magnets, traps and explosives have failed miserably, so he’s catching his breath to gather
observational data and learn more about how fast Street Sprinter is.
Trick E. Dingo and Street Sprinter both inhabit a single straight west-east road with a particularly
famous rock on it known affectionately as The Origin. Positions on this straight road are measured
numerically according to the distance from The Origin, and using negative numbers for positions
west of The Origin and positive numbers for positions east of The Origin.

The observations by Trick E. Dingo each contain two numbers: a time, and the value of Street
Sprinter’s position on the road at that time. Given this information, what speed must Street Sprinter
must be capable of?

## Input Specification
The first line contains a number $2 \leq N \leq 100000$, the number of observations that follow. The next $N$ lines each contain an integer $0 \leq T \leq 1000000000$ indicating the time, in seconds, of when a measurement was made, and an integer $−1000000000 \leq X \leq 1000000000$ indicating the position, in metres, of the Street Sprinter at that time. No two lines will have the same value of $T$.

For 7 of the 15 available marks, $N \leq 1000$.

## Output Specification
Output a single number $X$, such that we can conclude that Street Sprinter’s speed was at least $X$ metres/second at some point in time, and such that $X$ is as large as possible. If the correct answer
is $C$, the grader will view $X$ as correct if $|X − C|/C < 10^{-5}$