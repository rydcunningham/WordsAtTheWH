import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time
from bs4 import BeautifulSoup
import streamer

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

def main(p):
	try:
		page = p
		sourceCode = opener.open(page).read()
		print "read source code using opener"
		#print sourceCode
		#prints out the entire HTML file. Now let's pull the links from the RSS feed

		try:
			#titles = re.findall(r'<title>(.*?)</title>',sourceCode)
			#in regular expressions, a period represenys any character
			links = re.findall(r'<link>(.*?)</link>',sourceCode)
			#for title in titles:
			#	print title
			for link in links:
				if '.rdf' in link:
					pass
				elif link == p:
					pass
				else:
					#Let's go ahead and open that link so we can pull content from there
					#Regex stuff
					#? = 0 or 1 repetitions
					#. = any character except for a new line
					#\w = any letter
					#* = 0 or more repetitions
					#+ = 1 or more repetitions
					#| is or sign
					contentlist = []
					linkSource = opener.open(link).read()
					soup = BeautifulSoup(linkSource)
					article = soup.find('div', {'id' : 'content'}).text
					#content = c[c.index("The White House"):c.index("Latest blog posts")
					#content = [p.string for p in main_div.findAll('p')]
					"""
					print ""
					print "Begin content"
					print "----------------------------------"
					print article
					print "----------------------------------"
					print ""
					"""
					output = "%s. See for yourself:" % (first_five(article))
					print "%s %s" % (output, link)
					print len(output)+19
					time.sleep(5)
					#so what do we split the bottom content with? HuffPo has a bar.
					#It's up to you to find the separator on other websites.
		except Exception, e:
			print str(e)
	except Exception, e:
		print str(e)

def first_five(text):
	words = text.split()
	worddict = {}
	 
	stopwords = ['a', 'a', 'able', 'about', 'about', 'above', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'after', 'after', 'afterwards', 'again', 'again', 'against', 'against', 'ah', 'all', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'am', 'among', 'amongst', 'an', 'an', 'and', 'and', 'announce', 'another', 'any', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'applause', 'approximately', 'are', 'are', 'aren', 'arent', 'aren\'t', 'arise', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'at', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'be', 'be', 'became', 'because', 'because', 'become', 'becomes', 'becoming', 'been', 'been', 'before', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'being', 'believe', 'below', 'below', 'beside', 'besides', 'between', 'between', 'beyond', 'biol', 'both', 'both', 'brief', 'briefly', 'but', 'but', 'by', 'by', 'c', 'ca', 'came', 'can', 'cannot', 'cannot', 'can\'t', 'can\'t', 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'could', 'couldnt', 'couldn\'t', 'd', 'date', 'did', 'did', 'didn\'t', 'didn\'t', 'different', 'do', 'do', 'does', 'does', 'doesn\'t', 'doesn\'t', 'doing', 'doing', 'done', 'don\'t', 'don\'t', 'down', 'down', 'downwards', 'due', 'during', 'during', 'e', 'each', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'from', 'further', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'gone', 'got', 'gotten', 'h', 'had', 'had', 'hadn\'t', 'happens', 'hardly', 'has', 'has', 'hasn\'t', 'hasn\'t', 'have', 'have', 'haven\'t', 'haven\'t', 'having', 'having', 'he', 'he', 'hed', 'he\'d', 'he\'ll', 'hence', 'her', 'her', 'here', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'here\'s', 'hereupon', 'hers', 'hers', 'herself', 'herself', 'hes', 'he\'s', 'hi', 'hid', 'him', 'him', 'himself', 'himself', 'his', 'his', 'hither', 'home', 'how', 'how', 'howbeit', 'however', 'how\'s', 'hundred', 'i', 'i', 'id', 'i\'d', 'ie', 'if', 'if', 'i\'ll', 'i\'ll', 'im', 'i\'m', 'immediate', 'immediately', 'importance', 'important', 'in', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'into', 'invention', 'inward', 'is', 'is', 'isn\'t', 'isn\'t', 'it', 'it', 'itd', 'it\'ll', 'its', 'its', 'it\'s', 'itself', 'itself', 'i\'ve', 'i\'ve', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'let\'s', 'like', 'liked', 'likely', 'line', 'little', '\'ll', 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'more', 'moreover', 'most', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'mustn\'t', 'my', 'my', 'myself', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'nor', 'normally', 'nos', 'not', 'not', 'noted', 'nothing', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'of', 'off', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'on', 'once', 'once', 'one', 'ones', 'only', 'only', 'onto', 'or', 'or', 'ord', 'other', 'other', 'others', 'otherwise', 'ought', 'ought', 'our', 'our', 'ours', 'ours',\
	'ourselves', 'ourselves', 'out', 'out', 'outside', 'over', 'over', 'overall', 'owing', 'own', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'shan\'t', 'she', 'she', 'shed', 'she\'d', 'she\'ll', 'she\'ll', 'shes', 'she\'s', 'should', 'should', 'shouldn\'t', 'shouldn\'t', 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'so', 'so', 'some', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'such', 'sufficiently', 'suggest', 'sup', 'sure', 'than', 'that', 'thats', 'that\'s', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'there\'s', 'these', 'they', 'they\'d', 'they\'ll', 'they\'re', 'they\'ve', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn\'t', 'we', 'we\'d', 'we\'ll', 'well', 'were', 'we\'re', 'weren\'t', 'we\'ve', 'what', 'what\'s', 'when', 'when\'s', 'where', 'where\'s', 'which', 'while', 'who', 'whom', 'who\'s', 'why', 'why\'s', 'with', 'won\'t', 'would', 'wouldn\'t', 'you', 'you\'d', 'you\'ll', 'your', 'you\'re', 'yours', 'yourself', 'yourselves', 'you\'ve', '--', 'mr.', 'ms.', 'mrs.', '', 'will', 'earnest', 'members', 'president', 'united', 'states', 'american', 'america', 'carney']

	for word in words:
	    word =  re.sub(r'[^a-zA-Z0-9 ]', "", word)
	    if len(word) > 1:
		    if word.lower() not in stopwords:
		    	if word not in worddict:
		    		worddict[word] = 1
	        	else:
	        		worddict[word] += 1
	 
	wordcount = sorted(worddict.items(), key=lambda x: x[1], reverse=True)
	return "The words of the day at the White House are: %s, %s, %s, %s, %s" % (wordcount[0][0], wordcount[1][0], wordcount[2][0], wordcount[3][0], wordcount[4][0])


main('http://www.whitehouse.gov/feed/press')