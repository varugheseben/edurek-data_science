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
     - **Event $A$** : You have the disease, so $$P(A)$$ = 0.01 (1% of people have the disease)
     - **Event Not $A$** : You are healthy so $$P(Not A)$$ = 0.99 (99% of people are healthy)
     - **Event $B$** : Your test result is positive
  
     So we want to find $$P(A|B)$$, means what is the probability of person have disease given your test result is positive.

     So lets findout the components required for Bayes theorem
  
     - $$P(A)$$ (Prior) = 0.01
     - $$P(B|A)$$ (Likelihood) = 0.95 (Likelihood of testing positive if you are sick)
     - $$P(B)$$ (Evidence) : Here we have 2 possibilities
         - Person sick and test positive
         - Person healthy and test positive
         
          So,
       
          $$P(B) = (P(B|A) \cdot P(A)) + (P(B|\text{not } A) \cdot P(\text{not } A))$$
  
          = (0.95 * 0.01) + 0.05 * 0.99
  
          = 0.0095 + 0.0495

          $$\therefore\ \  Total\ \  P(B) = 0.059$$

          So we get, $$P(A|B) = \frac{0.95 \cdot 0.01}{0.059}$$
  
          = $$\frac{0.0095}{0.059}$$ = 0.1610 = 16.1%

    **Result** : Even though the test is 95% accurate, a positive result only means you have a 16.1% chance of actually being sick.

- **Email Spam Filter**: Every time an email lands in your inbox, your email provider uses a Bayesian filter to decide if it's spam.

  **The Scenario**:
       Let’s say 40% of all emails you receive are spam.
    - The word "Free" appears in 60% of spam emails.
    - The word "Free" appears in only 10% of legitimate (ham) emails.

  **Question**: If an incoming email contains the word "Free", what is the probability that it is spam?
  
  **Solution**:
    Lets say we have 2 events
  - Receive a spam email, say event A
  - Receive email with word 'Free', say event B

  So we can say,
  - $$P(A)$$ (Prior) = 0.40
  - $$P(\text{not } A)$$ = 0.60
  - $$P(B|A)$$ (Likelihood) = 0.60
  - $$P(B)  (Evidence) = (P(B|A) \cdot P(A)) + (P(B|\text{not } A) \cdot P(\text{not } A))$$
    
    = (0.60 + 0.40) + (0.10 * 0.60)

    = 0.24 + 0.6

    $$\therefore\ \  Total\ \  P(B) = 0.30$$

    So we get, $$P(A|B) = \frac{0.60 \cdot 0.40}{0.30}$$

    = $$\frac{0.24}{0.30}$$ = 0.8 = 80%
 
- **The Rainy Day Forecast**: You want to know if it's going to rain today, but you woke up late and can only look out the window to see if it's cloudy.

  **The Scenario**:
       In your city, it rains on 10% of days.
    - When it rains, 90% of the mornings start out cloudy.
    - When it doesn't rain, only 20% of the mornings start out cloudy.

  **Question**: You look outside and see clouds. What is the actual chance of rain today?
