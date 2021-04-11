from tkinter import*
import json
import requests

root=Tk()
root.title("My Weather App")
root.geometry("1000x1000")
root.configure(background="white")

label1 = Label(root)
Label1answer = Label(root)

label2 = Label(root)
label21 = Label(root)

def city_name():
    api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=b07d0b72cb8b4c0f9c0dfdce14176119")
    
    api_output_json = json.loads(api_request.content)
    
    title1 =api_output_json["articles"][0]["title"] 
    print(title1) 
    desc1 =api_output_json["articles"][0]["description"] 
    print(desc1)
    title2 =api_output_json["articles"][1]["title"] 
    print(title2) 
    desc2 =api_output_json["articles"][1]["description"] 
    print(desc2)
    
    

btn = Button(root,text = "Blah",command = city_name)
btn.pack()
root.mainloop()