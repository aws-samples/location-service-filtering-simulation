from datetime import datetime
import json
import os
import requests
import boto3
client = boto3.client('location')
def build_response(event, status):
    """A utility function used to build a response to CloudFormation"""

    response_data = {
        'Status': status,
        'Reason': 'Success',
        'PhysicalResourceId': 'myapp::{}'.format(event['LogicalResourceId']),
        'Data': {},
        'RequestId': event['RequestId'],
        "LogicalResourceId": event["LogicalResourceId"],
        "StackId": event["StackId"],
    }
    return response_data
def lambda_handler(event, context):
  request_type = event["RequestType"]
  if request_type == "Create":  
    Trackers = {
      "DistanceFilteringTracker": "Distance",
      "AccuracyFilteringTracker": "Accuracy",
      "TimeFilteringTracker": "Time"   
      }
    Collections = {
      "DistanceFilteringCollection": "Distance",
      "AccuracyFilteringCollection": "Accuracy",
      "TimeFilteringCollection": "Time"  
    }
    geofence_geom = [
              [
                -97.14111328125,
                37.35269280367274
              ],
              [
                -94.94384765625,
                37.35269280367274
              ],
              [
                -94.94384765625,
                38.06539235133249
              ],
              [
                -97.14111328125,
                38.06539235133249
              ],
              [
                -97.14111328125,
                37.35269280367274
              ]
            ]
    try:
      for tracker in Trackers:
        tracker_info = client.describe_tracker(
          TrackerName=tracker
          )
        tracker_arn = tracker_info['TrackerArn']
        tags = client.tag_resource(
          ResourceArn = tracker_arn,
          Tags = {
            "Filtering": Trackers[tracker]
          }
          )
      for collection in Collections:
        collection_info = client.describe_geofence_collection(
            CollectionName = collection
            )
        collection_arn = collection_info['CollectionArn']
        tags = client.tag_resource(
          ResourceArn = collection_arn,
          Tags = {
            "Filtering": Collections[collection]
          }
          )
        geofence = client.put_geofence(
          CollectionName = collection,
          GeofenceId = "FilteringGeofence",
          Geometry = {
            'Polygon': [
              geofence_geom
              ]
          }
          )
      response_url = event['ResponseURL']
      response_data = build_response(event, 'SUCCESS')
      result = requests.put(response_url, data=json.dumps(response_data))
      print("Created!")
    except Exception as e:
      # Catch any exceptions and ensure we always return a response
      
      print(e)
      response_data = build_response(event, 'FAILED')
      response_url = event['ResponseURL']
      result = requests.put(response_url, data=json.dumps(response_data))
    return result

  elif event["RequestType"] == "Delete":
    response_data = build_response(event, 'SUCCESS')
    response_url = event['ResponseURL']
    result = requests.put(response_url, data=json.dumps(response_data))
    return result
  print(json.dumps(event))
  #return result