
hdfs dfs -rm -r /user/$USER/assignment1/task5
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	  -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	-D mapred.reduce.tasks=1 \
	 -D mapred.text.key.comparator.options=-k1nr \
	-input /user/$USER/assignment1/task4 \
	-output /user/$USER/assignment1/task5 \
       	-mapper mapper.py -file mapper.py \
	-combiner combiner.py -file combiner.py \
       	-reducer reducer.py -file reducer.py
hdfs dfs -cat /user/$USER/assignment1/task5/* > *.out
			
