from flask import Flask, request, redirect, render_template, session
import json
app = Flask(__name__)

app.secret_key = 'QWERTYUIOP'  # 对用户信息加密

#@app.before_request

#def check_login():
#    # 检查用户是否已登录
#    if not session.get('logged_in'):
#        # 用户未登录，重定向到登录页面
#        return redirect('/login')

#@app.route('/home')
#def home():
#    # 用户已登录，可以访问该页面
#    return '欢迎回来！'


@app.route('/',methods=['GET', 'POST'])
def indexx():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # 处理 POST 请求
        return render_template('index.html')





@app.route('/whiteip', methods=['GET', "POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def addwhiteip():
    if request.method == 'GET':
        with open("whiteip.txt","r")  as f:
            recent_white_ip=f.readlines()
            print(recent_white_ip)
            recent_white_ip= [item.strip() for item in recent_white_ip]
        #return render_template('white_ip.html', recent_white_ip= recent_white_ip)
        return render_template('white_ip.html', recent_white_ip=recent_white_ip)



    #user = request.form.get('user')
    #pwd = request.form.get('pwd')
    #if user == 'admin' and pwd == '123':  # 这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
        #session['user_info'] = user  #用户登录信息保存到sesson中
       #return redirect('/white-ip')
    else:
#        return render_template('login.html', msg='格式错误')
        get_white_list=request.form.getlist("whiteip")
        ip_split=",".join(get_white_list)
        with open("whiteip.txt","w")  as f:
            print(get_white_list)
            ip_list=ip_split.split(",")
            for i in ip_list:
                print(i)
                f.write(i +"\n")

        return redirect("/isok")



@app.route('/blackip', methods=['GET', "POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def addblackip():
    if request.method == 'GET':
        with open("blackip.txt","r")  as f:
            recent_black_ip=f.readlines()
            print(recent_black_ip)
            recent_black_ip= [item.strip() for item in recent_black_ip]
   #     return render_template('black_ip.html', recent_black_ip= recent_black_ip)
            return render_template('black_ip.html', recent_black_ip=recent_black_ip)
    else:
#        return render_template('login.html', msg='格式错误')
        get_white_list=request.form.getlist("whiteip")
        ip_split=",".join(get_white_list)
        with open("blackip.txt","w")  as f:
            print(get_white_list)
            ip_list=ip_split.split(",")
            for i in ip_list:
                print(i)
                f.write(i +"\n")
        return redirect("/isok")


#域名节点配置相关功能
@app.route('/domaingroup', methods=['GET', "POST"])
def nodegroup():
    if request.method =="GET":
        with open("domaingroup.json","r") as f:
            json_obj = json.load(f)
            for key,value  in json_obj.items():
                print(key,value)
        return  render_template("domaingroup.html")
    else:
        domain_name=request.form.get("name")
        domain_name_node=request.form.get("content")
        with open("domaingroup.json","r") as f:
            json_obj = json.load(f)
            print(json_obj)
#            print(domain_name,domain_name_node)
            json_obj[domain_name]=domain_name_node,"删除","禁用"
#        domain_jason={domain_name:domain_name_node}
        with open("domaingroup.json","w",encoding="utf-8") as f:
            json.dump(json_obj,f,ensure_ascii=False)
            return redirect("/isok")

#cdn节点添加相关内容

@app.route('/cdnnode', methods=['GET', "POST"])
def cdnnode():
    if request.method == "GET":
        with open("domaingroup.json", "r") as f:
            json_obj = json.load(f)
            for key, value in json_obj.items():
                print(key, value)
        return render_template("domaingroup.html")
    else:
        domain_name = request.form.get("name")
        domain_name_node = request.form.get("content")
        with open("domaingroup.json", "r") as f:
            json_obj = json.load(f)
            print(json_obj)
            #            print(domain_name,domain_name_node)
            json_obj[domain_name] = domain_name_node, "删除", "禁用"
        #        domain_jason={domain_name:domain_name_node}
        with open("domaingroup.json", "w", encoding="utf-8") as f:
            json.dump(json_obj, f, ensure_ascii=False)
            return redirect("/isok")

import  requests
@app.route('/cachereget',methods=['GET', "POST"])
def cachereget():
    if  request.method=="GET":
        return render_template("cachereget.html")
    else:
        cachereget_url=request.form.getlist("cachereget")
        cachereget_url= [line.strip() for string in cachereget_url for line in string.split('\r\n')]
        #print(cachereget_url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",}
        for i in cachereget_url:
            url=i
            rrquest=requests.get(url=url,headers=headers)
            print(rrquest.reason)

        return "ok"


import time
@app.route('/adddomain',methods=['GET','POST'])
def adddomain():
    if request.method=="GET":
        return render_template("adddomain.html")
    else:
        get_domain_title=request.form.get("domaintitle")
        get_domain_get = request.form.get("domainget")
        get_domain_ip = request.form.get("domainip")
        print(get_domain_title,get_domain_get,get_domain_ip )
        return("ok")
        time.sleep(2)
        redirect("/")

@app.route('/isok')
def index():
    return '添加成功'



if __name__=='__main__':
    app.run("192.168.0.26","5000",debug=True)
