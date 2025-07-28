# 🛰️ Real-Time Visitor Analytics Dashboard (AWS Serverless)

A real-time visitor tracking system built with AWS: S3, API Gateway, Lambda (Python), and DynamoDB.

## Features

- Tracks real-time visitor metadata (browser, OS, language, time)
- Stores each visit in DynamoDB using serverless Lambda
- Simple dashboard to view recent visitors
- Extendable for IP logging, charts, geolocation, etc.

## Technologies Used

- Amazon S3 (Frontend Hosting)
- AWS Lambda (Backend Code)
- API Gateway (HTTP API v2)
- DynamoDB (NoSQL Storage)
- IAM Roles + CORS Config

## Folder Structure

```
visitor-analytics-dashboard/
├── backend/
│   └── lambda/
│       ├── TrackVisitorFunction.py
│       └── GetVisitorLogs.py
├── frontend/
│   ├── index.html
│   └── dashboard.html
├── README.md
```

## Setup Guide

1. Deploy Lambda functions in AWS Console
2. Create HTTP API Gateways (POST /collect and GET /visitors)
3. Create DynamoDB table named `VisitorLogs` with partition key `visitorId`
4. Upload HTML files to S3 bucket and enable static hosting
5. Update fetch URLs in HTML files with your actual API Gateway endpoints

## License

MIT License
