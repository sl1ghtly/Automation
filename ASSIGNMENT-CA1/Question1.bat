:: batch file to do 3 parts:
:: 1. open a browser, a word document and to note down daily task
:: 2. delete files from temporary internet files(cache)
:: 3. to check for the .exe and .bat or .cmd files created/saved 
:: in the last 24h
:: By: Eryk Gloginski

:: make output visible only and clear screen right after
@echo off
cls
echo "Part 1: "
:: start google chrome in incognito on the youtube website
start chrome www.youtube.com /incognito
:: start microsoft word
start winword
echo "Whenever ready, press any button to continue. "
pause

echo "Part 2"
:: delete everything in the directory without prompting for confirmation
RMDIR /s /q "C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Cache\Cache_Data"
echo "Whenever ready, press any button to continue. "
pause

echo "Part 3: "

