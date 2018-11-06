#creating  clusters of aurora serverless
import boto3

client = boto3.client('rds')


def client_raise_aurora_instance(event, context):
	client.start_db_cluster(DBClusterIdentifier='fast_query')
	client.start_db_cluster(DBClusterIdentifier='medium_query')
	client.start_db_cluster(DBClusterIdentifier='slow_query')
	return "Spinning up clusters"