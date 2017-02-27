# DeepCite
Citing original sources automatically

DeepCite is an algorithm which takes in artilces and returns not just the the citeations the article gives
but also the citations which those articles give. This then produces a tree of citeations. The algorithm 
will also return the paragraph where the infomation originates.
This allows the user to easily trace back otherwise difficult to find source and quickly figure out how reliable
a piece of information actually is.

It works by finding citation and then identifying the object that citation is referencing. Then it identifies
where that object is mentioned in the cited article and repeats the process. If that object is based on multiple
citations, as might be the case in an academic paper citing an algorithm, then the algorithm attempts to get the
most relevant citations and trace back those.

Our hope is that eventually we will be able to weight the returned citations by relevance and automatically
create citations based on the information given in an article.