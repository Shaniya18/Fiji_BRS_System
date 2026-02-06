✈️ Fiji Baggage Reconciliation System (BRS)

Credentials (Demo Only)

Username: staff_admin
Password: Fiji2026!

🏗️ System Architecture

This system is designed using a 3-Tier Architecture to ensure modularity, security, and scalability, aligned with aviation-grade system requirements.

Presentation Layer
        ↓
Logic Layer (API)
        ↓
Data Layer (Database)

🧱 Technology Stack
1️⃣ Data Layer — The Foundation

Database: MySQL (Hosted on Aiven Cloud)

Management Tool: DBeaver

Security:

SSL/TLS encrypted connections using ca.pem

Protection against Man-in-the-Middle attacks

Data Integrity:

Python ORM

Parameterized queries to prevent SQL Injection

2️⃣ Logic Layer — The Brain

Backend Framework: Django REST Framework (DRF)

Responsibilities:

Authentication & authorization

Business rule validation (e.g. baggage weight limits)

RESTful API routing

Integration:

API endpoints tested and simulated via Postman

Handles hardware-simulated baggage scans

Acts as a Digital Control Tower for all baggage operations.

3️⃣ Presentation Layer — Decoupled Frontends
🧑‍✈️ Staff Dashboard

Framework: ASP.NET MVC

Hosting: MonsterASP (Windows / IIS)

Purpose:
High-performance administrative interface for ground staff operations

🧳 Passenger Portal

Framework: Django + Bootstrap

Hosting: Render (Linux)

Purpose:
Mobile-responsive portal for passengers to track baggage status in real time

🛡️ Security Features

🔐 Data Encryption

End-to-end SSL encryption for all cloud traffic

🧾 Audit Trail

Every baggage scan recorded in the SCANS table

Includes timestamp and location for full traceability

🚫 Zero-Trust Validation

A bag cannot be marked as Loaded

Unless it is first Security Cleared

🚀 DevOps & Development Workflow

SDLC

Requirement Analysis → Design → Development → Testing → Deployment

CI/CD

Automated pipelines using GitHub Actions

Continuous deployment to Render

Testing

API testing via Postman

Database schema validation via DBeaver

📊 Future Enhancements

📈 Power BI Analytics

Visual dashboards for peak baggage flow

Bottleneck and performance analysis

📡 NFC / RFID Integration

Mobile-based instant baggage tagging

Faster scan times and improved tracking accuracy
