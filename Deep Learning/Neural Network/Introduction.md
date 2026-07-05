# Neural Network
  At its core, a **Neural Network** (or Artificial Neural Network) is a method in artificial intelligence that teaches computers to process data in a way that is inspired by the human brain.

  It is a key building block of Deep Learning, which powers many of today's smart technologies, from facial recognition to conversational AI.

  ## The core component: The Neuron(Perceptron)
  Just as our brains are made of interconnected biological neurons, an artificial neural network is made of digital processors called nodes or neurons.
  Each neuron takes in data, processes it, and passes it along. A single neuron consists of three main mathematical operations:
  - **Input($x$)**: The incoming data features.
  - **Weights ($w$) and Biases ($b$)**: Crucial coefficients that the network adjusts during training. Weights determine how much influence a specific input has, while the bias shifts the overall activation.
  - **Activation Function**: A mathematical formula (like ReLU or Sigmoid) that decides whether—and to what extent—the neuron should pass its signal to the next layer. It introduces non-linearity, allowing the network to learn complex patterns.

      $$y = \text{Activation}\left(\sum (x_i \cdot w_i) + b\right)$$

  ## Layers in Neural Network
  There are 3 different layers in a neural network
  - **Input Layer**: This is where the network receives the raw data (e.g., the pixels of an image, text tokens, or numerical values in a spreadsheet).
  - **Hidden Layer**: These sit between the input and output layers. This is where the "deep" in deep learning comes from. The network uses these layers to extract abstract features (e.g., first detecting edges, then shapes, then an entire face).
  - **Output Layer**: The final layer that produces the network's prediction or conclusion (e.g., classifying an image as a "cat" or predicting a stock price).

  ## Neural Network Learns
  A neural network starts out knowing nothing; its initial weights are randomized, so its first predictions are just wild guesses. It learns through a continuous two-step loop:
  - **Forward Propagation**: Data passes through the network from the input layer to the output layer to generate a prediction.
  - **Loss Function Evaluation**: The network compares its prediction against the actual correct answer (the ground truth) using a mathematical formula to calculate the "error" or loss.
  - **Backpropagation**: The network passes the error backward through the layers. Using an optimization algorithm (like Gradient Descent), it calculates how much each weight contributed to the mistake and adjusts them slightly to minimize the error next time.

    Through millions of repetitions of this loop, the network fine-tunes its weights until it can accurately predict outcomes on completely unseen data.
