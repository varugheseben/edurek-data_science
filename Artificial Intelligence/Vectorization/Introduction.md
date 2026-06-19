# Vectorization
In computing and data science, vectorization generally refers to the process of turning an operation or an object into a vector (a list of numbers) so that it can be processed efficiently by a computer or 
machine learning model.

Depending on your context, it usually means one of two things:
 - Vectorization in CPU/Array Programming (Speeding up Code)
   
   In data science and programming (like using Python's NumPy or Pandas), vectorization means applying an operation to an entire array or dataset at once, rather than looping through individual elements one by one.

   Modern CPUs and GPUs use **SIMD (Single Instruction, Multiple Data)** to perform the same mathematical operation on multiple data points simultaneously at the hardware level.
    - **Without Vectorization (Using a loop)**: You take the first number, add 2. Take the second number, add 2. Repeat 10,000 times.
    - **With Vectorization**: You tell the computer to add 2 to the entire array instantly. It runs significantly faster because it eliminates the overhead of Python loops.
  
 - Vectorization in Natural Language Processing (Text to Numbers)

   In Natural Language Processing (NLP), algorithms cannot natively read or understand words, sentences, or paragraphs. Text vectorization is the process of converting human language into numerical vectors that
   machine learning models can process.

   Common techniques include:
    - **Bag of Words / Count Vectorizer**: Counting how many times each word appears in a document.
    - **TF-IDF (Term Frequency-Inverse Document Frequency)**: Adding weightage to words based on how important they are to a specific document relative to a whole collection of text.
    - **Word Embeddings (e.g., Word2Vec, BERT)**: Mapping words into a continuous vector space where words with similar meanings (like "king" and "queen") are placed close together.

 ## Lab
  - [Vectorization Example-1](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Vectorization/vectorization_example_1.ipynb)
  - [Vectorization Example-2]()
  - 
