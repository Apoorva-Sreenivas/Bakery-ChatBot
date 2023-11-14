import chatterbot.comparisons
import chatterbot.response_selection
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# import chatterbot.logic
from textblob import TextBlob
# from chatterbot.conversation import Statement
# from spellchecker import SpellChecker
import re

# def get_feedback():

#     text = input()

#     if 'yes' in text.lower():
#         return True
#     elif 'no' in text.lower():
#         return False
#     else:
#         print('Please type either "Yes" or "No"')
#         return get_feedback()
    
# def TakeOrder():
#     print("\U0001F9C1 ","The items on the menu are : \n A:Macarons\n B:Profiterole\n C:Pain Au Chocolat\n D:Mille Feuille\n E:Eclair\n F:Chouquette\n G:Creme brulee\n H:Pralines\n I:Croissant")
#     print("\U0001F9C1 ","Please type your order as Item code and Number of Items needed and press enter for each new item") 
#     print("\U0001F9C1 ","Enter done to finish ordering")
#     order=""
#     order_list=[]
#     items={"A":"Macarons","B":"Profiterole","C":"Pain Au Chocolat","D":"Mille Feuille","E":"Eclair","F":"Chouquette","G":"Creme brulee","H":"Pralines","I":"Croissant"}
#     while "done" not in order: # changed to be any case of done 
#         order= input("Order >> ")
#         order1=order.replace(" ","").upper() # remove any spaces-- works normally but not in a loop 
#         order_list.append(order1)
#     order_list[-1]=order_list[-1].replace("DONE","")
#     if order_list[-1]=="":
#         order_list.remove("")
#     # print(order_list)
#     Calculate_Bill(order_list)
    
#     # exit(0)
# def Calculate_Bill(order_list):
#     cost={"A":200,"B":175,"C":550,"D":495,"E":235,"F":175,"G":330,"H":85,"I":220}
#     total = 0
#     for x in order_list:
#         if len(x)>2 or x[0]>'I':
#             print("You have made a mistake. Please place the order again")
#             TakeOrder()
#         else:
#             total += int(x[1])*cost[x[0]]
#     Display_Bill(order_list,total)

# def Display_Bill(order_list,total):
#     items={"A":"Macarons","B":"Profiterole","C":"Pain Au Chocolat","D":"Mille Feuille","E":"Eclair","F":"Chouquette","G":"Creme brulee","H":"Pralines","I":"Croissant"}
#     cost={"A":200,"B":175,"C":550,"D":495,"E":235,"F":175,"G":330,"H":85,"I":220}
#     print("------------------------------")
#     print("---------Le Patessier---------")
#     print("------------------------------")
#     print("----Item-Cost-Number-Total----")
#     for x in order_list:
#         print(items[x[0]],"-",cost[x[0]],"-",x[1],"-",cost[x[0]]*int(x[1]))
#     print("------------------------------")
#     print("--------- Total Cost ---------")
#     print("-------",total,"-------")
#     print("------------------------------")


# chatbot = ChatBot('Bakery Help',
#     logic_adapters=[
#         "chatterbot.logic.BestMatch"
#     ])
# ,storage_adapter="chatterbot.storage.SQLStorageAdapter"
chatbot = ChatBot('Bakery Help',  logic_adapters=[
{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
            "response_selection_method": chatterbot.response_selection.get_first_response
            # 'maximum_similarity_threshold': 0.90
        }
    ]
    )
with open('greetings.txt','r') as data:
    welcome = data.read().splitlines()
# welcome=[]
# conv1=[]
# for x in data :
#     welcome.append(x)
#     welcome.append("Hello, Welcome to Le Patessier.How may i help you?")

with open('asking_a_menu.txt','r') as ask:
    ask_menu = ask.read().splitlines()
# for x in ask_menu:
#     conv1.append(x)
#     conv1.append("Here are the items on the menu A:Macarons, B:Profiterole, C:Pain Au Chocolat, D:Mille Feuille, E:Eclair, F:Chouquette, G:Creme brulee, H:Pralines, I:Croissant ")

with open('seasonal_menu.txt','r') as ask1:
    seasonal_menu = ask1.read().splitlines()
# for x in seasonal_menu:
#     conv1.append(x)
#     conv1.append("The limited edition seasonal menu items are A:Pumpkin Spice Croissants, B:Cranberry Orange Macarons, C:Maple Pecan Pralines, D:Chestnut Praline Éclairs, E:Spiced Apple Eclairs, F:Hazelnut Macchiato Croissants, G:Fig and Honey Macarons, H:Chestnut Chocolate Macarons, I:Brown Butter Pecan Croissants")

with open('gift_box.txt','r') as ask2:
    gift_box = ask2.read().splitlines()
# for x in gift_box:
#     conv1.append(x)
#     conv1.append("we have many sets available A:Full Seasonal Set B:Mini Seasonal Set C:Sets for each item we offer D:Large Mix&Match E:Small Mix&Mathch")


with open('macarons.txt','r') as d1:
    macaron = d1.read().splitlines()

with open('chouquette.txt','r') as d2:
    chouquette = d2.read().splitlines()

with open('creme_brulee.txt','r') as d3:
    creme_brulee = d3.read().splitlines()

with open('croissant.txt','r') as d4:
    croissant = d4.read().splitlines()

with open('eclair.txt','r') as d5:
    eclair = d5.read().splitlines()

with open('mille_feuille.txt','r') as d6:
    mille_feuille = d6.read().splitlines()

with open('pain_au_chocolat.txt','r') as d7:
    pain_au_chocolat = d7.read().splitlines()

with open('pralines.txt','r') as d8:
    pralines = d8.read().splitlines()

with open('profiterole.txt','r') as d9:
    profiterole = d9.read().splitlines()

with open('extra_questions.txt','r') as d10:
    extra_questions = d10.read().splitlines()


trainer = ListTrainer(chatbot)
trainer.train(welcome)
trainer.train(ask_menu)
trainer.train(seasonal_menu)
trainer.train(gift_box)
# trainer.train(conv1)
trainer.train(macaron)
trainer.train(chouquette)
trainer.train(creme_brulee)
trainer.train(croissant)
trainer.train(eclair)
trainer.train(mille_feuille)
trainer.train(pain_au_chocolat)
trainer.train(pralines)
trainer.train(profiterole)
trainer.train(extra_questions)


# spell = SpellChecker()

print("Lets chat! Enter bye to exit")

while True:
    try:
        request = input("You >> ")
        blob = TextBlob(request)
        corrected_request = str(blob.correct())
        if "bye" in corrected_request:
            exit(0)
        # if re.search("order|buy",corrected_request):
        #     # TakeOrder()
        # else:
        response = chatbot.get_response(corrected_request)
        print("\U0001F9C1 ",response)
        # input_statement = Statement(text=input())
        # response = chatbot.generate_response(
        #     input_statement
        # )

        # print('\n Is "{}" a coherent response to "{}"? \n'.format(
        #     response.text,
        #     input_statement.text
        # ))
        # if get_feedback() is False:
        #     print('please input the correct one')
        #     correct_response = Statement(text=input())
        #     chatbot.learn_response(correct_response, input_statement)
        #     print('Responses added to bot!')

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    


