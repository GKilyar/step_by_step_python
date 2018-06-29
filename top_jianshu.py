import requests
from bs4 import BeautifulSoup

# 推荐作者
url = 'https://www.jianshu.com/recommendations/users?utm_source=desktop&utm_medium=index-users'
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
response = requests.get(url, headers=header)
html = response.text

# 解析html页面结构找到放置数据的标签
soup = BeautifulSoup(html, 'html.parser')

authors_info = soup.find_all('div',class_='wrap')

def return_a(info):
    str_a = []
    for item in info:
        str_a.append('https://www.jianshu.com'+item.a.get('href'))
    return str_a
aaa = return_a(authors_info)
# print(aaa)



# 待处理链接
def main_task():
    all_data = []
    for index in range(len(aaa)):
    # print(index)
        header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
        response = requests.get(aaa[index], headers=header)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')


        author_info = soup.find_all('div',class_='info')[0]
        author_info_name = soup.find_all('a',class_='name')[0]
        author_info_numbers = author_info.find_all('p')

        author_name = author_info_name.string[:]
        get_all_numbers_from_list = [int(item.string) for item in author_info_numbers]
        all_data.append([author_name,get_all_numbers_from_list])
        
    return all_data    
    # print(author_name)
    # print(get_all_numbers_from_list)



def print_author(author_list):
    for item in author_list:
        print('-----------------------------------','\n',
            '作者姓名:',item[0],'\n', 
            '获得:',item[1][0],'关注','\n',
            '作者拥有:',item[1][1],'个分数','\n',
            '共写了:',item[1][2],'篇', '\n',
            '共写了:',item[1][3],'字','\n',
            '收获:',item[1][4],'个喜欢'
            )

print_author(main_task())



