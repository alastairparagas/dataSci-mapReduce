import MapReduce
import sys

mr = MapReduce.MapReduce();

def mapper(document):
    documentName = document[0];
    documentContents = document[1];
    
    documentContentsTokens = documentContents.split()
    
    for token in documentContentsTokens:
        mr.emit_intermediate(token, documentName)

def reducer(word, documentNames):
    mr.emit((word, list(set(documentNames))))
    
mr.execute(open(sys.argv[1]), mapper, reducer);