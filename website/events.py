import feedparser

events = {
    'news' : "http://www.freebsd.org/news/rss.xml",
    'upcoming' : "http://www.freebsd.org/events/rss.xml",
    'press' : "http://www.freebsd.org/news/press-rss.xml",
    'security' : "http://vuxml.freebsd.org/freebsd/rss.xml",
    'notices' : "http://www.freebsd.org/security/errata.xml",
}

def parse_rss(event_type):
    url = events.get(event_type)
    if not url:
        return []
    data = feedparser.parse(url)
    return data.entries

