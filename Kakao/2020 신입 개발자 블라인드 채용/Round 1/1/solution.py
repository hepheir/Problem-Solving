def is_alpha(c):
    """ 문자를 입력하면 알파벳인지 여부를 알려주는 함수 """
    return 'a' <= c <= 'z'

def is_num(c):
    """ 문자를 입력하면 숫자인지 여부를 알려주는 함수 """
    return '0' <= c <= '9'

def is_special(c):
    """ 문자를 입력하면 (*허용된) 특수문자인지 여부를 알려주는 함수 """
    return c in '_-.'

def is_allowed(c):
    """ 입력된 문자가 허용된 문자인지 알려주는 함수 """
    return is_alpha(c) or is_num(c) or is_special(c)

def rem_dot_redundancy(string):
    """ 2번 이상 연속된 마침표를 하나의 마침표로 치환하는 함수. 시간 복잡도는 O(n) """
    new_string = ''
    prev_char = '?'
    for current_char in string:
        if prev_char == current_char == '.':
            pass
        else:
            new_string += current_char
        prev_char = current_char
    return new_string

def rem_first_and_last_dots(string):
    """ 문자열의 처음이나 끝에 위치한 마침표 제거. 최악의 경우 O(n) """
    start_offset = 0
    while start_offset < len(string):
        if string[start_offset] != '.':
            break
        else:
            start_offset += 1
    end_offset = len(string)-1
    while end_offset >= start_offset:
        if string[end_offset] != '.':
            break
        else:
            end_offset -= 1
    return string[start_offset:end_offset+1]

def solution(new_id:str):
    # Step1 
    new_id = new_id.lower()
    # Step2
    new_id = [c for c in new_id if is_allowed(c)]
    # Step3
    new_id = rem_dot_redundancy(new_id)
    # Step4
    new_id = rem_first_and_last_dots(new_id)
    # Step5
    new_id = "a" if not new_id else new_id
    # Step6
    new_id = rem_first_and_last_dots(new_id[:15])
    # Step7
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1]*(3-len(new_id))
    return new_id

print(solution('=.='))