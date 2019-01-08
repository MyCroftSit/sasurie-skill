from mycroft import MycroftSkill, intent_file_handler


class Sasurie(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sasurie.intent')
    def handle_sasurie(self, message):
        self.speak_dialog('sasurie')


def create_skill():
    return Sasurie()

