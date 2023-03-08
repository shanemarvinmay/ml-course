# Study Group Questions for Slide Deck Three
These questions are based on the slides we went over in class.

## [Three](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.gb97c1ea942_0_98)

### Learning Objectives
* Explain the **optimization algorithm** for solving linear regression problems.
* Describe the **derivative in the gradient descent algorithm**.
* Compare the **batch**, **stochastic** and **mini-batch gradient descent** algorithms.

What is Supervised Learning?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.gb97c1ea942_0_233)
* What is $X_i$?
* What is D?
* What is $X_i^j$?
* What is $Y_i$ in linear regression? In classification?

What are the building blocking of a *learning algorithm*?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p19)

What is *optimization* in ML?
* What is *Gradient Descent*?
    * Why do you think it is called descent?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p21)

What is *Linear Regression*?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.gba8d4a21f1_0_3)
* What is a *training example*?
* What is a good loss function for linear regression? What should it look like when you graph it?
* What is a problem that could be solved with linear regression?
* [Further explaination](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.gba8d4a21f1_0_46)

How are *derivatives* used in Gradient Descent?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p22)
* What does the slope of the derivative tell you? If it's positive? If its negative? 
    * [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p26)
* What is the margnitude of the derivative?
    * [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p26)
    * What is another name for the margnitude?
        * [Answer (look for it)](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p36)

What are some loss functions for linear models?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.gb97c1ea942_0_318)
* Why would you chose one of another?
    * [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.g1f03aad09bb_0_15)

What are some loss function for classification?
* When would you use one over another?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.g1f03aad09bb_0_23)

Can you adjust both m (slope) and b (y-int) at the same time? Why or why not?
* [Partial answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p35)

How does Gradient Descent work (mathmatically)?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p44)

Why does the loss function have to be differentiable?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p46)

What is local and global max/min? And how is it used in learn regression?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p52)

What are the pros and cons to a smaller/bigger learn rate?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p53)

What are 3 types of *Stochastic Gradient Descent*?
* [The first](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p54)
* [The second](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p61)
* [The third](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p67)
* [Illustration](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p68)

What is *Batch Gradient Descent*?
* [Answer from slides](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p54)
* [Better answer](https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a#:~:text=Batch%20Gradient%20Descent,in%20one%20epoch.)
* What are the cons of Batch Gradient Descent?
    * [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p56)

What is *Stochastic Gradient Descent*?
* [Answer from slides](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p61)
* What benefit might Stochastic Gradient Descent have over Batch Gradient Descent?
    * [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p61)
* [Illustration](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.g111c7606f7b_0_46)
* Should Stochastic Gradient Descent be done in order the training example come in? Why not?
    * [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p63)
* What does it mean if you see a low loss using Stochastic Gradient Descent?
* What does it mean if you see a high loss using Stochastic Gradient Descent?
    * [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p63)

What is *Mini-Batch Gradient Descent*?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.p67)

What is a *regressor*?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.g114c7f0866b_0_0)

What is the point of *Stochastic Gradient Descent*?
* [Answer](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.g114c7f0866b_0_0)

[Summary of what was covered in this section](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.g114c7f0866b_0_144)

**!** Random MAE is my favorite and seems most useful to me. [Link](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.g1f03aad09bb_0_9) **!**

**?** Why does this say "D + 1"? [Link](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.gba8d4a21f1_0_46) **?**

### Polling Questions
* ![Just click me to see the question.](https://awesomescreenshot.s3.amazonaws.com/image/4263219/37771061-b8627578a90d1b3c945dc79acb9d672b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20230307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230307T234856Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=8c04b11b9fdc8ad5943fb4b3aed45b7be98cd31d244261f3740fc0f37ee947d9)
    * Which method gives the highest correlation?
        * Linear with Dinucleotide composition
        * Polynomial with Dinucleotide composition
        * RBF with Dinucleotide composition

* ![Illustration of polling question](https://awesomescreenshot.s3.amazonaws.com/image/4263219/37771227-70baca69d3ae8fd61476337e71acc1a4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20230307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230307T235853Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=388c755dff57fb37debd31e38bd1aa6a3d7f2bde6d3e0e10896e85816b3c09f4)
    * Based on the previous images, which variable seems to be most correlated with gene expression (Exp) in this gene?
        * Time
        * Depth
        * Height
        * Width

    * [Polling question that goes with the illustration above](https://docs.google.com/presentation/d/1txqt9HGu2hrn3wmMHy9CtPVJYe_vhiI2/edit#slide=id.g114c7f0866b_0_170)