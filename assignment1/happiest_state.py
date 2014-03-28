import sys
import tweet_sentiment
    
def find_state(line):
    return "VA"

def statewise_sentiments(tweet_file, sent_dict):
    sentiment_dict = dict()
    for line in tweet_file.readlines():
        line_sent = tweet_sentiment.sentiment_of_one_tweet(line, sent_dict)
        if line_sent == 0 or line_sent == -1000000:
            continue
        state = find_state(line)
        if state in sentiment_dict.keys():
            sentiment_dict[state] += line_sent
        else:
            sentiment_dict[state] = line_sent
    return sentiment_dict
        
        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = tweet_sentiment.sentiment_dict(sent_file)
    state_dict = statewise_sentiments(tweet_file, sent_dict)
    print max(state_dict, key=sent_dict.get)


if __name__ == '__main__':
    main()
