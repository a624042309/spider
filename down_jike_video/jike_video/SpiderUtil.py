#!/usr/bin/python3
import string

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
           'Connection': 'keep-alive',
           'DNT': '1',
           'Host': 'www.jikexueyuan.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
           'cookie':'gr_user_id=9bed3c65-0090-4f38-9a3d-534fbe85b738; _umdata=2BA477700510A7DF9C6481D739EF0DEA80B17939EF02C15C35BAFB2237EB2EC3DF3A3DF9BC8A7E33CD43AD3E795C914C37F4053602999EC8BB27F6C57C1A13C5; uname=jike_8279379; uid=3816157; code=HQ2FZM; authcode=2708u3poCteDoflF1cHyXjpiaDfUVVMOuSoRWtqsayqDCz%2F2MUhHsbXvdHEw%2BqoqwVO5DYVZgMGjTcgJHlQo0M93KxaLLAjXPKnrY2ifWOTj7W7AOgKw%2B8u4HjfwlYVH; avatar=https%3A%2F%2Fassets.jikexueyuan.com%2Fuser%2Favtar%2Fdefault.gif; ca_status=0; vip_status=1; level_id=2; is_expire=0; domain=0JjPkWkgU; connect.sid=s%3ARqA8Y-uaJu8nfYt3i7FhCnmTDvc-C9S_.qI2iTBQTcF%2BfNboC0GMZ3lb61n9b9R71BmMFHwdLNv0; QINGCLOUDELB=7e36c8b37b8339126ed93010ae808701d562b81daa2a899c46d3a1e304c7eb2b|WT7bQ|WT7aG; _ga=GA1.2.26528028.1496352187; _gid=GA1.2.959985081.1497288414; gr_session_id_aacd01fff9535e79=79c6012c-06a2-42df-849f-25df158eb11d; gr_cs1_79c6012c-06a2-42df-849f-25df158eb11d=uid%3A3816157'
           }


def is_ok(str1):
    if isinstance(str1, str):
        return str1.lower() == "ok" or str1.lower() == "y" or str == ''
    else:
        return False


def is_all(str1):
    if isinstance(str1, str):
        return str1.lower() == "a" or str == ''
    else:
        return False


def is_valid_index(index, length):
    if isinstance(index, int):
        if (index >= 1) and (index <= length):
            return index - 1
    elif isinstance(index, str):
        try:
            index2 = int(index)
        except Exception as e:
            print(e)
            return 0
        else:
            if (index2 >= 1) and (index2 <= length):
                return index2 - 1
    else:
        return 0


def replace_special(source_str):
    special = ('/', '\\', ':', '<', '>', '|', '*', '?', '"', ' ')
    for s in special:
        source_str = source_str.replace(s, "")
    return source_str

if __name__ == '__main__':
    jieguo = is_valid_index("3", 10)
    print(jieguo)
    print(is_ok("Ok"))
    print(is_ok("oo"))
    print("特殊字符替换", replace_special('/ \\ " ? * | < > : '))