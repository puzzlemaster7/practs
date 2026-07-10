# Deep Learning Practicals Viva Guide

This file contains detailed viva answers for the practicals in this workspace.
Each answer is written in simple exam-friendly language.
Use it for quick revision before the viva.

## 1. Common Viva Questions

### 1) What is TensorFlow and why is it used?
TensorFlow is an open-source library for numerical computing and machine learning.
It helps us build, train, and deploy deep learning models efficiently.
It supports tensors, automatic differentiation, GPU acceleration, and high-level APIs like `tf.keras`.
In practicals, it is used because it makes model building and training much easier.

### 2) What is a tensor?
A tensor is a multidimensional array used to store data in deep learning.
A scalar is a 0D tensor, a vector is 1D, a matrix is 2D, and higher dimensions are also possible.
Images, sequences, and batches are all represented as tensors.
TensorFlow uses tensors as its basic data structure for computation.

### 3) What is the difference between tensor, NumPy array, and matrix?
A NumPy array is a general-purpose numerical array used in Python.
A tensor is a similar structure, but it is designed for deep learning workflows.
A matrix is a 2D tensor, while tensors can have any number of dimensions.
Tensors also support GPU operations and automatic gradient computation.

### 4) What is gradient descent?
Gradient descent is an optimization method used to reduce the loss of a model.
It updates model parameters in the direction that reduces error.
The learning rate controls how big each update step is.
The goal is to find weights and biases that give the minimum loss.

### 5) What is a loss function?
A loss function measures how far the model output is from the actual target.
If the loss is high, the model is making larger mistakes.
During training, the optimizer tries to minimize this loss.
Examples are MSE for regression and cross-entropy for classification.

### 6) What is the difference between training, validation, and testing?
Training data is used to fit the model parameters.
Validation data is used to tune hyperparameters and check performance during training.
Test data is used only at the end to measure final performance.
This separation helps us judge whether the model generalizes well.

### 7) What is overfitting?
Overfitting happens when a model learns the training data too well, including noise.
Such a model performs very well on training data but poorly on new data.
It usually happens when the model is too complex or trained for too long.
Regularization, early stopping, and more data can reduce overfitting.

### 8) What is underfitting?
Underfitting happens when the model is too simple to capture the pattern in the data.
It performs poorly on both training and test data.
This means the model has not learned enough from the dataset.
Increasing model capacity or training time can help.

## 2. Practical 1: TensorFlow Basics and XOR

### 1) What is a tensor in TensorFlow?
In TensorFlow, a tensor is the main object used to hold data.
It can represent numbers, vectors, matrices, images, or batches of data.
Each tensor has a shape and a data type.
All model inputs, outputs, and parameters are handled as tensors.

### 2) Why do we use reshaping, slicing, and indexing?
Reshaping changes the dimensions of a tensor without changing its values.
Slicing and indexing let us pick specific elements or sub-parts from a tensor.
These operations are useful when preparing data for models.
They also help us inspect data and work with specific rows, columns, or regions.

### 3) What is matrix multiplication and where is it used?
Matrix multiplication combines two matrices according to linear algebra rules.
It is different from element-wise multiplication because each output value is a sum of products.
In neural networks, matrix multiplication is used in dense layers.
It is one of the most important operations in deep learning.

### 4) What are eigenvalues and eigenvectors?
An eigenvector is a special vector that does not change direction when a matrix acts on it.
The corresponding eigenvalue tells how much the vector is stretched or shrunk.
They are important in linear algebra and dimensionality reduction.
They also appear in PCA and some numerical methods.

### 5) Why can XOR not be solved by a single perceptron?
XOR is not linearly separable.
This means no single straight line can divide the true outputs into two classes correctly.
A single perceptron can only learn linear boundaries.
So, XOR needs at least one hidden layer to solve it.

### 6) How does a neural network solve XOR?
A neural network with a hidden layer learns a nonlinear decision boundary.
The hidden neurons transform the input into a new representation.
In that transformed space, XOR becomes easier to separate.
This is why multilayer networks can solve problems that single neurons cannot.

