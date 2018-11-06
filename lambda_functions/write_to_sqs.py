import boto3
import random
# Get the service resource
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='aurora-sqs')


def write_to_sqs(event, context):
	# Create a new message
	response = queue.send_message(MessageBody='val1 + val2')



