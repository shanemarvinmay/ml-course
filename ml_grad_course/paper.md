# [Paper: Attention Is All You Need](https://arxiv.org/pdf/1706.03762v5.pdf)

# Task 
* 'you just present the paper's motivation, problem, data used, methodology, results and conclusions, followed by a short q&a if anyone has questions. 10 minutes is the time limit plus any q&a.'
* 5 of your peers grade you based on the grading rubric below.
* At the end of your research paper presentation you are required to also give an update on your project progress.
* ! **Insert picture of grading rubruic here** !

## Abstract

* RNNs and CNNs were seen as the best
    * They were used with encoders/decoders throughs an attention mechanism
* 3 tasks were done
    1. WMT 2014 English-to-German translation task. 
    Scored 28.4 BLEU.
    2. WMT 2014 English-to-French translation task. f 41.8 BLEU
    3. English constituency parsing
* Why this is important: better job translating, and trains faster.
* ? Maybe go over RNN, encoder, decoder, attention mechanism ?
    * ? if time, also what each task entails and what the score means ?


## Introduction
* Current state of the art: recurrent neural networks, long short-term memory, gated recurrent neural networks
    * advanced with encoder-decoderd architecture
* RNN takes in the word and the hidden state (output of the word before), to get the next hidden state
    * keeps track of these hidden states position (like in list)
    * this means training has to be done sequentially (bad and slow)
* Attention mechanisms help. 
    * ? they allow modeling of dependencies without regard to the distances of input or output sequences ?
* Transformers can train faster with higher accuracy by relying solely on the attention mechanism.
    * more parallelization for faster training
    * better translation

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
* ? End-to-end memory networks are based on a recurrent attention mechanism instead of sequence aligned recurrence and have been shown to perform well on simple-language question answering and
language modeling tasks ?
     * End-to-end is recurrent on the attention mechanism, NOT the sequenced aligned accurance (hidden layer stuff)

## Model Architecture
* ? given input *($x_1$, ..., $x_n$)*, output *($y_1$, ..., $y_n$)*. Labels are *($z_1$, ..., $z_n$)*
* Auto regressive means that future predictions are based off passed values
* 6 encoders are fully connected to 6 decoders
### Encoders and Decoder Stacks
#### Encoder
* 6 encoders were used
* Made of 2 sub layers
    1. Multi-Head self-attention mechanism
    2. Position-Wise fully connected feed-forward network
* ? 'Residual Connection' ? (untouched by layer) wraps around each layer
* After each layer, the 'residual connection' (untouched by layer) and the output from ther layer are normalized
    * *LayerNorm(x + Sublayer(x))*
        * *Sublayer(x)* is the function the sub-layer performs
#### Decoder
* 6 decoders were used
* simular 2 sub layers as the encoder with one additional one.
    * Differences
        * one of the sublayers take in the output from the encoder
        * Masking is used. (can't see the words left of the one we are on)
### Attention
* How relavant word in a sentence are to eachother. Which gives us context
    * "The big red monster ate brocoli and he hated it."
        * What is "it" refering to? Attention is our way to knowing that it refering to brocoli. 
            * Also how we know "red" has to do with "monster" than any other word.
* Query, key, and value are mapped to an output
* Everything is a vector
* ' The output is computed as a weighted sum
of the values, where the weight assigned to each value is computed by a compatibility function of the
query with the corresponding key'
#### Scaled Dot-Product Attention
* query and keys ($d_k$)
* values ($d_v$)
* dot product of query and every key
* divided each dot product by sqrt of $d_k$
* apply softmax to get values of the weights
* Additive is better but slower
    * this is because multiplying grows larger in magnitude and pushed the softmax function into regions with small gradients.
    * dividing by the sqrt  of $d_k$
#### Multi-Head Attention
* The *Linear* part takes the query, keys, and values and projects them 8 times with different learned linear projects.
    * Takes the the matrix representing query (or key or values) and multiplies by the model (weights) matrix.
    * Then splits into 8 equal section.
    * ! Since each section can run in parallel, this is a place where a lot of time is saved. !
* Scaled Dot-Product from before is performed
* Concatenates the 8 outputs
* Linear Projection happens on the concatenated output.
#### Applications of Attention in our Model
* Self-Attention Layers are the first layers in the encoder/decoder
    * Encoder self-attention: Each position can attend to each position from the previous layer
    * Decoder: Same as encoder but the right side is masked
* Queries come from previous decoder layer
* Keys and values come from the encoder


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


# [Highest level overview](https://www.youtube.com/watch?v=TQQlZhbC5ps)

RNN is a feed foward

S2S takes in a input and outputs a FIXED LENGTH VECTOR

LSTM is an improved RNN. RNN has issues with long sequences.
- Slower to train than RNN
- Has to train sequentially and not parallel 

## Transformer
* Encoder
* Decoder
* Both based on self-attention

### Encoder
* Embedding
    * Entire input sentence goes in at once
        * gets embedded all at once
        * embedded based on meaning and position
            * postitioning done with even/odd sin/cos func used
            * positioning provides context
* Attention (timestamp 5:05 ish)
    * tells us which words has the most todo with the word we are on.
        * word: "red"
        * sentence: The red house.
        * "red" and "house" has a lot more todo with our word than "the"
        * "The red house" -> [0.01, 0.85, 0.12]
* Feed Forwards Neural Net
    * turns the output of the attention block into a form that the decoder can diguest
    * This can be done in parallel
* ? outputs an attention vector for each work ?
    * attention vector is multi-headed

### Decoder
* Embedding done just like the encoder, except that it encodes the translated text (output)
    * ? Only embedds one word at a time ?
* Attention like encoder, but still for translated text (output)
    * Masked: the attention vector for each word only takes into account the words that came before it
* Attention for output of *Encoder* and the translated text (output)
* Feed Forward Neural Net
    * like the encoder's feed forward, except it goes into a form that can either be taken in by another decoder or the *Linear Layer*
* Linear Layer is another feed forward neural net
    * takes the output from the decoder and exands the dimensions to the number of words in the output language
* Softmax turns the output of the linear layer into a probability disctribution (? of the words ?)
* output is the most probably next word (in the translated language)

* Starts with start of sentence token. Finishes with end-of-sentence token.

* Multi-Head Attention
    * Attention vector will always show the word we are on as having the greatest relationship with itself.
    * Taking multiply attention vectors, then averaging them out is the multi-head attention


# [Deeper explaination](https://www.youtube.com/watch?v=XowwKOAWYoQ)

* Links for each part. These links go to places that go into further description on that part.

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


https://www.youtube.com/watch?v=iDulhoQ2pro

sect to sect tasks (translations)
* sequence to sequence

sketch of how it works around 2:45


* glove is a pretrained embedding

! could be best resource for project (Pervasive Attention): https://arxiv.org/abs/1808.03867 !