## 3. Practical 2: Linear Regression

### 1) What is linear regression?
Linear regression is a supervised learning method used to predict continuous values.
It assumes there is a linear relationship between input and output.
The model learns a line that best fits the data.
It is commonly used for prediction tasks like price estimation.

### 2) What is the equation of simple linear regression?
The simple linear regression equation is `y = wx + b`.
Here, `w` is the slope and `b` is the intercept.
The model learns these values from data during training.
After training, it can predict output for new input values.

### 3) Why is MSE used as the loss?
Mean squared error measures the average squared difference between prediction and actual value.
Squaring makes larger errors count more.
It is differentiable, so it works well with gradient descent.
For regression problems, MSE is one of the most common loss functions.

### 4) What does the loss curve tell us?
The loss curve shows how the error changes during training.
If the curve goes down, the model is learning.
If it becomes flat, the model may have converged.
If it rises or fluctuates too much, the learning rate may be too high.

### 5) Why do we plot the fitted line?
The fitted line shows how well the model matches the data.
It helps us visually verify that the regression learned the trend.
For a good linear regression model, the line should pass close to the points.
It is also useful for explaining the model in viva and reports.

## 4. Practical 3: Binary and Multiclass Classification

### 1) What is binary classification?
Binary classification means predicting one of two classes.
Examples are spam/not spam or pass/fail.
The output layer usually has one neuron with sigmoid activation.
The model gives a probability between 0 and 1.

### 2) What is multiclass classification?
Multiclass classification means choosing one class from more than two classes.
Examples are digit recognition from 0 to 9 or classifying different objects.
The output layer usually has one neuron per class.
Softmax converts the outputs into class probabilities.

### 3) Why is sigmoid used for binary classification?
Sigmoid outputs a value between 0 and 1.
This makes it suitable for probability-based binary decisions.
We can use a threshold like 0.5 to decide the class.
It works well with binary cross-entropy loss.

### 4) Why is softmax used for multiclass classification?
Softmax converts raw scores into probabilities that sum to 1.
This allows the model to compare all classes together.
The class with the highest probability is selected as the prediction.
It is usually paired with categorical cross-entropy loss.

### 5) What is the role of hidden layers in a feed-forward network?
Hidden layers learn intermediate features from the input data.
They let the network model nonlinear relationships.
Without hidden layers, the model would behave like a simple linear classifier.
More hidden layers can improve learning, but they can also increase complexity.

## 5. Practical 4: Image Segmentation

### 1) What is image segmentation?
Image segmentation is the process of labeling each pixel in an image.
Instead of giving one class to the whole image, the model predicts regions.
This helps identify object boundaries and shapes accurately.
It is used in medical imaging, self-driving cars, and object detection pipelines.

### 2) How is segmentation different from classification?
Classification gives one label for the entire image.
Segmentation gives a label for every pixel or region in the image.
So segmentation is more detailed and more difficult.
It tells us not just what is in the image, but where it is.

### 3) What is U-Net?
U-Net is a CNN architecture designed especially for image segmentation.
It has an encoder path that compresses the image and a decoder path that reconstructs it.
The skip connections help recover fine details from earlier layers.
It is popular because it works well even with limited data.

### 4) Why are skip connections used in U-Net?
Skip connections copy feature maps from the encoder to the decoder.
This helps the decoder recover spatial detail that may be lost during downsampling.
It improves boundary accuracy in segmentation masks.
Without skip connections, the output can become blurry or less precise.

### 5) What is a mask?
A mask is the output image in segmentation.
Each pixel in the mask shows whether that pixel belongs to the object or background.
For binary segmentation, the mask usually contains 0 and 1 values.
It is the target that the model learns to predict.

## 6. Practical 5: Image Captioning with LSTM

### 1) What is image captioning?
Image captioning is the task of generating a textual description for an image.
It combines computer vision and natural language processing.
The model must understand visual content and turn it into words.
It is a sequence generation problem based on image input.

