
from chat012.chat import chat_conversation as chat
def learn(data):

    if "day" in data:
        chat.day()

    elif "news" in data:
        chat.news()

    elif "time" in data:
        chat.current_time()

    elif "temp" in data:
        chat.temp()

    elif "greeting" in data:
        chat.greeting()

    elif "close" in data:
        chat.close()
        
    elif "bestcountry" in data:
        chat.bestcountry()
    
    elif "places" in data:
        chat.places()
    
    elif "clothes" in data:
        chat.clothes()
    
    elif "Domesticanimal" in data:
        chat.Domesticanimal()
    
    elif "Wildanimal" in data:
        chat.Wildanimal()
        
    elif "Birds" in data:
        chat.Birds()
        
    elif "picnicspot" in data:
        chat.picnicspot()
        
    elif "EngineeringCourse" in data:
        chat.EngineeringCourse()
    

    elif "exit" in data:
        chat.Exit()

    else:
        print(" Sorry,I don't know the answer")   
