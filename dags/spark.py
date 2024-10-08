{
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': '@daily',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

def source1_to_s3():
    # code that writes our data from source 1 to s3
def source3_to_s3():
    # code that writes our data from source 3 to s3
def source2_to_hdfs(config, ds, **kwargs):
    # code that writes our data from source 2 to hdfs
    # ds: the date of run of the given task.
    # kwargs: keyword arguments containing context parameters for the run.

def get_hdfs_config():
    #return HDFS configuration parameters required to store data into HDFS.
    return None #Return to none

config = get_hdfs_config()

dag = DAG(
  dag_id='my_dag', 
  description='Simple tutorial DAG',
  default_args=default_args)

src1_s3 = PythonOperator(
  task_id='source1_to_s3', 
  python_callable=source1_to_s3, 
  dag=dag)

src2_hdfs = PythonOperator(
  task_id='source2_to_hdfs', 
  python_callable=source2_to_hdfs, 
  op_kwargs = {'config' : config},
  provide_context=True,
  dag=dag
)

src3_s3 = PythonOperator(
  task_id='source3_to_s3', 
  python_callable=source3_to_s3, 
  dag=dag)

spark_job = BashOperator(
  task_id='spark_task_etl',
  bash_command='spark-submit --master spark://localhost:7077 spark_job.py',
  dag = dag)

# setting dependencies
src1_s3 >> spark_job
src2_hdfs >> spark_job
src3_s3 >> spark_job
