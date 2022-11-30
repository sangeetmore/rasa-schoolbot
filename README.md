# rasa-schoolbot
A custom AI-powered bot that is used for parents visiting a school website, made using Rasa

To run this project, you need the following dependencies:
1. Rasa Open Source (3.0+)
2. Python version (3.7,3.8 or 3.9) [Note: Rasa 3.0+ is not yet compatible with Python 3.10]

Installation Steps:
1. Set-Up a Python Virtual Environment in a separate folder https://rasa.com/docs/rasa/installation/environment-set-up
2. Install Rasa Open Source in the Virtual Environment https://rasa.com/docs/rasa/installation/installing-rasa-open-source
3. Open a terminal in the same folder and paste the follwing command, `git clone https://github.com/sangeetmore/rasa-schoolbot.git`
4. Now, you should have Rasa and the code of this repository along with a Python Virtual Environment Ready.

How to run this project:
1. Go over into the folder where you have this code as well as Rasa installed
2. Start the Virtual environement with the following command, `source ./{your-virtual-environment-name}/bin/activate`
3. Once the Virtual Environment is up and running, train the model. Use the following command, `rasa train`
4. Once the model has finished training, start the Rasa Action Server (More details about the Action Server: https://rasa.com/docs/rasa/action-server).Use the following command, `rasa run actions`
5. After the above step, start the rasa shell to start the trianed model. Use the following command, `rasa shell`

Rasa Docs and Community would have answer to any issue you may face while installing or running this project. Kudos!
