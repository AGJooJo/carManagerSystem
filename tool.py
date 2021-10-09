from gmssl import sm2,utils
import redis

# redis
def redis_u():
    r = redis.Redis(host='localhost',port=6379,decode_responses=True)
    return r

# sm2 密钥生成
class secretkey:
    def __init__(self):
        self.priKey = utils.PrivateKey()
        self.pubKey = self.priKey.publicKey()
        self.r = redis_u()
        self.set_key()

    def set_key(self):
        self.r.set('priKey',self.priKey.toString())
        self.r.set('pubKey',self.pubKey.toString(False))

    def get_prikey(self):
        priKey_str = self.r.get('priKey')
        return priKey_str

    def get_pubkey(self):
        pubkey_str = self.r.get('pubkey')
        return pubkey_str


