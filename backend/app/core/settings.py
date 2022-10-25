from redisearch import Client, IndexDefinition, TextField

REDIS_HOST = "redis://localhost"
SCHEMA = (TextField("id", weight=5.0), TextField("body"))
