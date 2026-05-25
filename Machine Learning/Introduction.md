# Machine Learning
   Machine learning is a subset of artificial intelligence that focus on building systems that learn from data. Conventional AI systems 
like decision support systems are rule based and cannot learn from data. Instead of being explicitly programmed with fixed rules to perform a task, 
a machine learning algorithm uses data to find patterns, make predictions, and improve its performance automatically over time.

## How Machine Learning Works
The machine learning process generally follows a continuous loop
  - **Data Collection**: Gathering historical data (numbers, text, images, or clicks).
  - **Training**: Feeding this data into an ML algorithm. The algorithm analyzes the data to discover hidden patterns or relationships.
  - **Building the Model**: The result of the training phase is a "model" — a mathematical representation of the patterns the algorithm found.
  - **Prediction and Tuning**: The model is given new, unseen data to see how accurately it can make predictions. If the errors are high, the algorithm tweaks its internal logic and tries again.

## Different type of machine learning
  There are 3 types of machine learning
  - Supervised Learning
  - UnSupervised Learning
  - Reinforcement Learning

  1. **Supervised Learning**: The algorithm is trained on labeled data, meaning every piece of input data comes with the correct answer or outcome. The goal is for the model to learn the mapping from inputs to outputs.

     There are two types of supervised learning based on the nature of the target variable(the outcome you are trying to predict)
     1. **Regression**: In regression tasks, the machine learning model predicts a continuous, numerical output.
        - Example: Predicting house prices based on square footage, location, and number of bedrooms
     2. **Classification**: In classification tasks, the model assigns the input data into specific, predefined categories or classes. The output is a discrete label rather than a continuous number.
        - Example: Predicting an email is spam or not spam.

     **Common Algorithms Used**
     - **Linear Regression** : Used for predicting continuous numerical values based on linear relationships.
     - **Decision Trees** : Tree-based models that split data based on feature values.
     - **Random Forests** : Random Forests combine multiple trees for better accuracy.
     - **Logistic Regression** : Despite its name, it is used for binary classification tasks.
     - **Support Vector Machines** : Finds the optimal hyperplane that best separates different classes in a high-dimensional space.

     **Different steps used in Machine model creation**
     - Collect the input data set
     - Convert the data such that it can be used by a machine learning algorithm. Typically this will be the step of creating a data frame
     - Define the feature and target
     - Split the data into training dataset and testing dataset
     - Create the model using suitable machine learning algorithm
     - Train the model using training dataset
     - Determine the test accuracy of the model
     - If we have test accuracy 1.0, that means model is 100% accurate. Ideal accuracy needs to be >= 70%
     - Once we have good accuracy model then we can use it for predicting the real time scenario.

  3. **Unsupervised Learning**: The algorithm is given unlabeled data and must find patterns, structures, or anomalies on its own without any guidance.
  
     It is primarily used for:
     - Clustering : Grouping similar data points together
     - Dimensionality Reduction : Compressing data by reducing the number of random variables under consideration, making it easier to visualize or process.
     - Association Rule Learning : Finding interesting relations between variables in large databases (e.g., "people who buy diapers also buy beer").

     **Example**
     - Customer segmentation for marketing, Recommendation engines(like Suggestions fron Netflix)

     **Common Algorithms Used**
     - **K-Means Clustering** : Partitioning data into $K$ distinct, non-overlapping clusters based on distance to a central point.
     - **Principal Component Analysis(PCA)** : A dimensionality reduction technique that transforms a large set of variables into a smaller one while retaining most of the original variance.
     - **Hierarchical Clustering** : Building a tree of clusters (dendrogram) to visualize data hierarchies.
     - **Isolation Forests** : An algorithm specifically designed for anomaly and outlier detection

  4. **Semi-Supervised Learning** : This approach sits comfortably between supervised and unsupervised learning. It uses a small amount of labeled data combined with a large amount of unlabeled data during training.

     This is incredibly useful because labeling data by hand is expensive and time-consuming, whereas acquiring raw, unlabeled data is usually cheap. The model uses the small labeled dataset to get its bearings, and then leverages the structural patterns in the unlabeled data to improve its overall predictive power.

     **Common Algorithms Used**
     - **Self Training** : The model is trained on the small labeled data, then uses its own highly confident predictions to label the unlabeled data, iterating on the newly expanded dataset.
     - **Graph-Based Models** : Data points are mapped as nodes on a graph, and labels are "propagated" from labeled nodes to neighboring unlabeled nodes based on similarity.

  6. **Reinforcement Learning**: The algorithm learns by interacting with an environment. It takes actions and receives feedback in the form of rewards (for correct actions) or penalties (for mistakes). Reinforcement learning operates on a completely different trial-and-error paradigm. Instead of analyzing a static dataset, an agent learns to interact with a dynamic environment. The agent takes actions, receives feedback in the form of rewards (for good moves) or penalties (for bad moves), and dynamically updates its strategy (policy) to maximize its total cumulative reward over time.
        - Example: Self-driving cars navigating traffic, Robotics

     **Common Algorithms Used**
     - **Q-Learning** : A model-free, value-based algorithm that learns the value of taking a specific action in a specific state.
     - **Deep Q-Networks(DQN)** : Combines Q-Learning with Deep Neural Networks to handle complex environments (like playing Atari games).
     - **Proximal Policy Optimization(PPO)** : A popular policy-gradient method often used in robotics and for fine-tuning modern AI language models.


