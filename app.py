from flask import Flask,request,render_template
from instance import mastodon, post, retrieve, delete
from bs4 import BeautifulSoup

app=Flask(__name__)
id_list=[]
@app.route("/") #means when the website goes to "/" route, run the function underneath
def main():
    return render_template('app.html',id=None, content=None,message=None,list=id_list) ##render the webpage and send the three variable to front end

@app.route("/post",methods=['GET','POST'])#route() only respond to GET method in default, this make rout() respond to POST method as well
def post_status():
    content=request.form.get('content')#get the frontend's form's input content
    id=post(content,mastodon)
    id_list.append(id)
    return render_template('app.html',id=id,content=content,message="Post Done!",list=id_list)#render the page and show user "Post Done!"


@app.route("/retrieve",methods=['GET','POST'])
def retrieve_status():
    id=request.form.get('id')
    if(id in id_list):
        soup = BeautifulSoup(retrieve(id,mastodon), "html.parser")
        content=soup.get_text()
        return render_template('app.html',id=id,content=content,message="retrieve succeed",list=id_list)
    return render_template('app.html',id=None,content=None,message=f"status id: {id} not existed",list=id_list)

@app.route("/delete",methods=['GET','POST'])
def delete_status():
    global id_list
    id=request.form.get('id')
    if(id in id_list):
        content=delete(id,mastodon)
        temp=list(filter(lambda x:x!=id,id_list))
        id_list=temp
        return render_template('app.html',id=id,content=content,message=f"status id: {id} delete success",list=id_list)
    return render_template('app.html',id=None,content=None,message=f"status id: {id} not existed",list=id_list)

if __name__=="__main__":
    app.run(debug=True)