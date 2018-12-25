import time

class node:

          def __init__(self,state,action,depth):
                    self.state=state
                    self.action=action
                    self.depth=depth

          def desply(self):
                    print(self.state)
                    print(str(self.action)+"\n"+str(self.depth))
#****************************************************************
found=False
selected_depth = 0
Max_Depth =50


cut_off=input("please enter cut-off number:(defualt = 50)\n")
while not cut_off.isnumeric() and  cut_off != "":
    print("Error!")
    cut_off=input("please enter cut-off number:(defualt = 50)\n")
if cut_off == "" :
    Max_Depth =50
else:
    Max_Depth =int (cut_off)
    
goal_state=[[1,2,3],[4,5,6],[7,8,0]]
print("enter your state:")
initial_state=[[0,0,0],[0,0,0],[0,0,0]]
i=0
while(i<3):
          j=0
          while(j<3):
                    initial_state[i][j]=int(input('['+str(i+1)+']'+","+'['+str(j+1)+']'+"=\n"))
                    j=j+1
          i=i+1
start_t= time.time()

start=node(initial_state,' ',0)
#****************************************************************
fronthere=[]
fronthere.append(start)
checked=[]
actions=[]
#****************************************************************
def print_state(state):
          i=0
          while i<3:
                    j=0
                    while j<3:
                              print(" | "+str(state[i][j]),end='')
                              j=j+1
                    print(" | ")
                    i=i+1
          print('')

#****************************************************************
def heuristic(state):
          match=0
          i=0
          while(i<3):
                    j=0
                    while(j<3):
                              if goal_state[i][j]==state[i][j]:
                                        match=match+1
                              j=j+1
                    i=i+1
          return 9-match

#****************************************************************
def get_state():
          what=node([[],[],[]],"",0)
          index=0
          selected_index=0
#          max_depth=max(node.depth for node in fronthere)
          min_f=int(Max_Depth+9)
          for nd in fronthere:
                    if int(nd.depth+heuristic(nd.state))<min_f:
                              min_f=int(nd.depth+heuristic(nd.state))
                              what.state=nd.state
                              what.depth=nd.depth
                              what.action=nd.action
                              selected_index=index
                    index=index+1
          del fronthere[selected_index]
          return what

#****************************************************************
def match(state1,state2):
          i=0
          while(i<3):
                    j=0
                    while(j<3):
                              if state1[i][j]!=state2[i][j]:
                                        return False
                              j=j+1
                    i=i+1
          return True
#****************************************************************
def get_action(state):
          for nd in checked:
                    if match(nd.state,state):
                              return nd.action
          return "none"
#****************************************************************          
def print_path(state,action):
          current_state=state
          if action=='right':
                    current_state=left(current_state)
                    actions.append('right')
          elif action=='left':
                    current_state=right(current_state)
                    actions.append('left')
          elif action=='up':
                    current_state=down(current_state)
                    actions.append('up')
          elif action=='down':
                    current_state=up(current_state)
                    actions.append('down')
          while not match(current_state,initial_state):
                    current_action=get_action(current_state)
                    if current_action=='right':
                              current_state=left(current_state)
                              actions.append('right')
                    elif current_action=='left':
                              current_state=right(current_state)
                              actions.append('left')
                    elif current_action=='up':
                              current_state=down(current_state)
                              actions.append('up')
                    elif current_action=='down':
                              current_state=up(current_state)
                              actions.append('down')
          print('actions count :'+str(len(actions))+'\n')
          a=int(len(actions))-1
          while a>=0:
                    if actions[a]=='right':
                              current_state=right(current_state)
                    elif actions[a]=='left':
                              current_state=left(current_state)
                    elif actions[a]=='up':
                              current_state=up(current_state)
                    elif actions[a]=='down':
                              current_state=down(current_state)
                    a=a-1
                    print_state(current_state)


#****************************************************************



#****************************************************************
def can_right(state):
          i=0
          while i<3:
                    if state[i][2]==0:
                              return False
                    i=i+1
          return True

def can_left(state):
          i=0
          while i<3:
                    if state[i][0]==0:
                              return False
                    i=i+1
          return True

