from __future__ import division
import sys
import json
import re


frequency = {}
word_count = 0


def analyze_tweet(tweet):
    global frequency
    global word_count

    text = re.compile("\w+").findall(tweet.lower())
    for word in text:
        try:
            frequency[word] += 1
        except KeyError:
            frequency[word] = 1

        word_count += 1

def main():
    tweet_file = open(sys.argv[1])

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        try:
            analyze_tweet(tweet["text"])
        except KeyError:
            pass

    for word, freq in frequency.items():
        global word_count
        print "{} {}".format(word, freq/word_count)

if __name__ == '__main__':
    main()
