```mermaid
flowchart TD
    subgraph "Frontend Layer"
        Browser["Web Browser UI"]:::frontend
        Template["Jinja2 Template (index.html)"]:::frontend
    end

    HTTP["HTTP Request/Response"]:::infra

    subgraph "Backend Layer"
        FlaskApp["Flask App (app.py)"]:::backend
        ReqTxt["Dependencies (requirements.txt)"]:::infra
    end

    subgraph "Project Metadata"
        Readme["README.md"]:::infra
        Gitignore[".gitignore"]:::infra
    end

    Browser -->|"GET/POST"| HTTP
    HTTP -->|"routes to"| FlaskApp
    FlaskApp -->|"renders template"| Template
    Template -->|"HTML response"| HTTP
    HTTP -->|"delivers response"| Browser
    FlaskApp -->|"declares dependencies"| ReqTxt

    click FlaskApp "https://github.com/geethasagarb/tip-calculator/blob/main/app.py"
    click Template "https://github.com/geethasagarb/tip-calculator/blob/main/templates/index.html"
    click ReqTxt "https://github.com/geethasagarb/tip-calculator/blob/main/requirements.txt"
    click Readme "https://github.com/geethasagarb/tip-calculator/blob/main/README.md"
    click Gitignore "https://github.com/geethasagarb/tip-calculator/blob/main/.gitignore"

    classDef frontend fill:#BDE0FE,stroke:#0366D6,color:#0366D6;
    classDef backend fill:#95D5B2,stroke:#2F855A,color:#2F855A;
    classDef infra fill:#E9ECEF,stroke:#6C757D,color:#6C757D;
```

#  Tip 🤔

Hey there! 

This is **Tip**, a tiny but smart tip calculator I built as a fun side project. It's built using **Flask**, has a clean UI with **light/dark mode**, and even remembers your past tip calculations using a **SQLite database**.

I made this to get better at deploying real-world apps and just to have something of my own that actually works online 😄

---

## 🛠️ What it does

- You enter your **meal cost** (like `$45.00`)
- Enter a **tip percentage** (like `15%`)
- Hit "Calculate" and it'll show you the tip 💰
- Behind the scenes, it stores your tip in a mini database (just for you)

---
