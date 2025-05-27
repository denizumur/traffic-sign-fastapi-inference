# Traffic Sign Classification API (FastAPI + Docker)
Bu proje, Google Colab üzerinde eğitilen bir trafik işareti tanıma (classification) modelinin **FastAPI** kullanılarak **Docker konteyneri** üzerinden sunulmasını sağlar.

## 🔧 Özellikler
Docker ile hızlı kurulum
FastAPI ile REST servisi
Görsel yükleyerek sınıf tahmini
Model `.keras` formatında
Sadece **çıkarım (inference)** için gerekli dosyaları içerir
Eğitim, veri ön işleme veya grafik kodları bu repoda yer almaz.
FastAPI sunucusu konteyner içinde 7001 portunda çalışır.

---

## Kurulum

### repoyu klonlayın: ###Docker servisini başlatın:
### repoyu klonlayın:
```bash
git clone https://github.com/denizumur/traffic-sign-fastapi-inference.git
cd traffic-sign-fastapi-inference
---

### Docker servisini başlatın:
docker-compose up --build

###Servisin çalıştığını kontrol etmek için: 
#İstek:
GET http://localhost:7001/

#Yanıt:
{
  "message": "Trafik işareti sınıflandırma servisine hoş geldiniz!"
}

###POST /predict
Bir trafik işareti görüntüsünü sınıflandırmak için:

#İstek:
curl -X POST http://localhost:7001/predict \
  -H "accept: application/json" \
  -F "file=@test_sign.png"

  #!!!!!!!!! test_sign.png görselinin bu komutun çalıştığı dizinde bulunması gerekir.

#Yanıt:
Kodu kopyala
{
  "class_id": 14,
  "label": "Stop",
  "confidence": "97.35%"
}