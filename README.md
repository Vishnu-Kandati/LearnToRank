## Team Members

Kandati VishnuSai

Midhilesh E

# Learning to Rank

Learning to Rank is the application of machine learning, typically supervised, semi-supervised or reinforcement learning, in the construction of ranking models for information 
retrieval systems.

## Approaches

1. Pairwise
2. Pointwise
3. Listwise

## Data collection and preprocessing
![alt text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/dataprep.png)
### 1. Crawler
   Web Crawler is used to crawl the World Wide Web and extract webpages automatically similar to the query. We have build two types of crawler
1. **BFS crawler**

    BFs crawler uses breadth wise search over the WWW graph given the start node.
  
2. **Focused crawler**

    Focused crawler uses relavance between the document and query and crawls the page if it's relavance score is greater than a threshold (user given)
### 2. Indexing
   The crawler create a corpus containing documents relavant to the given query. Since, we need to ```access the documents quickly documents are indexed using
   inverted indexing which contains dictonary and posting list```. The posting list contains both the document ID and the frequency of occurence of a term in the
   document.
### 3. Data Creation
   Since we are using pairwise learning-to-rank paradigm, we generated an artifical dataframe which contains the relavant and non-relavent documents for a query. The dataframe looks like below, where 1 - relavent, 0 - non relavent.
   
| Query  | Document | Target|
| -----| ---------|---------|
| q1  | d1  | 1|
| q1| d2| 1 |
|q1|d3|1|
|q1|d4|0|
|q1|d5|0|

## Model building
![alt text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/engine.png)
### 1. Bag-of-Words model
   Give the document corpus, bag-of-word model was generated using gensium package. Bag-of-Word model is one form of converting text to vector representation for a document. ```A value 1 in vector represents present of a term and 0 represents absence of a word```.
   
   | doc/term  | t1 | t2|t3|t4|t5|
| -- | -- | -- | -- | -- | -- |
| d1  | 1  | 0 | 1 | 0 | 0 |
| d2| 0 | 1 | 0| 1| 0 |
|d3| 1  | 0 | 1 | 0 | 1 |

### 2. Tf-IDF vectorizer
   TF-IDF is an abbreviation for Term Frequency Inverse Document Frequency. 
   This is very common algorithm to transform text into a meaningful representation of numbers which is used to fit machine algorithm for prediction.
   
   formula used: tf-idf(d, t) = tf(t) * idf(d, t)
   
   ![alt text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/Data.png)

   **Count Vectorizer**

   | doc/term  | blue | bright|sky|sun|
   | -- | -- | -- | -- | -- |
   | d1 | 1  | 0  | 1  | 0  |
   | d2 | 0  | 1  | 0  |  1 |

   **TF-IDF Vectorizer**
   
   | doc/term  | blue | bright|sky|sun|
   | -- | -- | -- | -- | -- |
   | d1  | 0.70107 | 0.00 | 0.707107| 0.00 |
   | d2| 0.00 | 0.707107 | 0| 0.707107 |

### 3. Latent Semantic Indexing

   ![alt_test](https://github.com/Midhilesh29/LearnToRank/blob/main/img/Screenshot%20from%202020-11-22%2013-51-57.png)

   1. Latent semantic indexing (LSI) is a concept used by search engines to discover how a term and content work together to mean the same thing, even if they do not share keywords or synonyms. 
   2. It is used to improve the accuracy of information retrieval
   3. It uses a singular value decomposition technique to scan unstructured data within documents and identify relationships between the concepts.
   4. LSI was designed to help searchers find what they're looking for, not just what they searched for.
   
   (**Since we had 6 different subtopics in artificial intelligence, we reduced to dimensions to 6 (i.e k=6)**)
   
### 4. Deep Neural Network
   Neural Network models are usually termed as universal approximators which can be used for classifying documents as relavent or non-relavent with respect to
   the query. An example for simple neural network is as follows.
   
   ![alt text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/NN.jpeg)
   
   Here we will be using two neural network which shares same parameters to project the query and documents in low dimensional space. The following describes the
   characteristics of the low dimensional space.
   
   1. Documents and query which are related are present close together.
   2. Documenst and query which are unrelated are present far apart.
   
   **Ranknet Architecture (pictorial representation)**
   ![alt_text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/Screenshot%20from%202020-11-22%2014-09-01.png)
   
   
   **Loss function** -> **binary cross entropy** function
   
   **Optimizer** -> **Adams optimizer** with **learning rate = 0.003**.
   
## Evaluation metrics
### F1-Score plot
![alt text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/f1_plot.png)
### Loss plot
![alt text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/loss_plot.png)
### Precision plot
![alt text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/precision_plot.png)
### Recall plot
![alt text](https://github.com/Midhilesh29/LearnToRank/blob/main/img/recall_plot.png)

# Paper refered
1. [RankNet:Learning to Rank using Gradient Descent (ICML 2015)](https://www.microsoft.com/en-us/research/blog/ranknet-a-ranking-retrospective/)
2. [DSSM: Learning semantic representations using convolutional neural networks for web search (ACM 2015)](https://posenhuang.github.io/papers/cikm2013_DSSM_fullversion.pdf)
