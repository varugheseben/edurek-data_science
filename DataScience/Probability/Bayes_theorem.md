# Bayes Theorem
Bayes theorem is a fundamental concept in probability which allows to update probability of an event 
as more evidence or information become available

Lets say we have two event A and B, using Bayes theorem we can say what is the probability of event A which is caused by event B.
Basically based on out come from event B we can update the probability of event A.

It is mathematically written as 

**$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$**

Where 

- **$$P(A|B)$$** (Conditional Probability): The probability of event $A$ occurring given that $B$ has already happened. This is what you want to find out (called as  **Posterior**)
- **$$P(B|A)$$** : The probability of event $B$ occurring given that $A$ is true (called as **Likelihood**)
  
    This doesnt mean event $A$ has actually happened in reality. Basically when we say "The probability of event $B$ occurring given that $A$ is true", we are making an
    assumption to understand the relation between 2 events. So we can say

      - ** It is a conditional assumption**: The phrase "given that $A$ is true" means you are temporarily assuming $A$ has happened, just to see how it would
           change the chances of $B$. It is a hypothetical scenario used to calculate the relationship between the two events.

- **$$P(A)$$** : The baseline probability of event $A$ occurring before looking at any evidence (called as **Prior**)
- **$$P(B)$$** : The total probability of event $B$ occurring under all circumstances (called as **Evidence**)
