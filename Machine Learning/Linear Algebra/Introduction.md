# Linear Algebra
  Different types of values in Linear Algebra
  - Scalars : A scalar is a single, isolated number. It represents magnitude but has no direction.
    - Example: x = 5
  - Vectors : A vector is an ordered list or sequence of numbers
    - Example: $[1 \quad 2 \quad 3]$
  - Matrices : A matrix is a two-dimensional rectangular array of numbers arranged in rows and columns
  - Tensors: A tensor is a generalization of scalars, vectors, and matrices to an arbitrary number of dimensions.

|Value Type|Dimensions|Representation|Typical Application|
|----------|----------|--------------|-------------------|
|Scalar|0D|A Single Number|Scaling factors, learning rates, constants|
|Vector|1D|An ordered array / line of numbers|Representing a single data point or feature vector|
|Matrix|2D|A grid of rows and columns|Linear transformations, systems of linear equations, datasets|
|Tensor|ND|Multi-dimensional arrays|Complex data structures, volumetric data, deep learning weights|

Every machine learning algorithm is based of a mathematical engine known as **Linear Algebra**.

Below are the different areas where Linear Algebra is used in machine learning workflow
 - **Data Representation(Vectores and Matrices)**

      In machine learning, data isn't just a list of numbers; it is structured as vectors and matrices.
 - **Linear Transformations and Neural Networks**

      Deep learning is essentially a massive chain of linear transformations combined with non-linear functions.
 - **Dimensionality Reduction** :

      Datasets often contain too many features (the "curse of dimensionality"), which can slow down training and cause overfitting. Linear algebra provides tools to compress data while keeping the most important information
 - **Measuring Distance and Similarity**

      How does a model know if two data points are similar?  It treats them as geometric vectors and applies linear algebra metrics:
   - **Distance**: Euclidean distance (calculating the length of a vector using the Pythagorean theorem) is used in algorithms like $K$-Nearest Neighbors ($K$-NN) and $K$-means clustering
   - **Direction/Angle**: As mentioned with Cosine Similarity, calculating the dot product of two normalized vectors tells us how close their directions are, which is vital for text embeddings and recommendation engines.
   
 - **Optimization (Loss Functions and Gradients)**

      To train a model, you have to minimize a loss function (the error)
