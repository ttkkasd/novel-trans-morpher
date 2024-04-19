import os

os.environ['OPENAI_API_KEY'] = 'test'
os.environ['OPENAI_API_BASE'] = "http://localhost:3040/v1"
os.environ['OPENAI_BASE_URL'] = "http://localhost:3040/v1"
from langchain_openai import ChatOpenAI
from database_manager import DatabaseManager

# 导入LangChain中的提示模板
from langchain_core.prompts import PromptTemplate

db_manager = DatabaseManager('localhost', 'root', '123456', 'test')

text = """
江城机场。
人来人往。
一个着一袭白色长裙的女孩走出通道。
女孩一头墨发及腰，拉着行李箱站在人群中看着这久违的机场，脸上挂着浅浅的笑。
她本就长得漂亮，这一笑更是惹人侧目。
清纯，甜美，是很多男生心目中的初恋白月光形象，尽管她现在已经有二十三岁。
走出机场，坐上出租车。
一路往城东的方向去。
看着车窗外不断倒退的街道，女孩有片刻恍惚。
前前后后加起来，这些熟悉的街景她有好些年没有看到了。
半个多小时的车程，出租车来到一处别墅区。做了登记，出租车直接开进小区。
停车，扫码付款，打开车门下车。
一下车，女孩的目光就顿住了。
不远处，铁门，围墙，围墙上爬满盛开的月季花。
门前，盛开的月季花下，一人站在那里。
白衬衫，金色边框眼镜，样貌出众，身材高挑，约莫有一米八七的身高。他站在那里，手边牵着一只藏獒，正朝女孩看过来。
目光交汇。
沉默的对视持续了好半晌。
对方先开的口：“言言，回来了？”
声音很好听，磁性中透着沉稳，一如他这个人。
路言兮弯眉，笑容清甜：“嗯，绥哥哥，我回来了。”
回来有三年了。
二十八岁那年，病房里，她闭上眼那刻，宋绥将她的手握得很紧，她看到向来从容的宋绥落了泪。
她死在了病床上，一睁眼回到八年前。
三年前她刚重生回来时，天知道她有多想马上联系他。但她忍住了，因为那时的她很糟糕。
她想以最好的状态来见他，为此，她准备了整整三年。
出租车师傅把行李箱交给路言兮，路言兮接过，拖着行李箱朝宋绥走去。宋绥一直站在那里没有动。
“今天星期五，绥哥哥不上班吗？”
宋家三代经商，在江城有着举足轻重的地位。宋家是人人艳羡的对象，因为除了有过人的财富和社会地位，宋家还有两子一女，三个孩子都是别人家的孩子，特别是宋家的两个儿子。
长子宋绥和次子宋淮从小优秀，有着出众的样貌和头脑。
长子宋绥十七岁保送国内最顶尖大学的医学专业，花四年时间就完成本硕博连读，毕业后回到江城市医院就职，入职才五年就已是江城市医院知名的心外科主任医师，在业内有着很高的地位。
次子宋淮有极高的商业天赋。刚步入大学就进自家公司学习，现在年仅二十三岁才大学毕业一年就能独自撑起偌大的宋氏集团，宋家的当家人也就是他们的父亲宋庚已经处于半退休状态，公司的事务很少需要宋庚再操心。
“今天休息。”
宋绥眼睑微垂，视线从她脸上移到她拉着的行李箱上，上前从她手里将行李箱接过，与此同时空出的手拍拍藏獒的脑袋，松开牵引绳，藏獒自己转身跑回院中。
“我帮你把行李拿回去。回来怎么不提前打个电话？也好叫个人去机场接你。”
看着被他夺过去的行李箱，路言兮笑了笑没有拒绝他的帮忙：“想着今天星期五，大家应该都在上班就没有打扰，反正机场离家也不远，打个车很快就到了。”
“嗯。”宋绥淡淡应一声，当先拉着行李箱往隔壁走去。
他们两家是邻居。
“你家里这么久没住人，要我找个阿姨来帮你收拾收拾吗？”
路言兮站在原地看着拉着行李箱走在前面的高挑背影，心里有些酸有些涩，又有些甜。
带着笑红了眼眶。
小跑跟上他：“不用，决定回来我就提前找人来收拾好了。”
她爸妈在她六岁那年因公殉职，他爸这边没什么亲人，外公外婆家又远在北城，很小的时候她就自己和保姆住在这里。
不过她初中前外婆大部分时间都是在这里照顾她，她上初中后外婆才回北城，回北城后，外婆也是一得空就来江城小住陪她。
邻居又对她照顾有加。
她那些年过得不算孤单。
打开大门的锁，两人走进院子。
路家和宋家一样大，只是宋家人多路家人少，路家又自路言兮出国后整整五年没有住过人，比起宋家，路家少了点人气。好在提前让人来收拾过，屋里屋外都很干净。
进屋后宋绥径直上楼将路言兮的行李箱搬到二楼她的房间外，路言兮跟着上楼将小包放到房间，只拿着手机下楼。
“绥哥哥，谢谢你帮我搬行李，我刚回来，家里什么都没有，想给你倒杯水都没有条件。这样，等我整理好，过几天请你来家里吃饭。”
“没事。”宋绥扫一眼空荡荡的屋子，望向她，“先去我家吧，这几天你先收拾，不急着开火，直接到我家吃饭。”
很周到，语气不算太熟稔，却也不会让人觉得生疏，标准的相处多年的邻居家哥哥对邻居家妹妹的态度。
“好啊，那这几天我就打扰了。”
“不打扰，我爸妈和妹妹都很喜欢你，你和阿淮……又是从小一起长大关系要好的朋友，不用见外。”
阿淮，宋淮……
听到这个名字，路言兮脸上的笑稍稍敛了一下，很快恢复：“瞧绥哥哥这话说的，像是我只和他们关系好，和你关系不好似的。”
宋绥一愣，望向她。
没有避开，路言兮迎着他的目光笑着说：“绥哥哥，我们也是从小一起长大的，叔叔阿姨喜欢我，我和宋淮安欣关系好，和你的关系也很好啊。”
她语气中带着很自然的撒娇意味，仿佛他们真的很熟关系真的很亲近一般。
宋绥盯着她看了看，轻轻地“嗯”了一声，说：“先去我家，我妈在家，见到你她一定很高兴。”
那你呢？你见到我高兴吗？
这话路言兮当然没有问出来。
宋家还是路言兮熟悉的样子，不管和五年前相比还是五年后相比，宋家的布局变化都不大。
两人一进门藏獒就激动地跳起来，只可惜它早被宋家的保姆拴好，没能成功扑到两人身上。
路言兮欣喜地冲它喊一声：“梨花！”
藏獒跳得更欢了，甚至还冲她叫唤两声回应她。
是的，这么威风一只藏獒有个很不符它气质的名字，叫梨花，路言兮给取的名。
"""
# 创建原始模板
template = """
Please extract all the personal names from the text below. Only extract specific names, regardless of whether they are Chinese or foreign names. Do not extract titles, such as 'Mrs.' or 'tribal chief.' List only the names, separated by commas, and omit any irrelevant responses. There is no need to include pinyin.: {text}
"""

