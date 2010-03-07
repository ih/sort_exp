import pyglet
import pdb
import time
import datetime
import textinput
import copy
import pickle
from random import randint,shuffle
from itertools import permutations
from selectable import SelectableSprite
from pyglet.sprite import Sprite
from pyglet.window import key, mouse

####uncomment for debugging
#window.push_handlers(pyglet.window.event.WindowEventLogger())

batch=pyglet.graphics.Batch()
display=False

num_stim=5
selected=[]
stim=[[]]
labels=[]
#maybe make this a shape with random color

image=pyglet.image.load('stim.gif')
window=pyglet.window.Window()
#scale the image based on the number of stimuli and the size of the window

image_scale=(min(window.width,window.height)/num_stim)/(image.width*1.0)

#keep track of the choices of the user
fname=str(datetime.datetime.now())+'.dat'
logfile=open(fname,'w')
userlog=[]


stim_order=range(num_stim)

#positioning functions
def even_spacing(num_objs,boundary):
    """returns an array of evenly spaced positions for the passed number of objects from 0,boundary; it should be noted the intervals must be integers"""
    if num_objs == 1:
        return [boundary/2]
    else:
        interval=boundary/(num_objs+1)
        positions=[i for i in range(0,boundary,interval)]
        return positions[1:num_objs+1]


#given the list within data returns the x coordinate which applies to all the items in that list
def x_pos(list_num):
    return even_spacing(len(stim), window.width)[list_num]

def y_pos(item_num):
    return even_spacing(num_stim, window.height)[item_num]


#data is a list of lists where each list contains selectablesprites
#generate the stimuli initially a single list
    
    #create a single list containing all the elements; initially set position to origin
def init_episode():
#assign an order to the stimuli; the index is the item label and the value is the order position
    userlog.append([])
    global stim_order,stim
    stim=[[]]
    shuffle(stim_order)
    print stim_order

    for i in range(num_stim):
        label=pyglet.text.Label(str(i), font_name='Times New Roman', font_size=36, x=x_pos(0), y=y_pos(i), anchor_x='center', anchor_y='center', batch=batch)
        ssprite=SelectableSprite(image,x_pos(0),y_pos(i),batch=batch,label=label)
        ssprite.color=(randint(0,255),randint(0,255),randint(0,255))

        ssprite.scale=image_scale

        (pos,s)=(stim_order[i],ssprite)
        stim[0].append((pos,s))
        window.push_handlers(s.on_mouse_press)
        window.push_handlers(s.on_mouse_drag)    

init_episode()




@window.event
def on_draw():
    global display
    if display:
        time.sleep(3)
        display=False
    window.clear()
#    batch.draw()
    for lst in stim:
        for pos,obj in lst:
            obj.draw()
            if obj.selected and lst.index((pos,obj))!=0:
#add list/remove obj from lists based on the 4 different cases
                head_pos,head=lst[0]
                lst_indx=stim.index(lst)
                if pos < head_pos and (lst_indx==0 or not inside((pos,obj),stim[lst_indx-1])):
#                    pdb.set_trace()
                    #create a list and add to front of stim
                    remove_greater((pos,obj),lst_indx)
                    small_lst=new_lst((pos,obj),lst)
                    stim.insert(0,small_lst)
                    stim.sort()
                    obj.selected=False

                elif not pos<head_pos and (lst_indx==len(stim)-1 or not inside((pos,obj),stim[lst_indx+1])):
#                    pdb.set_trace()
                    #create a list and add to end of stim
                    remove_less((pos,obj),lst_indx)
                    small_lst=new_lst((pos,obj),lst)
                    stim.append(small_lst)
                    stim.sort()
                    obj.selected=False

                elif pos<head_pos:
#                    pdb.set_trace()
                    #remove obj from list and all lists after
                    remove_greater((pos,obj),lst_indx)
                else:
#                    pdb.set_trace()
                    #remove obj from list and all lists before
                    remove_less((pos,obj),lst_indx)
                userlog[-1].append(copy.copy(stim))
                #start a new episode if finished
    if len(stim)==num_stim:
        for e in userlog:
            i=userlog.index(e)
            pyglet.text.Label("Episode"+str(i)+':'+str(len(e)), font_name='Times New Roman', font_size=40, x=window.width/2, y=i*40).draw()
        display=True
        print "SORTED"
        pickle.dump(userlog,fname)
        init_episode()
    set_stim_pos()
    print stim
    print stim_order

def remove_less((pos,obj),lst_indx):
    for l in stim[0:lst_indx+1]:
        for p,o in l:
            if p==pos:
                l.remove((p,o))

def remove_greater((pos,obj),lst_indx):
    for l in stim[lst_indx:]:
        for p,o in l:
            if p==pos:
                l.remove((p,o))

def inside((pos,obj),lst):
    for p,o in lst:
        if p==pos:
            return True
    return False
        

def set_stim_pos():
    for lst in stim:
        for (pos,obj) in lst:
            obj.x=obj.label.x=x_pos(stim.index(lst))
            obj.y=obj.label.y=y_pos(lst.index((pos,obj)))
#    pdb.set_trace()
            

def new_lst((pos,obj),lst):
#    pdb.set_trace()
    #copy the list
    lst_copy=[]
    for (lpos,lobj) in lst[1:]:
        label=pyglet.text.Label(lobj.label.text, font_name='Times New Roman', font_size=36, x=x_pos(0), y=y_pos(lst.index((lpos,lobj))), anchor_x='center', anchor_y='center', batch=batch)
        s=SelectableSprite(lobj.image,x_pos(0),y_pos(lst.index((lpos,lobj))),batch=batch,label=label)
        s.scale=lobj.scale
        s.color=lobj.color
        lst_copy.append((lpos,s))
        window.push_handlers(s.on_mouse_press)
        window.push_handlers(s.on_mouse_drag)    

    lst_copy.insert(0,(pos,obj))
    return lst_copy

pyglet.app.run()

# def less(a,b):
#     pdb.set_trace()
#     return stim_order.index(a) < stim_order.index(b)



# def unselect_all():
#     for lst in stim:
#         for id,obj in lst:
#             obj.selected=False


# def compare():
#     """compares items in selected and returns a string 'a<b' """
#     i1=selected[0]
#     i2=selected[1]
#     if stim_order.index(i1) < stim_order.index(i2) and selected:
#     if stim_order.index(i1) < stim_order.index(i2):
#         return str(i1)+"<"+str(i2)
#     else:
#         return str(i2)+"<"+str(i1)

# def sorted():
#     comparisons=[stim[stim_order[i]].x<=stim[stim_order[i+1]].x for i in range(num_stim-1)]
# #    pdb.set_trace()
#     return reduce(lambda x,y: x and y, comparisons)



