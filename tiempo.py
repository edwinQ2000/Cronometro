import tkinter as tink


class tiempo:
    milisegundo = -1
    run = False
    segundo = 0
    minuto = 0
    hora = 0

    def var_name(self, mark):
        def value():
            if self.run:
                if self.milisegundo == -1:
                    msg = ""
                else:
                    if self.hora < 10:
                        msg = "0" + str(self.hora) + ":"
                    else:
                        msg = str(self.hora) + ":"
                    if self.minuto < 10:
                        msg = msg + "0" + str(self.minuto) + ":"
                    else:
                        msg = msg + str(self.minuto) + ":"
                    if self.segundo < 10:
                        msg = msg + "0" + str(self.segundo) + ":"
                    else:
                        msg = msg + str(self.segundo) + ":"
                    if self.milisegundo < 10:
                        msg = msg + "0" + str(self.milisegundo)
                    else:
                        msg = msg + str(self.milisegundo)
                mark['text'] = msg
                mark.after(17, value)

                self.milisegundo += 1

                if (self.milisegundo == 60):
                    self.milisegundo = 0
                    self.segundo += 1
                if (self.segundo == 60):
                    self.segundo = 0
                    self.minuto += 1
                if (self.minuto == 60):
                    self.minuto = 0
                    self.hora += 1;

        value()

    def Start(self, mark):
        self.run = True
        self.var_name(mark)

    def Stop(self):
        self.run = False

    def Reset(self):
        self.milisegundo = -1
        self.segundo = 0
        self.minuto = 0
        self.hora = 0


t = tiempo()
marco = tink.Tk()
marco.title("CRONOMETRO")
marco.minsize(width=300, height=200)
mark = tink.Label(marco, text="00:00:00:00", fg="blue", font="Times 25 bold", bg="white")
mark.pack()
iniciar = tink.Button(marco, text='INICIAR', width=25, command=lambda: t.Start(mark))
parar = tink.Button(marco, text='PARAR', width=25, command=t.Stop)
reiniciar = tink.Button(marco, text='REINICIAR', width=25, command=lambda: t.Reset())
iniciar.pack()
parar.pack()
reiniciar.pack()
marco.mainloop()
