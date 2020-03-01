from tkinter import (
    Tk, Label, LabelFrame, 
    Frame, LEFT, TOP, X, Y, BOTH, RIGHT,
    Entry,
    W, E, N, S,
    font, Spinbox, Button,
)


class Form:
    def __init__(self):
        self.window = Tk()
        self.font_style = font.Font(size=11)
        self.window.title("Cheap Shop Catalog Store")
        self.window.resizable(False, False)
        self.setup_watermark()
        self.setup_purchaser()
        self.setup_catalog_item()
        self.setup_footer()

    def setup_watermark(self):
        lbl = Label(
            master=self.window,
            text="Egemen Göl",
            font=font.Font(size=9, slant=font.ITALIC)
        )
        lbl.pack(anchor=E, padx=20)

    def setup_purchaser(self):

        purchaser = LabelFrame(
            master=self.window,
            text="Purchaser",
            font=font.Font(size=14, weight=font.BOLD),
        )

        master_frm = Frame(master=purchaser)

        label_texts = [
            ["Name:", "Phone:"],
            ["Postal Code:", "Province:", "City:"],
            ["Delivery Address:"],
            ["Today's Date:"],
            ["Credit Card No.:", "for dept use, validation id:"],
        ]

        master_frm.columnconfigure(0, minsize=60, weight=0)
        master_frm.columnconfigure(1, weight=1)

        for i_row, text_list in enumerate(label_texts):
            text = text_list[0]
            lbl_head = Label(
                master=master_frm,
                text=text,
                font=self.font_style
            )
            lbl_head.grid(row=i_row, column=0, sticky=E, pady=5)

            frm = Frame(master=master_frm)
            ent_name = Entry(
                master=frm,
                font=self.font_style,
                width=15
            )
            if text == "Delivery Address:":
                ent_name.pack(fill=X)
            else:
                ent_name.pack(side=LEFT)

            for text in text_list[1:]:
                lbl = Label(
                    master=frm,
                    text=text,
                    padx=10,
                    font=self.font_style
                )
                lbl.pack(side=LEFT, anchor=E)
                ent_name = Entry(
                    master=frm, 
                    font=self.font_style,
                    width=15
                )
                ent_name.pack(side=LEFT)

            frm.grid(row=i_row, column=1, sticky=W+E, pady=5, padx=10)
        master_frm.pack(fill=BOTH, padx=10, pady=10)
        purchaser.pack(fill=BOTH, padx=20, pady=5)

    def setup_catalog_item(self):
        catalog = LabelFrame(
            master=self.window,
            text="Catalog Item",
            font=font.Font(size=14, weight=font.BOLD),
        )

        frm = Frame(master=catalog)

        lbl_number = Label(
            master=frm,
            text="Number:",
            font=self.font_style
        )
        ent_number = Entry(
            master=frm,
            font=self.font_style,
            width=20,
        )
        lbl_qtt = Label(
            master=frm,
            text="Quantity:",
            font=self.font_style
        )
        spin_qtt = Spinbox(
            master=frm,
            from_=1, to_=100,
            width=4,
        )
        lbl_cost = Label(
            master=frm,
            text="Cost/item:",
            font=self.font_style,
        )
        ent_cost = Entry(
            master=frm,
            font=self.font_style,
            width=14,
            state="readonly",
        )
        lbl_total = Label(
            master=frm,
            text="Total:",
            font=self.font_style,
        )
        ent_total = Entry(
            master=frm,
            font=self.font_style,
            width=14,
            state="readonly",
        )
        lbl_number.pack(side=LEFT, padx=2, pady=5)
        ent_number.pack(side=LEFT, padx=2, pady=5)
        lbl_qtt.pack(side=LEFT, padx=2, pady=5)
        spin_qtt.pack(side=LEFT, padx=2, pady=5)
        lbl_cost.pack(side=LEFT, padx=2, pady=5)
        ent_cost.pack(side=LEFT, padx=2, pady=5)
        lbl_total.pack(side=LEFT, padx=2, pady=5)
        ent_total.pack(side=LEFT, padx=2, pady=5)

        frm.pack(fill=BOTH, padx=10, pady=10)
        catalog.pack(fill=X, padx=20, pady=5)

    def setup_footer(self):
        frm = Frame(master=self.window)
        frm.rowconfigure(0, weight=0)
        frm.rowconfigure(1, weight=0)
        frm.columnconfigure(0, weight=0)
        frm.columnconfigure(1, weight=0)
        frm.columnconfigure(2, weight=1)
        frm.columnconfigure(3, weight=0, minsize=300)

        lbl = Label(
            master=frm,
            font=self.font_style,
            text="Balance Owing:",
        )
        ent = Entry(
            master=frm,
            font=self.font_style,
            state="readonly",
            width=14,
        )
        btn_next = Button(
            master=frm,
            text="Next Catalog Item",
            font=self.font_style,
        )
        btn_invoice = Button(
            master=frm,
            text="Trigger Invoice",
            font=self.font_style,
        )

        lbl.grid(column=0, row=0, rowspan=2, padx=20)
        ent.grid(column=1, row=0, rowspan=2, padx=20)
        btn_next.grid(column=3, row=0, sticky=W+E, padx=20, pady=3)
        btn_invoice.grid(column=3, row=1, sticky=W+E, padx=20, pady=3)

        frm.pack(fill=BOTH, padx=20, pady=10)


if __name__ == "__main__":
    form = Form()
    form.window.mainloop()