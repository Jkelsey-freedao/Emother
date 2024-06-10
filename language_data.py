import os

# Translations dictionary containing the text for various prompts and labels in English, French, and Chinese
translations = {
    "EN": {
        "enter_birth_month": "Enter your birth month (MM): ",
        "enter_birth_day": "Enter your birth day (DD): ",
        "enter_birth_year": "Enter your birth year (YYYY): ",
        "enter_current_month": "Enter the current month (MM): ",
        "enter_current_day": "Enter the current day (DD): ",
        "enter_current_year": "Enter the current year (YYYY): ",
        "life_path": "Life Path",
        "birth_day": "Birth Day",
        "challenges": "Challenges",
        "period_cycles": "Period Cycles",
        "first": "First",
        "second": "Second",
        "third": "Third",
        "fourth": "Fourth",
        "sun_number": "Sun Number",
        "personal_year": "Personal Year",
        "personal_month": "Personal Month",
        "personal_day": "Personal Day",
        "daily_challenge": "Daily Challenge",
        "generate_report_prompt": "Do you want to generate a Numerology report? (Y/N): ",
        "report_skipped": "Numerology report generation skipped.",
        "no_text_available": "No text available for this combination.",
        "app_title": "Numerology Calculator",
        "app_description": "Enter your birth date and the current date to calculate your numerology numbers."
    },
    "FR": {
        "enter_birth_month": "Entrez votre mois de naissance (MM): ",
        "enter_birth_day": "Entrez votre jour de naissance (JJ): ",
        "enter_birth_year": "Entrez votre année de naissance (AAAA): ",
        "enter_current_month": "Entrez le mois actuel (MM): ",
        "enter_current_day": "Entrez le jour actuel (JJ): ",
        "enter_current_year": "Entrez l'année actuelle (AAAA): ",
        "life_path": "Chemin de vie",
        "birth_day": "Jour de naissance",
        "challenges": "Défis",
        "period_cycles": "Cycles de période",
        "first": "Premier",
        "second": "Deuxième",
        "third": "Troisième",
        "fourth": "Quatrième",
        "sun_number": "Nombre solaire",
        "personal_year": "Année personnelle",
        "personal_month": "Mois personnel",
        "personal_day": "Jour personnel",
        "daily_challenge": "Défi quotidien",
        "generate_report_prompt": "Voulez-vous générer un rapport de numérologie ? (O/N): ",
        "report_skipped": "Génération du rapport de numérologie ignorée.",
        "no_text_available": "Aucun texte disponible pour cette combinaison.",
        "app_title": "Calculateur de numérologie",
        "app_description": "Entrez votre date de naissance et la date actuelle pour calculer vos numéros de numérologie."
    },
    "ZH": {
        "enter_birth_month": "请输入您的出生月份（MM）：",
        "enter_birth_day": "请输入您的出生日期（DD）：",
        "enter_birth_year": "请输入您的出生年份（YYYY）：",
        "enter_current_month": "请输入当前月份（MM）：",
        "enter_current_day": "请输入当前日期（DD）：",
        "enter_current_year": "请输入当前年份（YYYY）：",
        "life_path": "生命路径",
        "birth_day": "生日",
        "challenges": "挑战",
        "period_cycles": "周期",
        "first": "第一",
        "second": "第二",
        "third": "第三",
        "fourth": "第四",
        "sun_number": "太阳数",
        "personal_year": "个人年份",
        "personal_month": "个人月份",
        "personal_day": "个人日期",
        "daily_challenge": "每日挑战",
        "generate_report_prompt": "您想生成一份数字命理报告吗？（Y/N）：",
        "report_skipped": "数字命理报告生成已跳过。",
        "no_text_available": "没有可用的文本。",
        "app_title": "数字命理计算器",
        "app_description": "输入您的出生日期和当前日期以计算您的数字命理号码。"
    }
}

# Function to load report text from a file based on the category and language
def load_report_text(category, language):
    file_path = os.path.join("report_texts", f"{category}_{language.lower()}.md")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        sections = text.split("|||")
        data = {}
        for section in sections:
            if section.strip():  # Ensure the section is not empty
                parts = section.split("\n", 1)
                if len(parts) > 1:
                    number = parts[0].strip()
                    description = parts[1].strip()
                    if number.isdigit():  # Ensure the first line is a number
                        data[(category, int(number))] = description
        return data
    except FileNotFoundError:
        print(f"Warning: File not found for category '{category}' and language '{language}'. Skipping...")
        return {}

# Dictionary containing the report text for each category and number combination in English, French, and Chinese
report_text = {
    "EN": {
        **load_report_text("life_path", "EN"),
        **load_report_text("birth_day", "EN"),
        **load_report_text("challenges_first", "EN"),
        **load_report_text("challenges_second", "EN"),
        **load_report_text("challenges_third", "EN"),
        **load_report_text("challenges_fourth", "EN"),
        **load_report_text("period_cycles_first", "EN"),
        **load_report_text("period_cycles_second", "EN"),
        **load_report_text("period_cycles_third", "EN"),
        **load_report_text("sun_number", "EN"),
        **load_report_text("personal_year", "EN"),
        **load_report_text("personal_month", "EN"),
        **load_report_text("personal_day", "EN"),
        **load_report_text("daily_challenge", "EN")
    },
    "FR": {
        **load_report_text("life_path", "FR"),
        **load_report_text("birth_day", "FR"),
        **load_report_text("challenges_first", "FR"),
        **load_report_text("challenges_second", "FR"),
        **load_report_text("challenges_third", "FR"),
        **load_report_text("challenges_fourth", "FR"),
        **load_report_text("period_cycles_first", "FR"),
        **load_report_text("period_cycles_second", "FR"),
        **load_report_text("period_cycles_third", "FR"),
        **load_report_text("sun_number", "FR"),
        **load_report_text("personal_year", "FR"),
        **load_report_text("personal_month", "FR"),
        **load_report_text("personal_day", "FR"),
        **load_report_text("daily_challenge", "FR")
    },
    "ZH": {
        **load_report_text("life_path", "ZH"),
        **load_report_text("birth_day", "ZH"),
        **load_report_text("challenges_first", "ZH"),
        **load_report_text("challenges_second", "ZH"),
        **load_report_text("challenges_third", "ZH"),
        **load_report_text("challenges_fourth", "ZH"),
        **load_report_text("period_cycles_first", "ZH"),
        **load_report_text("period_cycles_second", "ZH"),
        **load_report_text("period_cycles_third", "ZH"),
        **load_report_text("sun_number", "ZH"),
        **load_report_text("personal_year", "ZH"),
        **load_report_text("personal_month", "ZH"),
        **load_report_text("personal_day", "ZH"),
        **load_report_text("daily_challenge", "ZH")
    }
}
