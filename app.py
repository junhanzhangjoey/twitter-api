from flask import Flask,request,render_template
from instance import post, retrieve, delete
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route("/")
def main():
    return render_template('app.html',id=None, content=None,message=None)

@app.route("/post",methods=['GET','POST'])
def post_status():
    content=request.form.get('content')
    id=post(content)
    return render_template('app.html',id=id,content=content,message="Post Done!")


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

if __name__=="__main__":
    app.run(debug=True)