# Statistics
   It is the science of learning from the data. It involves collection, organization, analysis, interpretation and presentation of 
information to uncover patterns, make predictions and inform decision-making in the face of uncertainity.

   There are two branches of statistics
## Descriptive Statistics
  This branch focus on summarizing and describing the features of specific data set. It doesn't try to make conclusions beyond the data at hand; it simply paints a clear picture of what the data looks like.
   1. **Measure of Central Tendency** :  Finding the middle of the data (Eg: Mean, Median, Mode)

   2. **Meausure of Dispersion** : Understanding how 'spread out' the data is (Eg: Range, Variance, Standard Deviation)

      Equation for variance

**$$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$$**

      Equation for Standard Deviation

**$$\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{N}}$$**

   4. **Visualiztions** : Using tools like histogram, pie chart and scatter plot to see trends visually.
        
## Inferential Statistics
  This branch uses small sample of data to make 'inferences' or generalizarions about a much larger population.
  Since you can’t always survey every single person or item in the world, you use math to determine how likely your sample results are to be true for everyone else.

   1. **Hypothesis Testing** : Determining if a result is "statistically significant" or just due to random chance.

   2. **Regression Analysis** : Predicting the value of one variable based on another (e.g., how height might predict weight).

   3. **Confidence Intervals** : Estimating a range where the true population value likely falls (e.g., "We are 95% sure the average score is between 80 and 85").
        
## Domain Applications
   Statistics is the backbone of almost every modern industry:

   1. **Medicine** : Testing whether a new drug is actually effective compared to a placebo.

   2. **Business** : Predicting consumer behavior and managing financial risk.

   3. **Data Science** : Using algorithms and probability to build AI models and analyze "Big Data."

   4. **Government** : Using census data to plan for infrastructure, schools, and healthcare.

## Use Case
   Lets say we have a list of ages of people. 

   ages = [25, 35, 30, 28, 40, 45, 100, 150, 175, 35]

   Now if were to find the average value of these ages we will get 
      (25 + 35 + 30 + 28 + 40 + 45 + 100 + 150 + 175 + 35) / 10 = 66.3

   So we get average as 66.3
   
   So with that average value if we say peoples average age is 66.3 then it will be wrong. Because most of the people's age is less than 60.
   That means out 10 only 3 people's age is more than 60. So we cannot use average.

   So in such situations we need to remove outliers from the data to calculate the accurate value. outliers are 100,150 and 175 which are far distributed from other values.

   So statistics can be used for that purpose.
