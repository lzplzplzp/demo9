import redis

def rcon():
    # redis.StrictRedis(host="111.230.226.183", password="lzp123", port=6379, db=0)
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    return redis.Redis(connection_pool=pool)