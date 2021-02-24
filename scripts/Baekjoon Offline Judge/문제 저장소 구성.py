import os
import ssl
import subprocess
import sys
import typing
import urllib.request


ESCAPE = {
    '\\': '(backslash)',
    '/': '(slash)',
    ':': '-',
    '*': 'x',
    '?': '',
    '"': '',
    '<': '(gt)',
    '>': '(lt)',
    '|': '(or)',
    '×': 'x',
}


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


def find_sample_data(html:str) -> typing.Iterator[typing.Tuple[str, str]]:
    for i in range(1, 10):
        sample_in = find_innerHtml(html, f'<pre class="sampledata" id="sample-input-{i}">')
        sample_out = find_innerHtml(html, f'<pre class="sampledata" id="sample-output-{i}">')
        if not sample_in:
            break
        sample_in = sample_in.replace('\r\n', '\n')
        sample_out = sample_out.replace('\r\n', '\n')
        yield sample_in, sample_out


def make_file(path:os.PathLike, content=''):
    with open(path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    pid = int(sys.argv[1] if len(sys.argv) >= 2 else input('문제 번호: '))

    with urllib.request.urlopen(f'https://acmicpc.net/problem/{pid}', context=ssl.SSLContext()) as https:
        html = https.read().decode('utf-8')

        title = find_innerHtml(html, '<span id="problem_title">')
        for keyword, replace in ESCAPE.items():
            title = title.replace(keyword, replace)
        print('[INFO]', f': {pid} {title}')

        problem_path = os.path.join('problem', f'{pid} {title}')
        data_path = os.path.join(problem_path, 'data', 'boj', 'sample')

        if not os.path.exists(data_path):
            os.makedirs(data_path)

        for idx, (data_in, data_out) in enumerate(find_sample_data(html)):
            idx += 1
            print('[INFO]', f'데이터 셋 생성 중... {idx}')
            make_file(os.path.join(data_path, f'{idx}.in'), data_in)
            make_file(os.path.join(data_path, f'{idx}.out'), data_out)

    print('[INFO]', '데이터 셋 생성완료.')
    
    subprocess.run(f'git add "{data_path}"')
    subprocess.run(f'git commit -m "{pid}번 데이터 셋 추가"')

    make_file(os.path.join(problem_path, '.gitkeep'))