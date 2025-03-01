class TwitterMonitor:
    def __init__(self):
        self.stream = TwythonStreamer(...)
        self.contract_scanner = ContractScanner()

    def on_tweet(self, tweet):
        if self._is_relevant(tweet):
            urls = extract_urls(tweet.text)
            for url in urls:
                if 'faucet' in url:  # 自动识别领水链接
                    self.faucet_handler(url)
                elif 'github.com' in url:  # 扫描智能合约仓库
                    self.contract_scanner.clone_repo(url)

    def _is_relevant(self, tweet):
        score = (tweet['retweet_count'] * 0.3 +
                 tweet['user']['followers_count'] * 0.5 +
                 contains_testnet_keywords(tweet) * 0.2)
        return score > 0.7
