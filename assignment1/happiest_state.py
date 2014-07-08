import sys
import json
import re
import operator

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

happiest_places = {}

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

def happy_place(place, score):
    place = place.lower()
    for abr, name in states.items():
        abr = abr.lower()
        name = name.lower()
        if place.find(name) != -1 or place.find(abr) != -1:
            try:
                happiest_places[abr.upper()] += score
            except KeyError:
                happiest_places[abr.upper()] = score

def main():
    words_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = get_word_dict(words_file)

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        try:
            score = analyze_tweet(tweet["text"], scores)
            happy_place(tweet["place"]["full_name"], score)

        except (KeyError, TypeError):
            pass

    items = sorted(happiest_places.iteritems(), key=operator.itemgetter(1), reverse=True)
    print items[0][0]


if __name__ == '__main__':
    main()
