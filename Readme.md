# 🎓 Intelligent Educational CRM & Automated Enquiry System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![SQLite](https://img.shields.io/badge/SQLite-Integrated-green)
![HTML/CSS/JS](https://img.shields.io/badge/Frontend-Vanilla-orange)

A lightweight, rule-based chatbot and Customer Relationship Management (CRM) system designed to automate college administrative inquiries, eliminate telephonic congestion, and capture prospective student leads seamlessly. Originally developed for **Chandrabhan Sharma College of Arts, Commerce & Science**.

## 🚀 Key Features

*   **24/7 Automated Enquiry Desk:** Instantly answers repetitive queries regarding fee structures, admission deadlines, course availability, and college timings with 100% deterministic accuracy.
*   **Zero-Party Data Capture (CRM):** Automatically captures the visitor's Name and Phone Number before initiating the conversation, transforming casual web traffic into actionable admission leads.
*   **Secure Admin Dashboard:** A hidden, passkey-protected route (`/see_chats`) allows college administrators to view real-time chat histories and follow up with prospective students.
*   **Fault-Tolerant Database:** Embedded SQLite database gracefully handles missing data fields (assigning "Anonymous") to ensure zero transaction crashes.
*   **Asynchronous UI:** Mobile-responsive "app-like" interface built with vanilla JavaScript (Fetch API) to ensure conversations flow without page reloads.

## 🛠️ Technology Stack

*   **Backend:** Python 3, Flask (WSGI Micro-framework)
*   **Database:** SQLite3 (Serverless)
*   **Frontend:** HTML5, CSS3 (Flexbox), Vanilla JavaScript
*   **Data Interchange:** JSON

## 📂 Project Structure

```text
├── chatbot.py           # Main Flask application and routing logic
├── responses.py         # Institutional knowledge base dictionary
├── chat_history.db      # SQLite database (auto-generates on first run)
├── templates/
│   └── chatbot.html     # Frontend user interface
└── README.md            # Project documentation