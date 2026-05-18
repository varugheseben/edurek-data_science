# Bayes Theorem
Bayes theorem is a fundamental concept in probability which allows to update probability of an event 
as more evidence or information become available

Lets say we have two event A and B, using Bayes theorem we can say what is the probability of event A which is caused by event B.
Basically based on out come from event B we can update the probability of event A.

It is mathematically written as 

**$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$**

Where 

- **$$P(A|B)$$** (Conditional Probability): This can be read "The probability of A given B". The probability of event $A$ occurring given that $B$ has already happened. This is what you want to find out (called as  **Posterior**)

    Here we assume event $B$ has happened. When you are looking for the posterior probability—written as $P(A|B)$—you are calculating the probability of $A$ under the assumption that $B$ is a known, established fact.

    **How to think about it**

    - **Before the Evidence**: You start with the Prior, $P(A)$, which is how likely $A$ is to happen in general, before you know anything about $B$.
    - **After the Evidence (The Assumption)**: Someone hands you the data and says, "Event $B$ has definitely occurred."
    - **The Posterior**: Now, you update your beliefs. You ignore all the possibilities where $B$ didn't happen, and you calculate how likely $A$ is within this new reality where $B$ is true.

- **$$P(B|A)$$** : This can be read "The probability of B given A". The probability of event $B$ occurring given that $A$ is true (called as **Likelihood**)
  
    This doesnt mean event $A$ has actually happened in reality. Basically when we say "The probability of event $B$ occurring given that $A$ is true", we are making an
    assumption to understand the relation between 2 events. So we can say

    - **It is a conditional assumption**: The phrase "given that $A$ is true" means you are temporarily assuming $A$ has happened, just to see how it would
           change the chances of $B$. It is a hypothetical scenario used to calculate the relationship between the two events.
    - **Think of it as "Zooming In"**: Imagine you are looking at a master list of all possible outcomes. When you condition on $A$, you throw away every outcome where $A$ didn't happen, and you only look at the world where $A$ is true. So with that assumption we can say when $A$ is true how often $B$ also happen.

- **$$P(A)$$** : The baseline probability of event $A$ occurring before looking at any evidence (called as **Prior**)
- **$$P(B)$$** : The total probability of event $B$ occurring under all circumstances (called as **Evidence**)

## Real World Examples
- **Medical Testing** : Medical testing is the classic way to understand why Bayes' Theorem is so important. It shows why a positive test result doesn't always mean you are actually sick.

  **The Scenario**
       Imagine there is a rare disease that affects 1% of the population.
    - You take a lab test for this disease.
    - The test is 95% accurate (if you have the disease, it correctly returns a positive result 95% of the time).
    - The test also has a 5% false positive rate (if you are healthy, it incorrectly returns a positive result 5% of the time).

    **You take the test and it comes back positive. What is the probability that you actually have the disease?**

    **SOLUTION**

     With our intution we can say 95% of chance for having disease. But Bayes theorem says probability of having disease is very low even if the test resulted as +ve.
