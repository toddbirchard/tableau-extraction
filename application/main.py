import requests
import json
from . import redis_store


def auth_token():
    """Starting point."""
    headers = {'Content-Type': 'application/xml'}
    r = requests.get(redis_store.gettoken, auth=(redis_store.user, redis_store.pass), headers=headers)
    result = r.content
    print(result)