def can_up(state):
          i=0
          while i<3:
                    if state[0][i]==0:
                              return False
                    i=i+1
          return True

def can_down(state):
          i=0
          while i<3:
                    if state[2][i]==0:
                              return False
                    i=i+1
          return True
#****************************************************************
def zero_position(state,width =True):
          what = 0
          i=0
          while i<3:
                    j=0
                    while j<3:
                              if state[j][i]==0:
                                        if width ==True:
                                                  what=i
                                        else:
                                                  what=j
                              j=j+1
                    i=i+1
          return what
#****************************************************************
def is_checked(state):
          what=False
          for nd in checked:
                    if match(nd.state,state):
                              what=True
          return what
#****************************************************************
def right (state):
          what=[[0,0,0],[0,0,0],[0,0,0]]
          height=0
          while height<3:
                    width=0
                    while width<3:
                              what[height][width]=state[height][width]
                              width=width+1
                    height=height+1
          j=zero_position(state,False)
          i=zero_position(state)
          what[j][i]=state[j][i+1]
          what[j][i+1]=0
          return what

def left (state):
          what=[[0,0,0],[0,0,0],[0,0,0]]
          height =0
          while height <3:
                    width=0
                    while width<3:
                              what[height][width]=state[height][width]
                              width=width+1
                    height =height +1
          j=zero_position(state,False)
          i=zero_position(state)
          what[j][i]=state[j][i-1]
          what[j][i-1]=0
          return what

def up (state):
          what=[[0,0,0],[0,0,0],[0,0,0]]
          height =0
          while height<3:
                    width=0
                    while width<3:
                              what[height][width]=state[height ][width]
                              width=width+1
                    height=height+1
          j=zero_position(state,False)
          i=zero_position(state)
          what[j][i]=state[j-1][i]
          what[j-1][i]=0
          return what

def down (state):
          what=[[0,0,0],[0,0,0],[0,0,0]]
          height =0
          while height<3:
                    width=0
                    while width<3:
                              what[height][width]=state[height ][width]
                              width=width+1
                    height=height+1
          j=zero_position(state,False)
          i=zero_position(state)
          what[j][i]=state[j+1][i]
          what[j+1][i]=0
          return what
                              




#****************************************************************
print("start state:\n")
print_state(initial_state)
print("goal state:\n")
print_state(goal_state)

while len(fronthere)!=0 and not found and selected_depth<=Max_Depth:
          best_result=get_state()
          if match(best_result.state,goal_state):
                    print_path(best_result.state,best_result.action)
                    found=True
          else:
                    if can_right(best_result.state) :
                              if(not is_checked(right(best_result.state))):
                                        data = node([[0,0,0,],[0,0,0],[0,0,0]],'',0)
                                        data.depth=best_result.depth+1
                                        data.state=right(best_result.state)
                                        data.action='right'
                                        fronthere.append(data)
                    if can_left(best_result.state) :
                              if (not is_checked(left(best_result.state))):
                                        data = node([[0,0,0,],[0,0,0],[0,0,0]],'',0)
                                        data.depth=best_result.depth+1
                                        data.state=left(best_result.state)
                                        data.action='left'
                                        fronthere.append(data)
                    if can_up(best_result.state) :
                              if(not is_checked(up(best_result.state))):
                                        data = node([[0,0,0,],[0,0,0],[0,0,0]],'',0)
                                        data.depth=best_result.depth+1
                                        data.state=up(best_result.state)
                                        data.action='up'
                                        fronthere.append(data)
                    if can_down(best_result.state) :
                              if (not is_checked(down(best_result.state))):
                                        data = node([[0,0,0,],[0,0,0],[0,0,0]],'',0)
                                        data.depth=best_result.depth+1
                                        data.state=down(best_result.state)
                                        data.action='down'
                                        fronthere.append(data)
                    selected_depth=best_result.depth
                    checked.append(best_result)
if selected_depth>Max_Depth:
          print("\n can't solve it!")
          
finish_t= time.time()
print("total time : ", finish_t - start_t, "s")
 

                              
          
                    
                              
          
