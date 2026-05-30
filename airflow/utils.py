from dataclasses import dataclass
from airflow.operators.bash import BashOperator


@dataclass
class AirFlowConfig: ...


@dataclass
class Dag:
    task_id: str
    command: str


def _dag_to_bash_operator(dag: Dag) -> BashOperator:
    return BashOperator(task_id=dag.task_id, bash_command=dag.command)


class DagPipeline:
    def __init__(self) -> None:
        self._dags: list[Dag] = []

    def append(self, dag: Dag):
        self._dags.append(dag)

    def get(self) -> list[BashOperator]:
        return [_dag_to_bash_operator(dag) for dag in self._dags]