### 2) Why do we use CNN and LSTM together?
The CNN extracts features from the image.
The LSTM generates a word sequence based on those features.
Together, they form an encoder-decoder architecture.
This is useful because images are visual data and captions are sequential text.

### 3) What is teacher forcing?
Teacher forcing is a training method for sequence models.
Instead of using the model's previous prediction, the true previous word is fed as input.
This makes training faster and more stable.
It helps the model learn the correct next-word pattern.

### 4) What is greedy decoding?
Greedy decoding means selecting the most probable next word at each step.
It is simple and fast.
However, it may not always give the best full sentence.
Beam search is a more advanced alternative.

### 5) Why are special tokens like `<start>` and `<end>` used?
`<start>` tells the model where the caption begins.
`<end>` tells the model where the caption should stop.
These tokens help the model learn sentence boundaries.
They are very important in sequence generation tasks.

## 7. Practical 6 and 8: Autoencoders

### 1) What is an autoencoder?
An autoencoder is a neural network that learns to copy its input to its output.
It does this by first compressing the input and then reconstructing it.
The compressed part is called the latent representation.
It is often used for dimensionality reduction and feature learning.

### 2) What is the difference between encoder and decoder?
The encoder compresses the input into a smaller representation.
The decoder reconstructs the original input from that representation.
Together they try to minimize reconstruction error.
This structure forces the model to learn useful compact features.

### 3) Why is an autoencoder unsupervised?
An autoencoder does not need separate label data.
The target output is the same as the input itself.
So the model learns patterns directly from the data.
That is why it is considered unsupervised learning.

### 4) What is the latent space?
Latent space is the compressed internal representation learned by the encoder.
It contains the most important features of the input.
If the latent space is too small, information may be lost.
If it is too large, the model may simply memorize the input.

### 5) What is reconstruction loss?
Reconstruction loss measures the difference between the original input and the reconstructed output.
Common choices are MSE or binary cross-entropy.
The autoencoder tries to reduce this loss during training.
Good reconstruction means the encoded features are useful.

### 6) What are autoencoders used for?
Autoencoders are used for compression, denoising, anomaly detection, and feature extraction.
They are also used to learn low-dimensional embeddings.
In image tasks, they can reconstruct images from compressed features.
They are useful when labels are not available.

## 8. Practical 7: CNN vs RNN for Character Recognition

### 1) What is the difference between CNN and RNN?
CNNs are designed for spatial data like images.
They use convolution filters to learn local patterns such as edges and shapes.
RNNs are designed for sequential data, where order matters.
In this practical, both are compared on the same digit dataset.

### 2) Why is CNN usually better for images?
CNNs can capture spatial relationships between neighboring pixels.
They share weights and are computationally efficient.
They are naturally suited to 2D image structures.
That is why CNNs usually perform better than RNNs on image recognition tasks.

### 3) How can an RNN process an image?
An image can be treated as a sequence of rows or columns.
Each row is fed as one time step into the RNN.
This allows the model to learn patterns in order, but it is not the most natural representation.
It is mainly used here for comparison purposes.

### 4) What is a GRU?
A GRU, or Gated Recurrent Unit, is a type of recurrent neural network cell.
It helps the model remember useful information over time.
It is simpler than LSTM and usually faster to train.
It is often used for sequence tasks when a lighter architecture is enough.

### 5) Why compare CNN and RNN on the same dataset?
The comparison shows which architecture is more suitable for image-like data.
It helps us understand how model design affects performance.
CNNs usually capture spatial patterns better than RNNs.
This practical makes that difference visible through accuracy results.

## 9. Practical 9: RNN for Stock-Price-Like Sequence Prediction

### 1) What is sequence prediction?
Sequence prediction means using earlier values to predict the next value.
The order of data is important, unlike in ordinary tabular tasks.
Examples include stock prices, weather, and sensor data.
This makes recurrent networks a natural choice.

### 2) Why is LSTM used for time series?
LSTMs are good at remembering patterns over long sequences.
They reduce the vanishing gradient problem found in simple RNNs.
This makes them strong for time-dependent data.
They are commonly used in forecasting and sequence modeling.

