# AWS-Orchestrating the Data Pipeline-Chapter 10

# Description

This Chapter will help us to understand :

1. How to decide the best option for Data Pipeline orchestation on AWS between ***MWAA(Airflow) & AWS Step Functions*** ? 
2. DEMO - 1
3. ***Study case about*** - How to extract data from Youtube Channel and orchestrate  it with AWS Step functions
4. Data Stats Channel
5. Data Video Features

# How to decide the best option for Data Pipeline orchestation ? 

![table](https://github.com/alexbonella/AWS-StudyClub/blob/upload_chapter10_2104/infra_demo/Airflow_VS_Step_Functions.png)

# DEMO - 1

For our Step Function state machine, we are going to start by using a Lambda function that checks the extension of an incoming 
file to determine the type of file. Once determined, we'll pass that information on to the next state, which is a CHOICE state. If it
is a file type we support, we'll call a Lambda function to process the file, but if it's not, we'll send out a notification, indicating that we cannot process the file.

If the Lambda function fails, we'll send a notification to report on the failure; otherwise,
we will end the state machine with a SUCCESS status.

![demo1](https://github.com/alexbonella/AWS-StudyClub/blob/upload_chapter10_2104/infra_demo/demo_chapter10.png)

# How to extract data from Youtube Channel and orchestrate  it with AWS Step functions ?

![demo2](https://github.com/alexbonella/AWS-StudyClub/blob/upload_chapter10_2104/infra_demo/infra_chapter_10_de.png)

# Data Stats Channel 

* Go to Data  👉 [Stats Channel](https://github.com/alexbonella/AWS-StudyClub/tree/upload_chapter10_2104/stats_channel)

# Data Video Features

* Go to Data  👉  [Video Featuresl](https://github.com/alexbonella/AWS-StudyClub/tree/upload_chapter10_2104/video_feature_data)


