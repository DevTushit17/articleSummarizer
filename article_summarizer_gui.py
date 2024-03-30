import tkinter as tk

bgColor = "#352F44"
secBgColor = "#5C5470"
buttonColor = "#B9B4C7"
textColor = "#FAF0E6"

mainFont = "Helvetica"

textBoxWidth = 73 

root = tk.Tk()
root.title("Article Summarizer")
root.configure(bg=bgColor)

heading = tk.Label(root, text = "ARTICLE SUMMARIZER", font=(mainFont, 20), bg=bgColor, fg=textColor)

inputFrame = tk.Frame(root, bg= secBgColor)

urlLabel=tk.Label(inputFrame,text="URL", bg=secBgColor, fg = textColor, font = (mainFont, 10))
urlLabel.grid(row = 0, column = 0)

urlText=tk.Text(inputFrame,bg=buttonColor, fg = bgColor,font = (mainFont, 10), width = 55, height = 2)
urlText.grid(row = 0, column = 1, ipady=2, padx=(0, 4))

summaryBtn=tk.Button(inputFrame, text="Summarize", bg=buttonColor, fg = bgColor, font = (mainFont, 10), height=2) 
"""command=summarize"""
summaryBtn.grid(row = 0, column = 2, pady=6, padx=6)

titleLabel = tk.Label(root, text="TITLE", font=(mainFont, 10), bg=bgColor, fg=textColor)

titleField = tk.Text(root,state='disabled', bg = secBgColor, fg = textColor, font=(mainFont, 10), width = textBoxWidth, height=2, wrap=tk.W)

authorLabel = tk.Label(root, text="AUTHOR", font=(mainFont, 10), bg=bgColor, fg=textColor)

authorField = tk.Text(root,state='disabled', bg = secBgColor, fg = textColor, font=(mainFont, 10), width = textBoxWidth, height=1)

publicationLabel = tk.Label(root, text="PUBLICATION DATE", font=(mainFont, 10), bg=bgColor, fg=textColor)

publicationField = tk.Text(root,state='disabled', bg = secBgColor, fg = textColor, font=(mainFont, 10), width = textBoxWidth, height=1)

summaryLabel = tk.Label(root, text="SUMMARY", font=(mainFont, 10), bg=bgColor, fg=textColor)

summaryField = tk.Text(root,state='disabled', bg = secBgColor, fg = textColor, font=(mainFont, 10), width = 66, height=10, wrap=tk.W)

summaryScroll = tk.Scrollbar(root, command=summaryField.yview, width=1, bg=secBgColor)

summaryField['yscrollcommand'] = summaryScroll.set

sentimentLabel = tk.Label(root, text="SENTIMENTAL ANALYSIS", font=(mainFont, 10), bg=bgColor, fg=textColor)

sentimentField = tk.Text(root,state='disabled', bg = secBgColor, fg = textColor, font=(mainFont, 10), width = textBoxWidth, height=1)

clearButton = tk.Button(root, text = "CLEAR", bg = secBgColor, fg = textColor, font = (mainFont, 10), width = 63)


heading.grid(row = 0, column= 0, columnspan=2, pady=4)
inputFrame.grid(row = 1, column = 0, columnspan=2, padx=4, pady=(0,6))
titleLabel.grid(row = 2, column = 0, columnspan=2, padx=4, sticky=tk.W)
titleField.grid(row = 3, column = 0, columnspan=2, padx=(4,0), pady=(0,6), sticky=tk.W)
authorLabel.grid(row = 4, column = 0, columnspan=2, padx=4, sticky=tk.W)
authorField.grid(row = 5, column = 0, columnspan=2, padx=(4,0), pady=(0,6), sticky=tk.W)
publicationLabel.grid(row = 6, column = 0, columnspan=2, padx=4, sticky=tk.W)
publicationField.grid(row = 7, column = 0, columnspan=2, padx=(4,0), pady=(0,6), sticky=tk.W)
summaryLabel.grid(row = 8, column = 0, columnspan=2, padx=4, sticky=tk.W)

summaryField.grid(row = 9, column = 0, padx=(4,0), pady=(0,6), sticky=tk.W)
summaryScroll.grid(row = 9, column = 1, padx=(0, 4), pady=(0,6), sticky='nsew')

sentimentLabel.grid(row = 10, column = 0, columnspan=2, padx=4, sticky=tk.W)
sentimentField.grid(row = 11, column = 0, columnspan=2,padx=(4,0), pady=(0,6), sticky=tk.W)

clearButton.grid(row = 12, column=0, columnspan=2, padx=4, pady=4, sticky=tk.W)



# root.mainloop()
