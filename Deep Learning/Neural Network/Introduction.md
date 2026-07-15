# Neural Network
  At its core, a **Neural Network** (or Artificial Neural Network) is a method in artificial intelligence that teaches computers to process data in a way that is inspired by the human brain.

  It is a key building block of Deep Learning, which powers many of today's smart technologies, from facial recognition to conversational AI.

  ## The core component: The Neuron(Perceptron)
  Just as our brains are made of interconnected biological neurons, an artificial neural network is made of digital processors called nodes or neurons.
  Each neuron takes in data, processes it, and passes it along. A single neuron consists of three main mathematical operations:
  - **Input($x$)**: The incoming data features.
  - **Weights ($w$) and Biases ($b$)**: Crucial coefficients that the network adjusts during training. Weights determine how much influence a specific input has, while the bias shifts the overall activation.
    
       Significance of Weights and Bias: https://www.youtube.com/watch?v=pPOZODXH61s
       **Note**: Bias is a constant which helps the model in a way that it can fit best for the given data.

  - **Activation Function**: A mathematical formula (like ReLU or Sigmoid) that decides whether—and to what extent—the neuron should pass its signal to the next layer. It introduces non-linearity, allowing the network to learn complex patterns.

      $$y = \text{Activation}\left(\sum (x_i \cdot w_i) + b\right)$$

      **Note**: We use **Sigmoid** as activation function when we have categorical dependent variable in the input.
  ## Step-by-Step Processing Breakdown

  [ Inputs ]          [ Weights ]         [ Summation Node ]      [ Activation ]      [ Output ]
  
     x₁  --------->  [  * w₁  ]  ----\
                                      \
     x₂  --------->  [  * w₂  ]  ------->  +----------------+
                                           |  Weighted Sum  |      +------------+
                                           |                | ---> | Activation | --->  Output (a)
     xₙ  --------->  [  * wₙ  ]   ------->  | Σ(x_i·w_i) + b |      |    f(z)    |
                                      /    +----------------+      +------------+
                                     /
                     ( Bias b )  ---/
  - **Input Reception ($x_i$)** : The node receives input features ($x_1, x_2, \dots, x_n$) either from the raw dataset or from a previous layer of neurons.
  - **Weight Multiplication ($w_i$)** : Each input is multiplied by its corresponding weight ($w_1, w_2, \dots, w_n$). Weights scale the importance of individual inputs.
  - **Summation & Bias Offset ($z$)** : The weighted inputs are summed together, and a bias ($b$) is added to shift the activation threshold.
              $$z = \sum_{i=1}^{n} (x_i w_i) + b$$
  - **Activation Function ($f(z)$)** : The net input $z$ is passed through a non-linear activation function (like ReLU, Sigmoid, or Tanh) to determine if and how strongly the neuron should "fire."
              $$a = f(z)$$

  ## Layers in Neural Network
  There are 3 different layers in a neural network
  - **Input Layer**: This is where the network receives the raw data (e.g., the pixels of an image, text tokens, or numerical values in a spreadsheet).
  - **Hidden Layer**: These sit between the input and output layers. This is where the "deep" in deep learning comes from. The network uses these layers to extract abstract features (e.g., first detecting edges, then shapes, then an entire face).
  - **Output Layer**: The final layer that produces the network's prediction or conclusion (e.g., classifying an image as a "cat" or predicting a stock price).

  ## How Neural Network Learns
  A neural network starts out knowing nothing; its initial weights are randomized, so its first predictions are just wild guesses. It learns through a continuous two-step loop:
  - **Forward Propagation**: Data passes through the network from the input layer to the output layer to generate a prediction.
  - **Loss Function Evaluation**: The network compares its prediction against the actual correct answer (the ground truth) using a mathematical formula to calculate the "error" or loss.

    Example of Loss Function: Binary Cross Entropy, Sparse Categorical Cross Entropy
  - **Backpropagation**: The network passes the error backward through the layers. Using an optimization algorithm (like Gradient Descent), it calculates how much each weight contributed to the mistake and adjusts them slightly to minimize the error next time.

    Example of optimizer algorithm: Stochastic Gradient Descent


  Through millions of repetitions of this loop, the network fine-tunes its weights until it can accurately predict outcomes on completely unseen data.
  
  **Note**: Watch Edureka Video(of June-20-2026) for details of Gradient Descent

  ## Example of implementing neural network with 1 hidden layer
  [Code Sample](https://github.com/varugheseben/edurek-data_science/blob/main/Deep%20Learning/Neural%20Network/Examples/neural_network_1.ipynb)
  ```
# Example of doing prediction using a neural network with one hidden layer
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = Sequential()
model.add(Dense(
    1,
    activation='sigmoid', # For categorical dependent variable we use sigmoid as the activation function
    input_shape=(1,) # Because our input has only one column
))

# Optimizer is sgd(Stochastic Gradient Descent), because we have continuous data in independent variable X
# Loss Function is 'binary_crossentropy' because we have two categorical data in dependent variable and activation is sigmoid
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=50, verbose=1)
for i in range(1,7):
  prediction = model.predict(np.array([[2]]))
  print(f"\nPredicted probability for {i}: {prediction[0][0]:.4f}")
```



