import os
import sys
import ssl
import urllib.request
import time

FORBIDDEN_CHAR = [
    '\\',
    '/',
    ':',
    '*',
    '?',
    '"',
    '<',
    '>',
    '|',
]

def find_innerHtml(html:str, tag_opening:str) -> str:
    # Construct tag closing
    tmp = tag_opening.split()
    tmp_hasAttributes = len(tmp) > 1
    tmp = list(tmp[0])
    tmp.insert(1, '/')
    if tmp_hasAttributes:
        tmp.append('>')
    tag_closing = ''.join(tmp)
    # Search
    start = html.find(tag_opening)
    if start == -1:
        return ''
    start += len(tag_opening)
    end = html.find(tag_closing, start)
    return html[start:end].rstrip()


if __name__ == '__main__':
    for pid in range(1000, 30000):
        problem_path = os.path.join('problem', str(pid))

        if not os.path.exists(problem_path):
            continue

        with urllib.request.urlopen(f'https://acmicpc.net/problem/{pid}', context=ssl.SSLContext()) as https:
            html = https.read().decode('utf-8')
            title = find_innerHtml(html, '<span id="problem_title">')
            for c in FORBIDDEN_CHAR:
                if c in title:
                    print(title)
                    raise Exception('특수문자가 포함된 문제명')
            os.rename(problem_path, problem_path+' '+title)
            time.sleep(5)