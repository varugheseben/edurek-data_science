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
  - [Auto Train And Predict Numbers](https://github.com/varugheseben/edurek-data_science/blob/main/Deep%20Learning/TensorFlow/auto_train_and_predict_number.ipynb)
    This program is a complete, classic implementation of **Computer Vision** and **Deep Learning**. At a high level, it trains an artificial neural network to read handwritten digits ($0$ through $9$) using the famous **MNIST dataset**, evaluates its performance on unseen test data, and provides an interactive interface for user-driven predictions.

    ---

    ## 📋 Table of Contents
      1. [Data Preparation (The Input)](#1-data-preparation-the-input)
      2. [Building the Brain (The Architecture)](#2-building-the-brain-the-architecture)
      3. [Compilation & Training (The Learning Phase)](#3-compilation--training-the-learning-phase)
      4. [Testing & User Verification (The Output)](#4-testing--user-verification-the-output)

    ---

## 1. Data Preparation (The Input)

The script begins by fetching the MNIST dataset, which contains $70,000$ pre-labeled grayscale images of handwritten digits, each sized $28 \times 28$ pixels.

* **Data Splitting:** It automatically partitions the data into two distinct sets:
  * **Training data (`X_train`, `y_train`):** $60,000$ images used to teach the model.
  * **Testing data (`X_test`, `y_test`):** $10,000$ images kept hidden away to act as a final exam.
* **Feature vs. Label Separation:** * `X` variables represent the **input features** (the matrix of pixel data the model looks at).
  * `y` variables represent the **target labels** (the correct ground-truth numerical answers, $0\text{--}9$).
* **Normalization:** Raw pixel values range from `0` (pure black) to `255` (pure white). The line `X_train / 255.0` scales these down to floating-point decimals between `0.0` and `1.0`. Because neural networks rely heavily on gradient descent and matrix calculus, smaller normalized inputs keep the internal math stable and speed up training significantly.

---

## 2. Building the Brain (The Architecture)

Using Keras's `Sequential` API, the script builds a 4-layered neural network stacked linearly like pancakes:


  - [Predict a Number]()
  - [Image Extraction](https://github.com/varugheseben/edurek-data_science/blob/main/Deep%20Learning/TensorFlow/detect_and_generate_numbers.ipynb)
