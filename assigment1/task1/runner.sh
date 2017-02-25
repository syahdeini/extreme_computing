
hdfs dfs -rm -r /user/$USER/assignment1/task1
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/$USER/data/input -output /user/$USER/assignment1/task1 -mapper mapper.py -file mapper.py 
#hdfs dfs -cat /user/$USER/assignment1/task1/part-00000 | head -20 > .out
hdfs dfs -cat /user/$USER/assignment1/task1/* | head -20  > .out
