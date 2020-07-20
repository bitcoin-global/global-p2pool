import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '50c96a24'.decode('hex')
P2P_PORT = 18222
ADDRESS_VERSION = 111
RPC_PORT = 18444
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'test')
    )
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'tBG'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'BitGlobal') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/BitGlobal/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitglobal'), 'bitglobal.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://testnet.bitcoin-global.io/block-analysis/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://testnet.bitcoin-global.io/address/'
TX_EXPLORER_URL_PREFIX = 'https://testnet.bitcoin-global.io/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
