# Hinglish Sentiment Analysis Pipeline

An idea proposal for a Pipeline for Sentiment Analysis on Hinglish Text

## Problem Statement and Expected Challenges ##
* PROBLEM STATEMENT : Classifying Hinglish texts Sentimentally. Ex: positive, negative and neutral.
* Hinglish language will not have uniformity in spellings, syntatic and semantic structures. It might contain purely english words too.
* Can result in large vocabulary size with many tokens sharing exactly same semantic and syntatic entity. Ex: English : NOT, Hinglish Variants: Nahi, Nahii, Nai, Nhi etc
* Cannot directly apply Frequency based approaches directly as many tokens (either words or n-grams) will share same semantic and syntatcic entity.
* No pretrained embeddings available, cannot directly train given corpus to extract embeddings either. 

## Approach ##

The overall approach will be split in two steps:

#### STEP 1 ####

A one-time only , computationally heavy task. Getting word embeddings from the given Hinglish Corpus using the 'Subword Information Advanced Approach for word2vec model'. This apporach can provide us embeddings for the words not present in the corpus along with all the words in the corpus. So, good embeddings for slight variants of same word present in corpus or absent can be found out easily once an initial set of embeddings is extracted. This will also ensure that all the variants of same word ( 
* [Link to the research Paper 'Enriching word vectors with Subword Information' by Mikolov et-al](http://aclweb.org/anthology/Q17-1010)
* [My article on HackerNoon Medium, explaining the approach in plain english](https://hackernoon.com/enriching-word-vectors-with-subword-information-paper-summary-fa66d50ea071)
* [My short implementation of this research paper](https://colab.research.google.com/drive/11Zqc3soPQnF3joamG6eXnkog0ZRJzKBw)

#### STEP 2 ####

For any new unseen text corpus, we can easily get new embeddings for this corpus from the embeddings extracted earlier within a very short time by tensor additions of previous embeddings. This will cover all the newly appeared words and variants in the current corpus and provide good embeddings for them semantically. Then we can move forward with our classification task.

## Pipeline ##
* The first step would be to pre-process the text, removing non-ascii charecters, converting the text to lowercase etc
* Then the second task would be to tokenize the corpus and create a vocabulary, word to index dictionary and index to word dictionary.
* Next step, would be getting word embeddings for all the words in the corpus using the initial embeddings calculated in Step 1 of Approach.
* Next we can perform classification tasks with these word embeddings. 

### Supervised Sentiment Analysis ###
* Assuming we have a labelled dataset.
* First step would be to make the sentence / document lenth equal for all the samples in the corpus, this can be done by simple padding.
* Next, we can train a simple feed-forward Neural Network with sufficient reguarization (dropout) as a single-label-multi-classification problem. (can take three softmax ouputs from final layer for pos / neg / neutral each)
* We can also follow CNN based approaches, which will just involve another step of reshaping the one-dimensional vectors into multiple dimensions.

### Un-Supervised Sentiment Analysis ###
* The preprocessing and embeddings extraction will be same as that of Supervised case.
* Then we can follow a simple Clustering to divide our our documents in two/three clusters.
* It is quite possible that the obtained cluster may not correlate sufficiently with the actual sentiment classification. To achieve maximum correlation we can first perform topic modelling techniques like LDA & LSA and then perform our clustering with the modeled topics.
* Yet another and the most efficient way of Unsupervised Sentiment Analysis would be building a Lexicon for Hinglish Language, similar to the ones for English like "Harvard General Enquirer" and "MPQA".
 This again would require huge manual labor, but this will be an one-time job and can be achieved via an open-sourced approach easily. 
* Once we have our Lexicon, we can perform clustering or any other Scoring technique to perform a highly correlated Classification of sentiments.



## Tools & Resources Required ##
* BeautifulSoup & requests : To scrape off huge hinglish text corpus off the web.
* Pytorch / Keras / Tensorflow : To build neural models for extracting word embeddings, classification tasks etc
* Scikit-learn : To perform clustering, LDA, LSA etc
* NLTK / SpaCy : Might be required for Tokeninzing, pre-processing etc


## Suggestions ##

For any suggestions and interested collaborations, contact me here : rajp4480@gmail.com 



