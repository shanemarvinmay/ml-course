# Course Intro Notes

## Some bio data terms I am going to need to know
* Terminology - Where does sequence data come from
* Read:  A sequenced molecule of DNA.
* Insert:  Length of the molecule being sequenced.
* Library:  A collection of the genomic DNA from a sample (e.g. single organism).
* Contig: A contiguous sequence of assembled DNA.
* Scaffold: Series of contigs that may have gaps.
* Assembly: A concise representation of a genome as a set of contigs.
* Coverage: The number of times a base of the genome is represented in distinct reads.

## [one hot encoding](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.gb9697a3adf_0_0)

## I don't understand this
? [TF-IDF](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g1fdb22e475a_0_457) ?

**Word2Vec** Neutral Network based approach to generate Word Embeddings

**CBOW**, the neural network is setup in a way that it uses the context for each word as input and aims at predicting the word based on the context.
* CBOW is trained to predict a single word from a fixed window size of context words

**Skip-gram** does the opposite, and tries to predict several context words from a single input word.


# ML Fundamentals 1

## Definition of machine learning
“A computer program is said to learn from experience E with respect to  some class of tasks T and performance measure P, if its performance at  tasks in T , as measured by P, improves with experience E .”
- Tom M Mitchell. Machine Learning. McGraw-Hill, New York, 1997

## Types of Machine Learning Tasks
* ### Supervised
    * #### Classification
        * Labels are discrete
        * Examples: (Linear) SVC, *Naive Bayes*, KNeighbos Classifier, SGD Classifier Kernel Approximation, Ensemble Classifiers
            * Naive Bayes can be used on text data
    * #### Regression
        * Labels are real values
    * #### Learning to Rank
        * Order ideas by desirability
    * Problem: given the data set as input, create a “model” that can be used to predict the value of y for an unseen x
    * most common type of learning.
* ### Semi-Supervised
* ### Unsupervised
    * Clustering
        * Examples: K-Means, DBSCAN, Hierarchical
    * Dimensionality Reduction
        * Example: Principal Component Analysis (PCA), t-Distributed Stochatic, Neighbor Embedding (t-SNE)
    * Anomaly Detection
        *Example: One-Class SVM
    * Problem: given the data set as input, create a “model” that capture  relationships in the data. In clustering, the task is to assign each example  to a cluster. 
* ### Reinforment

![ml algos](https://scikit-learn.org/stable/_static/ml_map.png)

## Dimensionality Reduction
The task is to reduce the number  of features in the input space.
