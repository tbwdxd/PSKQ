## What is PSKQ

PSKQ stands for Spark Spacial Keyword Query System, which was first initialized by Hwasung Lee with Dr. Yun Tian in the Cloud Computing Lab at California State University, Fullerton.

The project  is focusing on solving Spacial Keyword Query based on real distance by utilizing Voroni Algorithms and Apache Spark.

Also, Bowen Tian, Yijie Sun, Suraj Bennur, Brandon Huebert, Yuting Zhang, Sahar Ghanei, Vikram Harish Swaminathan, Danqi Chen are participated as project researchers.

## Current State

PSKQ phase one was partially completed with low-performance result. The reason is we did not implemented garbage collection (or the lack of customize our unique library).

## Our Effort

We are trying to migrate all current project from python based code into scala based code, which we believe will increase the performance significantly.

## sbt Installation
```
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
sudo apt-get update
sudo apt-get install sbt

```
