import numpy as np
from datetime import datetime
import warnings


warnings.simplefilter("ignore")


class StaticVariable:
    count = 0
    countTree = 0
    countBFS = 0
    sonuc = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    dir = ''
    back = 9
    artıs = False
    solutionlist = []
    Leftlistcount = 0
    Rightlistcount = 0
    Uplistcount = 0
    Downlistcount = 0
    countWarning = 0

    def __init__(self):
        self.solutionlist.append([])

def compera(data):
    #print(data)
    gercek = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    toplam = 0
    for j in range(0, gercek.shape[0]):
        for k in range(0, gercek.shape[1]):
            toplam = toplam + (gercek[j][k] - data[j][k])*(gercek[j][k] - data[j][k])

    return toplam

def sonucgoster(data):
    length = data.shape[0]/9 - 1
    index = 0
    sonuc = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    for j in range(0, sonuc.shape[0]):
        for k in range(0, sonuc.shape[1]):
            sonuc[j][k] = data[index]
            index += 1
    print(sonuc)

    for i in range(0,int(length)):
        print("Step ",i+1)
        for j in range(0, sonuc.shape[0]):
            for k in range(0, sonuc.shape[1]):
                sonuc[j][k] = data[index]
                index += 1
        print(sonuc)

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.data = data
        self.Heuristic = 999999

    def insert(self, data, count, dir='NONE'):
        if True:
            if count == 0:
                if self.left is None and dir != 'right':
                    self.left = Node(data)
                elif dir != 'right':
                    self.left.insert(data, count, dir='left')
                else:
                    self.left.insert('YOK', count, dir='left')
            elif count == 1:
                if self.right is None and dir != 'left':
                    self.right = Node(data)
                elif dir != 'left':
                    self.right.insert(data, count, dir='right')
                else:
                    self.right.insert('YOK', count, dir='right')
            elif count == 2:
                if self.up is None and dir != 'down':
                    self.up = Node(data)
                elif dir != 'down':
                    self.up.insert(data, count, dir='up')
                else:
                    self.up.insert('YOK', count, dir='up')
            elif count == 3:
                if self.down is None and dir != 'up':
                    self.down = Node(data)
                elif dir != 'up':
                    self.down.insert(data, count, dir='down')
                else:
                    self.down.insert('YOK', count, dir='down')
        else:
            #self.data = data
            if self.down is None:
                self.down = Node(data)
            else:
                self.down.insert(data, count)

