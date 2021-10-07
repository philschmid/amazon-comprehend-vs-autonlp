from datasets import load_dataset

# AG News dataset

dataset = load_dataset("ag_news")

dataset["train"].to_csv(
    "ag_news_train_comprehend_without_header.csv", index=False, header=False, columns=["label", "text"]
)
dataset["test"].to_csv(
    "ag_news_test_comprehend_without_header.csv", index=False, header=False, columns=["label", "text"]
)

dataset["train"].to_csv("ag_news_train_autonlp_with_header.csv", index=False, header=True, columns=["label", "text"])
dataset["test"].to_csv("ag_news_test_autonlp_with_header.csv", index=False, header=True, columns=["label", "text"])


# Tweet eval

dataset = load_dataset("tweet_eval", "emotion")

dataset["train"].to_csv(
    "tweet_eval_train_comprehend_without_header.csv", index=False, header=False, columns=["label", "text"]
)
dataset["test"].to_csv(
    "tweet_eval_test_comprehend_without_header.csv", index=False, header=False, columns=["label", "text"]
)

dataset["train"].to_csv(
    "tweet_eval_train_autonlp_with_header.csv", index=False, header=True, columns=["label", "text"]
)
dataset["test"].to_csv("tweet_eval_test_autonlp_with_header.csv", index=False, header=True, columns=["label", "text"])


# BANKING 77

dataset = load_dataset("banking77")


dataset["train"].to_csv(
    "banking77_train_comprehend_without_header.csv", index=False, header=False, columns=["label", "text"]
)
dataset["test"].to_csv(
    "banking77_test_comprehend_without_header.csv", index=False, header=False, columns=["label", "text"]
)

dataset["train"].to_csv("banking77_train_autonlp_with_header.csv", index=False, header=True, columns=["label", "text"])
dataset["test"].to_csv("banking77_test_autonlp_with_header.csv", index=False, header=True, columns=["label", "text"])
