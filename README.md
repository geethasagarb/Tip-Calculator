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

# Tip 🤔

Hey there!

**Tip** is a tiny, fun tip calculator I built using Flask. It has a clean UI, works in light and dark mode, and even remembers your past tips using a small SQLite database.

I made it to get better at deploying real apps and to have something of my own that actually runs online 😄

---

## What it does

- Enter your meal cost (like `$50.00`)
- Enter a tip % (like `15%`)
- It calculates your tip instantly 💸
- Stores your tips in a local database (SQLite)

---

##  Try it live

👉 [Live App](https://tip-ug1e.onrender.com)

---

## 🧪 Run it locally

```bash
git clone https://github.com/geethasagarb/Tip-Calculator.git
cd Tip-Calculator
pip install -r requirements.txt
python app.py
