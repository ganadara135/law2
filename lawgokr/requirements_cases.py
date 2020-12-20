url = 'https://law.go.kr/LSW/precInfoR.do'

headers = {
    'Connection': 'keep-alive',
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://law.go.kr',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://law.go.kr/LSW/precSc.do?menuId=7&query=&tabMenuId=213&subMenuId=47',
    'Accept-Language': 'en-US,en;q=0.9',
}

cookies = {
    'PCID': '16077926315534274127659',
    'elevisor_for_j2ee_uid': '8htbcf3q8tz52',
    'JSESSIONID': 'JvArzJIzrG9gqrFMxAkc4u-r.LSW10',
    'lawHistory': '---010104%2C212509',
}


def data(case_id):
    return {'precSeq': case_id, 'vSct': '*'}