# Print the tree
    def PrintTree(self):
        print(self.data)
        if self.data != 'YOK':
            if self.left:
                #print("Left", self.data)
                self.left.PrintTree()
            if self.right:
                #print("Right", self.data)
                self.right.PrintTree()
            if self.up:
                #print("Up", self.data)
                self.up.PrintTree()
            if self.down:
                #print("Down", self.data)
                self.down.PrintTree()

    def DFS(self, Sbulundu):
        if self.data != 'YOK':
            Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.data)
            # print("Sonuc : ",Sbulundu.sonuc)
            # print("Uzunluk : ", Sbulundu.sonuc.shape[0])
            #print(self.data)
            if self.left and Sbulundu.count == 0:
                self.left.DFS(Sbulundu)
                #print(self.data)
                if self.left.data != 'YOK':
                    if compera(self.left.data) == 0:
                        Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.left.data)
                        Sbulundu.count = Sbulundu.count + 1
                        print('Bulundu.')
                        print(self.left.data)
                        print('-')
                        #return Sbulundu.sonuc
                    else:
                        #print(self.data)
                        #Sbulundu.sonuc = np.delete(Sbulundu.sonuc, self.data)
                        delete = True
                        if Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-9] == 1 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-8] == 2 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-7] == 3 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-6] == 4 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-5] == 5 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-4] == 6 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-3] == 7 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-2] == 8 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-1] == 0:
                            if Sbulundu.sonuc[Sbulundu.sonuc.shape[0] - 9] == 1 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 17] == 2 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 16] == 3 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 15] == 4 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 14] == 5 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 13] == 6 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 12] == 7 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 11] == 8 and Sbulundu.sonuc[Sbulundu.sonuc.shape[0] - 10] == 0:
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 9, Sbulundu.sonuc.shape[0] - 8,
                                                            Sbulundu.sonuc.shape[0] - 7, Sbulundu.sonuc.shape[0] - 6,
                                                            Sbulundu.sonuc.shape[0] - 5, Sbulundu.sonuc.shape[0] - 4,
                                                            Sbulundu.sonuc.shape[0] - 3, Sbulundu.sonuc.shape[0] - 2,
                                                            Sbulundu.sonuc.shape[0] - 1])

                        else:
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc, [Sbulundu.sonuc.shape[0]-9, Sbulundu.sonuc.shape[0]-8,
                                                                    Sbulundu.sonuc.shape[0]-7, Sbulundu.sonuc.shape[0]-6,
                                                                    Sbulundu.sonuc.shape[0]-5, Sbulundu.sonuc.shape[0]-4,
                                                                    Sbulundu.sonuc.shape[0]-3, Sbulundu.sonuc.shape[0]-2,
                                                                    Sbulundu.sonuc.shape[0]-1])
                        #print("Sonuc Else : ", Sbulundu.sonuc)
            if self.right and Sbulundu.count == 0:
                self.right.DFS(Sbulundu)
                #print(self.data)
                if self.right.data != 'YOK':
                    if compera(self.right.data) == 0:
                        Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.right.data)
                        Sbulundu.count = Sbulundu.count + 1
                        print('Bulundu.')
                        print(self.right.data)
                        print('-')
                        #return Sbulundu.sonuc
                    else:
                        #print(self.data)
                        #Sbulundu.sonuc = np.delete(Sbulundu.sonuc, self.data)
                        if Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-9] == 1 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-8] == 2 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-7] == 3 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-6] == 4 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-5] == 5 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-4] == 6 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-3] == 7 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-2] == 8 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-1] == 0:
                            if Sbulundu.sonuc[Sbulundu.sonuc.shape[0] - 9] == 1 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 17] == 2 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 16] == 3 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 15] == 4 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 14] == 5 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 13] == 6 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 12] == 7 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 11] == 8 and Sbulundu.sonuc[Sbulundu.sonuc.shape[0] - 10] == 0:
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 9, Sbulundu.sonuc.shape[0] - 8,
                                                            Sbulundu.sonuc.shape[0] - 7, Sbulundu.sonuc.shape[0] - 6,
                                                            Sbulundu.sonuc.shape[0] - 5, Sbulundu.sonuc.shape[0] - 4,
                                                            Sbulundu.sonuc.shape[0] - 3, Sbulundu.sonuc.shape[0] - 2,
                                                            Sbulundu.sonuc.shape[0] - 1])
                        else:
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc, [Sbulundu.sonuc.shape[0]-9, Sbulundu.sonuc.shape[0]-8,
                                                                    Sbulundu.sonuc.shape[0]-7, Sbulundu.sonuc.shape[0]-6,
                                                                    Sbulundu.sonuc.shape[0]-5, Sbulundu.sonuc.shape[0]-4,
                                                                    Sbulundu.sonuc.shape[0]-3, Sbulundu.sonuc.shape[0]-2,
                                                                    Sbulundu.sonuc.shape[0]-1])
            if self.up and Sbulundu.count == 0:
                self.up.DFS(Sbulundu)
                #print(self.data)
                if self.up.data != 'YOK':
                    if compera(self.up.data) == 0:
                        Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.up.data)
                        Sbulundu.count = Sbulundu.count + 1
                        print('Bulundu.')
                        print(self.up.data)
                        print('-')
                        #return Sbulundu.sonuc
                    else:
                        #print(self.data)
                        #Sbulundu.sonuc = np.delete(Sbulundu.sonuc, self.data)
                        if Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-9] == 1 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-8] == 2 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-7] == 3 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-6] == 4 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-5] == 5 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-4] == 6 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-3] == 7 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-2] == 8 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-1] == 0:
                            if Sbulundu.sonuc[Sbulundu.sonuc.shape[0] - 9] == 1 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 17] == 2 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 16] == 3 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 15] == 4 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 14] == 5 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 13] == 6 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 12] == 7 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 11] == 8 and Sbulundu.sonuc[Sbulundu.sonuc.shape[0] - 10] == 0:
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 9, Sbulundu.sonuc.shape[0] - 8,
                                                            Sbulundu.sonuc.shape[0] - 7, Sbulundu.sonuc.shape[0] - 6,
                                                            Sbulundu.sonuc.shape[0] - 5, Sbulundu.sonuc.shape[0] - 4,
                                                            Sbulundu.sonuc.shape[0] - 3, Sbulundu.sonuc.shape[0] - 2,
                                                            Sbulundu.sonuc.shape[0] - 1])
                        else:
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc, [Sbulundu.sonuc.shape[0]-9, Sbulundu.sonuc.shape[0]-8,
                                                                    Sbulundu.sonuc.shape[0]-7, Sbulundu.sonuc.shape[0]-6,
                                                                    Sbulundu.sonuc.shape[0]-5, Sbulundu.sonuc.shape[0]-4,
                                                                    Sbulundu.sonuc.shape[0]-3, Sbulundu.sonuc.shape[0]-2,
                                                                    Sbulundu.sonuc.shape[0]-1])
            if self.down and Sbulundu.count == 0:
                self.down.DFS(Sbulundu)
                #print(self.data)
                if self.down.data != 'YOK':
                    if compera(self.down.data) == 0:
                        Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.down.data)
                        Sbulundu.count = Sbulundu.count + 1
                        print('Bulundu.')
                        print(self.down.data)
                        print('-')
                        #return Sbulundu.sonuc
                    else:
                        #print(self.data)
                        #Sbulundu.sonuc = np.delete(Sbulundu.sonuc, self.data)
                        if Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-9] == 1 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-8] == 2 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-7] == 3 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-6] == 4 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-5] == 5 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-4] == 6 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-3] == 7 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-2] == 8 and  Sbulundu.sonuc[Sbulundu.sonuc.shape[0]-1] == 0:
                            if Sbulundu.sonuc[Sbulundu.sonuc.shape[0] - 9] == 1 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 17] == 2 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 16] == 3 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 15] == 4 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 14] == 5 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 13] == 6 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 12] == 7 and Sbulundu.sonuc[
                                Sbulundu.sonuc.shape[0] - 11] == 8 and Sbulundu.sonuc[Sbulundu.sonuc.shape[0] - 10] == 0:
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 9, Sbulundu.sonuc.shape[0] - 8,
                                                            Sbulundu.sonuc.shape[0] - 7, Sbulundu.sonuc.shape[0] - 6,
                                                            Sbulundu.sonuc.shape[0] - 5, Sbulundu.sonuc.shape[0] - 4,
                                                            Sbulundu.sonuc.shape[0] - 3, Sbulundu.sonuc.shape[0] - 2,
                                                            Sbulundu.sonuc.shape[0] - 1])
                        else:
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc, [Sbulundu.sonuc.shape[0]-9, Sbulundu.sonuc.shape[0]-8,
                                                                    Sbulundu.sonuc.shape[0]-7, Sbulundu.sonuc.shape[0]-6,
                                                                    Sbulundu.sonuc.shape[0]-5, Sbulundu.sonuc.shape[0]-4,
                                                                    Sbulundu.sonuc.shape[0]-3, Sbulundu.sonuc.shape[0]-2,
                                                                    Sbulundu.sonuc.shape[0]-1])

            # if not self.left and not self.right and not self.up and not self.down and  Sbulundu.count == 0:
            #     Sbulundu.sonuc = np.delete(Sbulundu.sonuc, self.data)


    def BFS(self, Sbulundu, dir = ''):
        if self.data != 'YOK':
            #print(Sbulundu.sonuc)
            if self.left and self.left.data != 'YOK':
                #print(self.left.data)
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.left.data)
                if compera(self.left.data) == 0:
                    Sbulundu.countBFS += 1
            if self.right and self.right.data != 'YOK':
                #print(self.right.data)
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.right.data)
                if compera(self.right.data) == 0:
                    Sbulundu.countBFS += 1
            if self.up and self.up.data != 'YOK':
                #print(self.up.data)
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.up.data)
                if compera(self.up.data) == 0:
                    Sbulundu.countBFS += 1
            if self.down and self.down.data != 'YOK':
                #print(self.down.data)
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.down.data)
                if compera(self.down.data) == 0:
                    Sbulundu.countBFS += 1

            if self.left and Sbulundu.countBFS == 0:
                self.left.BFS(Sbulundu, dir='left')
            if self.right and Sbulundu.countBFS == 0:
                self.right.BFS(Sbulundu, dir='right')
            if self.up and Sbulundu.countBFS == 0:
                self.up.BFS(Sbulundu, dir='up')
            if self.down and Sbulundu.countBFS == 0:
                self.down.BFS(Sbulundu, dir='down')

            tempdir = ''
            if self.left and self.left.data != "YOK":
                if compera(self.left.data) == 0:
                    print("Bulundu.")
                    print(self.left.data)
                    print("-")
                    tempdir = dir
                    #print("Dir : ", Sbulundu.dir)
                    Sbulundu.count = Sbulundu.count + 1
                else:
                    if Sbulundu.count == 0:
                        #print("left else s\n", Sbulundu.sonuc)
                        if (self.down.data != 'YOK') and (self.up.data != 'YOK') and (self.right.data != 'YOK'):
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 36, Sbulundu.sonuc.shape[0] - 35,
                                                        Sbulundu.sonuc.shape[0] - 34, Sbulundu.sonuc.shape[0] - 33,
                                                        Sbulundu.sonuc.shape[0] - 32, Sbulundu.sonuc.shape[0] - 31,
                                                        Sbulundu.sonuc.shape[0] - 30, Sbulundu.sonuc.shape[0] - 29,
                                                        Sbulundu.sonuc.shape[0] - 28])
                        elif (self.down.data != 'YOK' or self.up.data != 'YOK') and (self.right.data != 'YOK'):
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 27, Sbulundu.sonuc.shape[0] - 26,
                                                        Sbulundu.sonuc.shape[0] - 25, Sbulundu.sonuc.shape[0] - 24,
                                                        Sbulundu.sonuc.shape[0] - 23, Sbulundu.sonuc.shape[0] - 22,
                                                        Sbulundu.sonuc.shape[0] - 21, Sbulundu.sonuc.shape[0] - 20,
                                                        Sbulundu.sonuc.shape[0] - 19])
                        elif (self.down.data != 'YOK') and (self.up.data != 'YOK' or self.right.data != 'YOK'):
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 27, Sbulundu.sonuc.shape[0] - 26,
                                                        Sbulundu.sonuc.shape[0] - 25, Sbulundu.sonuc.shape[0] - 24,
                                                        Sbulundu.sonuc.shape[0] - 23, Sbulundu.sonuc.shape[0] - 22,
                                                        Sbulundu.sonuc.shape[0] - 21, Sbulundu.sonuc.shape[0] - 20,
                                                        Sbulundu.sonuc.shape[0] - 19])
                        elif (self.down.data != 'YOK') or (self.up.data != 'YOK') or (self.right.data != 'YOK'):
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 18, Sbulundu.sonuc.shape[0] - 17,
                                                        Sbulundu.sonuc.shape[0] - 16, Sbulundu.sonuc.shape[0] - 15,
                                                        Sbulundu.sonuc.shape[0] - 14, Sbulundu.sonuc.shape[0] - 13,
                                                        Sbulundu.sonuc.shape[0] - 12, Sbulundu.sonuc.shape[0] - 11,
                                                        Sbulundu.sonuc.shape[0] - 10])
                        else:
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 9, Sbulundu.sonuc.shape[0] - 8,
                                                        Sbulundu.sonuc.shape[0] - 7, Sbulundu.sonuc.shape[0] - 6,
                                                        Sbulundu.sonuc.shape[0] - 5, Sbulundu.sonuc.shape[0] - 4,
                                                        Sbulundu.sonuc.shape[0] - 3, Sbulundu.sonuc.shape[0] - 2,
                                                        Sbulundu.sonuc.shape[0] - 1])
                        #print("left else e\n", Sbulundu.sonuc)
                    else:
                        if Sbulundu.dir != 'left':
                            #print("left")
                            #print("left else s\n", Sbulundu.sonuc)
                            if (self.down.data != 'YOK') and (self.up.data != 'YOK') and (self.right.data != 'YOK'):
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 36 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 35 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 34 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 33 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 32 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 31 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 30 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 29 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 28 - Sbulundu.back])
                            elif (self.down.data != 'YOK' or self.up.data != 'YOK') and (self.right.data != 'YOK'):
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 27 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 26 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 25 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 24 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 23 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 22 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 21 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 20 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 19 - Sbulundu.back])
                            elif (self.down.data != 'YOK') and (self.up.data != 'YOK' or self.right.data != 'YOK'):
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 27 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 26 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 25 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 24 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 23 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 22 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 21 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 20 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 19 - Sbulundu.back])
                            elif (self.down.data != 'YOK') or (self.up.data != 'YOK') or (self.right.data != 'YOK'):
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 18 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 17 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 16 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 15 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 14 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 13 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 12 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 11 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 10 - Sbulundu.back])
                            else:
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 9 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 8 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 7 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 6 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 5 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 4 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 3 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 2 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 1 - Sbulundu.back])
                            #print("left else e\n", Sbulundu.sonuc)
                            if Sbulundu.artıs and self.right.data == "YOK" and self.up.data == "YOK" and self.down.data == "YOK":
                                Sbulundu.artıs = False
                                #print("Left ", Sbulundu.artıs)
                                Sbulundu.back += 9
                        else:
                            tempdir = dir
                            #print("Dir : ", Sbulundu.dir)
                            if self.right.data == "YOK" and self.up.data == "YOK" and self.down.data == "YOK":
                                Sbulundu.back += 9
                            else:
                                Sbulundu.artıs = True
                                #print("Left ", Sbulundu.artıs)
            if self.right and self.right.data != "YOK":
                if compera(self.right.data) == 0:
                    print("Bulundu.")
                    print(self.right.data)
                    print("-")
                    tempdir = dir
                    #print("Dir : ", Sbulundu.dir)
                    Sbulundu.count = Sbulundu.count + 1
                else:
                    if Sbulundu.count == 0:
                        #print("right else s\n", Sbulundu.sonuc)
                        if (self.down.data != 'YOK') and (self.up.data != 'YOK'):
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 27, Sbulundu.sonuc.shape[0] - 26,
                                                        Sbulundu.sonuc.shape[0] - 25, Sbulundu.sonuc.shape[0] - 24,
                                                        Sbulundu.sonuc.shape[0] - 23, Sbulundu.sonuc.shape[0] - 22,
                                                        Sbulundu.sonuc.shape[0] - 21, Sbulundu.sonuc.shape[0] - 20,
                                                        Sbulundu.sonuc.shape[0] - 19])
                        elif (self.down.data != 'YOK') or (self.up.data != 'YOK'):
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 18, Sbulundu.sonuc.shape[0] - 17,
                                                        Sbulundu.sonuc.shape[0] - 16, Sbulundu.sonuc.shape[0] - 15,
                                                        Sbulundu.sonuc.shape[0] - 14, Sbulundu.sonuc.shape[0] - 13,
                                                        Sbulundu.sonuc.shape[0] - 12, Sbulundu.sonuc.shape[0] - 11,
                                                        Sbulundu.sonuc.shape[0] - 10])
                        else:
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 9, Sbulundu.sonuc.shape[0] - 8,
                                                        Sbulundu.sonuc.shape[0] - 7, Sbulundu.sonuc.shape[0] - 6,
                                                        Sbulundu.sonuc.shape[0] - 5, Sbulundu.sonuc.shape[0] - 4,
                                                        Sbulundu.sonuc.shape[0] - 3, Sbulundu.sonuc.shape[0] - 2,
                                                        Sbulundu.sonuc.shape[0] - 1])
                        #print("right else e\n", Sbulundu.sonuc)
                    else:
                        if Sbulundu.dir != 'right':
                            #print("right")
                            #print("right else s\n", Sbulundu.sonuc)
                            if (self.down.data != 'YOK') and (self.up.data != 'YOK'):
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 27 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 26 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 25 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 24 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 23 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 22 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 21 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 20 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 19 - Sbulundu.back])
                            elif (self.down.data != 'YOK') or (self.up.data != 'YOK'):
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 18 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 17 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 16 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 15 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 14 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 13 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 12 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 11 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 10 - Sbulundu.back])
                            else:
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 9 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 8 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 7 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 6 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 5 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 4 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 3 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 2 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 1 - Sbulundu.back])
                            #print("right else e\n", Sbulundu.sonuc)
                            if Sbulundu.artıs and self.up.data == "YOK" and self.down.data == "YOK":
                                Sbulundu.artıs = False
                                #print("Right ", Sbulundu.artıs)
                                Sbulundu.back += 9
                        else:
                            tempdir = dir
                            #print("Dir : ", Sbulundu.dir)
                            if self.up.data == "YOK" and self.down.data == "YOK":
                                Sbulundu.back += 9
                            else:
                                Sbulundu.artıs = True
                                #print("Right ", Sbulundu.artıs)
            if self.up and self.up.data != "YOK":
                if compera(self.up.data) == 0:
                    print("Bulundu.")
                    print(self.up.data)
                    print("-")
                    tempdir = dir
                    #print("Dir : ", Sbulundu.dir)
                    Sbulundu.count = Sbulundu.count + 1
                else:
                    if Sbulundu.count == 0:
                        #print("up else s\n", Sbulundu.sonuc)
                        if self.down.data != 'YOK':
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 18, Sbulundu.sonuc.shape[0] - 17,
                                                        Sbulundu.sonuc.shape[0] - 16, Sbulundu.sonuc.shape[0] - 15,
                                                        Sbulundu.sonuc.shape[0] - 14, Sbulundu.sonuc.shape[0] - 13,
                                                        Sbulundu.sonuc.shape[0] - 12, Sbulundu.sonuc.shape[0] - 11,
                                                        Sbulundu.sonuc.shape[0] - 10])
                        else:
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 9, Sbulundu.sonuc.shape[0] - 8,
                                                        Sbulundu.sonuc.shape[0] - 7, Sbulundu.sonuc.shape[0] - 6,
                                                        Sbulundu.sonuc.shape[0] - 5, Sbulundu.sonuc.shape[0] - 4,
                                                        Sbulundu.sonuc.shape[0] - 3, Sbulundu.sonuc.shape[0] - 2,
                                                        Sbulundu.sonuc.shape[0] - 1])
                        #print("up else e\n", Sbulundu.sonuc)
                    else:
                        if Sbulundu.dir != 'up':
                            #print("up")
                            if self.down.data != 'YOK':
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 18 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 17 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 16 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 15 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 14 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 13 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 12 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 11 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 10 - Sbulundu.back])
                            else:
                                Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                           [Sbulundu.sonuc.shape[0] - 9 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 8 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 7 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 6 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 5 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 4 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 3 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 2 - Sbulundu.back,
                                                            Sbulundu.sonuc.shape[0] - 1 - Sbulundu.back])
                            if Sbulundu.artıs and self.down.data == "YOK":
                                Sbulundu.artıs = False
                                #print("Up ", Sbulundu.artıs)
                                Sbulundu.back += 9
                        else:
                            tempdir = dir
                            #print("Dir : ", Sbulundu.dir)
                            if self.down.data == "YOK":
                                Sbulundu.back += 9
                            else:
                                Sbulundu.artıs = True
                                #print("Up ", Sbulundu.artıs)
            if self.down and self.down.data != "YOK":
                if compera(self.down.data) == 0:
                    print("Bulundu.")
                    print(self.down.data)
                    print("-")
                    tempdir = dir
                    #print("Dir : ", Sbulundu.dir)
                    Sbulundu.count = Sbulundu.count + 1
                else:
                    if Sbulundu.count == 0:
                        #print("down else s\n", Sbulundu.sonuc)
                        Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                   [Sbulundu.sonuc.shape[0] - 9, Sbulundu.sonuc.shape[0] - 8,
                                                    Sbulundu.sonuc.shape[0] - 7, Sbulundu.sonuc.shape[0] - 6,
                                                    Sbulundu.sonuc.shape[0] - 5, Sbulundu.sonuc.shape[0] - 4,
                                                    Sbulundu.sonuc.shape[0] - 3, Sbulundu.sonuc.shape[0] - 2,
                                                    Sbulundu.sonuc.shape[0] - 1])
                        #print("down else e\n", Sbulundu.sonuc)
                    else:
                        if Sbulundu.dir != 'down':
                            #print("down else s\n", Sbulundu.sonuc)
                            #print("Dir : ", Sbulundu.dir)
                            #print("down")
                            Sbulundu.sonuc = np.delete(Sbulundu.sonuc,
                                                       [Sbulundu.sonuc.shape[0] - 9 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 8 - Sbulundu.back,
                                                        Sbulundu.sonuc.shape[0] - 7 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 6 - Sbulundu.back,
                                                        Sbulundu.sonuc.shape[0] - 5 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 4 - Sbulundu.back,
                                                        Sbulundu.sonuc.shape[0] - 3 - Sbulundu.back, Sbulundu.sonuc.shape[0] - 2 - Sbulundu.back,
                                                        Sbulundu.sonuc.shape[0] - 1 - Sbulundu.back])
                            #print("down else e\n", Sbulundu.sonuc)
                            #Sbulundu.back += 9
                            if Sbulundu.artıs:
                                Sbulundu.artıs = False
                                #print("Down ", Sbulundu.artıs)
                                Sbulundu.back += 9
                        else:
                            tempdir = dir
                            #print("Dir : ", Sbulundu.dir)
                            Sbulundu.back += 9

            #print(Sbulundu.artıs)
            Sbulundu.dir = tempdir

    def FindSolution(self, Sbulundu, dir = ''):
        if self.data != 'YOK':
            Sbulundu.solutionlist[Sbulundu.count].append(dir)
            #print(Sbulundu.solutionlist)
            if self.left:
                self.left.FindSolution(Sbulundu, dir='left')
                if self.left.data != 'YOK':
                    if compera(self.left.data) == 0:
                        Sbulundu.count = Sbulundu.count + 1
                        # print('Bulundu.')
                        # print(self.left.data)
                        # print('-')
                        ### burada dizinin ilk boyu bitecek ve şu ana kadar ki değerler en son değer hariç diğer boyuta aktarılacak
                        Sbulundu.solutionlist.append([])
                        for i in range(0, len(Sbulundu.solutionlist[Sbulundu.count - 1]) - 1):
                            Sbulundu.solutionlist[Sbulundu.count].append(Sbulundu.solutionlist[Sbulundu.count - 1][i])

                    else:
                        Sbulundu.solutionlist[Sbulundu.count].pop(len(Sbulundu.solutionlist[Sbulundu.count])-1)

            if self.right:
                self.right.FindSolution(Sbulundu, dir='right')
                if self.right.data != 'YOK':
                    if compera(self.right.data) == 0:
                        Sbulundu.count = Sbulundu.count + 1
                        # print('Bulundu.')
                        # print(self.right.data)
                        # print('-')
                        Sbulundu.solutionlist.append([])
                        for i in range(0, len(Sbulundu.solutionlist[Sbulundu.count - 1]) - 1):
                            Sbulundu.solutionlist[Sbulundu.count].append(Sbulundu.solutionlist[Sbulundu.count - 1][i])
                    else:
                        Sbulundu.solutionlist[Sbulundu.count].pop(len(Sbulundu.solutionlist[Sbulundu.count]) - 1)
            if self.up:
                self.up.FindSolution(Sbulundu, dir='up')
                if self.up.data != 'YOK':
                    if compera(self.up.data) == 0:
                        Sbulundu.count = Sbulundu.count + 1
                        # print('Bulundu.')
                        # print(self.up.data)
                        # print('-')
                        Sbulundu.solutionlist.append([])
                        for i in range(0, len(Sbulundu.solutionlist[Sbulundu.count - 1]) - 1):
                            Sbulundu.solutionlist[Sbulundu.count].append(Sbulundu.solutionlist[Sbulundu.count - 1][i])
                    else:
                        Sbulundu.solutionlist[Sbulundu.count].pop(len(Sbulundu.solutionlist[Sbulundu.count]) - 1)

            if self.down:
                self.down.FindSolution(Sbulundu, dir='down')
                if self.down.data != 'YOK':
                    if compera(self.down.data) == 0:
                        Sbulundu.count = Sbulundu.count + 1
                        # print('Bulundu.')
                        # print(self.down.data)
                        # print('-')
                        Sbulundu.solutionlist.append([])
                        for i in range(0, len(Sbulundu.solutionlist[Sbulundu.count - 1]) - 1):
                            Sbulundu.solutionlist[Sbulundu.count].append(Sbulundu.solutionlist[Sbulundu.count - 1][i])
                    else:
                        Sbulundu.solutionlist[Sbulundu.count].pop(len(Sbulundu.solutionlist[Sbulundu.count]) - 1)

    def PutHeuristic(self, Sbulundu, list, dir = ''):
        if self.data != 'YOK':

            minLeft = 999990
            minRight = 999990
            minUp = 999990
            minDown = 999990
            index = 999990
            Leftlist = []
            Leftlist.append([])
            Rightlist = []
            Rightlist.append([])
            Uplist = []
            Uplist.append([])
            Downlist = []
            Downlist.append([])
            Sbulundu.Leftlistcount = 0
            Sbulundu.Rightlistcount = 0
            Sbulundu.Uplistcount = 0
            Sbulundu.Downlistcount = 0

            if self.left and self.left.data != 'YOK':
                #print(self.left.data)
                if self.Heuristic != 999990:
                    if self.Heuristic == 999999:
                        for i in range(0, len(Sbulundu.solutionlist)):
                            try:
                                if Sbulundu.solutionlist[i][1] == 'left':
                                    for j in range(2, len(Sbulundu.solutionlist[i])):
                                        Leftlist[Sbulundu.Leftlistcount].append(Sbulundu.solutionlist[i][j])
                                    Leftlist.append([])
                                    Sbulundu.Leftlistcount += 1
                                    if len(Sbulundu.solutionlist[i]) < minLeft:
                                        minLeft = len(Sbulundu.solutionlist[i])
                                        index = i
                            except:
                                Sbulundu.countWarning += 1
                        self.left.Heuristic = minLeft
                        #print("Left1 Heuristic : ", minLeft)
                    else:
                        for i in range(0, len(list)):
                            try:
                                if list[i][0] == 'left':
                                    if len(list[i]) > 0:
                                        for j in range(1, len(list[i])):
                                            Leftlist[Sbulundu.Leftlistcount].append(list[i][j])
                                        Leftlist.append([])
                                        Sbulundu.Leftlistcount += 1
                                    if len(list[i]) < minLeft:
                                        minLeft = len(list[i])
                                        index = i
                            except:
                                Sbulundu.countWarning += 1
                        self.left.Heuristic = minLeft
                        #print("Left2 Heuristic : ", minLeft)
                else:
                    self.left.Heuristic = minLeft
                    #print("Left3 Heuristic : ", minLeft)
            if self.right and self.right.data != 'YOK':
                #print(self.right.data)
                if self.Heuristic != 999990:
                    if self.Heuristic == 999999:
                        for i in range(0, len(Sbulundu.solutionlist)):
                            try:
                                if Sbulundu.solutionlist[i][1] == 'right':
                                    for j in range(2, len(Sbulundu.solutionlist[i])):
                                        Rightlist[Sbulundu.Rightlistcount].append(Sbulundu.solutionlist[i][j])
                                    Rightlist.append([])
                                    Sbulundu.Rightlistcount += 1
                                    if len(Sbulundu.solutionlist[i]) < minRight:
                                        minRight = len(Sbulundu.solutionlist[i])
                                        index = i
                            except:
                                Sbulundu.countWarning += 1
                        self.right.Heuristic = minRight
                        #print("Right1 Heuristic : ", minRight)
                    else:
                        for i in range(0, len(list)):
                            try:
                                if list[i][0] == 'right':
                                    if len(list[i]) > 0:
                                        for j in range(1, len(list[i])):
                                            Rightlist[Sbulundu.Rightlistcount].append(list[i][j])
                                        Rightlist.append([])
                                        Sbulundu.Rightlistcount += 1
                                    if len(list[i]) < minRight:
                                        minRight = len(list[i])
                                        index = i
                            except:
                                Sbulundu.countWarning += 1
                        self.right.Heuristic = minRight
                        #print("Right2 Heuristic : ", minRight)
                else:
                    self.right.Heuristic = minRight
                    #print("Right3 Heuristic : ", minRight)
            if self.up and self.up.data != 'YOK':
                #print(self.up.data)
                if self.Heuristic != 999990:
                    if self.Heuristic == 999999:
                        for i in range(0, len(Sbulundu.solutionlist)):
                            try:
                                if Sbulundu.solutionlist[i][1] == 'up':
                                    for j in range(2, len(Sbulundu.solutionlist[i])):
                                        Uplist[Sbulundu.Uplistcount].append(Sbulundu.solutionlist[i][j])
                                    Uplist.append([])
                                    Sbulundu.Uplistcount += 1
                                    if len(Sbulundu.solutionlist[i]) < minUp:
                                        minUp = len(Sbulundu.solutionlist[i])
                                        index = i
                            except:
                                Sbulundu.countWarning += 1
                        self.up.Heuristic = minUp
                        #print("Up1 Heuristic : ", minUp)
                    else:
                        for i in range(0, len(list)):
                            try:
                                if list[i][0] == 'up':
                                    if len(list[i]) > 0:
                                        for j in range(1, len(list[i])):
                                            Uplist[Sbulundu.Uplistcount].append(list[i][j])
                                        Uplist.append([])
                                        Sbulundu.Uplistcount += 1
                                    if len(list[i]) < minUp:
                                        minUp = len(list[i])
                                        index = i
                            except:
                                Sbulundu.countWarning += 1
                        self.up.Heuristic = minUp
                        #print("Up2 Heuristic : ", minUp)
                else:
                    self.up.Heuristic = minUp
                    #print("Up3 Heuristic : ", minUp)
            if self.down and self.down.data != 'YOK':
                #print(self.down.data)
                if self.Heuristic != 999990:
                    if self.Heuristic == 999999:
                        for i in range(0, len(Sbulundu.solutionlist)):
                            try:
                                if Sbulundu.solutionlist[i][1] == 'down':
                                    for j in range(2, len(Sbulundu.solutionlist[i])):
                                        Downlist[Sbulundu.Downlistcount].append(Sbulundu.solutionlist[i][j])
                                    Downlist.append([])
                                    Sbulundu.Downlistcount += 1
                                    if len(Sbulundu.solutionlist[i]) < minDown:
                                        minDown = len(Sbulundu.solutionlist[i])
                                        index = i
                            except:
                                Sbulundu.countWarning += 1
                        self.down.Heuristic = minDown
                        #print("Down1 Heuristic : ", minDown)
                    else:
                        for i in range(0, len(list)):
                            try:
                                if list[i][0] == 'down':
                                    if len(list[i]) > 0:
                                        for j in range(1, len(list[i])):
                                            Downlist[Sbulundu.Downlistcount].append(list[i][j])
                                        Downlist.append([])
                                        Sbulundu.Downlistcount += 1
                                    if len(list[i]) < minDown:
                                        minDown = len(list[i])
                                        index = i
                            except:
                                Sbulundu.countWarning += 1
                        self.down.Heuristic = minDown
                        #print("Down2 Heuristic : ", minDown)
                else:
                    self.down.Heuristic = minDown
                    #print("Down3 Heuristic : ", minDown)

            if self.left:
                self.left.PutHeuristic(Sbulundu, Leftlist, dir='left')
            if self.right:
                self.right.PutHeuristic(Sbulundu, Rightlist, dir='right')
            if self.up:
                self.up.PutHeuristic(Sbulundu, Uplist, dir='up')
            if self.down:
                self.down.PutHeuristic(Sbulundu, Downlist, dir='down')

    def Astar(self, Sbulundu, dir = ''):
        if self.data != 'YOK':

            LeftHeuristic = 999990
            RightHeuristic = 999990
            UpHeuristic = 999990
            DownHeuristic = 999990

            if self.left and self.left.data != 'YOK':
                #Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.left.data)
                LeftHeuristic = self.left.Heuristic
                #print("LeftHeuristic : ", LeftHeuristic)
            if self.right and self.right.data != 'YOK':
                #Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.right.data)
                RightHeuristic = self.right.Heuristic
                #print("RightHeuristic : ", RightHeuristic)
            if self.up and self.up.data != 'YOK':
                #Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.up.data)
                UpHeuristic = self.up.Heuristic
                #print("UpHeuristic : ", UpHeuristic)
            if self.down and self.down.data != 'YOK':
                #Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.down.data)
                DownHeuristic = self.down.Heuristic
                #print("DownHeuristic : ", DownHeuristic)

            mindir = ''

            if LeftHeuristic <= RightHeuristic and LeftHeuristic <= DownHeuristic and LeftHeuristic <= UpHeuristic:
                mindir = 'left'
            elif RightHeuristic <= LeftHeuristic and RightHeuristic <= DownHeuristic and RightHeuristic <= UpHeuristic:
                mindir = 'right'
            elif UpHeuristic <= LeftHeuristic and UpHeuristic <= RightHeuristic and UpHeuristic <= DownHeuristic:
                mindir = 'up'
            elif DownHeuristic <= LeftHeuristic and DownHeuristic <= RightHeuristic and DownHeuristic <= UpHeuristic :
                mindir = 'down'

            # print(mindir)
            # print("LeftHeuristic : ", LeftHeuristic)
            # print("RightHeuristic : ", RightHeuristic)
            # print("UpHeuristic : ", UpHeuristic)
            # print("DownHeuristic : ", DownHeuristic)

            if self.left and Sbulundu.countBFS == 0 and mindir == 'left' and self.left.data != 'YOK':
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.left.data)
                if compera(self.left.data) == 0:
                    Sbulundu.countBFS += 1
                self.left.Astar(Sbulundu, dir='left')
            if self.right and Sbulundu.countBFS == 0 and mindir == 'right' and self.right.data != 'YOK':
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.right.data)
                if compera(self.right.data) == 0:
                    Sbulundu.countBFS += 1
                self.right.Astar(Sbulundu, dir='right')
            if self.up and Sbulundu.countBFS == 0 and mindir == 'up' and self.up.data != 'YOK':
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.up.data)
                if compera(self.up.data) == 0:
                    Sbulundu.countBFS += 1
                self.up.Astar(Sbulundu, dir='up')
            if self.down and Sbulundu.countBFS == 0 and mindir == 'down' and self.down.data != 'YOK':
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, self.down.data)
                if compera(self.down.data) == 0:
                    Sbulundu.countBFS += 1
                self.down.Astar(Sbulundu, dir='down')


    def CreateTree(self, data, sayac, Sbulundu, Level, dirCreate=''):
        #print(self.data)
        sayac += 1
        list = data
        for j in range(0, list.shape[0]):
            for k in range(0, list.shape[1]):
                if list[j][k] == 0:
                    x = k
                    y = j
        templist = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        kilit0 = True
        kilit1 = True
        kilit2 = True
        kilit3 = True
        for n in range(0, 4):
            kilit = True
            Left = False
            Rigth = False
            Up = False
            Down = False
            for j in range(0, list.shape[0]):
                for k in range(0, list.shape[1]):
                    if k == x - 1 and j == y and kilit and kilit0:
                        # print(1)
                        kilit = False
                        kilit0 = False
                        Left = True
                        templist[j][k] = 0
                        templist[j][k + 1] = list[j][k]
                    elif k == x + 1 and j == y and kilit and kilit1:
                        kilit = False
                        kilit1 = False
                        Rigth = True
                        templist[j][k] = 0
                        templist[j][k - 1] = list[j][k]
                    elif j == y - 1 and k == x and kilit and kilit2:
                        # print(3)
                        kilit = False
                        kilit2 = False
                        Up = True
                        templist[j][k] = 0
                        templist[j + 1][k] = list[j][k]
                    elif j == y + 1 and k == x and kilit and kilit3:
                        # print(4)
                        kilit = False
                        kilit3 = False
                        Down = True
                        templist[j][k] = 0
                        templist[j - 1][k] = list[j][k]
                    else:
                        if list[j][k] != 0:
                            templist[j][k] = list[j][k]

            if Left and not kilit:
                if dirCreate != 'right':
                    temptemp = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                    for j in range(0, list.shape[0]):
                        for k in range(0, list.shape[1]):
                            temptemp[j][k] = templist[j][k]
                    self.insert(temptemp, 0, dir='left')
                    #print(temptemp)
                    if compera(temptemp) == 0:
                        # print('bitti0')
                        # print(temptemp)
                        Sbulundu.countTree = Sbulundu.countTree + 1
                else:
                    self.insert('YOK', 0, dir='left')
            elif Rigth and not kilit:
                if dirCreate != 'left':
                    temptemp = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                    for j in range(0, list.shape[0]):
                        for k in range(0, list.shape[1]):
                            temptemp[j][k] = templist[j][k]
                    self.insert(temptemp, 1, dir='right')
                    #print(temptemp)
                    if compera(temptemp) == 0:
                        # print('bitti1')
                        # print(temptemp)
                        Sbulundu.countTree = Sbulundu.countTree + 1
                else:
                    self.insert('YOK', 1, dir='right')
            elif Up and not kilit:
                if dirCreate != 'down':
                    temptemp = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                    for j in range(0, list.shape[0]):
                        for k in range(0, list.shape[1]):
                            temptemp[j][k] = templist[j][k]
                    self.insert(temptemp, 2, dir='up')
                    #print(temptemp)
                    if compera(temptemp) == 0:
                        # print('bitti2')
                        # print(temptemp)
                        Sbulundu.countTree = Sbulundu.countTree + 1
                else:
                    self.insert('YOK', 2, dir='up')
            elif Down and not kilit:
                if dirCreate != 'up':
                    temptemp = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                    for j in range(0, list.shape[0]):
                        for k in range(0, list.shape[1]):
                            temptemp[j][k] = templist[j][k]
                    self.insert(temptemp, 3, dir='down')
                    #print(temptemp)
                    if compera(temptemp) == 0:
                        # print('bitti3')
                        # print(temptemp)
                        Sbulundu.countTree = Sbulundu.countTree + 1
                else:
                    self.insert('YOK', 3, dir='down')

            # print(list)
            # print(templist)

        if kilit0:
            self.insert('YOK', 0)
        if kilit1:
            self.insert('YOK', 1)
        if kilit2:
            self.insert('YOK', 2)
        if kilit3:
            self.insert('YOK', 3)

        threshold = Level

        if self.left.data != 'YOK' and sayac < threshold:
            self.left.CreateTree(self.left.data, sayac, Sbulundu, Level, dirCreate='left')
        if self.right.data != 'YOK' and sayac < threshold:
            self.right.CreateTree(self.right.data, sayac, Sbulundu, Level, dirCreate='right')
        if self.up.data != 'YOK' and sayac < threshold:
            self.up.CreateTree(self.up.data, sayac, Sbulundu, Level, dirCreate='up')
        if self.down.data != 'YOK' and sayac < threshold:
            self.down.CreateTree(self.down.data, sayac, Sbulundu, Level, dirCreate='down')

