import random
import boto3


def weight_choice(choice_list, weight):
    """
    :param choice_list: 待选取序列
    :param weight: list对应的权重序列
    :return:选取的值
    """
    new_list = []
    for i, val in enumerate(choice_list):
        new_list.extend(val * weight[i])
    return random.choice(new_list)


def handler(event, context):
    # session = boto3.Session(profile_name='tw-aws-beach')
    # cloudwatchClient = session.client('cloudwatch')
    cloudwatchClient = boto3.client('cloudwatch')
    randomValue = weight_choice([60, 70, 80, 90, 95], [1, 3, 3, 2, 1]) + random.randint(-5, 5)

    response = cloudwatchClient.put_metric_data(
        Namespace='MyCoolApp',
        MetricData=[
            {
                'MetricName': 'CPURate',
                'Dimensions': [
                    {
                        'Name': 'PURCHASES_SERVICE',
                        'Value': 'MyCoolService'
                    },
                    {
                        'Name': 'APP_VERSION',
                        'Value': '1.0'
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
