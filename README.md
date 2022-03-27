# Website Navigation Chatbot

How to run the code:

- create and activate `conda` environment

      conda create --name env
      conda activate

- uncomment line 4 in nltk_utils.py and run the following command

      python nltk_utils.py

  then comment line 4 again

- run crawler.py to create intents.json for a website

      python crawler.py

- train the model

      python train.py

- run the chat
      python chat.py

<hr>

### Credits

Extended from
https://github.com/python-engineer/pytorch-chatbot
