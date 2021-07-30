import requests


apikey = '8aff6b954e64846f77c3b6e10af4f47fcb8c59e482c2bfa20a17491b4d84c026'

def main():
    scan_url(input(" Enter url:"))

def scan_url(url):
    params = {'apikey': apikey, 'url': url}
    response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
    scan_id = response.json()['scan_id']
    report_params = {'apikey': apikey, 'resource': scan_id}
    report_response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=report_params)
    scans = report_response.json()['scans']


    positive_sites = []
    for key, value in scans.items():
        if value['detected'] == True:
            positive_sites.append(key)


    if len(positive_sites)==0:
        print("website does not contain malicious content.")
    else:
        print("This website contain malicious content are as follows:")
        print(positive_sites)







if __name__ == '__main__':
    main()