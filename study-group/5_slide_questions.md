# Study Group Questions for Slide Deck Five
These questions are based on the slides we went over in class.

## [Five](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbe3701c345_0_60)

### Learning Objectives
* [Tokenization in text](#tokenization-and-similarity-metrics)
* [Similarity metrics](#tokenization-and-similarity-metrics)
* [Word-embeddings: TF-IDF, Word2Vec](#word-embeddings)
* Kmers (bio n-grams)
* One-hot encoding
* DNA2Vec


### Tokenization and Similarity Metrics

[What is **Language Modeling**? And why is it useful?](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20805386c74_0_613)

[What is a **Term-Document Matrix**?](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_506)

[What is **Jaccard Index/Coefficient/Similarity**?](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_962)
* [What is **Weighted Jaccard Similarity**?](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20805386c74_0_608)

### Word-Embeddings

TF-IDF vs Word2Vec
* Which has dense vectors and which has sparse vectors?
* Which is created by training a classifier to distinguish nearby and far-away words?
* Which is based on a function of nearby words?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_496)

Why is it called an "*embedding*"?
* What is word embeddings used for? Or why are they useful?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_1026)


(Hard)
What is a **Co-Occurrrence Matrix** and why is it useful?
* What is a **Distributional Representation**?
    * What are some examples of a Distributional Representation?
* What is the dimension of the Co-Occurrence Matrix?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gb570f567eb_0_14)


What is a **Distributional Similarity**?
* Where does it get it's meaning from?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_19)


What is **Cosine Similarity**?
* What is it used for?
    * [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_556)
* What possible values could you get from it? 
    * What do each of those values mean?
    * [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_569)


(Note) Word2Vec ensures vectors are low-dimensional (few hundred) and dense (most values are not 0)


(Note)[Example of how to make and use a Word2Vec embedding](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_32)


What % of overlap do you want between a pretrained embedding to and your custom domain?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_128)


How does Word2Vec decide whether 2 words are similar?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_710)
* How does it train to do this (old way)?
    * [Answer (and following 5 slides)](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20805386c74_0_827)
    * What is the new way?
        * [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g11579432e38_2_2)


How can you take a word vectors to find similar meaning?
* [Answer (and the following 2 slides)](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_859)


(Note)[How to use Word2Vec in code (and following slides)](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_153)


(hard) How to get vector embedding for whole text?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_123)


What is FastText?
* What is the advantage of FastText? How does it do it?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_97)


What is Doc2Vec?
* What is it's advantage over Word2Vec and FastText?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_102)


How do you pass embeddings in to Neural Net?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_147)


All text representations are inherently biased based on what they saw in training data (True/False).
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_107)


### Kmers and One-Hot Encoding


(Note) Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different.


What is a **Kmer**?
* How can you tell how many there will be?
* [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20805386c74_0_5)


(Note) Jaccard can be used with kmers.


### Polling Questions
* You will need to create a Doc2Vec for your document corpus since there is no universal Doc2Vec model that applies to all corpus (True/Fase)
    * [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_190)
* Does DNA2Vec cosine similarity correspond well to Needleman-Wunsch sequence sim score?
    * [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20888ddd21f_0_224)
* (NO IDEA) In this paper k-mers are used for clustering sequences and a sequence can belong to >1 cluster (True/False).
    * [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20805386c74_0_544)
* (NO IDEA) What value would “GPT” have?
    * [Answer](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.g20805386c74_0_587)


### I don't understand the following
* [This slide](https://docs.google.com/presentation/d/1d8-Yuped-SUHB-hi3-PCCSjzvntMtECClr4slO7e3eE/edit#slide=id.gbd4865de7f_0_752)