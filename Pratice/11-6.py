# 다른 사람이 만든 패키지  가져와 쓰기
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#터미널에 pip list >> 설치된 pip 나열
# pip show (pip이름)

