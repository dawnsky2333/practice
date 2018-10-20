import requests
import re


url = 'http://thepokerlogic.com/glossary'
response = requests.get(url)
response.encoding = 'utf-8'
html_txt = response.text
html_url = re.findall(r'a href="/glossary/(.*?)\.html', html_txt, re.S)

for html in html_url:

    html_urls = "http://thepokerlogic.com/glossary/%s.html" % html
    # print(html_urls)

    html_response = requests.get(html_urls)
    html_response.encoding = 'utf-8'
    detail_html = html_response.text
    title_content = re.findall(r'<h3>(.*?)</h3>', detail_html, re.S)
    b = str(title_content)
    if b == '[]':
        print("none")
    else:
        print(b)