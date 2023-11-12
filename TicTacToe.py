#--------------Import--------------#
import tkinter
import click
import time
import random

#--------------Window creation--------------#
window = tkinter.Tk()
window.title('TicTacToe-Game')
graph_zone = tkinter.Canvas(window, width = 300, height = 300, bg = 'white')
graph_zone.pack()

#--------------Grid list creation--------------#
grid=  [[0,0,0],
        [0,0,0],
        [0,0,0]]

def show_grid(color):
    '''create lines/borders with tkinter'''
    graph_zone.create_line(0, 200, 300, 200, width=3, fill=color)
    graph_zone.create_line(0, 100, 300, 100, width=3, fill=color)
    graph_zone.create_line(100, 0, 100, 300, width=3, fill=color)
    graph_zone.create_line(200, 0, 200, 300, width=3, fill=color)

def show_symbols():
    '''create players symbol with tkinter'''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                graph_zone.create_oval(i*100+10, j*100+10, i*100+90, j*100+90, fill='blue')
            elif grid[i][j]==2:
                graph_zone.create_line(i*100+10, j*100+10, i*100+90, j*100+90, width=10, fill='red')
                graph_zone.create_line(i*100+10, j*100+90, i*100+90, j*100+10, width=10, fill='red')

def winner():
    '''return winner by his number when he win (3 symbols aligned)'''
    if grid[0][0]==1 and grid[0][1]==1 and grid[0][2]==1 or grid[1][0]==1 and  grid[1][1]==1 and grid[1][2]==1 or grid[2][0]==1 and  grid[2][1]==1 and grid[2][2]==1 or grid[0][0]==1 and  grid[1][0]==1 and grid[2][0]==1 or grid[0][1]==1 and  grid[1][1]==1 and grid[2][1]==1 or grid[0][2]==1 and  grid[1][2]==1 and grid[2][2]==1 or grid[0][0]==1 and grid[1][1]==1 and grid[2][2]==1 or grid[0][2]==1 and grid[1][1]==1 and grid[2][0]==1:
        return 1
    elif grid[0][0]==2 and grid[0][1]==2 and grid[0][2]==2 or grid[1][0]==2 and  grid[1][1]==2 and grid[1][2]==2 or grid[2][0]==2 and  grid[2][1]==2 and grid[2][2]==2 or grid[0][0]==2 and  grid[1][0]==2 and grid[2][0]==2 or grid[0][1]==2 and  grid[1][1]==2 and grid[2][1]==2 or grid[0][2]==2 and  grid[1][2]==2 and grid[2][2]==2 or grid[0][0]==2 and grid[1][1]==2 and grid[2][2]==2 or grid[0][2]==2 and grid[1][1]==2 and grid[2][0]==2:
        return 2
    else:
        return False

def show(color):
    '''show the board game'''
    graph_zone.delete('all')
    show_grid(color)
    show_symbols()
    graph_zone.update()

def search_empty_cases():
    '''search empty cases'''
    empty_cases=[]
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            if grid[j][i]==0:
                empty_cases.append([j,i])
    return empty_cases

def choix():
    '''make a random choice for the bot player'''
    a=random.randint(0,len(search_empty_cases())-1)
    return search_empty_cases()[a]

def clic(event):
    '''main function with click event'''
    show('black')
    global grid
    x=event.x // 100
    y=event.y // 100
    if grid[x][y]==0:
        grid[x][y]=1
        show('black')
        if winner()==1 :
            show('blue')
            print('You Win!')
            time.sleep(1)
            window.destroy()
        else:
            case=choix()
            grid[case[0]][case[1]]=2
            show('black')
            if winner()==2:
                show('red')
                print('Bot Win...')
                time.sleep(1)
                window.destroy()

show('black')
window.bind("<Button-1>", clic)
window.mainloop()