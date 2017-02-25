
hdfs dfs -rm -r /user/$USER/assignment1/task7_1
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D stream.num.map.output.key.fields=2 \
	-D num.key.fields.for.partition=2 \
	-D mapreduce.partition.keypartitioner.options='-k1,1n -k2,2r' \
	-input /user/$USER/data/input_part2 \
	-output /user/$USER/assignment1/task7_1 \
       	-mapper mapper.py -file mapper.py \
       	-reducer reducer.py -file reducer.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner



hdfs dfs -rm -r /user/$USER/assignment1/task7
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D stream.num.map.output.key.fields=2 \
	-D num.key.fields.for.partition=2 \
	-D mapreduce.partition.keypartitioner.options='-k1,1n -k2,2r' \
	-input /user/$USER/assignment1/task7_1 \
	-output /user/$USER/assignment1/task7 \
      	-mapper mapper2.py -file mapper2.py \
       	-reducer reducer2.py -file reducer2.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner




hdfs dfs -cat /user/$USER/assignment1/task7/* | sort > .out
