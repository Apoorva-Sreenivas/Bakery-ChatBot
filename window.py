import tkinter as tk
import bakery_chatbot

def send_data(event=None):
    output.insert(tk.END,"\nYou>> "+input.get()+"\n\U0001F9C1")
    response = chatbot.get_chatbot_response(input.get())

    if response == "exit":
        exit(0)
    else:
        input.delete(0,'end')
        output.insert(tk.END,response,"bot-tag")
        output.see(tk.END)


chatbot = bakery_chatbot.Chat_Bot()

root = tk.Tk()
root.title("Le Petessier Help")
root.option_add("*Font","Comfortaa 14 bold")
root.configure(background="purple4")
# root.geometry("466x700")
output = tk.Text(root,bg="thistle1",yscrollcommand=True)
output.config(wrap="word")
output.tag_config("bot-tag",foreground="purple4")
output.insert(tk.END,"Let's chat! Enter bye to exit")
# output.pack()
output.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
input = tk.Entry(root,width=80)
input.bind('<Return>',send_data)
# input.pack()
input.grid(row=1,column=0,sticky="w",padx=10,pady=15)
send = tk.Button(root,text="SEND",command=send_data)
# send.pack()
send.grid(row=1,column=1,sticky="w",padx=10,pady=15)
root.mainloop()
