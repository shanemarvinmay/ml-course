# [Paper: Attention Is All You Need](https://arxiv.org/pdf/1706.03762v5.pdf)

## Abstract

* RNNs and CNNs were seen as the best
    * They were used with encoders/decoders throughs an attention mechanism
* 3 tasks were done
    1. WMT 2014 Englishto-German translation task. 
    Scored 28.4 BLEU.
    2. WMT 2014 English-to-French translation task. f 41.8 BLEU
    3. English constituency parsing
* Why this is important: better job translating, and trains faster.
* ? Maybe go over RNN, encoder, decoder, attention mechanism ?
    * ? if time, also what each task entails and what the score means ?


## Introduction
* Current state of the art: recurrent neural networks, long short-term memory, gated recurrent neural networks
    * advanced with encoder-decoderd architecture
* ? don't understand 2 and 3rd paragraphs ?

## Background
* ? relate signals from input and output ?
    * ? this distance between signals grows linear and logarithmacially with ConvS2S and BtyeNet respectively ?
        * ? This makes it more difficult to learn dependencies between distant positions ?
    * ? This distance remains constant with the transformer ?
        * This results in a worse performance
            * to fix this, *Multi-Head Attention* is used
            * ? look up multi-head attention ?
* ? *Self-Attention* (*intra-attention*) is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence ?
    * ? look up self-attention (intra-attention) ?
* ? End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and
language modeling tasks ?



RNN
* good for text (CNN for images)
* takes in input
    * input includes current word and output for the word that came before
    * if input is the first word, you'd pass in 0 (since there is not word that came before)
1. each sentence would run through
2. loss is evaluated for each word
3. once the sentence is done, the total loos is calculated and the weights are adjusted
4. repeat for each sentence. (steps 1 through 4 are one epoch)
* [Good video for RNN](https://www.youtube.com/watch?v=Y2wfIKQyd1I)

Encoder
* takes in language to be translated
* differs from decoders by not being masked
    * pays attention to the word being turned into a vector, the words that came before, and the words that come AFTER.
    * this is referred to as being bidirectional


Decoder 
* outputs the language you want to translate to
* Difference than encoder, is that it is masked
    * only pays attents to the word being turned into a vector, and the words that came before. NOT AFTER.
    * this is described as being unidirectional
* Good at: Given context (words that came before), predict next word

LSTM (long short term memory)
* type of RNN but with state ? in the hidden layer ?
* state contains 3 parts
    1. Forget Gate: What should be forgotten
    2. Input Gate
    3. Output Gate
        * Each gate will have a number from 0 to 1
            * 0 means it's closed and nothing gets through
            * 1 means it's open and everything gets through

Transformer
* encoder used once
* decoder used for every word 
    * each word will be received from the encoder
    * decoders uses it's output as an input to itself. (like RNN)



! [Attention Mechanism described (around this time)](https://youtu.be/WCUNPb-5EYI?t=1051) !

BERT is a popular transformer
* ? should use it for our project ?
* can also be used as a encoder and/or decoder

https://www.youtube.com/watch?v=iDulhoQ2pro

sect to sect tasks (translations)
- sequence to sequence

sketch of how it works around 2:45

https://www.youtube.com/watch?v=XowwKOAWYoQ

* Transformer using attention
    * Encoder (there was 6) (runs only once) (runs in parallel)
        * Embedd the words. Turn words into 512 length vector. Goes through once.
        * Postional Encoding. used to get information about position in the sentence. (9:50) Goes through once.
        * Multi-Head Attention
        * Add & Normalize
        * Feed Forward
        * Add & Normalize
    * Decoder (there was 6, encoders match to all of them) (run many times) (not in parrallel during? )
        * training
            * Give start of sentence (few words) and cover up the rest with the mask (masking)
        * Encodes output (labels)
        * Multi-Head Attention of output
        * Multi-Head Attention with input (from encoder)