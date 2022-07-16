import requests,csv
from bs4 import BeautifulSoup
# enter roll numbers in the list below
rollnumbers=[212002732,212002736,212002737,212002738,212002744]
result,header,flag=[],'',False

Url="https://egovernance.unom.ac.in/results/ugresultpage.asp"
for rollnum in rollnumbers:
    # we send a post request and parse it using BeautifulSoup
    r=requests.post(url=Url,data={'regno':rollnum}) 
    soup=BeautifulSoup(r.text,'html.parser')
    # we get row wise data and append it to result
    rows=[u.findAll('span')[3].text.strip() for u in soup.table.center.findAll("table")[2].findAll("tr")]
    rows[0]=rollnum 
    result.append(rows)
    # get the subject codes (make sure all rollnumbers have same subjects)
    if not(flag):
        header=[u.findAll('span')[0].text.strip() for u in soup.table.center.findAll("table")[2].findAll("tr")]
        header[0]='Roll num'
        flag=True
result.insert(0,header) 
# open a file in append mode with no newline (writer inserts a newline automatically)
with open('marks.csv','a',newline='') as f:
    file=csv.writer(f)
    file.writerows(result)
