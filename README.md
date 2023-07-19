# Mouse_Heartrate
利用鼠标位移测量心率(或者抖腿频率)的程序<br>
-Measure heart rate (or leg shaking frequency) using mouse displacement

## 原理/Method
测量时把鼠标倒过来放在桌子上,然后把手指悬在鼠标传感器上一点点高的位置(测量抖腿频率时也可以把鼠标搭在腿上)<br>
读取一段时间内(默认5s,采样速度100/s)的鼠标位移数据,然后做ICA变换和滤波处理,最后以频谱图上最高峰作为心率/抖腿频率<br>
心率测量准确率受手的位置等影响较大<br>
-Place the mouse upside down on a flat surface and hover your finger slightly above the mouse sensor (you can also place the mouse on your leg to measure leg shaking frequency)<br>
-Read the mouse displacement data over a period of time (default 5s, sampling rate 100/s), then apply ICA transform and filtering to the data. Finally, take the highest peak in the frequency spectrum as the estimated heart rate or leg shaking frequency<br>
-The accuracy of heart rate measurement can be significantly affected by the positioning of the hand and other factors<br>

## 演示/Demo
### 测量心率:
(整只手臂悬空,右手中指放在鼠标传感器上面一点点)<br>
<img width="300" alt="Screenshot 2023-07-19 at 10 13 47" src="https://github.com/sszzz830/Mouse_Heartrate/assets/32834442/49cb7a1a-3936-4681-957d-717a77f5361a"><br>
<img width="440" alt="Screenshot 2023-07-19 at 10 13 50" src="https://github.com/sszzz830/Mouse_Heartrate/assets/32834442/ac006090-b199-46ab-89e1-923a8a6db407"><br>
Galaxy Watch 4测量结果:<br>
<img width="300" alt="gw4 result" src="https://github.com/sszzz830/Mouse_Heartrate/assets/32834442/b8e9936b-a268-4b21-a101-61e0ce9a8624">
<br>
### 测量抖腿:
(右手食指放在鼠标传感器上面一点点,同时抖腿)<br>
<img width="300" alt="Screenshot 2023-07-19 at 09 53 24" src="https://github.com/sszzz830/Mouse_Heartrate/assets/32834442/a54d5120-927f-465c-83eb-aad79474792b"><br>
<img width="440" alt="Screenshot 2023-07-19 at 09 53 42" src="https://github.com/sszzz830/Mouse_Heartrate/assets/32834442/fd9a06a1-4c28-460e-ac30-a1e61b1bcf78">

## 
看到这个然后想做的(原推主未附代码)<br>
<img width="230" alt="tw" src="https://github.com/sszzz830/Mouse_Heartrate/assets/32834442/97d4e930-d560-44e1-8d3a-5b0a79239d52">
