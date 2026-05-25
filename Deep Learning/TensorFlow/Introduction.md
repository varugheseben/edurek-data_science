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
  - [**Auto Train And Predict Numbers**](https://github.com/varugheseben/edurek-data_science/blob/main/Deep%20Learning/TensorFlow/auto_train_and_predict_number.ipynb)

    This program is a complete, classic implementation of **Computer Vision** and **Deep Learning**. At a high level, it trains an artificial neural network to read handwritten digits ($0$ through $9$) using the famous **MNIST dataset**, evaluates its performance on unseen test data, and provides an interactive interface for user-driven predictions.

    ---

    ## 📋 Table of Contents
      - [Data Preparation (The Input)](#1-data-preparation-the-input)
      - [Building the Brain (The Architecture)](#2-building-the-brain-the-architecture)
      - [Compilation & Training (The Learning Phase)](#3-compilation--training-the-learning-phase)
      - [Testing & User Verification (The Output)](#4-testing--user-verification-the-output)

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

       - Flatten &rarr; Converts 2D grid into a single line of 784 numbers.
       - Dense (ReLU) &rarr; Hidden layer (128 neurons) that looks for patterns/edges.
       - Dropout &rarr; Randomly shuts off 20% of neurons to prevent memorization (overfitting).
       - Dense (Softmax) &rarr; Output layer (10 neurons). Gives a probability score for numbers 0-9.

       ### Key Components Explained:
       * **`layers.Flatten`:** Neural networks require standard, flat arrays as inputs rather than 2D matrices. This flattens the $28 \times 28$ pixel grid into a single row of $784$ numbers.
       * **`layers.Dense`:** A fully connected layer where every input neuron links to every output neuron. It calculates weighted sums to recognize high-level patterns.
       * **`Activation='relu'`:** Rectified Linear Unit ($f(x) = \max(0, x)$). This introduces non-linearity, allowing the model to learn complex relationships instead of just basic linear combinations.
       * **`layers.Dropout(0.2)`:** A regularization technique. By turning off a random subset of neurons during training, it forces the network to find multiple paths to the correct answer rather than relying too heavily on specific pixels.

    ---

    ## 3. Compilation & Training (The Learning Phase)

      Before training begins, `model.compile()` equips the model with its underlying mathematical strategies:
      * **Adam Optimizer:** The network's internal navigator. It automatically calculates how to tweak internal weights and biases based on errors to minimize mistakes.
      * **Sparse Categorical Crossentropy Loss:** The grading rubric. It calculates exactly *how wrong* a guess was (e.g., punishing the model more heavily if it confidently mistakes a `1` for an `8` vs. a `7`).
      * **Metrics (`['accuracy']`):** Monitors the percentage of correctly classified images during training.

      When `model.fit()` runs, the entire dataset passes through the network **5 times (epochs)**. With each epoch, the loss drops and accuracy climbs as the network learns the defining characteristics of each digit.

    ---

    ## 4. Testing & User Verification (The Output)

    * **`model.evaluate()`:** The script runs the $10,000$ isolated test images through the finalized model. It outputs a final test accuracy (typically around **$97\text{--}98\%$**), proving whether the model can accurately generalize its learning to handwriting it has never seen before.
    * **Interactive Prediction Pipeline:**
    * 1. The script prompts the user to input an index number (any position from `0` to `9999`).
      2. It isolates that exact image from `X_test` and feeds it to `model.predict()`.
      3. `np.argmax(prediction)` grabs the output neuron with the highest probability score and prints it as the `Predicted Digit`.
      4. Finally, it displays the `Actual Digit` from `y_test` to verify whether the AI succeeded or failed.

  - [Predict a Number](https://github.com/varugheseben/edurek-data_science/blob/main/Deep%20Learning/TensorFlow/predict_a_number.ipynb)

     This Python program is an intelligent **Handwritten Digit Recognition System**. It automatically trains a Convolutional Neural Network (CNN) on the standard MNIST dataset, smart-preprocesses custom user images to make them compatible with the network, and runs a loop to test its predictions across 10 sample image files (digit_0.jpg through digit_9.jpg).

     What sets this script apart from basic implementations is its robust preprocessing—it dynamically detects whether your user image has a dark or light background and adjusts the image padding and colors accordingly.

     **Core Components Breakdown**
       - **Dynamic Background Detection (detect_image_background)**

           The MNIST dataset is strictly composed of white numbers on pure black backgrounds. If a user uploads a photo of a black number on white paper, the model will fail.
            - This function converts the user's image to grayscale and shrinks it down to a small $50 \times 50$ grid (which removes distracting pixels and compression noise).
            - It finds the most common pixel value (the dominant color).
            - If the dominant color is very bright (value $> 220$), it returns 1 (indicating a white background). If it's dark (value $< 35$), it returns 0.
         
       - **Smart Preprocessing (predict_digit)**

           Before passing your custom image file into the network, this function morphs it into an MNIST-identical format

            - **Aspect Ratio Preservation** :
                 If an image is tall or wide, resizing it directly to a square will warp the digit. The script calculates the difference and pads the shorter side with a white border (constant_values=255) to make a perfect square first.
            - **Auto Color Inversion** :
                 'detect_image_background' reported that your image has a white background, the code mathematically subtracts the image from 1.0 (1.0 - img_normalized). This seamlessly flips white paper to black, and dark ink to white.
            - **Noise Filtering** :
                 Any residual grayish background noise below 0.15 intensity is clamped to pure 0.0 (black).
            - **Visual Matplotlib Plot** :
                 It pops up a quick comparison window showing the original vs. what the network actually sees to help you debug layout issues.

       - **Training with Spatial Data Augmentation (main)**

           When operation_mode == 1, the program trains a fresh model from scratch:

            - **Dataset Augmentation** : To make the network more resilient to off-center handwriting, it manually creates two copies of the training data—one shifted 2 pixels to the left, and one shifted 2 pixels to the right—using clean zero-padding (np.pad). This triples your training dataset from 60,000 to 180,000 images.
            - **CNN Architecture** : It compiles a robust Sequential model using two Convolutional (Conv2D) and Pooling (MaxPooling2D) layer pairs for high-accuracy feature extraction, ending with a 10-node Softmax layer to calculate digit probability distributions.
       - **Continuous Terminal Testing & Feedback**

           Once trained for 2 epochs, the script loops through numbers 0 to 9:

            - It expects to find files located at data/digit_0.jpg through data/digit_9.jpg.
            - It runs the image through the pipeline and prints the results in color directly into your terminal using ANSI escape codes: **Green** if the AI accurately guessed your file, and **Red** if the prediction failed.

  - [Image Extraction](https://github.com/varugheseben/edurek-data_science/blob/main/Deep%20Learning/TensorFlow/detect_and_generate_numbers.ipynb)

     This Python script uses the **OpenCV** (cv2) library to automatically find, isolate, and slice out individual numbers from a larger composite image (like a grid of handwritten digits) and save them as separate image files.

     It specifically expects a layout containing exactly **10 digits arranged in two rows of 5** (digits 0–4 on top, 5–9 on bottom).

     Here is the step-by-step breakdown of how the program accomplishes this:
       - **Image Loading and Grayscale Conversion**
   
                 img = cv2.imread(image_path)
                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

           The program reads the image from sample_data/images/Numbers.jpg and converts it from standard color (BGR) into grayscale. Computer vision algorithms process single-channel grayscale images much faster because they only have to evaluate brightness rather than complex color data.

       - **Inverted Thresholding (Binarization)**

                 _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

           This line converts the gray image into a pure black-and-white binary image.
            - The cv2.THRESH_BINARY_INV flag is critical here: it inverts the colors.
            - Assuming your original document features dark text on a light background, this operation flips it so the digits/boxes become pure white pixels (255) and the background becomes pure black (0). OpenCV's contour-finding algorithms are specifically designed to look for white objects against a black background.
         
       - **Finding and Filtering Contours (Object Detection)**

                 contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

           The script scans the binary image to find the boundaries or outlines (called contours) of all isolated white shapes.

                 for cnt in contours:
                   x, y, w, h = cv2.boundingRect(cnt)
                   area = w * h
                   if area > 1000 and w > 50 and h > 50:
                       digit_boxes.append((x, y, w, h))

           Images often contain tiny specs of background noise, dust, or smudges. To prevent the program from saving these artifacts as numbers, it calculates a bounding box around every shape and uses an if statement to filter them. It only keeps shapes that have an area larger than 1,000 pixels and a width/height greater than 50 pixels.

       - **Smart Row and Column Sorting**

           When OpenCV finds contours, it extracts them in a completely random order based on how they sit in memory. If you saved them immediately, your digits would be totally jumbled up. The code fixes this with a clever sorting pipeline:

                 # 1. Sort everything from top to bottom based on the Y-axis
                 digit_boxes.sort(key=lambda box: box[1])

                 # 2. Split the boxes into a top row of 5 and a bottom row of 5, 
                 # then sort each row individually from left to right using the X-axis
                 top_row = sorted(digit_boxes[:5], key=lambda box: box[0])
                 bottom_row = sorted(digit_boxes[5:], key=lambda box: box[0])
                 final_sorted_boxes = top_row + bottom_row

           By doing this, the script guarantees that the images correspond perfectly to their natural reading order (Index 0 will be the top-left item, Index 4 will be the top-right item, Index 5 will be the bottom-left item, etc.).

       - **Cropping and Saving**

                 for idx, (x, y, w, h) in enumerate(final_sorted_boxes):
                    cropped = img[y:y+h, x:x+w]
                    filename = f"sample_data/images/digit_{idx}.jpg"
                    cv2.imwrite(filename, cropped)

           Finally, the script loops through the correctly ordered boxes. It uses NumPy slicing (img[y:y+h, x:x+w]) to crop the region of interest out of the original color image and writes it to your disk. You will end up with 10 individual image files named digit_0.jpg through digit_9.jpg.

