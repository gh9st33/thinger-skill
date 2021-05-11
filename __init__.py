from mycroft import MycroftSkill, intent_file_handler


class Thinger(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('thinger.intent')
    def handle_thinger(self, message):
        self.speak_dialog('thinger')


def create_skill():
    return Thinger()

