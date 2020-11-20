# LearnToRank
## Data collection and preprocessing
### 1. Crawler
   Web Crawler is used to crawl the World Wide Web and extract webpages automatically similar to the query. We have build two types of crawler
1. BFS crawler

    BFs crawler uses breadth wise search over the WWW graph given the start node.
  
2. Focused crawler

    Focused crawler uses relavance between the document and query and crawls the page if it's relavance score is greater than a threshold (user given)
### 2. Indexing
   The crawler create a corpus containing documents relavant to the given query. Since, we need to ```access the documents quickly documents are indexed using
   inverted indexing which contains dictonary and posting list```. The posting list contains both the document ID and the frequency of occurence of a term in the
   document.
### 3. Data Creation
   Since we are using pairwise learn-to-rank paradim, we generated an artifical dataframe which contains the relavant and non-relavent documents for a query. The dataframe looks like below, where 1 - relavent, 0 - non relavent.
   
| Query  | Document | Target|
| -----| ---------|---------|
| q1  | d1  | 1|
| q1| d2| 1 |
|q1|d3|1|
|q1|d4|0|
|q1|d5|0|

## Model building
### 1. Bag-of-Words model
   Give the document corpus, bag-of-word model was generated using gensium package. Bag-of-Word model is one form of converting text to vector representation for a document. ```A value 1 in vector represents present of a term and 0 represents absence of a word```.
   
   | doc/term  | t1 | t2|t3|t4|t5|
| -- | -- | -- | -- | -- | -- |
| d1  | 1  | 0 | 1 | 0 | 0 |
| d2| 0 | 1 | 0| 1| 0 |
|d3| 1  | 0 | 1 | 0 | 1 |

### 2. Tf-IDF vectorizer
### 3. Latent Semantic Indexing
### 4. Deep Neural Network

