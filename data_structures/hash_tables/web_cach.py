cache = {
    'instagram.com': '180.123.123',
    'tiktok.com': '180.123.124',
    'github.com': '180.123.125',
}

server = {
    'vk.com': '192.23.23',
    'leedcode.com': '192.23.24',
    'pornohub.com': '192.23.25',
    'anime.com': '192.23.26'
}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        date = server.get(url)
        cache[url] = date
        return date

result = get_page(input('Введите адрес: '))
print(result)
