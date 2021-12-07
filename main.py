import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import random

f = open(r'data.txt', 'w')
f.write('') 
f.close()

def create_text():
    mb.showinfo("登録が完了しました", "タブから「ゲーム」をクリックして先にすすめてください")
    name = entry1_1.get()
    grade = entry1_2.get()
    r_text = name + " " + grade
    f = open(r'data.txt', 'a')
    f.write(r_text)
    f.close()

counter = 1
def make_q():
    global num_n, num_i, num_i_l, ans, counter
    if counter == 1:
        num_n = str(3)
        num_i = ""
        num_i_l = []
        for _ in range(int(num_n)):
            ans = str(_ + 2)
            num_i += ans + "cm, "
            num_i_l.append(int(ans))
    elif counter == 2:
        num_n = str(3)
        num_i = ""
        num_i_l = []
        for _ in range(int(num_n)):
            ans = str(random.randint(1, 20))
            num_i += ans + "cm, "
            num_i_l.append(int(ans))
        label2_2['text'] = str(num_n + "本の棒があります. 棒の長さは" + num_i + "です.\n あなたは,それらの棒から3本を選んでできるだけ周長（周りの長さ）の長い三角形を作ろうと考えます.\n その三角形の周長を求めなさい.\n ただし三角形が作れない場合は0と答えてください.")
    else:
        num_n = str(random.randint(3, 10))
        num_i = ""
        num_i_l = []
        for _ in range(int(num_n)):
            ans = str(random.randint(1, 50))
            num_i += ans + "cm, "
            num_i_l.append(int(ans))
        label2_2['text'] = str(num_n + "本の棒があります. 棒の長さは" + num_i + "です.\n あなたは,それらの棒から3本を選んでできるだけ周長（周りの長さ）の長い三角形を作ろうと考えます.\n その三角形の周長を求めなさい.\n ただし三角形が作れない場合は0と答えてください.")

make_q()

def validation():
    global a2
    a2 = 0 
    for i in range(int(num_n)):
        for j in range(i + 1, int(num_n)):
            for k in range(j + 1, int(num_n)):
                LEN = num_i_l[i] + num_i_l[j] + num_i_l[k]
                ma = max(num_i_l[i], max(num_i_l[j], num_i_l[k]))
                rest = LEN - ma
                if ma < rest:
                    a2 = max(a2, LEN)
validation()

def send_ans():
    global counter
    mb.showinfo("解答を送信しました", "解答を送信")
    ans_f = entry2_1.get()
    if int(ans_f) == a2:
        mb.showinfo("採点", "正解です！")
        make_q()
        validation()
        f = open(r'data.txt', 'a')
        f.write("\n"+str(counter))
        f.close()
        counter += 1
    else:
        mb.showinfo("採点", "不正解です！もう一度頑張ってください！")

root = tk.Tk() 
root.geometry('800x600')
root.title("Game")

nb = ttk.Notebook(width=200, height=200)

tab1 = tk.Frame(nb)
tab2 = tk.Frame(nb)
tab3 = tk.Frame(nb)
nb.add(tab1, text='登録', padding=3)
nb.add(tab2, text='ゲーム', padding=3)
nb.add(tab3, text='その他', padding=3)
nb.pack(expand=1, fill='both')

label1_1 = tk.Label(tab1,text="【受験者登録】",font=("",16),height=2)
label1_1.pack(fill="x")

frame1_1 = tk.Frame(tab1,pady=10)
frame1_1.pack()
label1_2 = tk.Label(frame1_1,font=("",14),text="名前")
label1_2.pack(side="left")
entry1_1 = tk.Entry(frame1_1,font=("",14),justify="center",width=15)
entry1_1.pack(side="left")

frame1_2 = tk.Frame(tab1,pady=10)
frame1_2.pack()
label1_3 = tk.Label(frame1_2,font=("",14),text="学年")
label1_3.pack(side="left")
entry1_2 = tk.Entry(frame1_2,font=("",14),justify="center",width=15)
entry1_2.pack(side="left")

button1_4 = tk.Button(tab1,text="登録",font=("",14),width=5,bg="gray",command=create_text)
button1_4.pack()

label2_1 = tk.Label(tab2,text="【ゲーム画面】",font=("",16),height=2)
label2_1.pack(fill="x")

label2_2 = tk.Label(tab2,text=num_n + "本の棒があります. 棒の長さは" + num_i + "です.\n あなたは,それらの棒から3本を選んでできるだけ周長（周りの長さ）の長い三角形を作ろうと考えます.\n その三角形の周長を求めなさい.\n ただし三角形が作れない場合は0と答えてください.",font=("",14),height=7,wraplength=500)
label2_2.pack(fill="x")

frame2_1 = tk.Frame(tab2,pady=10)
frame2_1.pack()
label2_3 = tk.Label(frame2_1,font=("",14),text="周長（周りの長さ）")
label2_3.pack(side="left")
entry2_1 = tk.Entry(frame2_1,font=("",14),justify="center",width=15)
entry2_1.pack(side="left")

button2_4 = tk.Button(tab2,text="解答",font=("",14),width=5,bg="gray",command=send_ans)
button2_4.pack()

root.mainloop() 
