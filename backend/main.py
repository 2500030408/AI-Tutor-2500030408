from fastapi import FastAPI
klu=FastAPI(title="AI Tutor",
            description="AI Tutor PBL project",
            version="1.0.0"
)
@klu.get("/")
def home():
    return {"message":"Welcome to the AI Tutor Project"}
@klu.get("/demo")
def demo():
    return {"message":"KL university"}
@klu.get("/askquestion")
def ask():
    return {"message":"What is llm?","Answer":"Large Language Model"}
@klu.get("/student")
def student():
    return {"id":1,"name":"Ram","gender":"male","course":"DSA"}
@klu.get("/students")
def getstudents():
    return [{"id":1,"name":"Ram","gender":"male","course":"DSA"},
            {"id":2,"name":"klu","gender":"male","course":"DSA"},
            {"id":3,"name":"Seetha","gender":"female","course":"DSA"}]

   