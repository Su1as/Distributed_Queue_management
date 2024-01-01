# cred.py

class RabbitMQConfig:
    HOST = 'localhost'
    PORT = 5672
    USER = 'guest'
    PASSWORD = 'guest'
    QUEUE_NAME = 'task_queue'

class MySQLConfig:
    HOST = 'localhost'
    PORT = 3306
    USER = 'root'
    PASSWORD = 'admin'
    DATABASE = 'db_production'

class CeleryConfig:
    BROKER_URL = f'pyamqp://{RabbitMQConfig.USER}:{RabbitMQConfig.PASSWORD}@{RabbitMQConfig.HOST}:{RabbitMQConfig.PORT}//'
    RESULT_BACKEND = 'redis://localhost:6379/0'
