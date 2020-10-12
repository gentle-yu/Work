::monkey测试


set package = com.golemon.wegoo.funny



::adb shell monkey -p %package% -s 23  --throttle 2000 --ignore-crashes --ignore-timeouts -v -v -v 100000>C:\Desktop\monkey_log.txt 2>&1 &



adb shell monkey -p %package% -s 23  --throttle 500 --ignore-crashes --ignore-timeouts -v -v -v 100000>C:\Users\testing\Desktop\monkey_log.txt 2>&1 &