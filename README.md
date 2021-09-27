<h1 align='Center'> Analyzing real-time data with Spark Streaming and Kafka</h1>

![ban](https://user-images.githubusercontent.com/61430438/134847738-85341b01-cccd-4be5-a01d-dd73d5549f60.png)

## Project Description

&#160;&#160;&#160;&#160;&#160;The project deals with the processing the weather data from www.weatherbit.io using Kafka and Spark Streaming. Here we are simulating the streaming data using previous days data. Then we used a PySpark program to run the spark SQL queries to process the data consumed from the kafka topic along with their required dependencies and finally publish the processed data to another Kafka topic. Then we will consume the data into another python program and plotted the real time graph using Matplotlib.


## Workflow
<p align='center'>
<img src="https://user-images.githubusercontent.com/61430438/134847903-91414708-78bd-45ba-be25-6c21b895cd77.png" width="800" height="300">
</p>

## Technologies Used

* Python 3.9.2
* Spark 3.1.2
* Kafka 2.8.0
* PySpark 2.4.8
* Matplotlib 3.4.3
* Hadoop 2.7.7
* kafka-python 2.0.2
* requests 2.26.0

   <p align='center'>
  <img src="https://user-images.githubusercontent.com/61430438/133730265-6c9c8f4a-9675-46dd-a24a-7eb630ec6afc.png" alt="python" width="60" height="60"/> 
   &#160;&#160;&#160;&#160;
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRa479E6j4fipjDOpxCNJcuhMO9U4Ewuur-3dfxOTQrFRLd46j7WOW9zUO3dlOp8WojB6k&usqp=CAU" alt="kafka" width="150" height="60"/>
  &#160;&#160;&#160;&#160;
  <img src="https://user-images.githubusercontent.com/61430438/133730487-d4f8501e-378d-44b0-baf0-6c05d3497509.png" alt="spark" width="150" height="60"/> 
   &#160;&#160;&#160;&#160;
  <img src="https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-icon.svg" alt="hadoop" width="60" height="60"/> 
   &#160;&#160;&#160;&#160;
  <img src="https://user-images.githubusercontent.com/61430438/134849819-7d137789-ee8b-4089-9385-6ef1965c6894.png" alt="matplotlib" width="130" height="60"/>
    <img src="https://user-images.githubusercontent.com/61430438/134850007-31da8908-f434-4770-8993-083a854b206a.png" alt="request" width="60" height="80"/>
</p>


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

## Output
<p align='center'>
<img src ="https://user-images.githubusercontent.com/61430438/134848005-b8d75b10-06cc-49da-9a79-0afeb6690024.png" width="700" height="400">
</p>

## Contirbutors
* [Meenal Shree](https://github.com/meenal-shree)
* [Rushikesh Lavate](https://github.com/Rushi21-kesh)
* [Neha Kumari](https://github.com/nkneha)
* [Nirosha M](https://github.com/Niroshamurugan)

## License
This project uses the [MIT](./LICENSE) license.

## Reference
https://www.weatherbit.io/api

https://www.goavega.com/install-apache-kafka-on-windows/

https://phoenixnap.com/kb/install-spark-on-windows-10

https://matplotlib.org/devdocs/index.html
