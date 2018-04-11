# 导入re模块 re模块使Python语言拥有全部的正则表达式。
# match() 从字符串开头开始匹配
import re
match = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s\d{3}', match)
print(result.span()) # span()函数返回匹配字符串的index跨度。
print(result.group()) # group()函数返回匹配到的字符串
result = re.match('Hello\s(\d+)', match)
print(result.group(1)) # 1代表返回第一个()中匹配的字符串
result = re.match('^Hello.*Demo$', match) # ^匹配字符串的开头 $匹配字符的结尾
print(result.group())
result = re.match('^Hello.*(\d+).*o$', match) # 贪婪模式匹配
print(result.group(1))
result = re.match('^Hello.*?(\d{5}).*o$', match) # 非贪婪模式匹配
print(result.group(1))
match = '''www.
baidu123.com
'''
result = re.match('^w.*?(\d+).*m$', match, re.S) # re.S表示可以匹配换行
print(result.group(1))
# 转义匹配
match = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', match)
print(result.group())
# search() 扫描整个字符串，返回第一个匹配成功的结果。
# 从网页中搜索实战
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result.group(1), result.group(2))
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if result:
	print(result.group(1), result.group(2))
else:
	print('啥也找不到')
# findall() 以列表的形式返回匹配到的所有结果，几个括号内的字符串以Tuple的形式返回
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
	print(result)
# sub() replace()
match = 'as56asdf54ads54ads54'
result = re.sub('\d+', '被替换处', match)
print(result)
match = re.sub('<a.*?>|</a>', '', html)
results = re.findall('<li.*?>(.*?)</li>', match, re.S)
if results:
	for result in results:
		print(result.strip())
# compile() 可以将正则字符串编译成正则表达式对象，以便于在后面的匹配中复用。
import re
content1 = '2016.12.15 12:00'
content2 = '2017.12.15 12:00'
content3 = '2018.12.15 12:00'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)