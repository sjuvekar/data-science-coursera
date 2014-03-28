register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- Filter the tuples by subject
filter1 = FILTER ntriples BY subject matches '.*business.*';
DESCRIBE filter1;

-- Copy the filter explicitly, renaming the columns
filter2 = FOREACH filter1 GENERATE subject AS subject2, predicate AS predicate2, object AS object2;
DESCRIBE filter2
 
-- Finally, perform the required join the subject
common = JOIN filter1 BY subject, filter2 BY subject2;
DESCRIBE common;

-- store the results in the folder /tmp
store common into '/tmp/finaloutput' using PigStorage();