# Use the insert method to add nodes

# list = np.array([[3, 6, 0], [1, 4, 2], [7, 5, 8]])
# list = np.array([[1, 2, 0], [4, 5, 3], [7, 8, 6]])
# list = np.array([[0, 1, 2], [4, 5, 3], [7, 8, 6]])

if False:
    print("Bu Ornek Sirali.")
else:
    list = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    zero = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    print("Çıkmak için x tuşuna basınız.")
    print("Lütfen sadece integer değerler kullanınız.")
    print("Örnek giriş: 123456780")
    print("Bu girişin anlamı aşağıdaki gibidir.\n[[1 2 3\n  4 5 6\n  7 8 0]]")
    while True:
        number = input("Lütfen 8-Puzzle matrisini giriniz.\n")
        if number == 'x':
            break
        else:
            try:
                if number.__len__() == 9:
                    index = 0
                    for j in range(0, list.shape[0]):
                        for k in range(0, list.shape[1]):
                            list[j][k] = number[index]
                            index += 1
                    break
                else:
                    print("Uzunluğu kontrol ediniz.")
            except:
                print("Hatalı giriş yaptınız, lütfen tekrar deneyiniz.")
    if compera(list)==0:
        print("Bu Ornek Sirali.")
    else:
        root = Node(list)
        MaxCount = -1
        while True:
            LevelTemp = input("Lütfen maximum hamle sayısını giriniz.\nTahmini süre 20 hamle için maximum 43 saniye.\n"
                              "Tahmini süre 15 hamle için maximum 3 saniye.\n")
            Level = int(LevelTemp)
            if type(Level) is int:
                break
            else:
                print("Hatalı giriş yaptınız, lütfen tekrar deneyiniz.")
            if LevelTemp == 'x':
                break
        Sbulundu = StaticVariable()
        tstart = datetime.now()
        root.CreateTree(list, MaxCount, Sbulundu, Level)
        root.FindSolution(Sbulundu)
        Sbulundu.count = 0
        Sbulundu.countTree = 0
        Sbulundu.sonuc = zero
        root.PutHeuristic(Sbulundu, [])
        tend = datetime.now()
        # print(Sbulundu.solutionlist)
        # print(root.left.Heuristic)
        # print(root.left.left.Heuristic)
        # print(root.down.Heuristic)
        # print(root.down.left.Heuristic)
        # print(root.down.down.Heuristic)
        print("Ağaç oluştuma süresi :", tend-tstart)
        print("Örnek arama algoritmaları aşağıdaki gibidir.\n DFS, BFS, A*")
        Sbulundu.count = 0
        Sbulundu.countTree = 0
        Sbulundu.sonuc = zero
        while True:
            Arama = input("Lütfen arama algoritmasını giriniz.\n")
            if Arama.lower() == 'dfs':
                print("Arama algoritması DFS.\nMatris :\n", list)
                print("Cozum Aranıyor...")
                tstart0 = datetime.now()
                root.DFS(Sbulundu)
                tend0 = datetime.now()
                Sbulundu.sonuc = np.delete(Sbulundu.sonuc, [0, 1, 2, 3, 4, 5, 6, 7, 8])
                sonucgoster(Sbulundu.sonuc)
                Sbulundu.count = 0
                Sbulundu.countTree = 0
                Sbulundu.sonuc = zero
                Sbulundu.countBFS = 0
                Sbulundu.dir = ''
                Sbulundu.artıs = False
                Sbulundu.solutionlist = ''
                print("Bulunma süresi :", tend0 - tstart0)
                print("Program Bitti.")
            elif Arama.lower() == 'bfs':
                print("Arama algoritması BFS.\nMatris :\n", list)
                print("Cozum Aranıyor...")
                tstart1 = datetime.now()
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, list)
                root.BFS(Sbulundu)
                tend1 = datetime.now()
                Sbulundu.sonuc = np.delete(Sbulundu.sonuc, [0, 1, 2, 3, 4, 5, 6, 7, 8])
                sonucgoster(Sbulundu.sonuc)
                Sbulundu.count = 0
                Sbulundu.countTree = 0
                Sbulundu.sonuc = zero
                Sbulundu.countBFS = 0
                Sbulundu.dir = ''
                Sbulundu.artıs = False
                Sbulundu.back = 9
                Sbulundu.solutionlist = ''
                print("Bulunma süresi :", tend1 - tstart1)
                print("Program Bitti.")
            elif Arama.lower() == 'a*' or Arama.lower() == 'astar':
                print("Arama algoritması A*.\nMatris :\n", list)
                print("Cozum Aranıyor...")
                tstart1 = datetime.now()
                Sbulundu.sonuc = np.append(Sbulundu.sonuc, list)
                root.Astar(Sbulundu)
                tend1 = datetime.now()
                Sbulundu.sonuc = np.delete(Sbulundu.sonuc, [0, 1, 2, 3, 4, 5, 6, 7, 8])
                sonucgoster(Sbulundu.sonuc)
                Sbulundu.count = 0
                Sbulundu.countTree = 0
                Sbulundu.sonuc = zero
                Sbulundu.Leftlistcount = 0
                Sbulundu.Rightlistcount = 0
                Sbulundu.Uplistcount = 0
                Sbulundu.Downlistcount = 0
                Sbulundu.solutionlist = []
                Sbulundu.countBFS = 0
                Sbulundu.dir = ''
                Sbulundu.artıs = False
                print("Bulunma süresi :", tend1 - tstart1)
                print("Program Bitti.")
            elif Arama == 'x':
                break
            else:
                print("Hatalı giriş")


