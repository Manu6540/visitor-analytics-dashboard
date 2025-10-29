![Project Status](https://img.shields.io/badge/status-completed-brightgreen)
![Built With](https://img.shields.io/badge/built%20with-AWS%20Lambda%20%7C%20S3%20%7C%20DynamoDB-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


# 🛰️ Real-Time Visitor Analytics Dashboard (AWS Serverless)

A fully serverless real-time visitor tracking system built using **Amazon S3**, **API Gateway**, **AWS Lambda (Python)**, and **DynamoDB**.

It captures website visitors’ platform, language, browser, and timestamp — then visualizes it live in a simple HTML dashboard.

## 🚀 Live Demo

| Page            | URL |
|-----------------|-----|
| 🔍 Tracking Page | https://visitor-analytics-demo-manu.s3.us-east-1.amazonaws.com/index+(1).html |
| 📊 Dashboard     | https://visitor-analytics-demo-manu.s3.us-east-1.amazonaws.com/dashboard.html |


## 📦 Project Structure

visitor-analytics-dashboard/

├── backend/

│ └── lambda/

│ ├── TrackVisitorFunction.py

│ └── GetVisitorLogs.py

├── frontend/

│ ├── index.html

│ └── dashboard.html

├── README.md


## ✅ Features
- Real-time tracking of visitors (OS, language, browser)
- All visits stored in DynamoDB
- Visual dashboard showing each visitor as a table row
- Redirect-based GitHub/LinkedIn tracking (optional)
- 100% Serverless, secure, scalable

## 🧠 How It Works
1. Visitor loads `index.html` hosted on S3
2. JS sends metadata to API Gateway → Lambda → DynamoDB
3. `dashboard.html` fetches data from another Lambda via GET
4. Dashboard shows all visits in real-time

## 🧰 AWS Services Used
- S3
- API Gateway
- Lambda
- DynamoDB
- IAM
- CloudWatch

## 🙌 Author
Created by **Manmohan Bandaru**
