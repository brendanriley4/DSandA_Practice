Things from machine learning course:
	-NumPy arrays - like normal arrays but they can be vectorized (parallelized) (good for machine learning).
	-Correlation coefficient - a number between -1 and 1 that describes the relationship between two variables
	
Selecting data from a NumPy array, x is all rows, every column but the last
```python
	X = df_numpy[:, :-1]
```


-Multiple Linear Regression Model - uses multiple inputs to predict an output
-MSE (mean squared error) vs. MAE (mean absolute error) vs. RMSE (root mean squared error) - pretty self explanatory, in MAE units are the same so this is a plus
-Can have numerical (continuous) variables, binary variables, or categorical (word, letter) variables
-If a categorical variable has an ordering it is called an Ordinal, if it does not it is called a nominal
-Encoding - taking raw features from a dataset and changing them into a form that ML models can use
-Dummy encoding - one hot encoding but first column is removed (to indicate this value, all values 0)
-Standardization - mathematically speaking transforms each value of a column by subtracting the column average and dividing by the column's standard deviation
-Hyperparameters - numbers that humans set as part of the training experiment

-Bias-Variance Tradeoff - We want our models to not overfit and not underfit, the pattern is understood from the training set but not memorized. 
	-Bias - model is unable to capture complex patterns (underfit)
	-Variance - model has too much complexity and is unstable (overfits)

-Total Error:
		T.E. = Bias^2 + Variance + Noise
		-Noise = possums with same belly length but different chest length 

-Regression model - has a numerical (continuous) output
-Classification model - has a categorical output

-Confusion matrix - graphically shows when the model was confused (got the wrong answer) and was not confused (got the right answer)

-For binary classification model - negative class (0's) and positive class(1's) so confusion matrix has true negatives and true positives along with false negatives and false positives 
	-False negative - model got it wrong and predicted false

Precision of binary classification model = True positives / (True positives + False Positives)
	-How likely are we to be right when we say positive
Recall of binary classification model = True positives / (True positives + False negatives)
	-How many positives did the model actually predict

F1-Score = 2 * ((precision * recall) / (precision + recall))

-Insert log loss function here***
-Log loss is another metric to determine accuracy:
	-Compares the predicted probabilities of a model to the actual class labels
	-penalizes inaccurate predictions
	-lower log loss = better model performance

-When printing shape of data (columns (items), rows (parameters of each))

-Accuracy - fraction of correct answers

-3 data sets important to training a model:
	-Training set - just as before, set of data model is trained with
	-Validation set - Evaluates each models performance and choose the best one
	-Hold out / test set - truthfully estimate and report the final models real world accuracy
-Overall idea: One to train the model, one to pick the model, and one to predict the model's real world accuracy

-Cross validation - divide data into n equal sets, train model on n-1 sets and use nth as validation, cycle n, continue until all n sets have been used for validation
-Useful for models that are quick to train, if computational cost of training is high, forget about it

-Decision Tree - a sequence of nodes where data is split based on certain conditions. Decision nodes are those points and leaf nodes are the final output where classification or values (regression) are determined

-Random forest regressor - uses a forest of these trees trained on different pieces of the data, when we want to predict a value the model takes an average of what all the trees are saying.

-K-nearest neighbors regressor - finding the 'k' closest points in the training data set and averaging their values to make its prediction. 'k' can be adjusted to control how many neighbors have input.

-Support vector machine (SVM) - finds the best fitting line or curve by focusing on the data points that are hardest to predict, called support vectors (an individual point can also be seen as a vector). SVMs are by far the most confusing.

-Gradient boosting models (eg. XGBoost) - uses a series of simple models to make predictions. Each new model in the series tries to correct mistakes made by the models before it. This step-by-step improvement aims to make the overall model very accurate and boosting models are commonly a good choice

-Regularization - allows us to have extra control over the complexity of a model.
	-Ridge - a linear regression model that automatically applies regularization
	-Designed to prevent overfitting in ML by adding a penalty to the loss function that the model is trying to minimize
	-Loss = MSE + a * LargeParameterPenalizer
	-Purpose of the penalty is to discourage the model from relying too heavily on any single feature by forcing parameter values to get closer to 0, which in essence forces the model to have less complexity
	-a (alpha) is  a hyperparameter representing the regularization strength which controls complexity, the higher the alpha the stronger the regularization, thus decreasing the model's complexity
	-Lasso - another kind of linear regression that employs regularization
		-In Lasso regression LargeParameterPenalizer is equal to the sum of all the absolute values of the coefficients, instead of squaring. Lasso allows some parameters values to shrink all the way to 0.
		-Ride more common

-Model is trying to minimize MSE while also being penalized for having large coefficients, we need to strike right balance

-Forecasting - regression but there is a time component

-Time series - the data used in forecasting

-Unsupervised learning - ML without a 'supervisor' which would be the true output or y. 
	-Used less frequently but simply trying to find patterns in the data set.
	-Clustering is a great example of this and K-means is a great way to do it
	-Clustering tries to group similar data points together
	-Centroids - center of data groups in clustering
	-K-means aims to make sure each point in a cluster is closer to its groups centroid than other centroids
	-DBSCAN is a good resource to learn about clustering

-Reinforcement learning - Not in the course, 'rarely used' LOOK UP LATER

-Dimensional reduction - another example of unsupervised learning, means meaningfully reducing the number of dimensions in our dataset
-PCA (principal component analysis) is a dimensional reduction algorithm