import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(dnaSequence):
    
    dnaSequenceId = dnaSequence[0]
    dnaNucleotidesTrimmed = dnaSequence[1][:-10].strip()
    
    mr.emit_intermediate(1, dnaNucleotidesTrimmed);


def reducer(dnaSequenceId, dnaNucleotides):
    
    uniqueDnaNucleotides = list(set(dnaNucleotides))
    
    for dnaNucleotide in uniqueDnaNucleotides:
        mr.emit(dnaNucleotide)
            
    
    
mr.execute(open(sys.argv[1]), mapper, reducer);