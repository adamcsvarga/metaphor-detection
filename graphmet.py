#!/usr/bin/python
# -*- coding: ISO-8859-2 -*-

"""
Calculating the Google Distance Graph between sentences in a corpus

Google AJAX Search Module
http://code.google.com/apis/ajaxsearch/documentation/reference.html
"""
import json
import urllib
import math

def showsome(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  # Optional extra logging
 # hits = data['results']
  
 # print 'Top %d hits:' % len(hits)
  #for h in hits: print ' ', h['url']
  #print 'For more results, see %s' % data['cursor']['moreResultsUrl']
  
  #print int(data['cursor']['estimatedResultCount'])
  #return data[0]['responseData']['cursor']['estimatedResultCount']

        
def google_dist(word1, word2):
    query = '"'+word1+'"'
    #print query
    first_occ=showsome(query)
    #print first_occ
    
    query = '"'+word2+'"'
    #print query
    second_occ=showsome(query)
    #print second_occ
    
    query='allintext: '+word1+' '+word2
    joint_occ=showsome(query)
    inv_gd=(math.log(float(max(first_occ,second_occ)))-math.log(float(joint_occ)))/(21.39-math.log(float(min(first_occ,second_occ))))
    #inv_gd=1-inv_gd
    return inv_gd
    
def weight_sentence(sentence):
	words=sentence.split()
	length=0
	for word in words:
	 length+=1
	word_graph=[[0]*length for i in range(length)]
	
	#print length
	
	for i in range(0, length):
	 for j in range(0, length):
	  if j>i:
	   word_graph[i][j]=google_dist(words[i], words[j])
	   #print word_graph[i][j]
	count=0
	avg=0
	for i in range(0,length-1):
         for j in range(0,length-1):
          if j>i:
           avg+=word_graph[i][j] 
           count+=1
   
    	avg=avg/count
        return avg
        
def compare(weight1, weight2):
	print 'Weight of sentence: %s '%(weight1)
	print 'Weight of sentence w\out target words: %s '%(weight2)
	
	if weight1>weight2:
	 print 'Target words are used metaphorically.'
	else:
	 print 'Target words are used literally.'
        
def read_file(filename):
	f=open(filename)
	line=f.readline()
	
	while line:
	 sentence=line
	# print sentence
	 sentence_weight=weight_sentence(sentence)
	 rmvd_sentence=f.readline()
	# print rmvd_sentence
	 rmvd_sentence_weight=weight_sentence(rmvd_sentence)
	 compare(sentence_weight,rmvd_sentence_weight)
	 line=f.readline()
	f.close()
	
    
    
if __name__ == "__main__":
    #import sys
    
    read_file("corpus.txt")
    
   

  
    
    
    
    
  
