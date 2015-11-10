import MapReduce
import sys
import collections

mr = MapReduce.MapReduce()

friendshipsGraph = collections.defaultdict(list)


def mapper(friendTuple):
    
    personName = friendTuple[0]
    friendName = friendTuple[1]
    
    friendshipsGraph[personName].append(friendName)
    mr.emit_intermediate(personName, friendName)
    

def reducer(personName, personFriends):
    
    for personFriend in personFriends:
        if (personName not in friendshipsGraph[personFriend]):
            mr.emit((personName, personFriend))
            mr.emit((personFriend, personName))
    
    
mr.execute(open(sys.argv[1]), mapper, reducer)