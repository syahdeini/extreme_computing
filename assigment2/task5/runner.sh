hdfs dfs -rm -r /user/$USER/assignment2/task5
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	 -D mapred.reduce.tasks=1 \
	-input /user/$USER/assignment2/input/task5 \
	-output /user/$USER/assignment2/task5 \
    	-mapper mapper.py -file mapper.py \
    	-reducer reducer.py -file reducer.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat /user/$USER/assignment2/task5/* > *.out
