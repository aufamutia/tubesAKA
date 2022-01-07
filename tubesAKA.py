from tkinter import *
import random
import time

root = Tk()
root.title('Sort Visualization InsertionSort ShellSort')
root.maxsize(1080,720)
root.config (bg='white')

data1 = []
data2 = []
time_start = time.time()

def insertionSort(arr, drawArr,canvas):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            drawArr(arr, ['green' if x == j or x == j+1 else 'red' for x in range(len(arr))], canvas)
            updateTime(timer1,time_start)
        arr[j+1] = key
        drawArr(arr, ['green' for x in range(len(arr))], canvas)       


def shellSort(data,drawArr,canvas): 
    global time_start
    time_start = time.time()  
    gap = len(data) // 2

    while gap > 0:
        for i in range(gap,len(data)):
            tmp = data[i]
            j = i
            while j >= gap and data[j-gap] > tmp:
                data[j] = data[j-gap]
                drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
                updateTime(timer2,time_start)
                j -= gap
            data[j] = tmp
        gap //= 2
    drawArr(data, ['green' for x in range(len(data))], canvas)
    
def updateTime(timeLabel,startTime):
    timeLabel.config(text=time.time() - time_start)

def drawArr(data, color, canvas):
    canvas.delete("all")
    c_width = 336
    c_height = 380
    x_width = c_width / (len(data) + 1)
    offset = 10
    space = 5
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        
        x0 = i * x_width + offset + space
        y0 = c_height - height * 336
       
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i], outline=color[i])

    root.update_idletasks()


def generateArr():
    global data1
    global data2
    data1 = []  
    data2 = []
    

    size = int(sizeInput.get())
    for _ in range(size):
        data1.append(random.randrange(5, 100))
    data2[:] = data1[:]
    drawArr(data1,['white' for x in range(len(data1))],canvas1)
    drawArr(data2,['white' for x in range(len(data2))],canvas2)

def startAlgo():
    global data1
    global data2

    shell_sort(data2, drawArr, canvas2)
    insertionSort(data1, drawArr,canvas1)


Label(root,text="Insertion Sort",bg='white').grid(row=0,column=0)
Label(root,text="Shell Sort",bg='white').grid(row=0,column=1)

canvas1 = Canvas(root, width=340, height=380, bg = 'black')
canvas1.grid(row=1, column=0, padx=10, pady=10)

canvas2 = Canvas(root, width=340, height=380, bg = 'black')
canvas2.grid(row=1, column=1, padx=10, pady=10)

buttonsFrame = Frame(root, width = 720, height = 50, bg ='white')
buttonsFrame.grid(row = 1, column=2, padx =10, pady=10)

labelFrame1 = Frame(root, width = 720, height = 50, bg='white')
labelFrame1.grid(row= 2,column=0, padx=20,pady=20)
Label(labelFrame1,text="Time (seconds):",bg='white').grid(row=1,column=0)
timer1 = Label(labelFrame1, text="",bg = "white")
timer1.grid(row=2, column=0,pady=20)

labelFrame2 = Frame(root, width = 720, height = 50, bg='white')
labelFrame2.grid(row= 2,column=1, padx=20,pady=20)
Label(labelFrame2,text="Time (seconds):",bg='white').grid(row=1,column=1)
timer2 = Label(labelFrame2, text="", bg = "white")
timer2.grid(row=2, column=1,pady=20)

Label(buttonsFrame, text="Tugas Besar AKA", bg= 'white').grid(row=0, column=0, padx=5,pady=5)

Label(buttonsFrame, text="Anggota Kelompok :", bg= 'white').grid(row=1, column=0, padx=5,pady=5)

Label(buttonsFrame, text="1. Aufa Mutia (1301204233)", bg= 'white').grid(row=2, column=0, padx=5,pady=5)

Label(buttonsFrame, text="2. Andri Zefrinaldi (1301204255)", bg= 'white').grid(row=3, column=0, padx=5,pady=5)

Label(buttonsFrame, text="Silahkan input total array yang akan di sorting (e.g 100) :", bg= 'white').grid(row=5, column=0, padx=5,pady=5)

sizeInput = Entry(buttonsFrame)
sizeInput.grid(row=6, column=0, padx=5,pady=5)

genButton =Button(buttonsFrame, text="Generate", command=generateArr)
genButton.grid(row=7, column=0, padx=5, pady=5)

startButton = Button(buttonsFrame, text="Sort array", command=startAlgo)
startButton.grid(row=8, column=0, padx=5, pady=5)

root.mainloop()
