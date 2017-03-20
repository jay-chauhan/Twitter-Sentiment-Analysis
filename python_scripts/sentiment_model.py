#from nltk import pos_tag, word_tokenize,FreqDist,NaiveBayesClassifier
import pickle

class sentiment_model:
    
    def __init__(self):
        save_word_features_f = open("/Users/jaychauhan/Twitter_Sentiment_Analysis/pickle_files/save_word_features.pickle","rb")
        self.save_word_features = pickle.load(save_word_features_f)
        save_word_features_f.close()
        
        classifier_f = open("/Users/jaychauhan/Twitter_Sentiment_Analysis/pickle_files/save_classfier.pickle", "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()
        
    def feature_extractor(self,document):
        words=set(document)
        feature={}
        for w in self.save_word_features:
            feature[w]=(w in words)
        return feature
    
    def classify_tweets(self,text):
        features=self.feature_extractor(text.split())
        return(self.classifier.classify(features))
