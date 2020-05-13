import examen as ex
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from PIL import ImageTk,Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Desarrollo():
    def __init__(self, window):
        self.root = window
        self.root.title('BMP Analizer')
        self.root.iconbitmap('flame.ico')
        self.root.geometry('1320x380')
        self.root.resizable(0,0)
        self.data_frame = Frame(self.root)
        self.data_frame.grid(row=0, column=0)
        self.label1 = LabelFrame(self.data_frame, text='Data Input', padx=5, pady=5)
        self.batch1 = Label(self.data_frame, text='Batch 1:').grid(row=0,column=0)
        self.batch2 = Label(self.data_frame, text='Batch 2:').grid(row=1,column=0)
        self.batch3 = Label(self.data_frame, text='Batch 3:').grid(row=2,column=0)
        self.batch4 = Label(self.data_frame, text='Batch 4:').grid(row=3,column=0)
        self.batch5 = Label(self.data_frame, text='Batch 5:').grid(row=4,column=0)
        self.batch6 = Label(self.data_frame, text='Batch 6:').grid(row=5,column=0)
        self.batch7 = Label(self.data_frame, text='Batch 7:').grid(row=6,column=0)
        self.batch8 = Label(self.data_frame, text='Batch 8:').grid(row=7,column=0)
        self.batch9 = Label(self.data_frame, text='Batch 9:').grid(row=8,column=0)
        self.batch10 = Label(self.data_frame, text='Batch 10:').grid(row=9,column=0)


        def abrir(e):
            archivo = filedialog.askopenfilename(initialdir="/",title="Open", filetypes=((('csv files','*.csv'),('all files','*.*'))))
            e.delete(0, END)
            e.insert(0, archivo)


        self.e1 = Entry(self.data_frame, width=80)
        self.e1.grid(row=0, column=2, columnspan=2)
        self.e2 = Entry(self.data_frame, width=80)
        self.e2.grid(row=1, column=2, columnspan=2)
        self.e3 = Entry(self.data_frame, width=80)
        self.e3.grid(row=2, column=2, columnspan=2) 
        self.e4 = Entry(self.data_frame, width=80)
        self.e4.grid(row=3, column=2, columnspan=2) 
        self.e5 = Entry(self.data_frame, width=80)
        self.e5.grid(row=4, column=2, columnspan=2)
        self.e6 = Entry(self.data_frame, width=80)
        self.e6.grid(row=5, column=2, columnspan=2) 
        self.e7 = Entry(self.data_frame, width=80)
        self.e7.grid(row=6, column=2, columnspan=2)
        self.e8 = Entry(self.data_frame, width=80)
        self.e8.grid(row=7, column=2, columnspan=2) 
        self.e9 = Entry(self.data_frame, width=80)
        self.e9.grid(row=8, column=2, columnspan=2) 
        self.e10 = Entry(self.data_frame, width=80)
        self.e10.grid(row=9, column=2, columnspan=2)
        self.b1 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e1)).grid(row=0, column=1)
        self.b2 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e2)).grid(row=1, column=1) 
        self.b3 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e3)).grid(row=2, column=1) 
        self.b4 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e4)).grid(row=3, column=1) 
        self.b5 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e5)).grid(row=4, column=1) 
        self.b6 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e6)).grid(row=5, column=1) 
        self.b7 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e7)).grid(row=6, column=1) 
        self.b8 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e8)).grid(row=7, column=1) 
        self.b9 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e9)).grid(row=8, column=1) 
        self.b10 = Button(self.data_frame, text='Open', command=lambda:abrir(self.e10)).grid(row=9, column=1)  
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.c1 = Checkbutton(self.data_frame, text='Biogas', variable= self.var1, pady=20).grid(row=10, column=2,sticky=W)
        self.c2 = Checkbutton(self.data_frame, text='Methane', variable= self.var2, pady=20).grid(row=10, column=2, sticky=E)
        self.entradas = [self.e1,self.e2,self.e3,self.e4,self.e5,self.e6,self.e7,self.e8,self.e9,self.e10]

        
        def analizar():
            self.scrollable_frame.destroy()
            self.scrollable_frame = Frame(self.canvas, background='#020e36')
            self.scrollable_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
            self.canvas.create_window((0,0), window=self.scrollable_frame, anchor='nw')
            biogas = []
            metano = []
            for e in self.entradas:
                if e.get():
                    batch = pd.read_csv(e.get(), sep=';')
                    bmp = ex.YieldConverter(batch)
                    biogas.append(bmp.biogas)
                    metano.append(bmp.metano)
                
            if self.var1.get() == 1 & self.var2.get() == 1:
                maxdi_biogas = ex.Compare(biogas).max_daily()
                Label(self.scrollable_frame, text='Daily biogas yields:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in maxdi_biogas:
                    batch,valor,day = i[0],i[1],i[2]
                    resultado = 'El rendimiento diario máximo de biogás del batch {} fue de {} mL/gSVd,\nalcanzado el día {}.'.format(valor,batch,day)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                maxdi_metano = ex.Compare(metano).max_daily()
                Label(self.scrollable_frame, text='Daily methane yields:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in maxdi_metano:
                    batch,valor,day = i[0],i[1],i[2]
                    resultado = 'El rendimiento diario máximo de metano del batch {} fue de {} mL/gSVd,\nalcanzado el día {}.'.format(valor,batch,day)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                maxcum_biogas = ex.Compare(biogas).max_cum()
                Label(self.scrollable_frame, text='Cumulative biogas yields:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in maxcum_biogas:
                    batch,valor = i[0],i[1]
                    resultado = 'El rendimiento acumulado máximo de biogás del batch {} fue de {} mL/gSV.'.format(valor,batch)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                maxcum_metano = ex.Compare(metano).max_cum()
                Label(self.scrollable_frame, text='Cumulative methane yields:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in maxcum_metano:
                    batch,valor = i[0],i[1]
                    resultado = 'El rendimiento acumulado máximo de metano del batch {} fue de {} mL/gSV.'.format(valor,batch)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                stop_biogas = ex.Compare(biogas).stopday()
                Label(self.scrollable_frame, text='Stop biogas production:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in stop_biogas:
                    batch,day = i[0],i[1]
                    resultado = 'La producción de biogás del batch {} mermó el día {}.'.format(batch,day)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                stop_metano = ex.Compare(metano).stopday()
                Label(self.scrollable_frame, text='Stop methane production:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in stop_metano:
                    batch,day = i[0],i[1]
                    resultado = 'La producción de metano del batch {} mermó el día {}.'.format(batch,day)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
            elif self.var1.get() == 1:
                maxdi_biogas = ex.Compare(biogas).max_daily()
                Label(self.scrollable_frame, text='Daily biogas yields:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in maxdi_biogas:
                    batch,valor,day = i[0],i[1],i[2]
                    resultado = 'El rendimiento diario máximo de biogás del batch {} fue de {} mL/gSVd,\nalcanzado el día {}.'.format(valor,batch,day)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                maxcum_biogas = ex.Compare(biogas).max_cum()
                Label(self.scrollable_frame, text='Cumulative biogas yields:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in maxcum_biogas:
                    batch,valor = i[0],i[1]
                    resultado = 'El rendimiento acumulado máximo de biogás del batch {} fue de {} mL/gSV.'.format(valor,batch)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                stop_biogas = ex.Compare(biogas).stopday()
                Label(self.scrollable_frame, text='Stop biogas production:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in stop_biogas:
                    batch,day = i[0],i[1]
                    resultado = 'La producción de biogás del batch {} mermó el día {}.'.format(batch,day)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')   
            elif self.var2.get() == 1:
                maxdi_metano = ex.Compare(metano).max_daily()
                Label(self.scrollable_frame, text='Daily methane yields:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in maxdi_metano:
                    batch,valor,day = i[0],i[1],i[2]
                    resultado = 'El rendimiento diario máximo de metano del batch {} fue de {} mL/gSVd,\nalcanzado el día {}.'.format(valor,batch,day)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                maxcum_metano = ex.Compare(metano).max_cum()
                Label(self.scrollable_frame, text='Cumulative methane yields:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in maxcum_metano:
                    batch,valor = i[0],i[1]
                    resultado = 'El rendimiento acumulado máximo de metano del batch {} fue de {} mL/gSV.'.format(valor,batch)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')
                stop_metano = ex.Compare(metano).stopday()
                Label(self.scrollable_frame, text='Stop methane production:', fg='white', background='#020e36', font='Courier').pack(anchor='nw', pady=5)
                for i in stop_metano:
                    batch,day = i[0],i[1]
                    resultado = 'La producción de metano del batch {} mermó el día {}.'.format(batch,day)
                    Label(self.scrollable_frame, text=resultado, fg='white', justify='left', background='#020e36', font=('Courier', 11)).pack(anchor='nw')    
            
                    
        self.analize = Button(self.data_frame, text='Analize', command=analizar).grid(row=11, column=2, sticky=W)
        self.an_frame = Frame(self.root, height=350, width=700)
        self.an_frame.config(borderwidth=5, relief=GROOVE)
        self.an_frame.grid(row=0, column=1)
        self.canvas = Canvas(self.an_frame, height=350, width=700, background='#020e36')
        self.scrollbar = Scrollbar(self.an_frame, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, background='#020e36')
        self.scrollable_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y')
        self.label2 = LabelFrame(self.an_frame, text='Analysis', padx=5, pady=5)
        
        
        def graficar():
            top = Toplevel()
            top.title('Plots')
            canvas_fig = Canvas(top)
            scroll = Scrollbar(top, orient='vertical', command=canvas_fig.yview)
            scroll_frame = Frame(canvas_fig)
            scroll_frame.bind('<Configure>', lambda e: canvas_fig.configure(scrollregion=canvas_fig.bbox('all')))
            canvas_fig.create_window((0,0), window=scroll_frame, anchor='nw')
            canvas_fig.configure(yscrollcommand=scroll.set)
            canvas_fig.pack(side='left', fill='both', expand=True)
            scroll.pack(side='right', fill='y')
            i = 0
            for e in self.entradas:
                i +=1
                if e.get():
                    batch = pd.read_csv(e.get(), sep=';')
                    bmp = ex.YieldConverter(batch)
                    if self.var1.get() == 1 & self.var2.get() == 1:
                        fig = Figure(figsize=(13.5,8))
                        axes = fig.subplots(2, 2)
                        axes[0,0].plot(bmp.x, bmp.biogas, 'b')
                        axes[0,0].set_xlim(left=0)
                        axes[0,0].set_ylabel('Diario [mL/gSV]')
                        axes[0,0].set_ylim(bottom=0)
                        axes[0,0].set_title('Rendimiento biogás batch {}'.format(i))
                        axes[0,1].plot(bmp.x, bmp.metano, 'g')
                        axes[0,1].set_xlim(left=0)
                        axes[0,1].set_ylabel('Diario [mL/gSV]')
                        axes[0,1].set_ylim(bottom=0)
                        axes[0,1].set_title('Rendimiento metano batch {}'.format(i))
                        axes[1,0].plot(bmp.x, bmp.biogas_cum, 'b')
                        axes[1,0].set_xlabel('Días')
                        axes[1,0].set_xlim(left=0)
                        axes[1,0].set_ylim(bottom=0)
                        axes[1,0].set_ylabel('Acumulado [mL/gSV]')
                        axes[1,1].plot(bmp.x, bmp.metano_cum, 'g')
                        axes[1,1].set_xlabel('Días')
                        axes[1,1].set_xlim(left=0)
                        axes[1,1].set_ylim(bottom=0)
                        axes[1,1].set_ylabel('Acumulado [mL/gSV]')
                        canvas_fig1 = FigureCanvasTkAgg(fig, master=scroll_frame)
                        canvas_fig1.draw()
                        canvas_fig1.get_tk_widget().pack(side='bottom', fill='both', expand=True)
                        toolbar = NavigationToolbar2Tk(canvas_fig1, scroll_frame)
                        toolbar.config(background='white')
                        toolbar._message_label.config(background='white')
                        toolbar.update()
                    elif self.var1.get() == 1:
                        fig = Figure(figsize=(13.5,10))
                        axes = fig.subplots(2, 1)
                        axes[0].plot(bmp.x, bmp.biogas, 'b')
                        axes[0].set_xlim(left=0)
                        axes[0].set_ylabel('Diario [mL/gSV]')
                        axes[0].set_ylim(bottom=0)
                        axes[0].set_title('Rendimiento biogás batch {}'.format(i))
                        axes[1].plot(bmp.x, bmp.biogas_cum, 'b')
                        axes[1].set_xlim(left=0)
                        axes[1].set_ylabel('Acumulado [mL/gSV]')
                        axes[1].set_ylim(bottom=0)
                        canvas_fig2 = FigureCanvasTkAgg(fig, master=scroll_frame)
                        canvas_fig2.draw()
                        canvas_fig2.get_tk_widget().pack(side='bottom', fill='both', expand=True)
                        toolbar = NavigationToolbar2Tk(canvas_fig2, scroll_frame)
                        toolbar.config(background='white')
                        toolbar._message_label.config(background='white')
                        toolbar.update()
                    elif self.var2.get() == 1:
                        fig = Figure(figsize=(13.5,10))
                        axes = fig.subplots(2, 1)
                        axes[0].plot(bmp.x, bmp.metano, 'g')
                        axes[0].set_xlabel('Días')
                        axes[0].set_xlim(left=0)
                        axes[0].set_ylim(bottom=0)
                        axes[0].set_ylabel('Diario [mL/gSV]')
                        axes[0].set_title('Rendimiento metano batch {}'.format(i))
                        axes[1].plot(bmp.x, bmp.metano_cum, 'g')
                        axes[1].set_xlabel('Días')
                        axes[1].set_xlim(left=0)
                        axes[1].set_ylim(bottom=0)
                        axes[1].set_ylabel('Acumulado [mL/gSV]')
                        canvas_fig3 = FigureCanvasTkAgg(fig, master=scroll_frame)
                        canvas_fig3.draw()
                        canvas_fig3.get_tk_widget().pack(side='bottom', fill='both', expand=True)
                        toolbar = NavigationToolbar2Tk(canvas_fig3, scroll_frame)
                        toolbar.config(background='white')
                        toolbar._message_label.config(background='white')
                        toolbar.update()
        
        
        self.graficar = Button(self.data_frame, text='Plot', command=graficar).grid(row=11, column=2, sticky=E)


        #def guardar():
        #    filepath = asksaveasfilename(defaultextension = 'txt', filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')])
        #    if not filepath:
        #        return
        #    with open(filepath, 'w') as output_file:
        #        text = self.scrollable_frame.get(1.0, END)
        #        output_file.write(text)
        
        
        #self.save = Button(self.data_frame, text='Save As', command=guardar).grid(row=12, column=2)

root = Tk()
Desarrollo(root)
root.mainloop()