
hdfs dfs -rm -r /user/$USER/assignment1/task4
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/$USER/assignment1/task2 -output /user/$USER/assignment1/task4 -mapper mapper.py -file mapper.py -combiner combiner.py -file combiner.py -reducer reducer.py -file reducer.py
hdfs dfs -cat /user/$USER/data/output_task4/part-00000  | head -20 > .out
#hdfs dfs -cat /user/$USER/data/output/* | sort > ww.out
