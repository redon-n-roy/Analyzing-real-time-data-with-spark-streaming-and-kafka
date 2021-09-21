# Analyzing real-time data with Spark Streaming and Kafka

## Project Description

The project deals with the processing the weather data from www.weatherbit.io using Kafka and Spark Streaming. Here we are simulating the streaming data using previous days data and visualizing the outcome using Matplotlib. The data processing program is developed using Python.

## Technologies Used

* Python 3.9.2
* Spark 3.1.2
* Kafka 2.8.0
* PySpark 2.4.8
* Matplotlib 3.4.3
* Hadoop 2.7.7
* kafka-python 2.0.2
* requests 2.26.0

## Features

List of features ready and TODOs for future development

* Get the data for any city my making minor changes.
* Show a set of graphs that are plotted at near real-time.
* Can use the same program for other real-time data like price of cryptocurrency with minor modifications.

To-do

* Change the data source to an actual real-time stream rather than simulation.
* Create a dashboard to display the real-time data.

## Getting Started
> All the operations below are for Windows OS

* Make sure to install the required dependencies as mentioned in the project.
* Start the Zookeeper server
```
zookeeper-server-start.bat C:\kafka\config\zookeeper.properties
```
* Start the Kafka server
```
kafka-server-start.bat C:\kafka\config\server.properties
```
* Create the required topics in Kafka
```
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic weather
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic output
```
* Clone this repository and execute the rest of the command within the directory containing the files.
```
git clone https://github.com/redon-n-roy/Analyzing-real-time-data-with-spark-streaming-and-kafka.git
```

## Usage
The following are the steps to get the program working.

* Execute the producer.py program. This will take the data from the API and start publishing to the Kafka topic "weather".
```
python producer.py
```
* Start the consumer using the Spark-Submit. This will start processing the data using Spark Structured Streaming and send the output to the Kafka topic "output".
```
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 consumer.py
```
* Execute the output.py program. This will take the data from the Kafka topic "output" and visualize it.
```
python output.py
```

## Contirbutors
* [Meenal Shree](https://github.com/meenal-shree)
* [Rushikesh Lavate](https://github.com/Rushi21-kesh)
* Neha Kumari
* Nirosha M

## License
This project uses the [MIT](./LICENSE) license.

## Reference
https://www.weatherbit.io/api

https://www.goavega.com/install-apache-kafka-on-windows/

https://phoenixnap.com/kb/install-spark-on-windows-10

https://matplotlib.org/devdocs/index.html
