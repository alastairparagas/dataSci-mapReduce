# Map Reduce
> Data Manipulation at Scale: Systems and Algorithms

![](http://twimgs.com/ddj/images/article/2013/0313/hadoopfig2.gif)

The following is my Python assignment turn-ins on the ["Data Manipulation at Scale: Systems and Algorithms"](https://www.coursera.org/learn/data-manipulation) course at Coursera (taught at University of Washington). 

The class goes in depth to the application of statistics and structures in the technology field to organize and find correlations on data, starting off with relational algebra (an abstraction) and its implementation (Structured Query Language - SQL - used at relational databases that powers apps and websites). It then proceeds to certain algorithms like [MapReduce](http://research.google.com/archive/mapreduce.html) that is pioneered by Google (and open-source, free software systems like [Apache Hadoop](https://hadoop.apache.org) that make it a reality) and non-SQL databases (the NoSQL movement) that do not use SQL (making them harder to use and a focus on doing things manually when storing data) but with the benefit of scalability - databases can now be on multiple servers.

This assignment has 6 parts:
  
* In `unique_trims.py`, the program filters through `dna.json`, and counts the occurence of a certain DNA sequence, where the DNA sequence we are looking for is the first parameter in the array of each line input in `dna.json` and the search space is the second parameter in the array of each line input in `dna.json`
* In `friend_count.py`, using the relations specified on `friends.json`, return a count of friends of a person.
* In `asymmetric_friendships.py`, using the data at `friends.json`, return a graph of people and those people they follow but don't follow back.
* In `multiply.py`, do a matrix multiplication of the matrix at `matrix.json`

And many more...


To make these files run on your computer, make sure you have Python installed and using the command line/terminal, run 

`python <oneOfThePythonFilesHere> <additionalArgumentsNeeded>`