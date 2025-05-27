from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.utils.predict import load_model_and_predict

import uvicorn

app = FastAPI(
    title="Trafik İşareti Sınıflandırıcı",
    description="Eğitilmiş trafik işareti modeline görsel göndererek sınıf tahmini alabilirsiniz.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Trafik işareti sınıflandırma servisine hoş geldiniz!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        result = load_model_and_predict(image_bytes)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
