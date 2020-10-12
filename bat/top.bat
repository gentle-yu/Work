::获取应用占用内存
@echo off 
::@mode con lines=18 cols=50

set package1=com.golemon.wegoo.funny

goto yyc
测试点：
1、空闲状态：切换至后台或者启动后不做任何操作，消耗内存最少。
2、中强度状态：时间偏长的操作应用。
3、高强度状态：高强度使用应用，可以跑monkey来测试（通常用来测试内存泄漏）

** 内存泄漏：指应用里的内存一直没有释放，内存一直增加 ,系统内存一直减少 **

测试关注点：
1、Native heap alloc
2、Dalvik heap alloc
3、PSS
:yyc

adb shell dumpsys meminfo %package1% | findstr "Pss"
adb shell dumpsys meminfo %package1% | findstr "Total"

:start
adb shell dumpsys meminfo %package1% | findstr "Native Heap"
adb shell dumpsys meminfo %package1% | findstr "Dalvik Heap"
adb shell dumpsys meminfo %package1% | findstr "TOTAL"


echo.
echo.
ping -n 2 127.1>nul
goto start