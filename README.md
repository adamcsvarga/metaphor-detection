# Automatic Metaphorical Phrase Detection
## Created by Adam Varga, 2014

This tool was used for experimenting with the automatic detection of metaphorical and/or idiomatic phrases in texts. The program calculates constructs a
full weighted graph for each sentence (the words being its nodes), where the weight is the [Google Distance](https://en.wikipedia.org/wiki/Normalized_Google_distance)
between two words, which serves as an automatic semantic distance measure. This version operated on an offline corpus, i. e. downloaded webpages.

For each word in the sentence, the program checks whether removing that word from the sentence increases or decreases the average weight of the graph. 
The hypothesis is that if words are used metaphorically/idiomatically, the average weight will decrease due to the shorter semantic distance between the other
words used literally. 