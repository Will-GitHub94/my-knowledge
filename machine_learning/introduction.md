# Introduction

### What is machine learning?

> A computer program is said to learn from experience 'E' with respect to some class of tasks 'T' and performance measure 'P', if its perforance at tasks in 'T', as measured by 'P', improves with experience 'E'

Bascially the quote above is saying that if a program can improve how it does a certain task based on past experience then you can say it has learned

3 types of learning/training:

1.  **Supervised**: *Train machine using data which is already tagged with correct answer/outcome (i.e. 'here is a picture with the letter 'A'"). The greater the data set, the more the machine can learn about the subject matter. Machine then presented with unlabelled data in sam subject & hope is it will use its past experience to get correct answers*
2. **Unsupervised**: *Machine given unlablled data (i.e. "here is a letter"). Idea is that if machine is exposed to hours of different letters, they will eventually be able to form patterns of how the alphabet works*
3. **Reinforcement**: *Uses unlabelled data but every answer that is given by machine is graded (i.e. playing chess... if a machine wins a game of chess then the moves that were played trickle down to reinforce the validity of those moves). As expected, this would only be useful is the machine were exposed to 1000s of games which it could then define a winning strategy*

What can be achieved with machine learning?

- Picture annotation (*Machine given a photo & asked to describe it (can help with the blind)*)
- Teaching machines how to write (*I.e. writers were asked to copy text on a smart white board which the pen was tracked via infrared which ended up producing a set of X and Y coordinates*)
- Using Neural Networks to model conversations

### Steps

There are 7 steps of machine learning:

1. **Gathering data**: *Just gathering the data that you are going to give the machine to train on. Aptly named ... training data*
2. **Data preparation**: *Put all data together & randomise the ordering. Also a good time to make any visualisations of the data... are there any relationships/inbalances? Need to also split the data into [2 parts](data_preprocessing.md##splitting-data-set-into-training-evaluation-data):*
  	2.1: Training: *The data used to train our model - the majority*
  	2.2: Evaluation: *The data used to evaluate our model after being given the training data - the minority*
3. **Choosing a model**: *Data scienists produced many models over the years. Some for image recognition, some for text etc.*
4. **Training**: *Use data to incrementally imporve models ability to differentiate between data sets. A similatity can be drawn up from someone learning to drive. Compare the output of the models predications with the inputs so can tailor the inputs everytime to get more accurate outputs. Okay, so when we first start training the model, the line of differentiation between the data sets is random but as progress', the line gets more and more accurate*
5. Evaluation: *Test model from what it has learnt from the training data against the evaluation data*
6. **(Hyper)Parameter Tuning**: *Refine training (i.e. how many times should we run through the training set before giving the model the evaluation data)*
7. **Prediction**: *The point of all of the work where the value of machine learning is realised. Able to determine difference of data sets using model rather than human rules*


<img src="assets/matrices-example.gif" alt="Matrices Example"/><br>

### Examples

1. Facebook face recognition
2. Kinect
3. Virtual reality headsets
4. Voice recognition
5. Robot dogs learning to walk
6. Facebook Ads
7. Recommendations (Netflix, Amazon, Audible)
8. Medicine
9. Space (recognise certain areas of the globe)
10. Explore new territories (Mars)


### Future of ML

Day to day life, people are leaving the "date exhaust" which is essentially like leaving a digital footprint everywhere you go (i.e. GPS data).

<img src="assets/human_data_production.png" alt="Human Data Production"/><br>

**Data Scientists** = Our capacity to process data though that's the data that's in the world
**Machines** = How much of the data that's in the world that the machines are actually using
**Machine Learning** = The potential to use this data that is not being used. Only with machine learning algorithms can you step up to that challenge
