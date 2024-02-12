from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from main import flow_full_operation

deployment = Deployment.build_from_flow(
    flow=flow_full_operation,
    name="memgraph_failover",
    work_queue_name="queue_memgraph_failover_application",
    work_pool_name='pool_memgraph_failover_application',
    tags=['memgraph_failover_application']
)

if __name__ == "__main__":
    deployment.apply()
