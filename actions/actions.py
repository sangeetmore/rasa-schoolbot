# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# imports

from pdb import Restart
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted

##--------------------------------------------------##
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]
##---------------------------------------------------##
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [Restarted()]
##---------------------------------------------------##
class ActionReturnInfo(Action):

    def name(self) -> Text:
        return "action_return_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        parent_name= tracker.get_slot('parent_name')
        student_name= tracker.get_slot('student_name')
        student_class =tracker.get_slot('student_class')
        student_roll =tracker.get_slot('student_roll')



        msg = "parent_name: {} ; student_name: {}; student_class : {} ; student_roll: {} ".format(parent_name,student_name,student_class,student_roll)
        print(msg)
        dispatcher.utter_message()
##-----------------------------------------------------##
