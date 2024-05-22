# direct fetch the deed record from masslandrecord.com
# the direct request was blocked by the website 
# need to find way to get around it 

import requests
from bs4 import BeautifulSoup 
import pdb 

url = 'https://www.masslandrecords.com/MiddlesexSouth/default.aspx' 

# Define the headers and data payload
headers = {
    'authority': 'www.masslandrecords.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'PopupImgWidth=911; PopupImgTop=133; PopupImgLeft=556; PopupImgHeight=774; DetailsViewMode=True; IsImageUndock=False; visid_incap_2183455=fh03/ClcTxmjKN7mW/C1UQdkvGUAAAAAQkIPAAAAAACAt8ayAWewmCuJG2utoqYd/33OTjyXphE6; ASP.NET_SessionId=usr3cm45ja0b2zz5wjkce345; nlbi_2183455=kbtSCDqRfAb73h5afQEw2QAAAAAHfi0y0Qw9XR53D4ItlNmJ; incap_ses_625_2183455=sKiEJZaOdgGr7DSnanOsCIgW/GUAAAAAIMdfOmMn8ZOWMRQO4OhqJQ==; PageSize=50; incap_ses_577_2183455=+J6RGxZX9XxtJ1oirusBCAyM/WUAAAAAN/YYJymVSZpCuLFW36F76Q==; incap_ses_1047_2183455=Hr3QDn3bOQhsHVJOErKHDrS4/WUAAAAAqOecCuW1QiXUQozTt1fMdA==; incap_ses_626_2183455=QhRxZCDNYVFb2l5W4gCwCG6d/mUAAAAAP1pgrfkkLhF3yXmqWpwOsg==',
    'dnt': '1',
    'origin': 'https://www.masslandrecords.com',
    'referer': 'https://www.masslandrecords.com/MiddlesexSouth/',
    'referrer-policy': 'strict-origin-when-cross-origin, strict-origin-when-cross-origin',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-microsoftajax': 'Delta=true',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
  'ScriptManager1': 'SearchFormEx1%24UpdatePanel%7CSearchFormEx1%24btnSearch',
  'ScriptManager1_HiddenField': '%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3Aeffe2a26%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3A475a4ef5%3A5546a2b%3A497ef277%3Aa43b07eb%3Ad2e10b12%3A37e2e5c9%3A5a682656%3A1d3ed089%3Af9029856%3Ad1a1d569%3B',
  '__VIEWSTATE': '',
  'Navigator1%24SearchOptions1%24DocImagesCheck': 'on',
  'SearchFormEx1%24ACSTextBox_StreetNumber': '22',
  'SearchFormEx1%24ACSTextBox_StreetName': 'dell',
  'SearchFormEx1%24ACSDropDownList_Towns': '-2',
  'SearchFormEx1%24ACSTextBox_Description': '',
  'SearchFormEx1%24ACSTextBox_DateFrom': '1%2F1%2F1900',
  'SearchFormEx1%24ACSTextBox_DateTo': '3%2F22%2F2024',
  'ImageViewer1%24ScrollPos': '',
  'ImageViewer1%24ScrollPosChange': '',
  'ImageViewer1%24_imgContainerWidth': '0',
  'ImageViewer1%24_imgContainerHeight': '0',
  'ImageViewer1%24isImageViewerVisible': 'true',
  'ImageViewer1%24hdnWidgetSize': '',
  'ImageViewer1%24DragResizeExtender_ClientState': '',
  'CertificateViewer1%24ScrollPos': '',
  'CertificateViewer1%24ScrollPosChange': '',
  'CertificateViewer1%24_imgContainerWidth': '0',
  'CertificateViewer1%24_imgContainerHeight': '0',
  'CertificateViewer1%24isImageViewerVisible': 'true',
  'CertificateViewer1%24hdnWidgetSize': '',
  'CertificateViewer1%24DragResizeExtender_ClientState': '',
  'DocList1%24ctl03': '',
  'DocList1%24ctl05': '',
  'DocDetails1%24PageSize': '',
  'DocDetails1%24PageIndex': '',
  'DocDetails1%24SortExpression': '',
  'BasketCtrl1%24ctl01': '',
  'BasketCtrl1%24ctl03': '',
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__LASTFOCUS': '',
  '__ASYNCPOST': 'true',
  'SearchFormEx1%24btnSearch.x': '59',
  'SearchFormEx1%24btnSearch.y': '13',
}

# Make the POST request
response = requests.post(url, headers=headers, data=data)



pdb.set_trace()

# Print the response text
print(response.text)
