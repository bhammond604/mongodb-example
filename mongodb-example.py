#!/usr/bin/python3

# Imports
import pymongo
import pprint
from sshtunnel import SSHTunnelForwarder

# Constants
MONGO_HOST = "127.0.0.1"
MONGO_DB = ""
MONGO_COLLECTION = ""
SSH_USER = ""
SSH_PASS = ""

def main():
	"""Connect to remote MongoDB and add document
	
	Arguments: None
	"""
	
	# Connect to the remote server
	server = SSHTunnelForwarder(
		MONGO_HOST,
		ssh_username=SSH_USER,
		ssh_password=SSH_PASS,
		remote_bind_address=('127.0.0.1', 27017)
	)
	
	# Start the SSH connection
	server.start()
	
	# Connect to MongoDB
	mongo_client = pymongo.MongoClient(MONGO_HOST, server.local_bind_port)

	# Connect to the database
	mongo_db = mongo_client[MONGO_DB]
	
	# Specify the collection to use
	mongo_collection = mongo_db[MONGO_COLLECTION]
	
	# Display every document
	for document in mongo_collection.find():
		print(document)
	
	# Stop SSH tunnel
	server.stop()
	
# Start the script
main()
