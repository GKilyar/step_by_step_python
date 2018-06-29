import requests
from bs4 import BeautifulSoup

# 分析url
url = 'https://www.jianshu.com/u/8ba96e299c08'

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
response = requests.get(url, headers=header)
html = response.text
# print(html)

soup = BeautifulSoup(html, 'html.parser')

author_info = soup.find_all('div',class_='info')[0]
author_info_name = soup.find_all('a',class_='name')[0]
author_info_numbers = author_info.find_all('p')


author_name = author_info_name.string[:]
get_all_numbers_from_list = [int(item.string) for item in author_info_numbers]



# 数据分析
def author(name,number_list):
    author_dict = {}
    author_dict['姓名'] = name
    author_dict['关注'] = number_list[0]
    author_dict['粉丝'] = number_list[1]
    author_dict['文章数'] = number_list[2]
    author_dict['文章总字数'] = number_list[3]
    author_dict['收获喜欢'] = number_list[4]
    
    return author_dict
   
def print_author(author_dict):
    print(
        '作者姓名:',author_dict['姓名'],'\n', 
        '获得:',author_dict['关注'],'关注','\n',
        '作者拥有:',author_dict['粉丝'],'个分数','\n',
        '共写了:',author_dict['文章数'],'篇', '\n',
        '共写了:',author_dict['文章总字数'],'字','\n',
        '收获:',author_dict['收获喜欢'],'个喜欢'
        )

print_author(author(author_name,get_all_numbers_from_list))