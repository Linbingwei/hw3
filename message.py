def shift_reduce(expression:str):
    tokens , i = [] , 0
    while i < len(expression):
        if expression[i].isalpha():
            token = ""
            while i < len(expression) and expression[i].isalpha():
                token += expression[i]
                i += 1
            tokens.append(token)
        elif expression[i].isdigit():
            token = ""
            while i < len(expression) and expression[i].isdigit():
                token += expression[i]
                i += 1
            tokens.append(token)
        else:
            tokens.append(expression[i])
            i += 1
    return tokens

def LR_Parsing_Table_query(num:str):
    query = "s" + num
    return query

def split_alpha_num(string:str):
    alpha = ""
    num = ""
    for i in string:
        if i.isalpha():
            alpha += i
        elif i.isdigit():
            num += i
    return num
LRParser = {
    "s0" : {"Action" : {"id":"s5","(":"s4"} , "Goto" : {"E":"r1","T":"r2","F":"r3"}},
    "s1" : {"Action" : {"+":"s6" , "$":"acc"} , "Goto" : {}},
    "s2" : {"Action" : {"+":"r2" , "*":"s7" , ")":"r2" , "$":"r2"} , "Goto" : {}},
    "s3" : {"Action" : {"+":"r4" , "*":"r4" , ")":"r4" , "$":"r4"} , "Goto" : {}},
    "s4" : {"Action" : {"id":"s5" , "(":"s4"} , "Goto" : {"E":"r8","T":"r2","F":"r3"}},
    "s5" : {"Action" : {"+":"r6" , "*":"r6" , ")":"r6" , "$":"r6"} , "Goto" : {}},
    "s6" : {"Action" : {"id":"s5" , "(":"s4"} , "Goto" : {"T":"r9","F":"r3"}},
    "s7" : {"Action" : {"id":"s5" , "(":"s4"} , "Goto" : {"F":"r10"}},
    "s8" : {"Action" : {"+":"s6" , ")":"s11"} , "Goto" : {}},
    "s9" : {"Action" : {"+":"r1" , "*":"s7" , ")":"r1" , "$":"r1"} , "Goto" : {}},
    "s10" : {"Action" : {"+":"r3" , "*":"r3" , ")":"r3" , "$":"r3"} , "Goto" : {}},
    "s11" : {"Action" : {"+":"r5" , "*":"r5" , ")":"r5" , "$":"r5"} , "Goto" : {}},
    "s12" : {"Action" : {"id":"s5" , "(":"s4"} , "Goto" : {"E":"s12","T":"r2","F":"r3"}},
}

Reduction = {
    "r1" : {"remove" : ["E","+","T"] , "add" : "E"},
    "r2" : {"remove" : ["T"] , "add" : "E"},
    "r3" : {"remove" : ["T","*","F"] , "add" : "T"},
    "r4" : {"remove" : ["F"] , "add" : "T"},
    "r5" : {"remove" : ["(","E",")"] , "add" : "F"},
    "r6" : {"remove" : ["id"] , "add" : "F"},
}


while True:
    try:
        input_string = input("")
        input_string = shift_reduce(input_string)
        input_string.append("$")
        stack = ["0"]
        rec_act = []
        i = 0
        while len(input_string) > 0:          
            query = LR_Parsing_Table_query(stack[-1]) 
            if input_string[0] in LRParser[query]["Action"]:
                action = LRParser[query]["Action"][input_string[0]]
                if action[0] == "s":
                    stack.append(input_string[0])
                    stack.append(action[1:])
                    input_string.pop(0)
                    i += 1
                elif action[0] == "r":
                    remove , add = Reduction[action]["remove"] , Reduction[action]["add"]
                    char_cnt = len(remove) * 2
                    stack = stack[:-char_cnt]
                    next_state = LR_Parsing_Table_query(stack[-1])
                    stack.append(add)
                    stack.append(split_alpha_num(LRParser[next_state]["Goto"][add]))
                elif action == "acc": 
                    print("Accept")
                    rec_act.append(action)
                    break
                rec_act.append(action)
            else:
                print("Error")
                break
    except:
        break
        