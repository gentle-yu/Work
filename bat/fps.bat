::得到一个矩阵数据，计算矩阵中帧率大于16的点所占比例，即为卡顿比

@echo off

goto yyc
打开手机：开发者选项—>profile GPU rendering —> in adb shell dumpsys gfxinfo
打开手机：开发者选项—>profile GPU rendering —> on screen as bars

含义：
Draw: 表示在Java中创建显示列表部分中，OnDraw()方法占用的时间。
Process：表示渲染引擎执行显示列表所花的时间，view越多，时间就越长。
Execute：表示把一帧数据发送到屏幕上排版显示实际花费的时间。
Draw + Process + Execute = 完整显示一帧 ，这个时间要小于16ms才能保存每秒60帧。

说明:
Android定义了流畅度的数据标准,以60FPS为标准(FPS为每秒绘制的帧数),帧数过小就会出现卡顿感
每一帧在安卓系统中分4个阶段,4个阶段的总和超过16.67(1秒60帧,算下来平均1帧的间隔就约是16.67ms)就认为丢帧
这个定义在Android6.0以前是一定的,但是现在已经没有固定的标准了,因为目前安卓系统有3层缓存机制,加上硬件上的进步,即使超过16.67,也不一定会出现卡顿感。所以这个数据在测试时作为一种对比和相对衡量标准，也可根据需求自定义标准。
:yyc

set package=com.golemon.wegoo.funny

adb shell dumpsys gfxinfo %package%
