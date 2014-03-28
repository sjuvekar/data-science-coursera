register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the BIG file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-*' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subjects = GROUP ntriples BY (subject) PARALLEL 50;
DESCRIBE subjects;

-- flatten the subjects out (because group by produces a tuple of each object
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each subject
count_by_subjects = FOREACH subjects GENERATE FLATTEN($0), COUNT($1) AS count PARALLEL 50;
DESCRIBE count_by_subjects;

-- Perform a second group by on counts obtained on subjects
group_by_count = GROUP count_by_subjects BY count PARALLEL 50;
DESCRIBE group_by_count;

-- Finally, create histogram using foreach
hist = FOREACH group_by_count GENERATE $0 AS x, COUNT($1) AS y;

-- store the results in the folder /user/hadoop/example2-results
store hist into '/user/hadoop/example4-results' using PigStorage();
