class MultiChainRPC:
    CHAIN_CONFIG = {
        'EVM': {
            'Monad': {'rpc': 'https://...', 'chain_id': 123},
            'OG Chain': {'rpc': 'https://...', 'chain_id': 456}
        },
        'Cosmos': {
            'Berachain': {'api': 'https://...', 'denom': 'bera'}
        }
    }

    def get_rpc_client(self, chain_name):
        config = self._detect_chain_config(chain_name)
        if config['type'] == 'EVM':
            return Web3.HTTPProvider(config['rpc'])
        elif config['type'] == 'Cosmos':
            return CosmosSDKClient(config['api'])

    def _detect_chain_config(self, name):
        # 使用模糊匹配算法确定最接近的链配置
        return difflib.get_close_matches(name, self.CHAIN_CONFIG.keys())[0]
