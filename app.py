from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        

        {
            "title": "careBot",
         "description": "CareBot is a doctor-assisted medical chatbot built with Python, Flask, Tailwind CSS, Bootstrap, and the Groq API. It is designed to provide general health guidance, basic symptom support, and safe over-the-counter (OTC) suggestions while reinforcing that it is not a replacement for professional medical care.",
         "link": "https://carebot-blue.vercel.app"

        },

        {"title": " BOQ-CAD Tanzania",
         "description": " Professional Web-Based Architectural Plan Drawing & Construction Cost Estimator Built with pure PHP, MySQL, HTML, CSS, JavaScript, AJAX, Fabric.js, Tailwind CSS, Bootstrap 5 and MySQL.",
         "link": "https://artzone.page.gd"

        },
        {"title": "Smart Tour Guide with AI Assistance",
                    "description": "An AI-powered Progressive Web App that helps tourists explore Tanzania with real-time GPS navigation, landmark recognition, and an intelligent travel chatbot. The system combines offline map support, weather and pricing insights, and an AI-moderated community forum into one platform, designed for reliable use even in remote areas with limited connectivity.",
                    "link": "https://smart-tourism.gt.tc"
                },
        
        {
            "title": "E-Commerce Platform",
            "description": "Built a full-stack e-commerce web application with product management, cart functionality, secure checkout, and dashboard analytics.",
            "link": "https://github.com/yourusername/ecommerce-platform"
        },
        {
            "title": "Inventory Management System",
            "description": "Developed a business dashboard for tracking inventory, sales, and stock movement using Python, PHP, and JavaScript.",
            "link": "https://github.com/yourusername/inventory-management"
        },
        {
            "title": "Task Management App",
            "description": "Created a productivity app with user authentication, task filtering, deadlines, and reminder features.",
            "link": "https://github.com/yourusername/task-manager"
        }
    ]

    skills = [
        "Python", "Flask", "PHP", "JavaScript", "HTML5", "CSS3",
        "Bootstrap", "Tailwind CSS", "MySQL", "REST APIs", "Git/GitHub",
        "UI/UX", "Responsive Design", "Problem Solving"
    ]

    return render_template("index.html", projects=projects, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)