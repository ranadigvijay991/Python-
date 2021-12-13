import requests
import win32com.client
import json

def text_to_voice(content):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(content)

print("TOP BUISNESS HEADLINES FROM USA RIGHT NOW")
a=requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d22688c2ded645c58f52fa946c80e72a").json()
news_desc_a=a['articles'][0]['description']
news_content_a=a['articles'][0]['content']
print(news_desc_a,news_content_a)

print("TOP BUISNESS HEADLINES FROM INDIA:")
b=requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=d22688c2ded645c58f52fa946c80e72a").json()
news_desc_b=b['articles'][0]['description']
news_content_b=b['articles'][0]['content']
print(news_desc_b,news_content_b)

print("TOP SPORTS HEADLINES FROM INDIA:")
c=requests.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=d22688c2ded645c58f52fa946c80e72a").json()
news_desc_c=c['articles'][0]['description']
news_content_c=c['articles'][0]['content']
print(news_desc_c,news_content_c)
text_to_voice("TOP BUISNESS HEADLINES FROM USA RIGHT NOW" + news_desc_a + news_content_a)
text_to_voice("TOP BUISNESS HEADLINES FROM INDIA:" + news_desc_b + news_content_b)
text_to_voice("TOP SPORTS HEADLINES FROM INDIA:" + news_desc_c + news_content_c)