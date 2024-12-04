# Study Group Questions for Slide Deck One
These questions are based on the slides we went over in class.

## [One](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.gb88abea73f_0_1276)

What is machine learning?
* [Answer from slides](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.gb88abea73f_0_186)

What is One-Hot Encoding?
* [Answer from slides](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g201448386ee_0_20)
* [Example](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_38)
    * What would be the One-Hot Encoding of D3 ("Dog eats meat.")?

What is Bag of Words?
* [Answer from slides](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g201448386ee_0_26)
* [Example](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_47)
    * What is the difference between Bag of Words and One-Hot Encoding?
    * What would be the Bag of Words from of D3 ("Dog eats meat.")? (N is still 2)
        * Remember: dog = 1, bites = 2, man = 3, meat = 4 , food = 5, eats = 6

What is Bag of N-Grams (BoN)?
* [Answer from slides](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g201448386ee_0_32)
* [Example](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_401)
    * What would be the Bag of N-Grams from of D3 ("Dog eats meat.")?

What is TF-IDF?
* Surprise Bonus Question: What does TF-IDF stand for?
* [Answer from slides](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g201448386ee_0_38)
    * [Further definitions of TF-IDF components](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_417)
* Example Problem:
    * D1 Dog bites man.
    * D2 Man bites dog.
    * D3 Dog eats meat.
    * D4 Man eats food.
    * What is the TF-IDF for i = "eats" and j = D3?

What is Word2Vec?
* [Answer first deck of slides](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g201448386ee_0_46)
* You can make the stuff from gensim.

What is CBOW?
* [Answer from slides](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g201448386ee_0_46)
* [Illustrative example](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_430)
* [More detailed breakdown](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2047974bd31_0_17)

What is Skip-Gram?
* [Answer from slides](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g201448386ee_0_46)
* [Illustrative example](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_430)
* [More detailed breakdown](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2047974bd31_0_6)

### Polling Questions
* [Bag of words results in sparse vectors. T/F](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_55)
* [Bag of words does not capture the similarity between different words that mean the same thing. T/F](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_68)
* [Bag of n-grams cannot deal with out-of-vocabulary words. T/f](https://docs.google.com/presentation/d/10bm8ewH8R7TqmZuta_r6lK5Fl_H6ke1LPihx9a_PBrY/edit#slide=id.g2021d0c3995_0_411)