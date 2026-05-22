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
     

