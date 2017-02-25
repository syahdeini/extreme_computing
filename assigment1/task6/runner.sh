
hdfs dfs -rm -r /user/$USER/assignment1/task6
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D stream.map.output.key.field.separator=" " \
	-D stream.num.map.output.key.fields=3 \
	-D mapreduce.map.output.key.field.separator=" " \
	-D num.key.fields.for.partition=2 \
	-D mapreduce.partition.keypartitioner.options=-k1,2 \
	-input /user/$USER/assignment1/task4 \
	-output /user/$USER/assignment1/task6 \
       	-mapper mapper.py -file mapper.py \
       	-reducer reducer.py -file reducer.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
hdfs dfs -cat /user/$USER/assignment1/task6/* | head -20 > .out
	
