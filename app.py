from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        
            {
                
                    "title": "English Teacher Bot",
                    "description": "A bot that can help you to learn English with interactive text to sound mode, created by using php,groq models, and AJAX.",
                    "link": "https://english-teach.kesug.com"
                },
{
  "title": "Smart Clinic — Medicine Availability & Healthcare Referral Platform",
  "description": "A healthcare platform that helps patients find live medicine availability, locate registered clinics on a map, request appointments, and track referrals. Clinics manage batch-level inventory, expiry risk, stock alerts, and unmet demand from one owner console, so shelf truth and patient access stay connected in real time.",
  "link": "https://smart-clinc.free.je"
            },

{
  "title": "Online Drafts — 10×10 International",
  "description": "A premium, mobile-first International Draughts arena with real-time multiplayer, CSS 3D board, challenge codes, bot opponents, majority capture and live clocks. Built for fast play on phones and reliable matches even with light connectivity.",
  "link": "https://agent-6ad788d08bf621689--unrivaled-mousse-762e09.netlify.app"
}

,

{"title": "Smart Tour Guide with AI Assistance",
                    "description": "An AI-powered Progressive Web App that helps tourists explore Tanzania with real-time GPS navigation, landmark recognition, and an intelligent travel chatbot. The system combines offline map support, weather and pricing insights, and an AI-moderated community forum into one platform, designed for reliable use even in remote areas with limited connectivity.",
                    "link": "https://smart-tourism.gt.tc"
                },
                {
  "title": "NewsPulse — Real-time News Aggregator",
  "description": "A clean, modern 2026 news app with live headlines, category browsing, keyword search, dark mode and responsive card layout. Powered by Currents API with production-ready free tier support. Built with Flask and Tailwind for fast reading on any device.",
  "link": "https://news-application-six-eta.vercel.app"
},
                {
  "title": "Universal POS — Point of Sale for Tanzanian Businesses",
  "description": "A full-stack Point of Sale platform built for shops across Tanzania, with fast selling, inventory and stock control, customer debts (madeni), multi-payment checkout including SonicPesa mobile money, role-based access, daily closing, and business reports. Designed for supermarkets, pharmacies, hardware stores, and minimarkets.",
  "link": "https://pos-system-rouge-nu.vercel.app"
},
         {
                            "title": "Inventory Management System",
                            "description": "Developed a business dashboard for tracking inventory, sales, and stock movement using Next.js and PSQL.",
                            "link": "https://inventorrry.netlify.app"
                        },


        {"title": " BOQ-CAD Tanzania",
         "description": " Professional Web-Based Architectural Plan Drawing & Construction Cost Estimator Built with pure PHP, MySQL, HTML, CSS, JavaScript, AJAX, Fabric.js, Tailwind CSS, Bootstrap 5 and MySQL.",
         "link": "https://artzone.page.gd"

        },
        
                
        {
            "title": "careBot",
         "description": "CareBot is a doctor-assisted medical chatbot built with Python, Flask, Tailwind CSS, Bootstrap, and the Groq API. It is designed to provide general health guidance, basic symptom support, and safe over-the-counter (OTC) suggestions while reinforcing that it is not a replacement for professional medical care.",
         "link": "https://carebot-blue.vercel.app"

        }
    ]

    skills = [
        "Python", "Flask", "PHP", "JavaScript", "HTML5", "CSS3",
        "Bootstrap", "Tailwind CSS", "PSQL/MySQL", "REST APIs", "Git/GitHub",
        "UI/UX", "Responsive Design", "Problem Solving"
    ]

    return render_template("index.html", projects=projects, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)