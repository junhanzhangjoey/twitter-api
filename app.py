from flask import Flask,request,render_template
from instance import post, retrieve, delete
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route("/") #means when the website goes to "/" route, run the function underneath
def main():
    return render_template('app.html',id=None, content=None,message=None) ##render the webpage and send the three variable to front end

@app.route("/post",methods=['GET','POST'])#route() only respond to GET method in default, this make rout() respond to POST method as well
def post_status():
    content=request.form.get('content')#get the frontend's form's input content
    id=post(content)
    return render_template('app.html',id=id,content=content,message="Post Done!")#go to the new route and show user "Post Done!"


@app.route("/retrieve",methods=['GET','POST'])
def retrieve_status():
    id=request.form.get('id')

    soup = BeautifulSoup(retrieve(id), "html.parser")
    content=soup.get_text()
    
    return render_template('app.html',id=id,content=content,message="retrieve succeed")

@app.route("/delete",methods=['GET','POST'])
def delete_status():
    id=request.form.get('id')
    content=delete(id)
    return render_template('app.html',id=id,content=content,message=f"status id: {id} delete success")

if __name__=="__main__":#
    app.run(debug=True)