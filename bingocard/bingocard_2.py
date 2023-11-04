import tkinter
import random
root = tkinter.Tk()
root.title("ビンゴカード")

bing_num1 = random.sample(range(1, 16), k = 5)
bing_num2 = random.sample(range(16, 31), k = 5)
bing_num3 = random.sample(range(31, 46), k = 4)
bing_num4 = random.sample(range(46, 61), k = 5)
bing_num5 = random.sample(range(61, 75), k = 5)

button1 = tkinter.Button(root, text=bing_num1[0], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=0, column=0)
button2 = tkinter.Button(root, text=bing_num1[1], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=1, column=0)
button3 = tkinter.Button(root, text=bing_num1[2], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=2, column=0)
button4 = tkinter.Button(root, text=bing_num1[3], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=3, column=0)
button5 = tkinter.Button(root, text=bing_num1[4], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=4, column=0)

button6 = tkinter.Button(root, text=bing_num2[0], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=0, column=1)
button7 = tkinter.Button(root, text=bing_num2[1], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=1, column=1)
button8 = tkinter.Button(root, text=bing_num2[2], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=2, column=1)
button9 = tkinter.Button(root, text=bing_num2[3], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=3, column=1)
button10 = tkinter.Button(root, text=bing_num2[4], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=4, column=1)

button11 = tkinter.Button(root, text=bing_num3[0], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=0, column=2)
button12 = tkinter.Button(root, text=bing_num3[1], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=1, column=2)
button13 = tkinter.Button(root, text="Free", font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=2, column=2)
button14 = tkinter.Button(root, text=bing_num3[2], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=3, column=2)
button15 = tkinter.Button(root, text=bing_num3[3], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=4, column=2)

button16 = tkinter.Button(root, text=bing_num4[0], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=0, column=3)
button17 = tkinter.Button(root, text=bing_num4[1], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=1, column=3)
button18 = tkinter.Button(root, text=bing_num4[2], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=2, column=3)
button19 = tkinter.Button(root, text=bing_num4[3], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=3, column=3)
button20 = tkinter.Button(root, text=bing_num4[4], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=4, column=3)

button21 = tkinter.Button(root, text=bing_num5[0], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=0, column=4)
button22 = tkinter.Button(root, text=bing_num5[1], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=1, column=4)
button23 = tkinter.Button(root, text=bing_num5[2], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=2, column=4)
button24 = tkinter.Button(root, text=bing_num5[3], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=3, column=4)
button25 = tkinter.Button(root, text=bing_num5[4], font=("MSゴシック", "20", "bold"), width=5, height=2).grid(row=4, column=4)




root.mainloop()
