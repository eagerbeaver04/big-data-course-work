from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import chain

from datetime import datetime, timedelta
from utils import Dag, DagPipeline

default_args = {
    "retries": 3,
    "retry_delay": timedelta(seconds=30),
}

with DAG(
    dag_id="spark_ml_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
):
    generate = Dag(
        task_id="generate_data",
        command="""
docker exec spark-master \
/opt/spark/bin/spark-submit \
--master spark://spark-master:7077 \
/opt/spark/dags/generate_data.py
""",
    )
    ml = Dag(
        task_id="distributed_ml",
        command="""
docker exec spark-master \
/opt/spark/bin/spark-submit \
--master spark://spark-master:7077 \
/opt/spark/dags/distributed_ml.py
""",
    )
    clickhouse = Dag(
        task_id="write_clickhouse",
        command="""
docker exec spark-master \
/opt/spark/bin/spark-submit \
--master spark://spark-master:7077 \
/opt/spark/dags/write_clickhouse.py
""",
    )
    validate = Dag(
        task_id="validate",
        command="""
echo Pipeline finished
""",
    )
    pipeline = DagPipeline()
    pipeline.append(generate)
    pipeline.append(ml)
    pipeline.append(clickhouse)
    pipeline.append(validate)
    dags = pipeline.get()
    chain(*dags)
