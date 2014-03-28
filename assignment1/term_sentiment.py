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

def term_sentiment_dict(tweet_file, sent_dict):
    term_sent_dict = dict()
    for line in tweet_file.readlines():
        json_dict = json.loads(line)
        if "text" not in json_dict.keys():
            continue
        json_txt = json_dict["text"].encode("utf-8")
        json_toks = json_txt.strip().split()
        sent_score = 0
        for word in json_toks:
            try:
                sent_score += sent_dict[word]
            except:
                pass
        for word in json_toks:
            if word in term_sent_dict.keys():
                term_sent_dict[word] = term_sent_dict[word] + sent_score
            else:
                term_sent_dict[word] = sent_score
    for word in term_sent_dict.keys():
        print "%s %f" % (word, term_sent_dict[word])
        
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = sentiment_dict(sent_file)
    term_sentiment_dict(tweet_file, sent_dict)


if __name__ == '__main__':
    main()
