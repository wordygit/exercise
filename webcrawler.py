from bs4 import BeautifulSoup
import requests
import time
import random

headers_tiayan = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64',
           "Cookie": 'TYCID=f5148010de3011eba934a72619b177f2; ssuid=5676834200; _ga=GA1.2.1553602542.1625558746; tyc-user-phone=%5B%2213815862601%22%5D; creditGuide=1; _gid=GA1.2.1911186708.1626051538; CT_TYCID=f6f0d701c9e34ac9983fae4099a34ffa; RTYCID=e189d9f161a64b03b03df27f65bf4956; acw_tc=2f6fc12f16261366123875643e417afe393f4734290ef8e9bd89652a7292ad; searchSessionId=1626136608.00652447; aliyungf_tc=cbdaeefd7fa4a7d18369e35303d56908d5a9245c2b166694d299ca72e9937f9d; csrfToken=zD8pR7Av8fw3FblI6JGePcDk; jsid=https://www.tianyancha.com/?jsid=SEM-BAIDU-PZ-SY-2021112-JRGW; sensorsdata2015jssdkcross={"distinct_id":"13815862601","first_id":"17a7ad9f975cd1-05b94215a8ac9b-62725472-1764000-17a7ad9f97633","props":{"$latest_traffic_source_type":"自然搜索流量","$latest_search_keyword":"天眼查","$latest_referrer":"https://www.baidu.com/other.php"},"$device_id":"17a7ad9f975cd1-05b94215a8ac9b-62725472-1764000-17a7ad9f97633"}; bdHomeCount=13; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1625816436,1625822426,1626057947,1626137601; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1626137610; tyc-user-info={"state":"0","vipManager":"0","mobile":"13815862601"}; tyc-user-info-save-time=1626137627461; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzgxNTg2MjYwMSIsImlhdCI6MTYyNjEzNzYzMiwiZXhwIjoxNjU3NjczNjMyfQ.rAgVR8h2XDymJLyT-QDEA4vhuwU2qhjtp_U7GtLI6W-JM7XlhtRuC9d_NsSG3Y6OfY3LQ4VSIGazIXrBGuY_IA'.encode('utf-8').decode('latin1')}
login = {'user':'13815862601','password':'xdpi7410.'}

session_tianyan = requests.session()
login_tianyan = session_tianyan.post('https://www.tianyancha.com/',data=login,headers=headers_tiayan)
def craylwer_tianyan(app):
    app_domain = None
    app_describe = None
    html_tianyan = session_tianyan.get('https://www.tianyancha.com/search?key={}'.format(app),headers=headers_tiayan,timeout=10)
    html_tianyan.raise_for_status()
    html_tianyan.encoding = 'utf-8' 
    soup = BeautifulSoup(html_tianyan.text,features="html.parser")
    #print(html_tianyan.text)
    try: 
        #获取app在天眼中的链接
        #href = soup.find_all('a',{'class': 'name'})[0].get('href')
        #print(soup.find_all('a',{'class': 'name'}))
        href = soup.find_all('a',{'class': 'name'})[0].get('href')
        print(href)
        
        time.sleep(random.randint(10,20))
        html_app = session_tianyan.get(href,headers=headers_tiayan,timeout=10)
        html_app.raise_for_status()
        html_app.encoding = 'utf-8'
        soup = BeautifulSoup(html_app.text,features="html.parser")
        if (soup.find_all('a',{'class': 'company-link', 'target':'_blank'})):
            app_domain = soup.find_all('a',{'class': 'company-link', 'target':'_blank'})[0].get('href')
        divs = soup.find_all('div',{'class': 'detail-content'})
        for div in divs:
            if div.get_text().startswith(' 简介'):
                app_describe = div.get_text().strip('收起').strip()
        time.sleep(random.randint(10,20))
    except Exception as e:   
        print(e)
    return app_domain,app_describe

#craylwer_tianyan('南京灵萌信息科技有限公司')

import csv
apps = {}
ff = open('C:\\Users\\Administrator\\.ssh\\github\exercise\\worklist_1.csv', 'r',encoding='gbk')
csvfile = csv.reader(ff)
for line in csvfile:
    if line[0] == '业务': continue 
    apps[line[0]] = {}
    apps[line[0]]['域名'] = line[1]
    apps[line[0]]['简介'] = line[2]
    #print(line[0], apps[line[0]]['域名'], apps[line[0]]['简介'])
ff.close()

cout = 0
for app in apps: 
    if cout == 50: 
        break
    if apps[app]['域名']: 
        continue
    print(f'_____{cout}')
    time.sleep(random.randint(90,130))
    apps[app]['域名'], apps[app]['简介'] = craylwer_tianyan(app)
    print(app, ' ', apps[app]['域名'],' ', apps[app]['简介'] )
    cout += 1

ff = open('C:\\Users\\Administrator\\.ssh\\github\exercise\\worklist_1.csv', 'w', encoding='utf-8', newline='')
csvwriter = csv.writer(ff) 
for app in apps: 
    print('writing ......................')
    csvwriter.writerow([app,str(apps[app]['域名']), str(apps[app]['简介'])])
ff.close()




