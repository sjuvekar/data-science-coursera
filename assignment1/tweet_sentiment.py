import sys
import json

def sentiment_dict(sent_file):
    sent_dict = dict()
    for line in sent_file.readlines():
        tok = line.strip().split()
        phrase = " ".join(tok[0:-1])
        score = int(tok[-1])
        sent_dict[phrase] = score    
    return sent_dict

def sentiment_of_one_tweet(tweet_line, sent_dict):
    TEXT_FIELD = "text"
    sent_score = 0
    json_dict = json.loads(tweet_line)
    if TEXT_FIELD not in json_dict.keys():
        return -1000000
    json_txt = json_dict[TEXT_FIELD].encode("utf-8")
    json_toks = json_txt.strip().split()
    for i in range(len(json_toks)):
        if i < len(json_toks) - 1:
            word = json_toks[i] + " " + json_toks[i+1]
            if word in sent_dict.keys():
                sent_score += sent_dict[word]
        word = json_toks[i]
        if word in sent_dict.keys():
            sent_score += sent_dict[word]
    return sent_score 
        
    
def compute_sentiments(tweet_file, sent_dict):    
    for line in tweet_file.readlines():
        sent_score = sentiment_of_one_tweet(line, sent_dict)
        if sent_score == -1000000:
            continue
        print "%f" % sent_score
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = sentiment_dict(sent_file)
    compute_sentiments(tweet_file, sent_dict)
    
    
if __name__ == '__main__':
    main()
