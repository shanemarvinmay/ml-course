# Study Group Questions for Slide Deck Six
These questions are based on the slides we went over in class.

## [Six](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.gafb90f898e_0_52)

### Learning Objectives
* Explain in your own words what unsupervised learning is
* Describe the main concepts and algorithms of unsupervised learning
* Understand the main concepts behind dimensionality reduction


What is **Unsupervised Learning**?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p3)
* What is the goal of unsupervised learning?
* [Answer on second blue bullet point](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p17)


What are 2 types of unsupervised learning tasks?
* Can you give examples of each of those types (specific algorithms)?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p32)


### Dimensionality Reduction


What is **Dimensionality Reduction**?
* What is the benefit of it?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_37)


What are the benefits of dimensionality reduction?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_45)


What is PCA?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_419)


What must happend to the data before applying PCA?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_400)


(Note) You want your PCA vectors to be othoganal, but why?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_334)


What I understand about PCAs so far.
* Each vector with be closest to the data points (so they have high correlation), which is reducing the number of features.
* Each vector will become and  axis.
* Ploting along the axis will give you good insight into the underlying structure of the data


What is **t-SNE**?
* Why is it better that PCA?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_503)


How does t-SNE work?
* [Answer on this and the following 2 slides](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_510)


(Note) Perplexity matters in t-SNE
* [This and the following 2 slides](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_537)


Does distance between clusters mean anything in PCA or t-SNE?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_589)


What are the downsides to t-SNE?
* [Answer on this and the next slide](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_599)


What benefit does UMAP have over t-SNE?
* [Answer in title of slide](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_628)
* [Rest of the answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_635)


? [UMAP has 2 parameters](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_640) ?


? [Don't understand this "Practical approach to PCA + t-SNE/UMAP](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_673) ?


What are the benefits to dimensionality reduction?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g1b648dfd2a0_0_678)


### Clustering


What is a cluster?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p43)


What is **KMeans**?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p47)


How does KMneas worK?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p58)


What is **Hierarchical Clustering** (UPGMA)?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p72)
* [Illustrations here and on the following slides](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g210bc727964_0_104)


(Note) [Illustration of how hierarchical clustering works](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p74)


What are the three types of linkage in UPGMA (hierarchical clustering?)? And what do they look like?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p79)


What is **Density-Based Clustering**?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g210bc727964_0_125)
* What are it's 2 parameters?
    * [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g210bc727964_0_130)


What is **DBSCAN**?
* What is Density (in this context)?
* What is a core point?
* What is a border point?
* What is a noise point?
* [Answer](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g210bc727964_0_251)


### Polling Questions
* [What shape of clusters would KMeans produce?](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p60)
* !Important! [Would you expect a KMeans solution to be the same every time you run it?](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.p61)
* [How would you measure the similarity for constructing this tree?](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.gbfbad680be_0_1)
* [DBSCAN can deal with outliers and non-spherical shaped clusters than KMeans (True/False)](https://docs.google.com/presentation/d/1okjUEjZKxoRpDZVNf3ukbF33TUa9RGNd/edit#slide=id.g210bc727964_0_296)



