import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(friendTuple):
    
    personName = friendTuple[0];
    
    mr.emit_intermediate(personName, 1);
    

def reducer(personName, personCardinalities):
    
    mr.emit((personName, sum(personCardinalities)))
    
    
mr.execute(open(sys.argv[1]), mapper, reducer)