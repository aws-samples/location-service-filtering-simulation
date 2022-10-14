# Location Service Tracker Filtering Simulation

This project contains source code and supporting files for Tracker and geofence resources associated with the Blog "Cost Effective Amazon Location Service Tracker Filtering" it includes the followings files and folders

- custom_resource - Code for the Lambda function that tags trackers and geofences and creates geofences for each collection
- events - Invocation events that you can use to invoke the function.
- mqtt_update_function - Code for the Lambda to connect IoT Core to Amazon Location Service Trackers
- template.yaml - A template that defines the application's AWS resources.

## Deployment
To deploy this solution, use the SAM CLI:
```bash
sam build
```

```bash
sam deploy --guided
```

Follow the prompts as such:
```bash
Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Not found

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-app]: location-filtering
        AWS Region [<Your region>]: <Press Enter>
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [y/N]: y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: y
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [y/N]: <Press Enter>
        Save arguments to configuration file [Y/n]: y
        SAM configuration file [samconfig.toml]: <Press Enter>
        SAM configuration environment [default]: <Press Enter>
```

## Cleanup

To delete the sample application that you created, use the SAM CLI:

```bash
sam destroy
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.
