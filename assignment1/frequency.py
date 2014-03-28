import json
import sys

def frequency_dict(tweet_file):
    TEXT_FIELD = "text"
    freq_dict = dict()
    for line in tweet_file.readlines():
        json_dict = json.loads(line)
        if TEXT_FIELD not in json_dict.keys():
            continue
        json_txt = json_dict[TEXT_FIELD].encode("utf-8")
        for word in json_txt.strip().split():
            if word in freq_dict.keys():
                freq_dict[word] = freq_dict[word] + 1
            else:
                freq_dict[word] = 1
    return freq_dict
    
def compute_frequency(freq_dict):
    total_freqs = float(sum(freq_dict.values()))
    for word in freq_dict.keys():
        print word, float(freq_dict[word]) / total_freqs

def main():
    tweet_file = open(sys.argv[1])
    freq_dict = frequency_dict(tweet_file)
    compute_frequency(freq_dict)
    
if __name__ == "__main__":
    main()