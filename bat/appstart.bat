::  获取应用n冷启动时间（热启动back后再执行命令）
@echo off

goto yyc
主要测试点：
1、冷启动：首次启动app的时间间隔（只是启动时间，不包括页面加载）
2、热启动：非首次启动app的时间间隔（只是启动时间，不包括页面加载）
3、完全启动：从启动到首页完全加载出来的时间间隔
4、有网启动：从发起跳转，到页面完全加载出来的时间间隔
5、无网启动：从发起跳转，到页面完全加载出来的时间间隔
（在项目中，主要测试关注点是冷启动，热启动）

含义：
ThisTime: 该Activity的启动耗时；
TotalTime: 应用自身启动耗时, ThisTime+应用application等资源启动时间；
WaitTime: 系统启动应用耗时, TotalTime+系统资源启动时间
:yyc

set package=com.golemon.wegoo.funny
set activity=com.GoLemon.splash.SplashActivity

adb shell am start -W %package%/%activity% 