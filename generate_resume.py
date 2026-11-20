#!/usr/bin/env python3
import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_resume(output_pdf_path):
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=45.6,
        rightMargin=45.6,
        topMargin=28.0,
        bottomMargin=24.0,
    )

    primary_color = colors.HexColor("#1A4F9E")

    name_style = ParagraphStyle(
        'Name',
        fontName='Times-Bold',
        fontSize=18.5,
        leading=21.5,
        alignment=1,
        textColor=colors.black,
        spaceAfter=3,
    )

    contact_style = ParagraphStyle(
        'Contact',
        fontName='Times-Roman',
        fontSize=8.8,
        leading=10.5,
        alignment=1,
        textColor=colors.black,
        spaceAfter=6,
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Times-Bold',
        fontSize=10.2,
        leading=11.5,
        textColor=colors.black,
        spaceBefore=5,
        spaceAfter=1,
        keepWithNext=True,
    )

    item_title_bold = ParagraphStyle(
        'ItemTitleBold',
        fontName='Times-Bold',
        fontSize=8.8,
        leading=10.4,
        textColor=colors.black,
    )

    item_title_roman = ParagraphStyle(
        'ItemTitleRoman',
        fontName='Times-Roman',
        fontSize=8.8,
        leading=10.4,
        textColor=colors.black,
        alignment=2,
    )

    item_sub_italic = ParagraphStyle(
        'ItemSubItalic',
        fontName='Times-Italic',
        fontSize=8.8,
        leading=10.4,
        textColor=colors.black,
    )

    item_sub_date = ParagraphStyle(
        'ItemSubDate',
        fontName='Times-Roman',
        fontSize=8.8,
        leading=10.4,
        textColor=colors.black,
        alignment=2,
    )

    link_style = ParagraphStyle(
        'ProjectLink',
        fontName='Times-Roman',
        fontSize=8.8,
        leading=10.4,
        textColor=primary_color,
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        fontName='Times-Roman',
        fontSize=8.6,
        leading=10.2,
        leftIndent=14,
        firstLineIndent=-14,
        spaceBefore=1,
        spaceAfter=1,
        textColor=colors.black,
    )

    story = []

    # 1. Header
    story.append(Paragraph("Ramanpreet Singh", name_style))
    contact_line = (
        'New York, NY | r.preet01@outlook.it | (929) 623-3075 | '
        f'<a href="https://www.linkedin.com/in/ramanpreet-singh-524448386" color="{primary_color}">www.linkedin.com/in/ramanpreet-singh-524448386</a> | '
        f'<a href="https://github.com/Ramanpreet8" color="{primary_color}">GitHub</a> | '
        f'<a href="https://portfolio-ramanpreet.netlify.app" color="{primary_color}">Portfolio</a>'
    )
    story.append(Paragraph(contact_line, contact_style))

    def add_section_divider(title):
        story.append(Paragraph(title, section_heading))
        story.append(HRFlowable(width="100%", thickness=0.7, color=colors.black, spaceBefore=1, spaceAfter=3))

    # 2. EDUCATION & CERTIFICATIONS
    add_section_divider("EDUCATION & CERTIFICATIONS")

    # College
    t1 = Table([
        [Paragraph("<b>CUNY New York City College of Technology</b>", item_title_bold),
         Paragraph("Brooklyn, NY", item_title_roman)]
    ], colWidths=[380, 140.8])
    t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t1)

    t2 = Table([
        [Paragraph("Bachelor of Technology (BTech), Computer Systems Technology. GPA: 3.73.", item_sub_italic),
         Paragraph("Expected Spring 2028", item_sub_date)]
    ], colWidths=[380, 140.8])
    t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t2)

    # NYC TTP
    t3 = Table([
        [Paragraph("<b>NYC Tech Talent Pipeline Residency</b>", item_title_bold),
         Paragraph("Brooklyn, NY", item_title_roman)]
    ], colWidths=[380, 140.8])
    t3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 1)]))
    story.append(t3)

    t4 = Table([
        [Paragraph("Resident", item_sub_italic),
         Paragraph("June 2026", item_sub_date)]
    ], colWidths=[380, 140.8])
    t4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t4)
    story.append(Paragraph("• Completed a 12-week full-stack development bootcamp covering data analysis and visualization in JupyterLab, security incident response and intelligence-cycle analysis, Linux/Windows system administration, and team-based development using Git/GitHub.", bullet_style))

    # Certifications
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Certifications</b>", item_title_bold))
    story.append(Paragraph("• <b>CodePath – AI110: Foundations of AI Engineering:</b> Python, AI-assisted programming, algorithms, machine learning, RAG, and AI application development.", bullet_style))
    story.append(Paragraph("• <b>CodePath – WEB101: Intro to Web Development:</b> HTML, CSS, JavaScript, DOM manipulation, responsive web design, and interactive website development.", bullet_style))
    story.append(Paragraph("• <b>Information Security Basics – TEEX (Texas A&M) / DHS-FEMA (11/2025):</b> 13-hour technical training in information security fundamentals.", bullet_style))

    # 3. PROJECTS
    add_section_divider("PROJECTS")

    # Project 1: Live Interactive Educational Game
    story.append(Paragraph("<b>Live Interactive Educational Game – MLH Hack Day @ CityTech</b>", item_title_bold))
    story.append(Paragraph(f'<a href="https://github.com/Ramanpreet8/Live-interactive-educational-game" color="{primary_color}">https://github.com/Ramanpreet8/Live-interactive-educational-game</a>', link_style))
    story.append(Paragraph("React 18, TypeScript, Node.js, Express, Socket.IO, Google Gemini API", item_sub_italic))
    story.append(Paragraph("• Co-built and shipped a real-time multiplayer quiz platform in under 7 hours, where players join a live game through a QR code or room code.", bullet_style))
    story.append(Paragraph("• Implemented the gameplay loop: live countdown scoring, answer streaks, XP progression, and animated podiums to keep players engaged.", bullet_style))
    story.append(Paragraph("• Integrated the Google Gemini API to automatically generate custom quizzes from any topic prompt.", bullet_style))
    story.append(Paragraph("• Engineered an authoritative Socket.IO state machine with shared TypeScript interfaces between client and server to prevent client-side desync.", bullet_style))

    # Project 2: NutriBloom
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>NutriBloom — AI-Augmented Full-Stack Nutrition Platform</b>", item_title_bold))
    story.append(Paragraph(f'<a href="https://nutribloom8.netlify.app/login" color="{primary_color}">https://nutribloom8.netlify.app/login</a>', link_style))
    story.append(Paragraph("React 19, Ionic, Express, PostgreSQL, Prisma, Recharts, Jest, GitHub Actions | Tooling: Google Antigravity", item_sub_italic))
    story.append(Paragraph("• Extended a 5-person academic prototype into a solo full-stack platform; engineered biometric Mifflin-St Jeor DRV calculation, USDA FoodData API integration, and Recharts historical telemetry dashboards.", bullet_style))
    story.append(Paragraph("• Partnered with Google Antigravity via an AI-assisted TDD workflow to draft and run 12 Jest/Supertest integration tests, systematically debugging a multi-item database loop flaw and UUID parsing bugs.", bullet_style))
    story.append(Paragraph("• Hardened API security through AI-guided code audits: eliminated sensitive request body logs, implemented Passport.js JWT auth, and added windowed rate limiting on 2 public authentication routes.", bullet_style))
    story.append(Paragraph("• Authored an idempotent database seeding engine for instant 1-click demo logins with 15-minute token TTLs and API-level write protection, establishing automated GitHub Actions CI/CD to Netlify and Render.", bullet_style))

    # Project 3: Air Pollution
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Air Pollution & Public Health Data Analysis</b>", item_title_bold))
    story.append(Paragraph(f'<a href="https://github.com/Ramanpreet8/AirPollution.git" color="{primary_color}">https://github.com/Ramanpreet8/AirPollution.git</a>', link_style))
    story.append(Paragraph("Python, Pandas, Seaborn, Plotly", item_sub_italic))
    story.append(Paragraph("• Merged 19,827 air-quality rows and 48 asthma rows in Pandas, filtering out 7,439 out-of-scope records to isolate borough-level data for analysis.", bullet_style))
    story.append(Paragraph("• Compared children's asthma ED visit rates across NYC boroughs, finding the Bronx rate was 284.3% higher than Staten Island's (212.5 vs. 55.3 per 100k).", bullet_style))
    story.append(Paragraph("• Visualized borough-level disparities in Seaborn and Plotly; tested for a PM2.5-asthma correlation and found it unsupported due to 0 overlapping years.", bullet_style))

    # 4. EXPERIENCE
    add_section_divider("EXPERIENCE")
    t5 = Table([
        [Paragraph("<b>Undergraduate Researcher, CUNY New York City College of Technology</b>", item_title_bold),
         Paragraph("10/2026 – 12/2026", item_title_roman)]
    ], colWidths=[380, 140.8])
    t5.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t5)

    t6 = Table([
        [Paragraph("Emerging Scholars Program (ESP) – Undergraduate Research", item_sub_italic),
         Paragraph("Brooklyn, NY", item_sub_date)]
    ], colWidths=[380, 140.8])
    t6.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t6)

    story.append(Paragraph("• Conducted independent systems-oriented research on quantum computing for the \"From Bits to Qubits\" project, designing a 14-row comparison table (1 maps, 4 deform, 8 break, 1 open) and auditing all technical claims against primary sources (RP 2011, NA 2019, and 2023+ literature).", bullet_style))
    story.append(Paragraph("• Drafted the 200-word research abstract and am currently preparing the final poster for presentation at the December 2026 Symposium.", bullet_style))

    # 5. SKILLS
    add_section_divider("SKILLS")
    skills = [
        ("Languages:", "Python 3, JavaScript (ES6+), TypeScript, Java, SQL, HTML5"),
        ("Frontend:", "React, Ionic, Recharts, Responsive Design"),
        ("Backend & Databases:", "Express.js, REST APIs, Socket.IO, Prisma ORM, PostgreSQL, MySQL"),
        ("Data Analysis & Visualization:", "Pandas, Seaborn, Plotly, Jupyter Notebook / JupyterLab"),
        ("Tools & DevOps:", "Git, GitHub, GitHub Actions (CI/CD), Linux, Windows System Administration"),
    ]
    for label, val in skills:
        story.append(Paragraph(f"<b>{label}</b> {val}", bullet_style))

    doc.build(story)
    print(f"Generated resume at: {output_pdf_path}")

if __name__ == '__main__':
    # 1. Update in portfolio assets
    portfolio_asset_path = '/Users/ramanpreetsingh/Ramanpreet-portfolio/Documents/ramanpreet - portfolio/assets/Ramanpreet_Singh_Resume.pdf'
    generate_resume(portfolio_asset_path)

    # 2. Update in user home directory
    home_resume_path = '/Users/ramanpreetsingh/Ramanpreet_Singh_Resume.pdf'
    shutil.copyfile(portfolio_asset_path, home_resume_path)
    print(f"Copied resume to: {home_resume_path}")
