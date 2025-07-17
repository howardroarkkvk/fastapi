import gradio as gr
import threading
from fastapi import FastAPI
import uvicorn

app =FastAPI()

@app.get('/hello')
def hello():
    return {'message':'Fast API is running'}


def launch_gradio():
    def greet(name):
        return f'hello {name}'
    gr.Interface(greet,inputs='text',outputs='text').launch()


threading.Thread(target=launch_gradio).start()
    

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
