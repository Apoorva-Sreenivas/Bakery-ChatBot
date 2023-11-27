import chatterbot.comparisons
import chatterbot.response_selection
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
# from spellchecker import SpellChecker
import logging

# def get_feedback():

#     text = input()

#     if 'yes' in text.lower():
#         return True
#     elif 'no' in text.lower():
#         return False
#     else:
#         print('Please type either "Yes" or "No"')
#         return get_feedback()
    
class Chat_Bot():

    def __init__(self):
        self.chatbot1 = ChatBot('Bakery Help',storage_adapter="chatterbot.storage.SQLStorageAdapter" ,logic_adapters=[
        {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand.',
                    "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
                    # "response_selection_method": chatterbot.response_selection.get_first_response
                    # 'maximum_similarity_threshold': 0.90
                }
            ]
            )
        logger=logging.getLogger()
        logger.setLevel(logging.CRITICAL)

        with open('greetings.txt','r') as data:
            welcome = data.read().splitlines()

        with open('asking_a_menu.txt','r') as ask:
            ask_menu = ask.read().splitlines()

        with open('seasonal_menu.txt','r') as ask1:
            seasonal_menu = ask1.read().splitlines()

        with open('gift_box.txt','r') as ask2:
            gift_box = ask2.read().splitlines()

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


        # trainer = ListTrainer(self.chatbot1)
        # trainer.train(welcome)
        # trainer.train(ask_menu)
        # trainer.train(seasonal_menu)
        # trainer.train(gift_box)
        # trainer.train(macaron)
        # trainer.train(chouquette)
        # trainer.train(creme_brulee)
        # trainer.train(croissant)
        # trainer.train(eclair)
        # trainer.train(mille_feuille)
        # trainer.train(pain_au_chocolat)
        # trainer.train(pralines)
        # trainer.train(profiterole)
        # trainer.train(extra_questions)


        # spell = SpellChecker()

        # print("Lets chat! Enter bye to exit")
    def get_chatbot_response(self,message):
        while True:
            try:
                input_statement = Statement(text=message)
                if "bye" in str(input_statement):
                    return "exit"
                elif "thank you" in str(input_statement):
                    response= "Is there anything else I can help you with ? Enter bye to exit"
                else:
                    response = self.chatbot1.generate_response(input_statement)

                    # print("\U0001F9C1 ",response.text)
                # print('\n Is "{}" a coherent response to "{}"? \n'.format(
                #     response.text,
                #     input_statement.text
                # ))
                # if get_feedback() is False:
                #     print('please input the correct one')
                #     correct_response = Statement(text=input())
                #     chatbot1.learn_response(correct_response, input_statement)
                #     print('Responses added to bot!')
                return response
            except (KeyboardInterrupt, EOFError, SystemExit):
                break
        


