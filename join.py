import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(dbTuple):
    
    dbIdentifier = dbTuple[1];
    
    mr.emit_intermediate(dbIdentifier, dbTuple)


def reducer(dbIdentifier, dbTuples):
    
    oneSideTuple = [];
    
    for dbTuple in dbTuples: 
        if dbTuple[0] == "order":
            oneSideTuple = dbTuple
            dbTuples.remove(dbTuple)
            break
            
    for dbTuple in dbTuples:
        mr.emit(oneSideTuple + dbTuple)
            
    
    
mr.execute(open(sys.argv[1]), mapper, reducer);