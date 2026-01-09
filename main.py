import os
import base64
import json
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key='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'
)

@app.get("/")
async def home():
    return FileResponse("templates/index.html")

@app.post("/chat")
async def chat(
    history: str = Form(...),
    message: str = Form(""),
    image: UploadFile = File(None)
):
    messages = json.loads(history)

    content = []

    if message:
        content.append({
            "type": "text",
            "text": message
        })

    if image:
        img_bytes = await image.read()
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:{image.content_type};base64,{img_base64}"
            }
        })

    messages.append({
        "role": "user",
        "content": content
    })

    response = client.chat.completions.create(
        model="qwen/qwen-2.5-vl-7b-instruct:free",
        messages=messages
    )

    return JSONResponse({
        "reply": response.choices[0].message.content
    })
