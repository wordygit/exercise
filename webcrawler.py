from bs4 import BeautifulSoup
import requests
import time
import random

headers_tiayan = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64',
           "Cookie": 'TYCID=f5148010de3011eba934a72619b177f2; ssuid=5676834200; _ga=GA1.2.1553602542.1625558746; tyc-user-phone=%5B%2213815862601%22%5D; creditGuide=1; bdHomeCount=11; aliyungf_tc=3bb9dd13be441906e924b27c401d177ec9ae9695434420e9fd4c1c498d14bb34; csrfToken=tyfu8mgjN3y-7FnZIP5O3ypg; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1625742613,1625799249,1625816436,1625822426; jsid=https://www.tianyancha.com/?jsid=SEM-BAIDU-PP-TYC-000423&bd_vid=7879822996666481674&userid=31769301&query=%CC%EC%D1%DB&keywordid=281785359769&campaignid=158356455&groupid=5915607911&renqun_youhua=2828757; sensorsdata2015jssdkcross={"distinct_id":"13815862601","first_id":"17a7ad9f975cd1-05b94215a8ac9b-62725472-1764000-17a7ad9f97633","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""},"$device_id":"17a7ad9f975cd1-05b94215a8ac9b-62725472-1764000-17a7ad9f97633"}; cloud_token=12af6ba786ef4ca0bc1be50e964d2c74; searchSessionId=1625907150.37112275; relatedHumanSearchGraphId=11004087842; relatedHumanSearchGraphId.sig=VnnmczaIcXV3VpyslplQnmcl6oKIuhuRkJ5v5rFnUME; acw_tc=2f6fc12216260515404711695e14607715040b59ec3eb514effb33660ff8f8; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1626051537; _gid=GA1.2.1911186708.1626051538; tyc-user-info={"state":"0","vipManager":"0","mobile":"13815862601"}; tyc-user-info-save-time=1626051623252; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzgxNTg2MjYwMSIsImlhdCI6MTYyNjA1MTYyOCwiZXhwIjoxNjU3NTg3NjI4fQ.FTvcb2lLSQMG6BlanOKeqDZZZ9Iy6n6LVgAKUKlelzx31S4aLJhXmoy3wJpTw5DAdBSsypyIInjbjIvGk5c8Iw; creditGuide=1; CT_TYCID=a7c9a14f21d6437ea289070519ae2da8; RTYCID=87e14f4d0c004e27ba8fe08356e84ca3; bdHomeCount=11; sensorsdata2015jssdkcross={"distinct_id":"13815862601","first_id":"17a7ad9f975cd1-05b94215a8ac9b-62725472-1764000-17a7ad9f97633","props":{"$latest_traffic_source_type":"自然搜索流量","$latest_search_keyword":"未取到值","$latest_referrer":"https://www.baidu.com/baidu.php"},"$device_id":"17a7ad9f975cd1-05b94215a8ac9b-62725472-1764000-17a7ad9f97633"}; searchSessionId=1625816447.29016589; aliyungf_tc=3bb9dd13be441906e924b27c401d177ec9ae9695434420e9fd4c1c498d14bb34; csrfToken=tyfu8mgjN3y-7FnZIP5O3ypg; jsid=https://www.tianyancha.com/?jsid=SEM-BAIDU-PP-TYC-000423&bd_vid=9929724746923713584&userid=31769301&query=%CC%EC%D1%DB&keywordid=281785359769&campaignid=158356455&groupid=5915607911&renqun_youhua=2828757; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1625742613,1625799249,1625816436,1625822426; acw_tc=781bad4f16258800238914614e78a3fee075c66dc46fd0c7da2088b99aa5b0; cloud_token=d5f8db964f074bbf8ed4f0b22a19c3be; cloud_utm=a83309ff2b094facbb0a9499c683862c; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1625880052; tyc-user-info={"state":"0","vipManager":"0","mobile":"13815862601"}; tyc-user-info-save-time=1625880224345; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzgxNTg2MjYwMSIsImlhdCI6MTYyNTg4MDIyOCwiZXhwIjoxNjU3NDE2MjI4fQ.0XxEylf6a7h32CTjkBUQTaO43TxPUzFqz6QiOD9P9In7Qm1oUspIzTnbLwxxMo_wDAnhNZTKgFEO-yxGJ_XzgQ'.encode('utf-8').decode('latin1')}
login = {'user':'1381581','password':'xdpi7410.'}

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
        print(soup.find_all('a',{'class': 'name'}))
        href = soup.find_all('a',{'class': 'name'})[0].get('href')
        
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
    apps[line[0]] = {}
    apps[line[0]]['域名'] = line[1]
    apps[line[0]]['简介'] = line[2]
    #print(line[0], apps[line[0]]['域名'], apps[line[0]]['简介'])
ff.close()

cout = 0
for app in apps: 
    #if cout == 20: 
    #    break
    if apps[app]['域名']: 
        continue
    time.sleep(random.randint(150,230))
    apps[app]['域名'], apps[app]['简介'] = craylwer_tianyan(app)
    print(app, ' ', apps[app]['域名'],' ', apps[app]['简介'] )
    cout += 1

ff = open('C:\\Users\\Administrator\\.ssh\\github\exercise\\worklist_1.csv', 'w', encoding='utf-8', newline='')
csvwriter = csv.writer(ff) 
for app in apps: 
    print('writing ......................')
    csvwriter.writerow([app,str(apps[app]['域名']), str(apps[app]['简介'])])
ff.close()

