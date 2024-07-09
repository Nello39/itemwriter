num = 0
while num != 'end':
    item = input("itemname(endと書いて処理を終了させます)")
    if item == 'end':
        break
    itemname = "|&attachref(item/"+item+".webp,60x60);&br;"+item
    price = "|"+input("price")
    status = input("status") #If the item has statuses more than 2, insert '/' among each status.
    if status.count('/') > 0:
        status = "|"+status.replace("/","&br;")
    else:
        status = "|"+status
    abillityname = "|"+input("abillityname") #If the item doesn't have any abillity, you don't need to fill this text-box.
    if len(abillityname) > 1:
        abillitydes = "&br;"+input("abillitydes")
    stuff = input("stuff") #If the item need more than 2 stuffs, add "/" at the end of name of the item. And type the name one and one.
    stuffed = "&attachref(item/"+stuff.replace('/','')+".webp,35x35);"
    many = stuff.count('/')
    while many != 0:
        stuff = input("stuff") #If the item need more than 2 stuffs, add "/" at the end of name of the item. And type the name one and one.
        stuffed = stuffed+"&attachref(item/"+stuff.replace('/','')+".webp,35x35);"
        many = stuff.count('/')
    stuffed = "|"+stuffed+"|"
    output = itemname+price+status+abillityname+abillitydes+stuffed
    print(output)
#|&attachref(item/苦痛のマスク.webp,60x60);&br;苦痛のマスク|2040|+120 魔法攻撃&br;+5% CD短縮&br;+800 最大HP|setume|&attachref(item/魔道の石.webp,35x35);&attachref(item/聖者の法典.webp,35x35);&attachref(item/レッドメノウ.webp,35x35);|