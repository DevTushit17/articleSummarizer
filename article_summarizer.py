from article_summarizer_gui import *
from tkinter import messagebox
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():

    url = urlText.get('1.0',"end").strip()
    if url == "":
        messagebox.showerror("Error", "No URL entered,\nplease enter a URL and then press the button")
        return
    #Putting summary data & sentimental analysis in the text boxes
    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    titleField.config(state='normal')
    authorField.config(state='normal')
    publicationField.config(state='normal')
    summaryField.config(state='normal')
    sentimentField.config(state='normal')

    titleField.delete('1.0','end')
    titleField.insert('1.0',article.title)

    authorField.delete('1.0','end')
    authorField.insert('1.0',article.authors)

    publicationField.delete('1.0','end')
    publicationField.insert('1.0',str(article.publish_date))

    summaryField.delete('1.0','end')
    summaryField.insert('1.0',article.summary)
    summaryField['yscrollcommand'] = summaryScroll.set

    analysis=TextBlob(article.text)
    sentimentField.delete('1.0','end')
    sentimentField.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment:{"POSITIVE" if analysis.polarity>0 else ("NEGATIVE" if analysis.polarity<0 else "NEUTRAL")}')

    titleField.config(state='disabled')
    authorField.config(state='disabled')
    publicationField.config(state='disabled')
    summaryField.config(state='disabled')
    sentimentField.config(state='disabled')


def clearBox ():
    
    #Function to clear all the fields when the clearButton is pressed
    titleField.config(state='normal')
    authorField.config(state='normal')
    publicationField.config(state='normal')
    summaryField.config(state='normal')
    sentimentField.config(state='normal')
    
    urlText.delete('1.0', 'end')
    titleField.delete('1.0', 'end')
    authorField.delete('1.0', 'end')
    publicationField.delete('1.0', 'end')
    summaryField.delete('1.0', 'end')
    sentimentField.delete('1.0', 'end')

    titleField.config(state='disabled')
    authorField.config(state='disabled')
    publicationField.config(state='disabled')
    summaryField.config(state='disabled')
    sentimentField.config(state='disabled')

summaryBtn.config(command=summarize)
clearButton.config(command=clearBox)



root.mainloop()
