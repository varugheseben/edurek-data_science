# TensorFlow
   It is an open source library created by Google Brian team for machine learning and atrificial intelligence. It is particularly known for its capabilities in 
training and running deep neural networks.

   At its core, Tensor flow provides a flexible framework for defining and executing mathematical functions involving multi-dimensional data arrays, which are 
called tensors

# Foundational Elements of TensorFlow
 - **Tensors** : In mathematics and computer science, a tensor is a generalization of vectors and matrices to potentially higher dimensions.
     - A 0-dimensional tensor is a scalar (a single number).
     - A 1-dimensional tensor is a vector (a list of numbers).
     - A 2-dimensional tensor is a matrix (a grid of numbers).
     - A 3-dimensional or higher tensor represents data like color images (height, width, color channels) or video. 
 - **Graphs/Dataflow**: TensorFlow conceptualizes computations as a directed graph where nodes represent mathematical operations,
   and the edges represent the tensors that flow between them.
   
   Example: If we have computational statement like sum = a + b,
    - \+ and = are a nodes
    - sum, a, b are tensors

# Advantage of TensorFlow
  TensorFlow is one of the most widely used libraries in the data science and AI community due to several distinct advantages:
   - **Hardware Acceleration** : Deep learning requires massive amounts of parallel matrix multiplication. TensorFlow can seamlessly run computations on standard Central Processing Units (CPUs), Graphics Processing Units (GPUs), and Google's custom-built Tensor Processing Units (TPUs) without requiring you to rewrite your core code.
   - **High Level and Low Level API** :
     - **Keras Integration** : TensorFlow uses Keras as its official high-level API. This allows developers to build, train, and evaluate complex deep learning models using just a few lines of highly readable Python code.
     - **Fine-Grained Control** : For researchers and advanced developers, TensorFlow offers low-level operations to write custom layers, loss functions, and optimization routines from scratch.
   - **Comprehensive Ecosystem** : TensorFlow isn't just a library; it is an entire ecosystem designed to take models from research to production. Different
ecosystems are
      - **TensorFlow Extended (TFX)** : An end-to-end platform for deploying production machine learning pipelines.
      - **TensorFlow Lite (TF Lite)** : A lightweight solution for deploying models on mobile and edge devices (iOS, Android, IoT).
      - **TensorFlow.js** : A library for training and deploying models entirely in the browser or on Node.js.
      - **TensorBoard** : A visualization toolkit used to track metrics like loss and accuracy, visualize model graphs, and profile resource consumption

# Analogy to understand the usage of Tensorflow
  Lets say a teacher is teaching a student, so below will be the different events can happen
   - Teacher can give multiple examples, which will be inputting data
   - Student tries to learn, which will be model training
   - Student makes mistakes, which will be error generation
   - Teacher helps to correct student's mistakes, which will be back propagation
   - Student improves, which will be better prediction

   So we can say tensorflow as framework which can perform all above events. Basically its a framework, that has libraries to help system learn from data by itself 
and improve by itself and generate better prediction results.

# Use cases
  Different areas where TensorFlow is used are
   - **Computer Vision** : Image recognition, object detection, and autonomous driving systems.
   - **Natural Language Processing (NLP)** : Sentiment analysis, machine translation, and text generation.
   - **Time-Series Analysis** : Stock market tracking, weather forecasting, and predictive maintenance.
   - **Recommendation Systems** : Powering the algorithms behind product or video recommendations on e-commerce and streaming platforms.

# Lab
  - [Auto Train And Predict Numbers]()
  - [Predict a Number]()
  - [Image Extraction]()
