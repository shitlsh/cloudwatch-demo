# cloudwatch-demo
1. cloudwatch-demo-1

创建cloudwatch event rule每分钟自动触发Lambda（Lambda功能需要自己实现，向cloudwatch     metrics里push自定义的metrics），设置alarm检测task中定义的metric，自定义并监控条件使alarm触发阈值，alarm触发SNS，SNS发告警到邮箱。
![](https://raw.githubusercontent.com/shitlsh/picture/main/img/20210626220805.png)
2. cloudwatch-demo-2

创建cloudwatch event rules，每分钟自动触发Lambda（输出固定格式的log message）。为lambda log创建metric filter，匹配log message，创建新的metric，自定义并监控条件使alarm触发阈值，alarm出发SNS，SNS发告警到邮箱。  