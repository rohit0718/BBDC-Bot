# BBDC Bot

Simple bot built with Selenium using `python` as the language which automatically select and confirms your favoured slots automatically with just one command `python bbdc_bot.py`. Built for those who are looking for last minute slots and are tired of having to always enter all their credentials, manually select favoured slots, and click past countless dialogues, only to be presented with `No more slots available.`


## Prerequisties

- selenium & seleneium chrome driver (or any other browser of your choice)
- chrome
- python
- basic python knowledge (at least how to access elements in a list)


## Config

Open the `bbdc_bot.py` file with your favourite IDE and change these following lines of code:
- `chromedriver_location` in line 5 with the path of your `chromedriver` that you had downloaded
- `username` and `password` in lines 7 and 8
- required `months` (line 15),`sessions` (line 19) `days` (line 23), and `slots` (line 25). These are all lists that contain all of the various options that you see in the UI, with elements in chronological order (first month is `months[0]`, second is `months[1]`, etc.)


## Steps to run

1) Navigate to folder with `bbdc_bot.py`
2) Run `python bbdc_bot.py`
3) Sit back and watch the bot select and confirm your selection automatically :)


If you have any enquries feel free to contact me and, of course, feel free to use this for your very own versions of the bot (including a fully functional UI, infintitely looping program that only quits once its found a slot, for e.g.).
