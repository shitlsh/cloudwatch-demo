# cloudwatch-demo
## description
This is a demo for aws cloudwatch, contains two type of custom metric.Use GithubAction as CI pipeline.

**ScheduledRule**: Trigger Lambda Function every minute, should be assigned the invoking permission

**LambdaFunction**: Put a custom metric & print a json log event, should be assigned the *PutMetricData* permission.

**MetricFilter**: Match the json log event & read value form it & transfer value into a metric

**CloudwatchAlarm**: add alarm rule for these two metrics

**SNS**: alarm actions trigger SNS send an email

**GitActions**: 
* Build python code to a docker image
* Upload image to ECR
* Deploy cloudformation, use imageUri as a parameter for creating lambda function.

![](https://raw.githubusercontent.com/shitlsh/picture/main/img/20210626220805.png)

## how to use
### use github-hosted runner
if you have an aws access user, you can use github-hosted runner, go to ``Settings->Secrets->Actions`` add two new repository secrets.

remove the annotation for the below key.
```yaml
aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```
### use self-hosted runner
Cause our learning account doesn't have the permission to create an access user, so I choose to use self-hosted runner.

There are two ways:
* use your own laptop
* use an EC2 instance

You can simply follow [adding-self-hosted-runners](https://docs.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners). In this case, your runner's credentials must have permissions to call any AWS APIs called by your Actions workflow.
Or, you can use this action to assume a role, and then use the role credentials for all AWS API calls made by your Actions workflow:
```yaml
uses: aws-actions/configure-aws-credentials@v1
with:
  aws-region: ap-southeast-2
  role-to-assume: my-github-actions-role
```
If you are using your laptop as a runner, make sure the profile is default.Because when no access key credentials are given in the action inputs, this action will use credentials from the runner environment using the default methods for the AWS SDK for Javascript.
### configure email address
Add your email address to ``Settings->Secrets->Actions`` named ``MY_EMAIL_ADDRESS``
### build & deploy
The workflows will be triggered when push a tag like ``v0.1.*``
```shell
git tag v0.1.*
git push origin v0.1.*
```