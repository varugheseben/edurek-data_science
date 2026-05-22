# Deep Learning
   Its a sub field of machine learning and is inspired by the structure and function of human brain.

   While traditional machine learning relies on algorithms that require human engineers to manually pick out relevant features from data, 
   deep learning algorithms can automatically learn features and patterns directly from raw data (like images, audio, or text).

   At the heart of deep learning are Artificial Neural Networks (ANNs). These networks are built out of layers of interconnected nodes, 
   called "neurons," that mimic the way biological neurons fire in our brains.

   The "deep" in deep learning refers to the depth of the layers in the network. 
   A standard machine learning model might only have 1 or 2 layers of data processing, 
   but a deep learning model typically contains dozens, hundreds, or even thousands of hidden layers.

   Every layer in a deep neural network acts as a filter for information, moving from abstract to specific:
   - Input Layer: Receives raw data (e.g., an image of a car).
   - Hidden Layers: The first hidden layer might detect basic edges and lines. 
     The next layer combines those lines to identify shapes (wheels, windows). 
     A deeper layer recognizes complex combinations (the grill, the headlights).
   - Output Layer: Makes the final prediction or classification (e.g., "98% probability this is a sedan"). 

## Difference between traditional machine learning and deep learning
Lets take an example of building a system that detects an image is dog or cat

|Feature|Traditional Machine Learning|Deep Learning|
|-------|----------------------------|-------------|
|Human Intervention|High. An engineer must manually code rules or "extract features" (e.g., measuring ear shapes, tail lengths) before feeding the data into the model.|Low. You feed raw images into the network, and it figures out which features (whiskers, snout shape) are important on its own.|
|Data Requirements|Can perform well with smaller datasets (hundreds or thousands of examples).|Requires massive amounts of data (millions of examples) to reach high accuracy.|
|Hardware|Runs fine on standard computer processors (CPUs).|Requires massive computational power, usually heavily relying on GPUs (Graphics Processing Units).|

 - In Machine learning we need to first convert images into features and then train the model and then do the prediction. The process of converting images into feature is called **feature engineering**. That means there will be human step involved to add logic for identifying the features like measuring ear shapes, tail length, etc. And once the data for feature is identified it will be used for training the model then it could predict whether image is a dog or cat. We can use machine learning when data is small and structured.
 - In the case of Deep learning, it uses neural networks to identify features. So it identifies the features automatically. These actions will be done in different layers like first level it will identify features of eye, then next level it will identfy fur texture, then next level it identfies another feature. And this identification is done automatically as it uses Artificial Neural Networks(ANN). So no manual intervention is needed in case of deep learning. Also there can be multiple level of learning based on the complexity of the data. More level learning will need more computation capacity. We can use Deep learning when data is complex and unstructured.

    