from langchain.output_parsers import CommaSeparatedListOutputParser

# 创建模型实例
llm = ChatOpenAI(model="text-embedding-ada-002")

# 设置模板
output_parser = CommaSeparatedListOutputParser()
prompt = PromptTemplate.from_template(template)

# 回答
chain = prompt | llm
answer = chain.invoke({'text': text})
print("answer=", answer)
# 解析
names = output_parser.parse(answer.content)
print("names=", names)

nameTemplate = """
Please rename the name '{name}' while adhering to the following conditions: 1. Retain the original surname and ensure the new given name has the same number of characters as the original. For example, if the original name is '路言兮', the new name might be '路非语'; if the original name is '宋淮', the new name could be '宋泽'. 2. Important: Respond only with the new name, without any additional comments or answers.
"""

namePrompt = PromptTemplate.from_template(nameTemplate)
nameChain = namePrompt | llm
for username in names:
    records = db_manager.fetch_usernames(username)
    if records is not None and len(records) > 0:
        continue
    # 翻译人名
    newText = nameChain.invoke({'name': username})
    db_manager.insert_username(username, newText.content)
    # 替换文章中原来的名字
    text = text.replace(username, newText.content)
# 设置为本地的模型，因为vicuna使用的是假名字"text-embedding-ada-002"
# chat = ChatOpenAI(model="text-embedding-ada-002",temperature=0)
# answer = chat.invoke("Translate this sentence from English to Chinese. I love programming.")
# print(answer)
