```mermaid
flowchart TD
    subgraph "Frontend Layer"
        Browser["Browser UI"]:::frontend
        Template["Jinja2 Template (index.html)"]:::frontend
    end

    subgraph "Backend Layer"
        Flask["Flask Application (app.py)"]:::backend
        Req["requirements.txt"]:::backend
    end

    subgraph "Infra / Metadata"
        HTTP["HTTP Transport"]:::infra
        README["README.md"]:::metadata
        GIT[".gitignore"]:::metadata
    end

    Browser -->|"GET/POST"| HTTP
    HTTP -->|"routes to"| Flask
    Flask -->|"renders template"| Template
    Template -->|"HTML Response"| HTTP
    HTTP -->|"delivers response"| Browser
    Req -->|"declares dependencies"| Flask

    click Flask "https://github.com/geethasagarb/tip-calculator/blob/main/app.py"
    click Template "https://github.com/geethasagarb/tip-calculator/blob/main/templates/index.html"
    click Req "https://github.com/geethasagarb/tip-calculator/blob/main/requirements.txt"
    click README "https://github.com/geethasagarb/tip-calculator/blob/main/README.md"
    click GIT "https://github.com/geethasagarb/tip-calculator/blob/main/.gitignore"

    classDef frontend fill:#E0F7FA,stroke:#0097A7;
    classDef backend fill:#E8F5E9,stroke:#388E3C;
    classDef infra fill:#EEEEEE,stroke:#616161;
    classDef metadata fill:#FFFFFF,stroke:#888888,stroke-dasharray:5 5;
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
