url = 'https://law.go.kr/LSW/precScListR.do'

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
    'JSESSIONID': 'UkrX65Cuc0LPoxNAUUQNoTot.LSW3',
}

params = (
    ('menuId', '7'),
    ('subMenuId', '47'),
    ('tabMenuId', '213'),
)


def data(page,size):
    return {
        'q': '*',
        'section': 'bdyText',
        'outmax': f'{size}',
        'pg': f'{page}',
        'fsort': '21,10,30',
        'precSeq': '0',
        'dtlYn': 'N'
    }
