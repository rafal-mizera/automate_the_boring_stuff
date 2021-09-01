import pyautogui
import time
from math import pi
from pyautogui import FailSafeException
#
# pyautogui.PAUSE = 1
# pyautogui.FAILSAFE = True
# print(pyautogui.size())
# width,height = pyautogui.size()
# print(width)

# for i in range(10):
#     try:
#         pyautogui.moveTo(100,100,duration=3)
#         pyautogui.moveTo(100,700)
#         pyautogui.moveTo(700,100)
#         pyautogui.moveTo(700,700)
#     except FailSafeException:
#         print("Program was interrupted...")

# try:
#     for i in range(10):
#         pyautogui.moveRel(100,100)
#         pyautogui.moveRel(-100,-100)
# except FailSafeException:
#     print("Program was interrupted...")

# print(pyautogui.position())
#
# pyautogui.click()
# pyautogui.click(1251,6)
# pyautogui.rightClick()

time.sleep(3)
# for i in range(50):
#     pyautogui.dragRel(i,-i)
#     pyautogui.dragRel(i,i)

# distance = 200
#
# while distance > 0:
#     pyautogui.dragRel(distance,0)
#     distance -= 5
#     pyautogui.dragRel(0,distance)
#     pyautogui.dragRel(-distance,0)
#     distance -= 5
#     pyautogui.dragRel(0,-distance)


# pyautogui.scroll(200)

import pyperclip
import time

numbers = ""
for i in range(200):
    numbers += str(i) + "\n"

pyperclip.copy(numbers)

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199

# time.sleep(5)
# for i in range(15):
#     pyautogui.scroll(100)
#     time.sleep(1)

# im = pyautogui.screenshot()
#
# print(im.getpixel((100,100)))
# print(pyautogui.pixelMatchesColor(100,100,(50,50,50)))
# print(pyautogui.pixelMatchesColor(100,100,(50,100,50)))

# print(pyautogui.center(pyautogui.locateOnScreen("windows.PNG")))
# pyautogui.click(25,747)

# pyautogui.click(400,400);pyautogui.typewrite("bla bla bla",0.25)

# pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

# pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
pyautogui.hotkey("ctrl","c")



