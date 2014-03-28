register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the big file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- Filter the tuples by subject
filter1 = FILTER ntriples BY subject matches '.*rdfabout\\.com.*';
DESCRIBE filter1;

-- Copy the filter explicitly, renaming the columns
filter2 = FOREACH filter1 GENERATE subject AS subject2, predicate AS predicate2, object AS object2;
DESCRIBE filter2
 
-- Finally, perform the required join the subject
common = JOIN filter1 BY object, filter2 BY subject2;
DESCRIBE common;

common_distinct = DISTINCT common;

-- store the results in the folder /tmp
store common_distinct into '/user/hadoop/example3-results' using PigStorage();
