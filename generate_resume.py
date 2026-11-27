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
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54,
    )

    name_style = ParagraphStyle(
        'Name',
        fontName='Times-Bold',
        fontSize=17,
        leading=19.5,
        alignment=1,
        textColor=colors.black,
        spaceAfter=2,
    )

    contact_style = ParagraphStyle(
        'Contact',
        fontName='Times-Roman',
        fontSize=10,
        leading=11.8,
        alignment=1,
        textColor=colors.black,
        spaceAfter=3,
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Times-Bold',
        fontSize=11,
        leading=12.5,
        textColor=colors.black,
        spaceBefore=2.5,
        spaceAfter=1,
        keepWithNext=True,
    )

    item_title_bold = ParagraphStyle(
        'ItemTitleBold',
        fontName='Times-Bold',
        fontSize=10,
        leading=11.8,
        textColor=colors.black,
    )

    item_title_roman = ParagraphStyle(
        'ItemTitleRoman',
        fontName='Times-Roman',
        fontSize=10,
        leading=11.8,
        textColor=colors.black,
        alignment=2,
    )

    item_sub_italic = ParagraphStyle(
        'ItemSubItalic',
        fontName='Times-Italic',
        fontSize=10,
        leading=11.8,
        textColor=colors.black,
    )

    item_sub_date = ParagraphStyle(
        'ItemSubDate',
        fontName='Times-Roman',
        fontSize=10,
        leading=11.8,
        textColor=colors.black,
        alignment=2,
    )

    link_style = ParagraphStyle(
        'ProjectLink',
        fontName='Times-Roman',
        fontSize=10,
        leading=11.8,
        textColor=colors.black,
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        fontName='Times-Roman',
        fontSize=10,
        leading=11.8,
        leftIndent=14,
        firstLineIndent=-14,
        spaceBefore=0,
        spaceAfter=0,
        textColor=colors.black,
    )

    story = []

    # 1. Header
    story.append(Paragraph("Ramanpreet Singh", name_style))
    contact_line = (
        'New York, NY | r.preet01@outlook.it | (929) 623-3075 | '
        '<a href="https://www.linkedin.com/in/ramanpreet-singh-524448386" color="black">LinkedIn</a> | '
        '<a href="https://github.com/Ramanpreet8" color="black">GitHub</a> | '
        '<a href="https://ramanpreet8.github.io/Ramanpreet-portfolio/" color="black">Portfolio</a>'
    )
    story.append(Paragraph(contact_line, contact_style))

    def add_section_divider(title):
        story.append(Paragraph(title, section_heading))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.black, spaceBefore=0.5, spaceAfter=2))

    # 2. EDUCATION & CERTIFICATIONS
    add_section_divider("EDUCATION & CERTIFICATIONS")

    # College
    t1 = Table([
        [Paragraph("<b>CUNY New York City College of Technology</b>", item_title_bold),
         Paragraph("Brooklyn, NY", item_title_roman)]
    ], colWidths=[370, 134])
    t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t1)

    t2 = Table([
        [Paragraph("Bachelor of Technology (BTech), Computer Systems Technology. GPA: 3.73.", item_sub_italic),
         Paragraph("Expected Spring 2028", item_sub_date)]
    ], colWidths=[370, 134])
    t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t2)

    # NYC TTP
    t3 = Table([
        [Paragraph("<b>NYC Tech Talent Pipeline Residency</b>", item_title_bold),
         Paragraph("Brooklyn, NY", item_title_roman)]
    ], colWidths=[370, 134])
    t3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t3)

    t4 = Table([
        [Paragraph("Resident", item_sub_italic),
         Paragraph("June 2026", item_sub_date)]
    ], colWidths=[370, 134])
    t4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t4)
    story.append(Paragraph("• Completed a 12-week full-stack bootcamp in JupyterLab data analysis, security incident response, Linux/Windows administration, and team-based development using Git/GitHub.", bullet_style))

    # Certifications
    story.append(Spacer(1, 1))
    story.append(Paragraph("<b>Certifications</b>", item_title_bold))
    story.append(Paragraph("• <b>CodePath – AI110 (AI Engineering):</b> Python, algorithms, machine learning, RAG, and AI application development.", bullet_style))
    story.append(Paragraph("• <b>CodePath – WEB101 (Intro to Web Development):</b> HTML, CSS, JavaScript, DOM manipulation, responsive design, and interactive web development.", bullet_style))
    story.append(Paragraph("• <b>Information Security Basics – TEEX / DHS-FEMA (11/2025):</b> 13-hour technical training in info security fundamentals.", bullet_style))

    # 3. PROJECTS
    add_section_divider("PROJECTS")

    # Project 1: Live Interactive Educational Game (3 bullets)
    story.append(Paragraph("<b>Live Interactive Educational Game – MLH Hack Day @ CityTech</b>", item_title_bold))
    story.append(Paragraph('<a href="https://github.com/Ramanpreet8/Live-interactive-educational-game" color="black">https://github.com/Ramanpreet8/Live-interactive-educational-game</a>', link_style))
    story.append(Paragraph("React 18, TypeScript, Node.js, Express, Socket.IO, Google Gemini API", item_sub_italic))
    story.append(Paragraph("• Co-built and shipped a real-time multiplayer quiz platform in under 7 hours; players join live via QR or room code.", bullet_style))
    story.append(Paragraph("• Implemented the gameplay loop: live countdown scoring, answer streaks, XP progression, and animated podiums.", bullet_style))
    story.append(Paragraph("• Engineered an authoritative Socket.IO state machine with shared TypeScript interfaces to prevent client desync.", bullet_style))

    # Project 2: NutriBloom (3 bullets)
    story.append(Spacer(1, 1))
    story.append(Paragraph("<b>NutriBloom — AI-Augmented Full-Stack Nutrition Platform</b>", item_title_bold))
    story.append(Paragraph('<a href="https://nutribloom8.netlify.app/login" color="black">https://nutribloom8.netlify.app/login</a>', link_style))
    story.append(Paragraph("React 19, Ionic, Express, PostgreSQL, Prisma, Recharts, Jest, GitHub Actions | Tooling: Google Antigravity", item_sub_italic))
    story.append(Paragraph("• Extended a 5-person prototype into a solo platform; built Mifflin-St Jeor DRV calculation, USDA FoodData API integration, and Recharts historical telemetry dashboards.", bullet_style))
    story.append(Paragraph("• Partnered with Google Antigravity via an AI-assisted TDD workflow to draft and run 12 Jest/Supertest integration tests, systematically debugging a multi-item database loop flaw and UUID parsing bugs.", bullet_style))
    story.append(Paragraph("• Authored an idempotent database seeding engine for instant 1-click demo logins with 15-minute token TTLs and API-level write protection, establishing automated GitHub Actions CI/CD to Netlify and Render.", bullet_style))

    # Project 3: Air Pollution (3 bullets)
    story.append(Spacer(1, 1))
    story.append(Paragraph("<b>Air Pollution & Public Health Data Analysis</b>", item_title_bold))
    story.append(Paragraph('<a href="https://github.com/Ramanpreet8/AirPollution" color="black">https://github.com/Ramanpreet8/AirPollution</a>', link_style))
    story.append(Paragraph("Python, Pandas, NumPy, SciPy, Seaborn, Matplotlib, Plotly, JupyterLab | Tooling: Google Antigravity", item_sub_italic))
    story.append(Paragraph("• Compared pediatric asthma ED rates across boroughs; Bronx rate was 3.8× Staten Island's (212.5 vs. 55.3 per 100k).", bullet_style))
    story.append(Paragraph("• Evaluated a 5-borough correlation (r = 0.78, p = 0.12) as underpowered and expanded to 42 neighborhoods across 4 matched periods (n = 168), finding a weak but significant association (r = 0.28, p &lt; 0.001) across two NYC public-health sources.", bullet_style))
    story.append(Paragraph("• Detected and resolved a double-counting bug that had inflated visit totals ~2×; added a validation check that borough totals match the citywide figure.", bullet_style))

    # 4. EXPERIENCE
    add_section_divider("EXPERIENCE")
    t5 = Table([
        [Paragraph("<b>Undergraduate Researcher, CUNY New York City College of Technology</b>", item_title_bold),
         Paragraph("10/2026 – 12/2026", item_title_roman)]
    ], colWidths=[370, 134])
    t5.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t5)

    t6 = Table([
        [Paragraph("Emerging Scholars Program (ESP) – Undergraduate Research", item_sub_italic),
         Paragraph("Brooklyn, NY", item_sub_date)]
    ], colWidths=[370, 134])
    t6.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0)]))
    story.append(t6)

    story.append(Paragraph("• Conducted systems research on quantum computing for \"From Bits to Qubits\", designing a 14-row comparison table (1 maps, 4 deform, 8 break, 1 open) and auditing all claims against literature (RP 2011, NA 2019, 2023+).", bullet_style))
    story.append(Paragraph("• Drafted the 200-word research abstract; preparing final poster for presentation at December 2026 Symposium.", bullet_style))

    # 5. SKILLS
    add_section_divider("SKILLS")
    skills = [
        ("Languages:", "Python 3, JavaScript (ES6+), TypeScript, Java, SQL, HTML5"),
        ("Frontend:", "React, Ionic, Recharts, Responsive Design"),
        ("Backend & Databases:", "Express.js, REST APIs, Socket.IO, Prisma ORM, PostgreSQL, MySQL"),
        ("Data Analysis & Visualization:", "Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly, Jupyter Notebook / JupyterLab"),
        ("Tools & DevOps:", "Git, GitHub, GitHub Actions (CI/CD), Linux, Windows System Administration"),
    ]
    for label, val in skills:
        story.append(Paragraph(f"<b>{label}</b> {val}", bullet_style))

    doc.build(story)
    print(f"Generated resume at: {output_pdf_path}")

if __name__ == '__main__':
    # 1. Update in portfolio assets
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    portfolio_asset_path = os.path.join(repo_dir, 'assets', 'Ramanpreet_Singh_Resume.pdf')
    generate_resume(portfolio_asset_path)

    # 2. Update in user home directory
    home_resume_path = '/Users/ramanpreetsingh/Ramanpreet_Singh_Resume.pdf'
    shutil.copyfile(portfolio_asset_path, home_resume_path)
    print(f"Copied resume to: {home_resume_path}")
