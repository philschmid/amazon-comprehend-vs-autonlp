# Amazon Comprehend vs AutoNLP

# Use-case 1: Single-Label Text-Classification

## Dataset: [AG News](https://huggingface.co/datasets/ag_news)

AG is a collection of more than 1 million news articles. News articles have been gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of activity. ComeToMyHead is an academic news search engine which has been running since July, 2004. The dataset is provided by the academic community for research purposes in data mining (clustering, classification, etc), information retrieval (ranking, search, etc), xml, data compression, data streaming, and any other non-commercial activity. For more information, please refer to the link http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .

Size: 12000 train | 10000 test


| Service    | f1 score | accuracy |
|------------|----------|----------|
| AutoNLP    | 94.93    | 94.93    |
| Comprehend | 94.5     | 94.5     |


## Dataset: [Tweet eval `Emotion`](https://huggingface.co/datasets/tweet_eval)

TweetEval consists of seven heterogenous tasks in Twitter, all framed as multi-class tweet classification. The tasks include - irony, hate, offensive, stance, emoji, emotion, and sentiment. All tasks have been unified into the same benchmark, with each dataset presented in the same format and with fixed training, validation and test splits.

Size: 3257 train | 374 test


| Service    | f1 score | accuracy |
|------------|----------|----------|
| AutoNLP    | 80.63   |  81   |
| Comprehend | 70.86     | 75.86     |

## Dataset [Banking 77](https://huggingface.co/datasets/banking77)

Dataset composed of online banking queries annotated with their corresponding intents.

BANKING77 dataset provides a very fine-grained set of intents in a banking domain. It comprises 13,083 customer service queries labeled with 77 intents. It focuses on fine-grained single-domain intent detection.

Size: 10 003 train | 3 080 test

| Service    | f1 score | accuracy |
|------------|----------|----------|
| AutoNLP    | 93.64   |  93.64    |
| Comprehend | 91.33     | 91.32      |