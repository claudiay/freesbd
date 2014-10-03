import datetime
import feedparser


EVENTS = {
    'news' : "http://www.freebsd.org/news/rss.xml",
    'upcoming' : "http://www.freebsd.org/events/rss.xml",
    'press' : "http://www.freebsd.org/news/press-rss.xml",
    'security' : "http://vuxml.freebsd.org/freebsd/rss.xml",
    'notices' : "http://www.freebsd.org/security/errata.xml",
}

def parse_date(date):
    if not date:
        return ''
    return datetime.datetime(*date[:6]).strftime('%b %d, %Y')

def process_rss(entries):
    clean_entries = []
    for entry in entries:
        e = {}
        e['url'] = entry.get('links', '')
        if e['url']:
            e['url'] = e['url'][0].get('href', '')
        e['date'] = parse_date(entry.get('published_parsed'))
        e['item'] = entry.get('title')
        e['detail'] = entry.get('title_detail')
        if e['detail']:
            e['detail'] = e['detail']['value']
        clean_entries.append(e)
    return clean_entries

def parse_rss(event_type):
    url = EVENTS.get(event_type)
    if not url:
        return []
    data = feedparser.parse(url)
    return process_rss(data.entries)

def get_rss(event_type):
    # Check cache here
    return parse_rss(event_type)


if __name__ == '__main__':
    print "Testing RSS Feed"
    for event_type in EVENTS.keys():
        print parse_rss(event_type)[0]

