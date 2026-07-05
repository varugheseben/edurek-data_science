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
