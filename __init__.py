"""
Spider Chain SDK
----------------
A cross-table hash architecture for tamper-proof blockchain data integrity.

Invented by: PlayWebit / CipherVault
Architecture: Spider Chain Hash Architecture

Usage:
    from spiderchain import SpiderChain
    from spiderchain.adapters.supabase_adapter import SupabaseAdapter
    from spiderchain.adapters.playwebit_adapter import PlayWebitAdapter
"""

from spider_chain import SpiderChain
from spider_hash import SpiderHashEngine
from chain_sequencer import ChainSequencer
from exceptions import (
    SpiderChainError,
    TamperDetectedError,
    ChainBrokenError,
    AdapterNotConfiguredError,
    InvalidHashError,
    TableNotRegisteredError
)

__version__ = "1.0.0"
__author__ = "PlayWebit / CipherVault"
__license__ = "MIT"

__all__ = [
    "SpiderChain",
    "SpiderHashEngine",
    "ChainSequencer",
    "SpiderChainError",
    "TamperDetectedError",
    "ChainBrokenError",
    "AdapterNotConfiguredError",
    "InvalidHashError",
    "TableNotRegisteredError"
]
