import redis
from app.config import Config

class Cache:
    """Handles caching scam explanations in Redis."""
    def __init__(self):
        self.client = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)
    
    def get(self, key):
        return self.client.get(key)
    
    def set(self, key, value):
        return self.client.set(key, value)
