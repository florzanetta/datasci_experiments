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
    unknown = []
    text = re.compile("\w+").findall(tweet)
    for word in text:
        try:
            score += scores[word.lower()]
        except KeyError:
            unknown.append(word)

    for word in unknown:
        print "{} {}".format(word, score)


def main():
    words_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = get_word_dict(words_file)

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        try:
            analyze_tweet(tweet["text"], scores)
        except KeyError:
            pass

if __name__ == '__main__':
    main()
