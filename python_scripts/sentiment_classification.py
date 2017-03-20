import json
import random
#from nltk import pos_tag, word_tokenize,FreqDist,NaiveBayesClassifier
import nltk
import pickle

class sentiment_classification:
    def __init__(self):
        self.all_tweets=None
        self.word_feature=None
    
    def load_tweets(self):
        test_tweets=[]
        allowed_words_type=['JJ','JJR','JJS','NN','NNS','NNP','NNPS','VB','VBG','VBD','VBN','VBP','VBZ']
        
        with open("/Users/jaychauhan/Twitter_Sentiment_Analysis/Tweet_Corpus/negative_tweets.json", encoding='utf-8') as data_file:
            for i in data_file:
                negative=(json.loads(i))            
                pos_tagged=[]
                words=nltk.word_tokenize(negative['text'])
                neg_words=nltk.pos_tag(words)
                for w in neg_words:
                    if w[1] in allowed_words_type and len(w[0])>2:
                        pos_tagged.append(w[0].lower())
                test_tweets.append((pos_tagged,"negative"))
                
        with open("/Users/jaychauhan/Twitter_Sentiment_Analysis/Tweet_Corpus/positive_tweets.json", encoding='utf-8') as data_file:
            for i in data_file:
                positive=(json.loads(i))            
                pos_tagged=[]
                words=nltk.word_tokenize(positive['text'])
                pos_words=nltk.pos_tag(words)
                for w in pos_words:
                    if w[1] in allowed_words_type and len(w[0])>2:
                        pos_tagged.append(w[0].lower())
                test_tweets.append((pos_tagged,"positive"))               
        return(test_tweets)
    
    def get_features(self,all_words):
        word_freq=nltk.FreqDist(all_words)
        word_features=word_freq.most_common(10000)
        return([word[0] for word in word_features])
        
    def get_words(self,all_tweets):
        all_words=[]
        for words,sentiment in all_tweets:
            all_words.extend(words)
        return(all_words)  

    def feature_extractor(self,document,word_features):
        words=set(document)
        feature={}
        for w in word_features:
            feature[w]=(w in words)
        return feature

    def classify_mod(self):
        self.all_tweets=self.load_tweets()
        self.word_feature=self.get_features(self.get_words(self.all_tweets))
        save_word_features = open("/Users/jaychauhan/Twitter_Sentiment_Analysis/pickle_files/save_word_features.pickle","wb")
        pickle.dump(self.word_feature,save_word_features)
        save_word_features.close()  
        features=[(self.feature_extractor(rev,self.word_feature),category) for rev,category in self.all_tweets]
        random.shuffle(features)
        print(len(features))
        training_set=features[:8500]
        testing_set=features[8500:]
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)

        save_classfier = open("/Users/jaychauhan/Twitter_Sentiment_Analysis/pickle_files/ssave_classfier.pickle","wb")
        pickle.dump(classifier,save_classfier)
        save_classfier.close()  
        
classification=sentiment_classification()
classification.classify_mod()