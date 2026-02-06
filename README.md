✈️ Fiji Baggage Reconciliation System (BRS)
[Live Demo: Passenger Portal (Render)] | [Live Demo: Staff Dashboard (MonsterASP)]
(Credentials: staff_admin / Fiji2026!)

🏗️ Architecture & Technology Stack
I designed this system using a 3-Tier Architecture to ensure modularity, security, and scalability—essential requirements for critical aviation infrastructure.

1. Data Layer (The Foundation)
Database: MySQL (Hosted on Aiven Cloud).

Management: Configured via DBeaver using SSL/TLS tunnels (ca.pem) to prevent Man-in-the-Middle attacks.

Integrity: Utilizes Python ORM with parameterized queries to neutralize SQL Injection threats.

2. Logic Layer (The Brain)
Backend: Django REST Framework (DRF).

Role: Acts as the "Digital Control Tower," handling Authentication, Business Logic Validation (e.g., weight limits), and RESTful API routing.

Integration: Serves as the endpoint for hardware-simulated scans via Postman.

3. Presentation Layer (Decoupled Frontends)
Staff Dashboard (ASP.NET MVC): * Platform: Hosted on MonsterASP (Windows/IIS).

Purpose: A high-performance administrative interface for ground staff.

URL: http://fijibrs.runasp.net

Passenger Portal (Django & Bootstrap): * Platform: Hosted on Render (Linux).

Purpose: A mobile-responsive portal for travelers to track baggage in real-time.

URL: https://fiji-brs-system.onrender.com

🛡️ Key Security Features
Data Encryption: All cloud traffic is protected by SSL certificates to ensure passenger data privacy.

Audit Trail: Every bag movement is logged in the SCANS table with a precise timestamp and location for full accountability.

Zero-Trust Logic: Backend validation ensures that a bag cannot be "Loaded" unless it has been "Security Cleared."

🚀 DevOps & Workflow
SDLC: Followed a strict Software Development Life Cycle from requirement analysis to deployment.

CI/CD: Automated deployment pipelines via GitHub Actions to Render, ensuring the system is always stable.

Testing: Comprehensive API testing conducted using Postman and database schema validation via DBeaver.

📊 Future Enhancements
Power BI Integration: Currently developing a Power BI Dashboard to visualize peak baggage flow and bottleneck trends.

NFC/RFID Support: Exploring mobile NFC integration for instant bag tagging.
