import tkinter

def foo(event):
	print(123)

root=tkinter.Tk()#создание окна
root.title('Заголовок')
h,w,x,y=150,300,0,0
root.geometry('{0}x{1}+{2}+{3}'.format(w,h,x,y))#w,h щирины и высота соответсвенно 
#x,y координаты левого верхнего угла окна 
#х слева направо,у сверху вниз
lab_1=tkinter.Label(root,text='test')#собснтвено создание
lab_1.pack()#это "складывание" блока текста в окно
#есть много видов вствки,но это самая простая(складывает посередине окна)
lab_1['text']='hello world'
b_1=tkinter.Button(root,text='test')
b_1.pack()
b_1.bind('<Button>',foo)
root.mainloop()
