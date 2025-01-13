# 🩺 Diabetic Retinopathy Detection API

## 📌 Overview
This is a **Flask-based API** for detecting **Diabetic Retinopathy** in fundus images using **Deep Learning**. The model is deployed as a RESTful API, allowing users to upload eye images and get a **diagnosis prediction**.

---

## 🚀 Features
✅ **Deep Learning Model** - Uses DenseNet for Diabetic Retinopathy detection.  
✅ **Flask API** - Simple and lightweight REST API for predictions.  
✅ **Postman Support** - Test API requests easily.  
✅ **GitHub Integration** - Version-controlled for continuous improvements.  
✅ **Future Plans** - Web UI & deployment on cloud services (AWS, Render, etc.).

---

## 🛠️ Setup Instructions
### **1️⃣ Install Requirements**
Before running the API, install the necessary Python packages:
```bash
pip install flask tensorflow pillow numpy pyngrok
```

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/GMustafaBME/diabetic-retinopathy-api.git
cd diabetic-retinopathy-api
```

### **3️⃣ Run the Flask API**
```bash
python app.py
```

### **4️⃣ Use Postman to Send Requests**
- Open **Postman**  
- Set **Method** = `POST`  
- URL = `http://127.0.0.1:5000/predict`
- Select **Body → form-data → Key: `file` → Upload an image**
- Click **"Send"**

Example Response:
```json
{
    "prediction": "Diabetic Retinopathy Detected",
    "confidence_score": 0.87
}
```

---

## 🛠️ Deployment
To run this API **on the internet**, use:
```bash
ngrok http 5000
```
This will generate a **public URL**, which can be used for testing.

---

## 🤝 Contributing
Contributions are welcome! If you want to improve the model or add new features:
1. **Fork the repository**
2. **Create a new branch** (`feature-xyz`)
3. **Make changes and commit**
4. **Submit a Pull Request (PR)**

---

## 📝 License
This project is **open-source** under the **MIT License**.

---

🎯 **Future Plans**
- ✅ **Deploy API on AWS / Render**
- ✅ **Create a Web UI for easier use**
- ✅ **Improve Model Accuracy**
- ✅ **Support for more eye diseases**
