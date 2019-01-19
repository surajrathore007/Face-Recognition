# Face-Recognition

This face recognition project is based on OpenCV .
This project requires python 2.7 and opencv library 2.4.13.

All the necessary details are given in Face_proj_2nd year.doc file so please read it thoroughly.
Remember copying project for any misuse and uploading anywhere without making changes is not allowed, 
specially for Face_proj_2nd year.doc file.

## 1 Face Recognition
Face recognition is the next step above face detection. After detecting a face
in an image, the next natural question is “to whom does this face belong
to?” This is the question that face detection tries to answer. To answer
this question, we have to build an AI that can has lots of labeled training
examples of people’s faces. These training examples really just consist of
an image and whose face it belongs to. This is really all we need! In the
training phase, we need a dataset of faces (we’ll be using the popular Yale
face dataset in particular though there are plenty of others like AT&T face
dataset). During the training phase, we need to do the following to all input
examples (consisting of images and labels)!
1. Detect the face in the image using standard face detection.
2. Capture and analyze the features of that particular face.
3. Store those features with the same label to be compared with new
examples.
The steps we take when we see a new example is very similar.
1. Detect all faces in the image using standard face detection.
2. Capture and analyze the features of that particular face.
3. Compare those features with the existing features of faces that we have
in our machine learning model.
1
4. Make a prediction with some confidence based on those features.
We need to first detect all of the faces that are in this image using plain
old face detection. Now that we know the location of these faces, we can
extract some features of out of the faces that are most representative of the
face itself using the same algorithm we used when we were training our AI.
Then we can compare those features from the new example to those that we
have already seen before. Then we can make a prediction as to which person
or label this face belongs to.

## 2 Dimensionality Reduction
## 3 Principle Components Analysis (PCA)
## 4 Linear Discriminant Analysis (LDA)
## 5 Difference Between PCA and LDA
## 6 Local Binary Patterns (LBP)

# Results

https://github.com/surajrathore007/Face-Recognition/issues/1#issue-400967092
