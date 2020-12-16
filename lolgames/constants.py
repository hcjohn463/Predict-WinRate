XPATHS_GAME = {
    'mmr': '//div[@class="TierRank"]/text()',
    'result': './/div[@class="GameResult"]/text()',
    '_match_type': './/div[@class="GameType"]/text()',
    '_matches': '//div[@class="GameItemWrap"]',
    '_champions_team_1': './/div[@class="Team"][1]//div[@class="ChampionImage"]',
    '_champions_team_2': './/div[@class="Team"][2]//div[@class="ChampionImage"]',
    '_summoners_team_1': './/div[@class="Team"][1]//div[@class="SummonerName"]',
    '_summoners_team_2': './/div[@class="Team"][2]//div[@class="SummonerName"]',
    '_champion_name': './/div/text()',
    'timestamp': './/div[@class="TimeStamp"]//span/text()',
    'profile_link': './/a/@href',
    'player': '//div[@class="Information"]/span//text()',
    'duration':'.//div[@class="GameLength"]/text()',
}

XPATHS_LADDER = {
    '_summoners': '//a[not(contains(@class, "ranking-highest__name"))]//@href[contains(.,"userName")]'}