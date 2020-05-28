import os
import argparse
import re
import requests

try:
    os.system('cls')
except Exception:
    os.system('clear')

parser = argparse.ArgumentParser(description='IP Address & Writing results')
parser.add_argument('-i', '--ip', type=str, required=True, help='Server\'s IP address')
parser.add_argument('-w', '--file', type=bool, help='True to save results in a txt file')

args = parser.parse_args()

# TO CLEAN UP DATA EXTRACTED FROM BING
def format_links(urls=None):
    urls = [] if urls==None else urls
    pattern = re.compile('(https?://[a-z0-9.-]+\.[a-z]+/)')
    links = [pattern.search(link).group(0) for link in urls if pattern.search(link) is not None]
    return links

page = 1
start_urls = []
while True:
    with requests.Session() as s:
        base = 'https://www.bing.com/search'
        data = {
            'q'  : f'ip::{args.ip}',
            'go' : 'Search',
            'qs' : 'ds',
            'first' : str(page)
        }
        header = {
            'User-Agent' : 'ElMehdiR',
            'From' : 'http://www.lulz.com'
        }
        r = s.get(base, params=data, headers=header)
        html = r.text
        pattern = re.compile('<h2><a\shref="(.*?)"\s')
        match = pattern.findall(html)
        try:
            start_urls.extend(match)
        except Exception:
            break
        print(*format_links(start_urls), sep='\n')

        nextp = re.compile('class="sw_next"')
        nextp = nextp.search(html)

        if nextp is not None:
            page += 10
        else:
            break

os.system('cls')
final_urls = format_links(start_urls)

print(*final_urls, sep='\n')
print(f'\n\n{len(final_urls)} websites found on {args.ip}')

if args.file:
    try:
        os.mkdir('results')
    except Exception:
        pass
    with open(f'results/{args.ip}.txt', 'a') as f:
        for url in final_urls:
            f.write(f'{url}\n')