## What is difference between algorithm and model in machine learning
Algorithm and model represents 2 distinct stages of machine learning work flow.

An algorithm is the blueprint or the step-by-step procedure used to learn from data. It defines how the computer will bend, twist, or split the data to find a pattern. It consists of pure mathematics and logic, completely devoid of any real-world knowledge until you feed it data.
- Examples: Linear Regression, Random Forest, Support Vector Machines (SVM), K-Means

A model is the actual software program or file that you use to make predictions. It is the specific result of running your training data through the machine learning algorithm. The model contains the specific mathematical coefficients, decision rules, or neural weights that fit your exact data.
- Examples: A specific file (like a .pkl, .h5, or .onnx file) that can take an input like "house square footage" and output a prediction like "$450,000".

Thin of it as : **The algorithm is the recipe, and the model is the cake**

Difference
|Feature|Machine Learning Algorithm|Machine Learning Model|
|-------|--------------------------|----------------------|
|What It is|A mathematical process, logic, or set of rules used to find patterns.|The specific output/artifact created after running data through an algorithm.|
|When it exists|It exists before you even touch your data (it is standard code or math).|It only exists after the learning/training process is complete.|
|What it contains|Pure logic, equations, and hyper-parameters (settings you choose).|Learned weights and biases (parameters) tailored to a specific dataset.|
|Dynamic|Static. Example: A Linear Regression algorithm is always the same mathematical formula.|Dynamic. A model changes depending on the data you use to train it.|

## How Algorithm and Model work together
The transition from algorithm to model happens during the training phase

$$\text{Algorithm} + \text{Training Data} \xrightarrow{\text{Training Process}} \text{Model}$$

- You choose an algorithm (e.g., Linear Regression: $y = mx + b$).
- You feed it your training data (e.g., historical housing prices and sizes).
- The algorithm runs, iteratively adjusting variables until it finds the best fit.
- The output is a model with fixed parameters (e.g., $\text{Price} = 250 \times \text{Size} + 50,000$).
- You deploy this model to make predictions on new data.

If you change the training data, the algorithm remains exactly the same, but it will produce a completely different model.

## Test Accuracy of a model

  **Test accuracy** is a metric used to evaluate how well a machine learning model performs on a completely unseen dataset (the **test set**). It represents the proportion of correct predictions out of the total number of predictions made during testing.

  Mathematically, for a classification model, it is calculated as:

   $$\text{Test Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}} = \frac{TP + TN}{TP + TN + FP + FN}$$

   (Where $TP$ = True Positives, $TN$ = True Negatives, $FP$ = False Positives, and $FN$ = False Negatives).

  **Why is Test Accuracy Important?**

   When training a model, we typically split your data into three distinct sets:
    Because the model has never encountered the test data during its training phase, test accuracy serves as the ultimate reality check for how the model will perform in the real world (generalization).
     
 

      
      
     
    
     


## Lab
- [Training the Model using Linear Regression](https://github.com/varugheseben/edurek-data_science/blob/main/Machine%20Learning/Chapter-1.ipynb)
- [Training the Model using Labelled Data](https://github.com/varugheseben/edurek-data_science/blob/main/Machine%20Learning/Chapter_2.ipynb)
- [Training the Model using DecisionTree Regression](https://github.com/varugheseben/edurek-data_science/blob/main/Machine%20Learning/Chapter_3.ipynb)
- [Training the Model using Random Forest Regression](https://github.com/varugheseben/edurek-data_science/blob/main/Machine%20Learning/Chapter_4.ipynb)
- [Draw Decision Tree generated by Decision Tree Regressor Modal](https://github.com/varugheseben/edurek-data_science/blob/main/Machine%20Learning/Chapter_5.ipynb)
- [Dummy data Generator for Regression testing](https://github.com/varugheseben/edurek-data_science/blob/main/Machine%20Learning/Chapter_6.ipynb)

