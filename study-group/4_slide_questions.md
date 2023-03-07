# Study Group Questions for Slide Deck Four
These questions are based on the slides we went over in class.

## [Four](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gb465403f2a_0_52)

### Learning Objectives
* Explain the concepts of bias-variance, regularization in the context of linear regression and logistic regression.

What is the difference between what regression and classification predict?
* [Answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g1f16f7326dd_0_90)

What is Text Regression?
* [Answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g1f16f7326dd_0_97)

What is Text Classification?
* [Answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g1f16f7326dd_0_102)

What are some loss functions for classification?
* [Answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g2072261b291_0_0)
* [Another clear answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g2072261b291_0_14)


### Start of Logistic Regression

What is *Logistical Regression*?
* What are the possible outputs of a logistic regression model?
* [Answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.p67)
* [Mathmatical explanation](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.p70)

[Picture with mathmatical explaination for logistic regression](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g113a388e588_0_315)

### Start of Bias-Variance

* What is **Bias**?
* What is **Variance**?
* What are Bias and Variance based off of?
* What are the issues with having a high/low Bias/Variance? 
* [Answers](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_43)

Given a graph showing the RMSE for validation and training set, how can one tell when overfitting has occured? Explain.
* RMSE is the y axis
* Epoch are the x axis
* There are 2 curves.
    1. 1 for how the model is doing on the training sets.
    2. The other is for how the model is doing on the validation sets.
* [Slide](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g1f03ae56056_0_5)

### Start of Regularization

[What is **Regularization**?](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_94)
* [Decent overview](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.p85)

What issues do outliers cause, and how does reggression fix it?
* [Answer in blue](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_404)


What is **Ridge Regression**?
* aka $ℓ_2-norm$
* How does it work?
* Does it directly change the weights?
* What is lambda? 
    * What happens when lambda is 0?
* [Answer on this and the following 2 slides (look in the blue square too!)](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_652)

What is **Lasso Regression**?
* aka $ℓ_1-norm$
* Bonus points if you can remember what Lasso stands for.
* How does Lasso Regression work? How is it different than ridge regression?
* What benefit is there do using Lasso over ridge regression? Can you explain how this occures?
* ~tricky to remember~ What models does Lasso regression favor?
    * Can you explain why? (I can't.)
* [Answer on this and the following slide](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_404)
* [Side note](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_493) "$ℓ_1-norm$ (Ridge) often gives better (than Lasso) results in practice.

What is **Elastic Net**?
* [Answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_505)

What is **Early Stopping**?
* [Answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.p85)

### Start of Polynomial Regression

What is **Polynomial Regression**?
* [This and the following 3 slides give an okay explaination](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g113a388e588_0_4)

### Polling Questions
* [In the previous example does Random Forest or Logistic Regression outperform?](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_1034)
* [Which model gives the least false positives](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_1013)
* ![Graph showing 3 models](https://awesomescreenshot.s3.amazonaws.com/image/4263219/37763828-89ad227248d8c0ba259c9c1e34d50338.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20230307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230307T183919Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=a7bdeaba8fd459f351f42320cc626a23f6231c64905a1c050d9155ec4fe6fe02 "Graph showing various models that under/over fit")
    * Which curve is underfitting (high bias)?
    * Which curve is overfitting (high variance)?
    * Will using a polynomial of degree 100 be more likely to overfit or underfit?
    * Will using a general (simple) linear model, like y=mx+b, be more likely to overfit or underfit?
    * [Answer on this and the following 3 slides](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_704)
* ![Graph showing model and training examples points](https://awesomescreenshot.s3.amazonaws.com/image/4263219/37764158-59361b06dd86d92092f4c66cd4e62c3e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20230307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230307T184924Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=458c9a9f6d488f51c4881771e8c44931d2e142ac6d3789a74e97cdc152ddfc57)
    * Is it an example of overfitting or underfitting?
    * [Answer](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.gbb7527c4e5_0_140)
* ![Graph showing ROC Curve with different regressions](https://awesomescreenshot.s3.amazonaws.com/image/4263219/37765118-35f18c2015da6d917332f6734f85ac04.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20230307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230307T192405Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=4b5034ef1eef4cf8743d28b0be02e8a9510d5e7c11cca241565de0de306cc015 "Graph showing ROC Curve with different regressions")
    * Which of the following had more outliers or sparse variables (top of bottom)?
    * [Answer with a bit of an explaination](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g11505709d84_0_33)


? NOT SURE WHAT THIS SECTION IS. MAYBE DELETE ?
For classification we have seen Precision, Recall, F1, AUC, Accuracy
https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g1f16f7326dd_0_119
[Some others to know](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g1f16f7326dd_0_125)
[Even more](https://docs.google.com/presentation/d/1YrktIpLDqTc4qJDdqSJfihtyz8NUEd8j/edit#slide=id.g1f16f7326dd_0_130)