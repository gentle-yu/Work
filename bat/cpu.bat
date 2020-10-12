::获取应用占用cpu情况

@echo off 
::@mode con lines=18 cols=50

set package1=com.golemon.wegoo.funny 

:start
adb shell dumpsys cpuinfo |grep %package1% 

timeout /t 1
goto start