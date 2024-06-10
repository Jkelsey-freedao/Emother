import streamlit as st
from calculate import (
    calculate_life_path,
    calculate_birth_day,
    calculate_challenges,
    calculate_period_cycles,
    calculate_sun_number,
    calculate_personal_year,
    calculate_personal_month,
    calculate_personal_day,
    calculate_daily_challenge,
    generate_report
)
from language_data import translations
from datetime import datetime

# Initialize session state
if 'generated' not in st.session_state:
    st.session_state.generated = False

if 'generate_report' not in st.session_state:
    st.session_state.generate_report = False

# Language selection
language = st.selectbox("Select Language", options=["EN", "FR", "ZH"])
st.session_state.language = language

# Streamlit app title and description
st.title(translations[language]["app_title"])
st.write(translations[language]["app_description"])

# User input for birth date
birth_month = st.text_input(translations[language]["enter_birth_month"], max_chars=2)
birth_day = st.text_input(translations[language]["enter_birth_day"], max_chars=2)
birth_year = st.text_input(translations[language]["enter_birth_year"], max_chars=4)

# User input for current date
current_month = st.text_input(translations[language]["enter_current_month"], max_chars=2)
current_day = st.text_input(translations[language]["enter_current_day"], max_chars=2)
current_year = st.text_input(translations[language]["enter_current_year"], max_chars=4)

# Button to trigger calculations
if st.button('Calculate'):
    try:
        # Construct birth date and current date strings
        birth_date = f"{birth_month}/{birth_day}/{birth_year}"
        current_date_input = f"{current_month}/{current_day}/{current_year}"

        # Parse current date
        current_date = datetime.strptime(current_date_input, '%m/%d/%Y')

        # Calculate numerology values
        st.session_state.life_path = calculate_life_path(birth_date)
        st.session_state.birth_day_number = calculate_birth_day(birth_date)
        st.session_state.first_challenge, st.session_state.second_challenge, st.session_state.third_challenge, st.session_state.fourth_challenge = calculate_challenges(birth_date)
        st.session_state.first_period, st.session_state.second_period, st.session_state.third_period = calculate_period_cycles(birth_date)
        st.session_state.sun_number = calculate_sun_number(birth_date)
        st.session_state.personal_year = calculate_personal_year(birth_date, current_date.year)
        st.session_state.personal_month = calculate_personal_month(birth_date, current_date)
        st.session_state.personal_day = calculate_personal_day(birth_date, current_date)
        st.session_state.daily_challenge = calculate_daily_challenge(birth_date, current_date)

        # Set generated state to True
        st.session_state.generated = True

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display results if generated
if st.session_state.generated:
    st.subheader(translations[language]['life_path'])
    st.write(st.session_state.life_path)
    st.subheader(translations[language]['birth_day'])
    st.write(st.session_state.birth_day_number)
    st.subheader(translations[language]['challenges'])
    st.write(f"{translations[language]['first']}: {st.session_state.first_challenge}")
    st.write(f"{translations[language]['second']}: {st.session_state.second_challenge}")
    st.write(f"{translations[language]['third']}: {st.session_state.third_challenge}")
    st.write(f"{translations[language]['fourth']}: {st.session_state.fourth_challenge}")
    st.subheader(translations[language]['period_cycles'])
    st.write(f"{translations[language]['first']}: {st.session_state.first_period}")
    st.write(f"{translations[language]['second']}: {st.session_state.second_period}")
    st.write(f"{translations[language]['third']}: {st.session_state.third_period}")
    st.subheader(translations[language]['sun_number'])
    st.write(st.session_state.sun_number)
    st.subheader(translations[language]['personal_year'])
    st.write(st.session_state.personal_year)
    st.subheader(translations[language]['personal_month'])
    st.write(st.session_state.personal_month)
    st.subheader(translations[language]['personal_day'])
    st.write(st.session_state.personal_day)
    st.subheader(translations[language]['daily_challenge'])
    st.write(st.session_state.daily_challenge)

    # Option to generate a report
    generate_report_input = st.checkbox(translations[language]["generate_report_prompt"], value=st.session_state.generate_report)

    if generate_report_input:
        st.session_state.generate_report = True
        if st.button('Generate Report'):
            st.subheader('Numerology Report')
            st.markdown(generate_report('life_path', st.session_state.life_path, language), unsafe_allow_html=True)
            st.markdown(generate_report('birth_day', st.session_state.birth_day_number, language), unsafe_allow_html=True)
            st.markdown(generate_report('challenges', st.session_state.first_challenge, language, translations[language]['first']), unsafe_allow_html=True)
            st.markdown(generate_report('challenges', st.session_state.second_challenge, language, translations[language]['second']), unsafe_allow_html=True)
            st.markdown(generate_report('challenges', st.session_state.third_challenge, language, translations[language]['third']), unsafe_allow_html=True)
            st.markdown(generate_report('challenges', st.session_state.fourth_challenge, language, translations[language]['fourth']), unsafe_allow_html=True)
            st.markdown(generate_report('period_cycles', st.session_state.first_period, language, translations[language]['first']), unsafe_allow_html=True)
            st.markdown(generate_report('period_cycles', st.session_state.second_period, language, translations[language]['second']), unsafe_allow_html=True)
            st.markdown(generate_report('period_cycles', st.session_state.third_period, language, translations[language]['third']), unsafe_allow_html=True)
            st.markdown(generate_report('sun_number', st.session_state.sun_number, language), unsafe_allow_html=True)
            st.markdown(generate_report('personal_year', st.session_state.personal_year, language), unsafe_allow_html=True)
            st.markdown(generate_report('personal_month', st.session_state.personal_month, language), unsafe_allow_html=True)
            st.markdown(generate_report('personal_day', st.session_state.personal_day, language), unsafe_allow_html=True)
            st.markdown(generate_report('daily_challenge', st.session_state.daily_challenge, language), unsafe_allow_html=True)
    else:
        st.session_state.generate_report = False
        st.write(translations[language]["report_skipped"])

# CSS to ensure proper text wrapping
st.markdown("""
    <style>
    .report-text {
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    </style>
    """, unsafe_allow_html=True)
