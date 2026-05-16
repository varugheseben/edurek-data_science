## Probability
   Probability is the mathematical measure how likely an event is to occur. It quantified uncertainity on scale from 0 to 1(that means 0% to 100%)

1. **0(0%)**: The event is impossible.
   Example: Rolling 7 on a standard six-sided die

2. **0.5(50%)**: The event is equally likely to happen or not happen
   Example: Flipping a coin and getting heads

3. **1(100%)**: The event is a certainty
   Example: Sun is rising tomorrow
   
## Different terms to understand probability

1. **Experiment**: An action or process that has an uncertain outcome (e.g., tossing a coin, rolling a die, drawing a card).

2. **Outcome**: A single potential result of an experiment (e.g., tossing a coin).

3. **Sample Space(S)**: The set of all possible outcomes. For a standard die, the sample space is {1, 2, 3, 4, 5, 6}.

4. **Event(E)**: A specific outcome or a collection of outcomes we are interested in (e.g., rolling an even number, which includes {2, 4, 6}).

## Equation to calculate probability

           
   **P(E) = Number of Favorable Outcomes / Total number of possible outcomes**
           
## Classic Examples

1. **Tossing a coin**: What is the probability of getting heads while tossing a coin

   Favorable outcomes(Heads) = 1

   Total outcomes (Head or Tail) = 2

   P(Head) = 1/2 = 0.5 = 50%

2. **Rolling a Die**: What is the probability of rolling an even number?

   Favorable outcomes(2, 4, 6) = 3

   Total outcomes (1, 2, 3, 4, 5, 6) = 6

   P(Even) = 3/6 = 0.5 = 50%

3. **Rolling a dice**: What is the probability of getting 3 in dice ?

   Favorable outcomes(3) = 1

   Total outcomes (1, 2, 3, 4, 5, 6) = 6

   P(Even) = 1/6 = 0.1666 = 16.67%

4. **Shuffling Playing Cards**: What is the probability of getting Ace(A) from a set of playing cards ?

   Favorable outcomes(A) = 4

   Total outcomes (Total number of cards) = 52

   P(Even) = 4/52 = 0.0769 = 7.69%

5. **Rolling a dice**: What is the probability of not getting 3 in dice ?

   P(Overall) = P(Getting 3) + P(Not getting 3) = 1

   So we can write,

   P(Not getting 3) = 1 - P(Getting 3)

                    = 1 - 1/6 = 5/6 = 0.8333 = 83.33%

7. **Tossing Coins**: What is the probability of getting heads in tossing 2 coins ?

   So events can be
   
<div align="center">

| Coin 1 | Coin 2 |
| ------ | ------ |
| H      | H      |
| H      | T      |
| T      | H      |
| T      | T      |

</div>

   a. **Probability of getting atleast one head**

            Favorable outcomes of atleast one head = 3
            Total outcomes  = 4
            P(Atleast one head) = 3/4 = 0.75  = 75%

   b. **Probability of getting exactly one head**

            Favorable outcomes of exactly one head = 2
            Total outcomes  = 4
            P(Exactly one head) = 2/4 = 0.5  = 50%

   c. **Probability of getting 2 heads**

            Favorable outcomes of exactly one head = 1
            Total outcomes  = 4
            P(Exactly one head) = 1/4 = 0.25  = 25%

## Different types of probabilty

1. **Theoretical(Classical) Probability**: Based purely on logic and math rules, assuming ideal conditions. No actual experiment needs to take place.
   Example: What is the probability of getting heads while tossing a coin

2. **Emperical(Experimental) Probability**: Based on real-world data and observations. It's calculated by running an experiment many times and recording the results.

   **P(E) = Number of times event occurred / Total number of trials**

3. **Subjective Probability**: Based on personal judgment, experience, or intuition rather than strict math (e.g., a sports analyst saying a team has a 70% chance of winning the championship).

## Addition Rule
P(A \cup B) -> Means Probability of A UNION B
$$P(A \cap B)$$ -> Means Probability fo A INTERSECTION B

   So equation is 

**$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$**

### Multiplication Rule

**$$P(A \cap B) = P(A) \times P(B)$$**


## Domain where probability is used

1. **Statistics & Data Science**: Used to infer patterns from data, train machine learning models, and determine if experimental results are statistically significant.

2. **Finance & Insurance**: Used to calculate risk, price insurance premiums, and manage investment portfolios.

3. **Weather Forecasting**: Predicting a "60% chance of rain" by analyzing past atmospheric conditions.

