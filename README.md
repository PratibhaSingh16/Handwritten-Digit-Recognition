# <u>Handwritten Digit Recognition</u>
Handwriting recognition (HWR), is the ability of a computer to receive and interpret intelligible handwritten input from sources such as paper documents or photographs.
It is used to recognize the digits which are written by hand. It is tough task for the machine because handwritten digits are not perfect.
Handwritten digit recognition is the solution to this problem as it uses the image of a digit and recognizes the digit present in the image.
It is already in use for automatic processing in different domain namely:
- Bank: characters and digits on check and forms.
- Postal address recognition for mail sorting
- Form data entry
- License Plate readers for parking structures/security cameras
Goal is to develop a model using Support Vector Machine which should correctly classify the handwritten digits from 0-9 based on the pixel values given as features. Thus, this is a 10-class classification problem.

## MNIST Dataset
We are using MNIST Dataset, which is:
- Set of 70,000 small images of digits handwritten by high school students and employees of the US Census Bureau.
- This dataset is one of the most popular datasets among machine learning and deep learning researchers.
- There are 70,000 images, and each image has 784 features.
- Each image is 28 x 28 pixels, and each feature simply represents one pixel’s intensity, from 0 (white) to 255 (black).

## SVM(Support Vector Machines)
In the last years, SVMs have gained a lot of attention.
Successfully applied to several different areas such as: Face Verification/Recognition, Image Retrieval, Speech Recognition, Text Categorization, Handwriting Recognition. SVMs show accurate results with minimal computation power when we have a lot of features.
SVM generally do not suffer condition of over fitting.
Outliers have less influence in SVM Algorithm.
In comparison with Naive Bayes Algorithm, SVM has a faster prediction along with better accuracy.

## SCIKIT Learn Toolkit
- Developed by David Cournapeau
- French Institute for Research in Computer Science and Automation published the first version.
- It features various classification, regression and clustering algorithms including SVM, random forests, gradient boosting, k-means and DBSCAN.
- Free software machine learning library for the Python programming language.

After using the above mentioned tools and using python code, this way we trained our model, ad then tested it, and to do properly test our model's accuracy we predicted it using python code, and turn our model was 97.9% accurate in predicting the Handwritten digits correctly.


Below is the screenshot to represent the Digit recognition done by our model:
![1](https://user-images.githubusercontent.com/77543839/119193650-eb6e7700-ba4f-11eb-9f59-9f16ba937a88.png)


![2](https://user-images.githubusercontent.com/77543839/119193656-ed383a80-ba4f-11eb-8d7e-1c80aa9e750a.png)


![3](https://user-images.githubusercontent.com/77543839/119193662-ee696780-ba4f-11eb-8517-9933beb700d4.png)

