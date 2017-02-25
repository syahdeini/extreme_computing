hdfs dfs -rm -r /user/$USER/assignment2/task2_1
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D stream.num.map.output.key.fields=1 \
	-D mapreduce.partition.keypartitioner.options=-k1 \
	 -D mapreduce.partition.keycomparator.options=-k1,1n \
	-input /user/$USER/assignment2/input/task4 \
	-output /user/$USER/assignment2/task2_1 \
    -mapper mapper.py -file mapper.py \
    -combiner combiner.py -file combiner.py \
    -reducer reducer.py -file reducer.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner



hdfs dfs -rm -r /user/$USER/assignment2/task2_2
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D mapred.reduce.tasks=1 \
	--D stream.num.map.output.key.fields=2 \
	-D mapreduce.partition.keypartitioner.options=-k1 \
	 -D mapreduce.partition.keycomparator.options=-k2,2nr \
	-input /user/$USER/assignment2/task2_1 \
	-output /user/$USER/assignment2/task2_2 \
    -mapper mapper2.py -file mapper2.py \
    -reducer reducer2.py -file reducer2.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat /user/$USER/assignment2/task2_2/* | sort -k2,2nr > *.out



	


