import tkinter as tk
import requests

def send_webhook(button_text):
    webhook_url = "Webhook"
    data = {"content": button_text}
    headers = {"Content-Type": "application/json"}
    

    try:
        response = requests.post(webhook_url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        print("Answer sent to sender!")
    except requests.exceptions.RequestException as e:
        print("Error sending webhook:", e)

root = tk.Tk()
root.title("Love letter")
root.config(background="#FFC0CB")  # Set background color to pink


label = tk.Label(root, text="Do you want to date me?\n We can watch anime and play video games.\n We can also go for walks together.\n", bg="#FFC0CB", fg="black")
label.pack()

button1 = tk.Button(root, text="Yes", command=lambda: send_webhook("She said yes boys"), bg="#FF69B4", fg="black")
button1.pack()

button2 = tk.Button(root, text="Yes lets get married", command=lambda: send_webhook("She said yes and wants to marry i aint cooked guys!!!!"), bg="#FF59A3", fg="black")
button2.pack()




root.mainloop()
