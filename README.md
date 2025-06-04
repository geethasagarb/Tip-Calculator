```mermaid
flowchart TB
    subgraph "Frontend Layer"
        Browser["Web Browser"]:::frontend
        Template["Index.html (Jinja2 Template)"]:::frontend
    end

    subgraph "Backend Layer"
        App["Flask Server\n(app.py)"]:::backend
        Calc["Tip Calculation\n(Function)"]:::backend
        Jinja["Jinja2 Engine"]:::backend
    end

    subgraph "Project Files"
        Gitignore[".gitignore"]:::docs
        Readme["README.md"]:::docs
        Req["requirements.txt"]:::docs
    end

    Browser -->|"HTTP GET Request"| App
    App -->|"invoke calculation"| Calc
    Calc -->|"returns tip value"| App
    App -->|"render template"| Template
    Template -->|"HTML Response"| Browser
    App -->|"uses"| Jinja

    click App "https://github.com/geethasagarb/tip-calculator/blob/main/app.py"
    click Template "https://github.com/geethasagarb/tip-calculator/blob/main/templates/index.html"
    click Req "https://github.com/geethasagarb/tip-calculator/blob/main/requirements.txt"
    click Readme "https://github.com/geethasagarb/tip-calculator/blob/main/README.md"
    click Gitignore "https://github.com/geethasagarb/tip-calculator/blob/main/.gitignore"

    classDef frontend fill:#ADD8E6,stroke:#333,color:#000
    classDef backend fill:#90EE90,stroke:#333,color:#000
    classDef docs fill:#D3D3D3,stroke:#333,color:#000
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
