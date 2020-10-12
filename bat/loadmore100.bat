@echo off

set times=50
set Dev=2cd4b315ee1d7ece

::set times=108
::set Dev=127.0.0.1:62001

for /l %%i in (1,1,%times%) do (

   timeout /t 1
   adb -s %Dev% shell input swipe 540 500 540 1400
   echo %%i times
 )
 pause
