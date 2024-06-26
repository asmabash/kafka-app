import psycopg2, json
from kafka import KafkaConsumer

# add your postgres connection details here
POSTGRES_SERVER="localhost"
POSTGRES_USER="resallaptop"
POSTGRES_PASSWORD="1234"
POSTGRES_DB="mydb"
PSODGRES_PORT=5432

db_conn = psycopg2.connect(database=POSTGRES_DB,
                        host=POSTGRES_SERVER,
                        user=POSTGRES_USER,
                        password=POSTGRES_PASSWORD,
                        port=PSODGRES_PORT)

cursor = db_conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS customer_points (customer_id INT, points INT)")
db_conn.commit()

consumer = KafkaConsumer(
    "customer_points_updates",
    bootstrap_servers='localhost:9092',
    api_version='3.8.0',
    auto_offset_reset="earliest",
    enable_auto_commit=True,
)
for message in consumer:
    data = json.loads(message.value.decode("utf-8"))
    if data.get('transaction_type') == 'EARN':
        cursor.execute("SELECT * FROM customer_points WHERE customer_id = %s", (data.get('customer_id'),))
        customer_points_record = cursor.fetchone()
        print('current points balance:', customer_points_record[1])
        print(data)
        cursor.execute("UPDATE customer_points SET points = %s WHERE customer_id = %s", (int(customer_points_record[1]) + data['points'], data['customer_id']))
        db_conn.commit()
        cursor.execute("SELECT points FROM customer_points WHERE customer_id = %s", (data.get('customer_id'),))
        customer_points = cursor.fetchone()[0]
        print('new points balance:', customer_points)
