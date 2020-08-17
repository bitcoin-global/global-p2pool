import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '3bf8ac8f'.decode('hex')
P2P_PORT = 8222
ADDRESS_VERSION = 38
RPC_PORT = 18444
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'BG'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'BitGlobal') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/BitGlobal/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitglobal'), 'bitglobal.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://mainnet.bitcoin-global.io/block-analysis/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://mainnet.bitcoin-global.io/address/'
TX_EXPLORER_URL_PREFIX = 'https://mainnet.bitcoin-global.io/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
