import sys
import json
import re


def get_word_dict(words_file):
    scores = {}  # initialize an empty dictionary
    for line in words_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


def analyze_tweet(tweet, scores):
    score = 0
    text = re.compile("\w+").findall(tweet)
    for word in text:
        try:
            score += scores[word.lower()]
        except KeyError:
            pass
    return score


def main():
    words_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = get_word_dict(words_file)

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        try:
            print analyze_tweet(tweet["text"], scores)
        except KeyError:
            print 0

if __name__ == '__main__':
    main()
