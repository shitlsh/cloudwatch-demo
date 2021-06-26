import random
import boto3


def handler(event, context):
    cloudwatchClient = boto3.client('cloudwatch')
    sampleList = [60, 70, 80, 90, 95]
    randomValue = random.choices(sampleList, weights=(30, 20, 15, 10, 5))[0] + random.randint(-5, 5)

    response = cloudwatchClient.put_metric_data(
        Namespace='SimCpuMonitor',
        MetricData=[
            {
                'MetricName': 'CPURate',
                'Dimensions': [
                    {
                        'Name': 'HOST_NAME',
                        'Value': 'TailongdeMac'
                    },
                ],
                # 'Timestamp': datetime(2015, 1, 1),
                'Value': randomValue,
                'Unit': 'Percent'
                # 'StatisticValues': { 'SampleCount': 123.0, 'Sum': 123.0, 'Minimum': 123.0, 'Maximum': 123.0 },
                # 'Values': [ 123.0, ], 'Counts': [ 123.0, ], 'Unit': 'Seconds' | 'Microseconds' | 'Milliseconds' |
                # 'Bytes' | 'Kilobytes' | 'Megabytes' | 'Gigabytes' | 'Terabytes' | 'Bits' | 'Kilobits' | 'Megabits' |
                # 'Gigabits' | 'Terabits' | 'Percent' | 'Count' | 'Bytes/Second' | 'Kilobytes/Second' |
                # 'Megabytes/Second' | 'Gigabytes/Second' | 'Terabytes/Second' | 'Bits/Second' | 'Kilobits/Second' |
                # 'Megabits/Second' | 'Gigabits/Second' | 'Terabits/Second' | 'Count/Second' | 'None',
                # 'StorageResolution': 123
            },
        ]
    )
    print(response)
