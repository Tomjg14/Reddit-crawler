from pushShift import PushShift

ps = PushShift()

ps.setAfter("1504224000")
ps.setSub('BitcoinMarkets')
ps.setQuery('/daily_discussion')

post_ids = ps.retrievePushshiftData()

ps.createOutputJson(post_ids)


