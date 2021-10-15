from gmssl import sm2,utils
from gmssl.sm2 import CryptSM2
import redis

# redis
def redis_u():
    r = redis.Redis(host='localhost',port=6379,decode_responses=True)
    return r

# sm2 密钥生成
class Secretkey:
    def __init__(self):
        self.priKey = utils.PrivateKey()
        self.pubKey = self.priKey.publicKey()
        self.r = redis_u()

    def set_key(self):
        pri = self.priKey.toString()
        pub = self.pubKey.toString(False)
        self.r.set('priKey',pri)
        self.r.set('pubKey',pub)

    def get_prikey(self):
        priKey_str = self.r.get('priKey')
        return priKey_str

    def get_pubkey(self):
        pubkey_str = self.r.get('pubKey')
        return pubkey_str
