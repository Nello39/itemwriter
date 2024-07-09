import tkinter

root = tkinter.Tk()
root.geometry("500x400")
root.title("test gui")

frame1 = tkinter.Frame(root)
frame1.pack()
frame2 = tkinter.Frame(root)
frame2.pack()

a = tkinter.Label(frame1,text="アイテム名")
item = tkinter.Entry(frame1)
b = tkinter.Label(frame1,text="値段")
pricetxt = tkinter.Entry(frame1)
c = tkinter.Label(frame1,text="ステータス名")
statustxt = tkinter.Entry(frame1)
d = tkinter.Label(frame1,text="能力")
ability1 = tkinter.Entry(frame1)
e = tkinter.Label(frame1,text="能力説明")
describe1 = tkinter.Entry(frame1)
g = tkinter.Label(frame1,text="能力２(オプション)")
ability2 = tkinter.Entry(frame1)
h = tkinter.Label(frame1,text="能力説明２(オプション)")
describe2 = tkinter.Entry(frame1)
f = tkinter.Label(frame1,text="材料")
stufftxt = tkinter.Entry(frame1)
a.grid(column=0,row=0)
b.grid(column=0,row=1)
c.grid(column=0,row=2)
d.grid(column=0,row=3)
e.grid(column=0,row=4)
g.grid(column=0,row=5)
h.grid(column=0,row=6)
f.grid(column=0,row=7)
item.grid(column=1,row=0)
pricetxt.grid(column=1,row=1)
statustxt.grid(column=1,row=2)
ability1.grid(column=1,row=3)
describe1.grid(column=1,row=4)
ability2.grid(column=1,row=5)
describe2.grid(column=1,row=6)
stufftxt.grid(column=1,row=7)


def btn_click():
    itemname = "|&attachref(item/"+item.get()+".webp,60x60);&br;"+item.get()
    price = "|"+pricetxt.get()
    status = statustxt.get() #If the item has statuses more than 2, insert '/' among each status.
    if status.count('/') > 0:
        status = "|"+status.replace("/","&br;")
    else:
        status = "|"+status

    if len(ability1.get()) > 1:
        abillityname1 = "|"+ability1.get() #If the item doesn't have any abillity, you don't need to fill this text-box.
        abillitydes1 = "&br;"+describe1.get()
    else:
        abillityname1 = "|"
        abillitydes1 = ""

    if len(ability2.get()) > 1:
        abillityname2 = "&br;"+ability2.get() #If the item doesn't have any abillity, you don't need to fill this text-box.
        abillitydes2 = "&br;"+describe2.get()
    else:
        abillityname2 = ""
        abillitydes2 = ""

    stuff = stufftxt.get() #If the item need more than 2 stuffs, add "/" at the end of name of the item. And type the name one and one.
    if stuff.count('/') > 0:
        stuffed = "|&attachref(item/"+stuff.replace('/','.webp,35x35);&attachref(item/')+".webp,35x35);|"
    else:
        if len(stuff) != 0:
            stuffed = "|&attachref(item/"+stuff+".webp,35x35);|"
        else:
            stuffed = "||"
    output = itemname+price+status+abillityname1+abillitydes1+abillityname2+abillitydes2+stuffed
    print(output)
    item.delete(0, tkinter.END)
    pricetxt.delete(0, tkinter.END)
    statustxt.delete(0, tkinter.END)
    ability1.delete(0, tkinter.END)
    describe1.delete(0, tkinter.END)
    ability2.delete(0, tkinter.END)
    describe2.delete(0, tkinter.END)
    stufftxt.delete(0, tkinter.END)

btn = tkinter.Button(root, text="決定", command=btn_click)
btn.pack()

root.mainloop()
