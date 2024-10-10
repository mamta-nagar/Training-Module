from flask import Flask, request, jsonify
import hashlib

app=Flask(__name__)

@app.route("/mypage", methods=["POST"])
def user():
    data=request.get_json()
    name=data.get('name','')
    name=name.strip()
    age=data.get('age','')
    age=age.strip()
    header=request.headers
    token = header.get('Authorization','')
    bearer =token.split(' ')[1]
    bearer=bearer.strip()
    hash_input = f"{name}{age}"
    md5_hash = hashlib.md5(hash_input.encode()).hexdigest()    
    
    
    

    dict={"e1":"",
          "e2":"",
          "e3":""}

    if(name==""):
        dict["e1"]="name is req"
    if(age==""):
        dict["e2"]="age is req"
    if(bearer==""):
        dict["e3"]="bearer is req"
    if (not(bearer==md5_hash)):
        dict["e3"]="data is invalid"
    if (dict["e1"]=="" and dict["e2"]=="" and dict["e3"]==""):
        return "successful"
    return f"{dict['e1']} {dict['e2']} {dict['e3']}"

    
    
        
       

    
if __name__=="__main__":
    app.run(debug=True)