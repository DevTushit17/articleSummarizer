import tkinter as tk
from tkinter import messagebox
import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')
def summarize():

    url = utext.get('1.0',"end").strip()
    if url == "":
        messagebox.showerror("Error", "No URL entered,\nplease enter a URL and then press the button")
        return
    #Putting summary data & sentimental analysis in the text boxes
    article = Article(url)
    article.download()
    article.parse()

    article.nlp()
    
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0','end')
    author.insert('1.0',article.authors)

    publication.delete('1.0','end')
    publication.insert('1.0',str(article.publish_date))

    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)

    analysis=TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment:{"POSITIVE" if analysis.polarity>0 else ("NEGATIVE" if analysis.polarity<0 else "NEUTRAL")}')
    
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

def clearBox ():
    
    #Function to clear all the fields when the clearButton is pressed
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    
    utext.delete('1.0', 'end')
    title.delete('1.0', 'end')
    author.delete('1.0', 'end')
    publication.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


#Configuration of the Graphical User Interface
    
bgColor = "#352F44"
secBgColor = "#5C5470"
buttonColor = "#B9B4C7"
textColor = "#FAF0E6"

mainFont = "Helvetica"

root = tk.Tk()
root.title("News Summarizer")
root.configure(bg=bgColor)

heading = tk.Label(root, text = "ARTICLE SUMMARIZER", font=(mainFont, 20), bg=bgColor, fg=textColor)
heading.grid(row = 0, column= 0, pady=4)

inputFrame = tk.Frame(root, bg= secBgColor, padx=4, pady=4)
inputFrame.grid(row = 1, column = 0)

ulabel=tk.Label(inputFrame,text="URL", bg=secBgColor, fg = textColor, font = (mainFont, 10))
ulabel.grid(row = 0, column = 0, padx=2)

utext=tk.Text(inputFrame,height=2,bg=buttonColor, fg = bgColor, width = 55)
utext.grid(row = 0, column = 1, padx=2, ipady=3)

btn=tk.Button(inputFrame, text="Summarize", bg=buttonColor, fg = bgColor, font = (mainFont, 10), height=2, command=summarize)
btn.grid(row = 0, column = 2, padx=2)

tlabel = tk.Label(root, text="TITLE", font = (mainFont, 10), bg = bgColor, fg = textColor)
tlabel.grid(row = 2, column = 0, sticky=tk.W, pady=(4, 0), padx=4)

title = tk.Text(root, height=1)
title.config(state='disabled', bg=secBgColor,fg=textColor, font = (mainFont, 10))
title.grid(row = 3, column = 0, stick=tk.W, padx=6)

aLabel = tk.Label(root, text="AUTHOR", font = (mainFont, 10), bg = bgColor, fg = textColor)
aLabel.grid(row = 4, column = 0, sticky=tk.W, pady=(4, 0), padx=4)

author = tk.Text(root, height=1)
author.config(state='disabled', bg=secBgColor, fg=textColor, font = (mainFont, 10))
author.grid(row = 5, column = 0, stick=tk.W, padx=6)

pLabel = tk.Label(root, text="PUBLICATION DATE", font = (mainFont, 10), bg = bgColor, fg = textColor)
pLabel.grid(row = 6, column = 0, sticky=tk.W, pady=(4, 0), padx=4)

publication = tk.Text(root, height=1)
publication.config(state='disabled', bg=secBgColor,fg=textColor, font = (mainFont, 10))
publication.grid(row = 7, column = 0, stick=tk.W, padx=6)

sLabel = tk.Label(root, text="SUMMARY", font = (mainFont, 10), bg = bgColor, fg = textColor)
sLabel.grid(row = 8, column = 0, sticky=tk.W, pady=(4, 0), padx=4)

summary = tk.Text(root)
summary.config(state='disabled', bg=secBgColor,fg=textColor, font = (mainFont, 10), height=10)
summary.grid(row = 9, column = 0, stick=tk.W, padx=6)

saLabel = tk.Label(root, text="SENTIMENTAL ANALYSIS", font = (mainFont, 10), bg = bgColor, fg = textColor)
saLabel.grid(row = 10, column = 0, sticky=tk.W, pady=(4, 0), padx=4)

sentiment = tk.Text(root, height=1)
sentiment.config(state='disabled', bg=secBgColor,fg=textColor, font = (mainFont, 10))
sentiment.grid(row = 11, column = 0, stick=tk.W, padx=6, pady = (0, 8))

clearBtn = tk.Button(root, text="CLEAR", bg=buttonColor, fg = bgColor, font = (mainFont, 10), height=1, command=clearBox, width = 70)
clearBtn.grid(row = 12, column = 0, padx=2, pady= (0, 8))

root.mainloop()
