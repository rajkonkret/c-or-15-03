import tkinter
import requests as re


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text="CHF")
        self.values = tkinter.StringVar()
        self.label2 = tkinter.Label(self.main_window, textvariable=self.values)
        self.button = tkinter.Button(self.main_window, text="ok", command=self.waluta)
        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.button.pack(side='right')

        tkinter.mainloop()

    def waluta(self):
        response = re.get("http://api.nbp.pl/api/exchangerates/rates/A/CHF/")
        print(response)
        # 200 ok
        # 4.. bledy
        # 5.. bledy serwera
        table = response.json()
        print(table)
        print(table['rates'][0]['effectiveDate'])
        kurs = table['rates'][0]['mid']
        self.values.set(kurs)


my_gui = MyGui()
