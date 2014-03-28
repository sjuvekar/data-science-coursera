import json
import sys
import operator

def hashtag_dict(tweet_file):
    h_dict = dict()
    for line in tweet_file.readlines():
        json_dict = json.loads(line)
        if "entities" not in json_dict.keys():
            continue
        if "hashtags" not in json_dict["entities"].keys():
            continue
        for h in json_dict["entities"]["hashtags"]:
            h_text = h["text"].encode("utf-8")
            if h_text in h_dict.keys():
                h_dict[h_text] = h_dict[h_text] + 1
            else:
                h_dict[h_text] = 1
    return h_dict

def top_ten_hashtags(h_dict):
    return sorted(h_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[0:10]

def main():
    tweet_file = open(sys.argv[1])
    h_dict = hashtag_dict(tweet_file)
    t_ten = top_ten_hashtags(h_dict)
    for s in t_ten:
        print s[0], s[1]
        
if __name__ == "__main__":
    main()