### 3) What is a lookback window?
A lookback window is the number of previous timesteps used as input.
For example, the model may use the last 10 values to predict the next one.
It converts a long time series into supervised learning samples.
The choice of window size affects prediction quality.

### 4) Why is stock prediction difficult?
Stock data is noisy, nonlinear, and influenced by many external factors.
The pattern changes over time, so the model cannot rely on a fixed rule.
Even good models may not predict it accurately in real markets.
That is why many practicals use synthetic or simplified stock-like data.

### 5) What is the vanishing gradient problem?
In long sequences, gradients can become very small during backpropagation.
This makes it difficult for the network to learn long-term dependencies.
Simple RNNs often suffer from this problem.
LSTM and GRU were designed to handle it better.

## 10. Practical 10: GAN

### 1) What is a GAN?
A GAN is a Generative Adversarial Network.
It has two models: a generator and a discriminator.
The generator creates fake samples, and the discriminator tries to detect them.
They train together in an adversarial game.

### 2) What is the role of the generator?
The generator takes random noise as input.
It learns to produce realistic-looking fake data.
Its goal is to fool the discriminator into thinking the fake data is real.
As training improves, the generator becomes better at producing convincing outputs.

### 3) What is the role of the discriminator?
The discriminator checks whether an input sample is real or fake.
It learns to classify true data apart from generated data.
Its feedback helps the generator improve.
So the discriminator is like a critic in the GAN setup.

### 4) Why are GANs called adversarial?
They are called adversarial because the two networks compete against each other.
The generator tries to win by making realistic samples.
The discriminator tries to win by spotting fakes.
This competition drives both networks to improve.

### 5) What is mode collapse?
Mode collapse happens when the generator produces very similar outputs repeatedly.
This means it is not learning the full diversity of the data.
It is a common problem in GAN training.
Careful tuning and better architectures can reduce it.

## 11. Important Comparison Questions

### 1) CNN vs RNN
CNNs are best for image and spatial data.
RNNs are best for sequential or time-dependent data.
CNNs use convolution filters, while RNNs use recurrent connections.
For images, CNN usually performs better than RNN.

### 2) LSTM vs GRU
Both are improved versions of RNNs.
LSTM has more gates and is usually more expressive.
GRU is simpler and faster with fewer parameters.
Both help handle long-term dependencies, but LSTM is often used when more memory control is needed.

### 3) Autoencoder vs GAN
An autoencoder learns to reconstruct its input.
A GAN learns to generate new realistic data from random noise.
Autoencoders are easier to train and are useful for compression.
GANs can generate sharper samples but are harder to train.

### 4) Binary classification vs multiclass classification
Binary classification has two possible classes.
Multiclass classification has more than two classes.
Binary classification usually uses sigmoid output.
Multiclass classification usually uses softmax output.

### 5) Segmentation vs classification
Classification gives one label for the whole image.
Segmentation gives a label for each pixel.
Segmentation is more detailed and useful when object location matters.
It is also more challenging than classification.

## 12. Quick Final Revision Points

### 1) What should you say if asked about the dataset?
Say whether the dataset is synthetic, offline, or from `sklearn`.
Mention why that dataset was chosen.
Explain the input shape and target shape.
Also mention whether preprocessing or normalization was applied.

### 2) What should you say if asked about model improvement?
You can mention increasing epochs, changing architecture, or tuning hyperparameters.
You can also mention regularization, dropout, or early stopping.
For image tasks, convolutional models usually help.
For sequence tasks, LSTM or GRU are better than simple dense layers.

### 3) What should you say if asked why the practical works offline?
Say the practical is designed to run without internet or external downloads.
This makes it easier to reproduce on any system.
It also avoids dependency on external datasets during viva preparation.
Offline datasets like `sklearn` digits or synthetic data make the setup stable.

### 4) What should you say if asked about results?
Do not just quote accuracy or loss.
Explain what the result means in simple terms.
Say whether the model learned the pattern well or needs improvement.
This shows understanding, not only memorization.

