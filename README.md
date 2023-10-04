# nitro
nitrogen defficiency detection from rgb images

Nitro: Deep learning classification of nitrogen deficiency from maize images

This code implements a deep learning model for classifying nitrogen deficiency in maize images. The model is based on a convolutional neural network (CNN) architecture. The CNN is trained on a dataset of maize images that have been labeled as either nitrogen deficient or not nitrogen deficient.

To use the code, first install the required dependencies:

pip install tensorflow keras scikit-learn
Then, download the dataset of maize images:

wget https://data.mendeley.com/public-files/datasets/g7xnn2bm4g/files/0caeb722-2a0e-4690-9f23-84f3230f2218/file_downloaded

The dataset should be placed in a directory called Images.

To train the model, run the commands from the notebook

The model will be trained for 100 to 1000 epochs. To train for more epochs, simply increase the value of the epochs variable in the code.

Once the model is trained, you can evaluate its performance on the test set by running the cells from the notebook.

This will print the accuracy, precision, recall, and F1 score of the model on the test set.

K-means segmentation

In addition to the CNN model, the code also implements K-means segmentation. K-means segmentation is a type of unsupervised learning that can be used to segment images into different regions.

To use K-means segmentation, set the use_segmentation flag to True in the code. This will cause the code to segment the images into two regions: background and plants. The masks for the two regions will be stored in the masks variable.

The masks can be used to improve the performance of the CNN model by providing additional information about the images. For example, the masks can be used to filter out the background from the images, which can help the model to focus on the plants.

Contributing

If you have any suggestions or improvements for the code, please feel free to contribute. You can submit a pull request to the GitHub repository:

https://github.com/vlattko/nitro