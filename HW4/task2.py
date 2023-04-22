import os
import re
import docx2txt
import string
import requests
from bs4 import BeautifulSoup

# Set the directory where the files are located
dir_path = "./texts/"


def clean_text(text):
    # Remove unwanted characters from the text
    text = re.sub(r'\[[0-9]+\]', '', text)
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\t+', ' ', text)

    # Remove punctuation except periods in lists
    for match in re.findall(r'(?m)^\d+[.)]\s+', text):
        text = text.replace(match, '')
    text = re.sub(r'(?m)^[^\S\n]*[-•–][^\S\n]+', '', text)
    text = text.replace('.', '')
    text = text.translate(str.maketrans(
        '', '', string.punctuation.replace('.', '')+'↑'))
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text


# Define the function to get the Wikipedia article
def get_wiki_article(article_name):
    # Replace spaces with underscores in article name
    article_name = article_name.replace(" ", "_")
    # Build the URL for the article
    url = f"https://ru.wikipedia.org/wiki/{article_name}"
    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the content div and extract the text
    content_div = soup.find('div', {'class': 'mw-parser-output'})
    # Remove unwanted elements from the content
    [s.extract() for s in content_div('sup')]
    [s.extract() for s in content_div('img')]
    [s.extract() for s in content_div('audio')]
    [s.extract() for s in content_div('video')]
    [s.extract() for s in content_div('map')]
    [s.extract() for s in content_div('timeline')]
    [s.extract() for s in content_div('table')]
    # Get the cleaned text
    text = content_div.get_text()
    text = clean_text(text)
    # Remove the [править | править код] artifact
    text = text.replace('[править | править код]', '')
    # Return the cleaned text
    return re.sub(r'\[[0-9]+\]', '', text)

# Define the function to calculate plagiarism


def calculate_plagiarism(text, wiki_text):
    # Split the text and wiki_text into words
    text_words = text.split()
    # Iterate over the text_words and compare to wiki_words
    match_count = 0
    for i in range(len(text_words)-2):
        text_tri = text_words[i] + " " + \
            text_words[i+1] + " " + text_words[i+2]
        if text_tri in wiki_text:
            match_count += 1
    # Calculate and return the plagiarism percentage
    plagiarism_percentage = (match_count / len(text_words)) * 100
    return plagiarism_percentage


authors = {
    'Корпоративные ценности': ['Фёдорова', 'Мыльченко', 'Гусев'],
    'Научный метод': ['Никифоров', 'Ершов', 'Иванова'],
    'Рентгеновское излучение': ['Коломиец', 'Агаев', 'Мартынюк'],
    'Жизнь': ['Скворцов', 'Мордовцев'],
    'Улыбка': ['Бахтина', 'Шевченко', 'Шимченко'],
    'Астероид': ['Морозова', 'Цветкова', 'Колтунова'],
    'Логика': ['Сидненко', 'Георгов', 'Резкаллах'],
    'Стресс': ['Шапиро', 'морозов', 'уразалин'],
    'Система управления базами данных': ['Шабанов', 'Абдулла', 'Гаджиева']
}


# Iterate over the files in the directory
for filename in os.listdir(dir_path):
    # Only process docx and rtf files
    if filename.endswith(".docx"):
        # Get the file path
        file_path = os.path.join(dir_path, filename)
        # Extract the article name from the filename
        article_name = os.path.splitext(filename)[0]
        # Read the text from the file
        text = docx2txt.process(file_path)
        text = clean_text(text)
        # Get the Wikipedia article for the same topic
        wiki_text = get_wiki_article(article_name)
        # Calculate the plagiarism percentage
        plagiarism_percentage = calculate_plagiarism(text, wiki_text)
        # Print the result
        print(
            f"Доклад: {article_name} ({filename})\nАвторы: {', '.join(authors[article_name])}\nПроцент плагиата: {plagiarism_percentage:.2f}%\n")
