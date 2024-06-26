# kafka-app
A simple app to use Kafka. The app send and receive messages to update a customer's points in the DB.

## Development
Install Postgres
```
brew install postgresql@15
```

Start Postgres
```
brew install postgresql@15
```

Install backend dependencies
```
pip3 install -r requirements.txt
```

Download Kafka from https://www.apache.org/dyn/closer.cgi?path=/kafka/3.7.0/kafka_2.13-3.7.0.tgz

Extract the Kafka folder
```
tar -xzf kafka_2.13-3.7.0.tgz
```

Navigate to the Kafka directory
```
cd kafka_2.13-3.7.0
```

Start Zookeeper service
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Start Kafka broker
```
bin/kafka-server-start.sh config/server.properties
```


References: https://dev.to/hesbon/apache-kafka-with-python-laa

