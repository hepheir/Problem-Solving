import os
import sys
import ssl
import urllib.request


def find_innerHtml(html, tag_opening):
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


def find_sample_data(html):
    for i in range(1, 10):
        sample_in = find_innerHtml(html, f'<pre class="sampledata" id="sample-input-{i}">')
        sample_out = find_innerHtml(html, f'<pre class="sampledata" id="sample-output-{i}">')
        if not sample_in:
            break
        yield sample_in, sample_out


if __name__ == '__main__':
    pid = int(sys.argv[1] if len(sys.argv) >= 2 else input('문제 번호: '))
    problem_path = os.path.join('problem', str(pid))
    data_path = os.path.join(problem_path, 'data')

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    with urllib.request.urlopen(f'https://acmicpc.net/problem/{pid}', context=ssl.SSLContext()) as https:
        html = https.read().decode('utf-8')

        print('[INFO] 제목:', find_innerHtml(html, '<span id="problem_title">'))

        for idx, (data_in, data_out) in enumerate(find_sample_data(html)):
            idx += 1
            print(f'[INFO] 데이터 셋 생성 중... {idx}')

            with open(os.path.join(data_path, f'boj.sample.{idx}.in'), 'w') as f:
                f.write(data_in)

            with open(os.path.join(data_path, f'boj.sample.{idx}.out'), 'w') as f:
                f.write(data_out)
    
    print('[INFO]', '데이터 셋 생성완료.')
    print(problem_path)