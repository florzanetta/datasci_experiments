import sys
import json
import operator

frequency = {}


def analyze_tweet(hashtags):
    global frequency

    for ht in hashtags:
        try:
            frequency[ht["text"]] += 1
        except KeyError:
            frequency[ht["text"]] = 1


def main():
    tweet_file = open(sys.argv[1])

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        try:
            analyze_tweet(tweet["entities"]["hashtags"])
        except KeyError:
            pass

    global frequency
    items = sorted(frequency.iteritems(), key=operator.itemgetter(1), reverse=True)
    for ht, freq in items[0:10]:
        print "{} {}".format(ht, freq)

if __name__ == '__main__':
    main()

