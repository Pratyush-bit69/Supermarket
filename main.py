import mysql.connector as mc
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivy.metrics import dp


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

conn = mc.connect(
    host="localhost",
    user="root",
    password="duggi11#",
    database="supermarket"
)

c = conn.cursor()

class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen=Builder.load_file("mainscreen.kv")
        self.prod = ''
        self.supp = 0
        self.value_3 = None
        self.z = []
        self.emp_id=0
        # menu = [{
        #         "viewclass": "IconListItem",
        #         "text": 'Stationary',
        #         "height": dp(56),
        #         "icon": "pencil",
        #         "on_release": lambda x="0": self.menu_callback(x)
        #     },
        #     {
        #         "height": dp(56),
        #         "text": 'Grocery',
        #         "icon": "barley",
        #         "viewclass": "IconListItem",
        #         "on_release": lambda x="1": self.menu_callback(x)
        #     },
        #     {
        #         "text": "Fruits",
        #         "icon": "fruit-cherries",
        #         "height": dp(56),
        #         "viewclass": "IconListItem",
        #         "on_release": lambda x="2": self.menu_callback(x)
        #     },
        #     {
        #         "text": "Vegeatables",
        #         "icon": "weather-night",
        #         "height": dp(56),
        #         "viewclass": "IconListItem",
        #         "on_release": lambda x="3": self.menu_callback(x)
        #     },
        #     {
        #         "text": "Frozen department",
        #         "icon": "coffee",
        #         "height": dp(56),
        #         "viewclass": "IconListItem",
        #         "on_release": lambda x="4": self.menu_callback(x)
        #     },
        #     {
        #         "text": "Clothes",
        #         "icon": "pill",
        #         "height": dp(56),
        #         "viewclass": "IconListItem",
        #         "on_release": lambda x="5": self.menu_callback(x)
        #     },
        #     {
        #         "text": "Kid section",
        #         "icon": "cart-outline",
        #         "height": dp(56),
        #         "viewclass": "IconListItem",
        #         "on_release": lambda x="6": self.menu_callback(x)
        #     },
        #     {
        #         "text": "Household",
        #         "icon": "pencil",
        #         "height": dp(56),
        #         "viewclass": "IconListItem",
        #         "on_release": lambda x="7": self.menu_callback(x)
        #     }
        # ]
        #
        # self.menu_items = MDDropdownMenu(
        #     caller=self.screen.ids.field,
        #     items=menu,
        #     position="bottom",
        #     width_mult=4
        # )

        menu_prod = [
            {
                "viewclass": "IconListItem",
                "text": 'Stationary',
                "height": dp(56),
                "icon": "pencil",
                "on_release": lambda y="0": self.menu_callback_prod(y)
            },
            {
                "height": dp(56),
                "text": 'Grocery',
                "icon": "barley",
                "viewclass": "IconListItem",
                "on_release": lambda y="1": self.menu_callback_prod(y)
            },
            {
                "text": "Fruits",
                "icon": "fruit-cherries",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda y="2": self.menu_callback_prod(y)
            },
            {
                "text": "Vegeatables",
                "icon": "weather-night",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda y="3": self.menu_callback_prod(y)
            },
            {
                "text": "Frozen department",
                "icon": "coffee",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda y="4": self.menu_callback_prod(y)
            },
            {
                "text": "Clothes",
                "icon": "pill",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda y="5": self.menu_callback_prod(y)
            },
            {
                "text": "Kid Section",
                "icon": "cart-outline",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda y="6": self.menu_callback_prod(y)
            },
            {
                "text": "Household",
                "icon": "pencil",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda y="7": self.menu_callback_prod(y)
            }
        ]
        self.menuitems = MDDropdownMenu(
            caller=self.screen.ids.field,
            items=menu_prod,
            position="bottom",
            width_mult=4
        )
        menu_supp = [
            {
                "viewclass": "IconListItem",
                "text": '1:Stationary:Kumar',
                "height": dp(56),
                "icon": "pencil",
                "on_release": lambda w="0": self.depart_call(w)
            },
            {
                "height": dp(56),
                "text": '2:Grocery:Gowda',
                "icon": "barley",
                "viewclass": "IconListItem",
                "on_release": lambda w="1": self.depart_call(w)
            },
            {
                "text": "3:Clothes:Pandey",
                "icon": "fruit-cherries",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda w="2": self.depart_call(w)
            },
            {
                "text": "4:Fruits:Sharma",
                "icon": "weather-night",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda w="3": self.depart_call(w)
            },
            {
                "text": "5:Vegeatables:Thakur",
                "icon": "coffee",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda w="4": self.depart_call(w)
            },
            {
                "text": "6:Frozen_department:gokul",
                "icon": "coffee",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda w="5": self.depart_call(w)
            },
            {
                "text": "7:Kid_section:Prashanth",
                "icon": "coffee",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda w="6": self.depart_call(w)
            },
            {
                "text": "8:Household:Sulaiman",
                "icon": "coffee",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda w="7": self.depart_call(w)
            }

        ]

        self.suppitems = MDDropdownMenu(
            caller=self.screen.ids.field_,
            items=menu_supp,
            position="bottom",
            width_mult=4
        )

    def menu_callback(self, text_item):
        if text_item == '0':
            print("0")
        elif text_item == '1':
            print("1")
        elif text_item == '2':
            print("2")
        elif text_item == '3':
            print("3")
        elif text_item == '4':
            print("4")
        elif text_item == '5':
            print("5")
        elif text_item == '6':
            print("6")
        elif text_item == '7':
            print("7")
        elif text_item == '8':
            print("8")
        else:
            print("lala")

    def depart_call(self,dept_text):
        if dept_text == '0':
            self.supp=1
        elif dept_text == '1':
            self.supp==2
        elif dept_text == '2':
            self.supp=6
        elif dept_text == '3':
            self.supp=3
        elif dept_text == '4':
            self.supp=4
        elif dept_text=='5':
            self.supp=5
        elif dept_text=='6':
            self.supp=7
        elif dept_text=='7':
            self.supp=8


    def menu_callback_prod(self, text_item_prod):
        if text_item_prod == '0':
            self.prod='stationary'
        elif text_item_prod == '1':
            self.prod='grocery'
        elif text_item_prod == '2':
            self.prod='fruits'
        elif text_item_prod == '3':
            self.prod='vegetables'
        elif text_item_prod == '4':
            self.prod='frozen department'
        elif text_item_prod == '5':
            self.prod='clothes'
        elif text_item_prod == '6':
            self.prod='kid section'
        elif text_item_prod == '7':
            self.prod='household'
        else:
            print("lala")




    def login(self,loginuser,password):
        if self.root.ids.password.text==" " and self.root.ids.loginuser.text==" ":
            self.var=1
            return self.var
        else:
            self.var=0
            return self.var

    def loging(self):
        if self.var==1:
            self.root.ids.appbutton.disabled=False
        else:
            self.root.ids.appbutton.disabled=True

    def log_out(self):
        self.root.ids.appbutton.disabled = True

    def on_save_2(self, instance, value_2, date_range):
        self.value_2=value_2
        print(value_2)
    def on_cancel_2(self, instance, value):
        pass

    def show_date_picker_2(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_2, on_cancel=self.on_cancel_2)
        date_dialog.open()
    def on_save(self, instance, value, date_range):
        self.value=value
        print(value)
    def on_cancel(self, instance, value):
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save_3(self, instance, value_3, date_range):
        self.value_3=value_3
        print(value_3)
    def on_cancel_3(self, instance, value):
        pass

    def show_date_picker_3(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_3, on_cancel=self.on_cancel_3)
        date_dialog.open()


    def custpress(self):
        c.execute("select max(cid) from customer;")
        val=c.fetchall()
        top=val[0][0]
        print(top)

        top=top+1
        name=self.root.ids.name.text
        address=self.root.ids.address_c.text
        num=int(self.root.ids.number.text)
        c.execute("insert into customer values(%s,%s,%s,0,%s,%s,%s)",(top,name,self.value,address,num,self.emp_id,))
        conn.commit()

    def prodpress(self):
        c.execute("select max(pid) from product;")
        val = c.fetchall()
        top = val[0][0]
        print(top)

        top=top+1
        prodname=self.root.ids.prodid.text
        mrp=int(self.root.ids.markp.text)
        cp=int(self.root.ids.costp.text)
        c.execute("insert into product values(%s,%s,%s,%s,%s,%s)",(top,prodname,self.prod,mrp,cp,self.supp,))
        conn.commit()

    def promopress(self):
        c.execute("select max(promo_id) from promo;")
        val = c.fetchall()
        top = val[0][0]
        print(top)

        top=top+1
        disc=int(self.root.ids.discount.text)
        self.dept = self.root.ids.departpromo.text
        c.execute("select did from department where dept_name=%s", (self.dept,))
        did = c.fetchall()
        didp=did[0][0]

        c.execute("insert into promo values(%s,%s,%s,%s)",(top,disc,self.value,didp,))
        conn.commit()

    def updatepr(self):
        prc=self.root.ids.promoin.text
        disprt=int(self.root.ids.discountmf.text)
        c.execute("update promo set discount=%s where promo_id=%s",(disprt,prc))
        c.execute("update promo set validity=%s where promo_id=%s", (self.value, prc))
        conn.commit()

    def displaycust(self):
        c.execute("6 are ",(self.root.ids.empins.text,))
        discust=c.fetchall()
        print(discust)
        for row in discust:
            cname=row[0]
            cjoindate=row[1]
            money_spent=row[2]
            caddress=row[3]
            phone=row[4]
            self.root.ids.discname.text = f' {cname}\n'
            self.root.ids.discjoin.text = f' {cjoindate}\n'
            self.root.ids.dismoney.text = f' {money_spent}\n'
            self.root.ids.discaddress.text = f' {caddress}\n'
            self.root.ids.discphone.text = f' {phone}\n'

    def releasepb(self):
        self.dptc = self.root.ids.textu.text
        c.execute("SELECT discount, validity, promo_id FROM promo WHERE dept IN (SELECT did FROM department WHERE dept_name = %s)",(self.dptc,))
        dispc = c.fetchall()

        for row in dispc:
            discount = row[0]
            validity = row[1]
            promo_id = row[2]
            self.root.ids.discountp.text += f' {discount}\n'
            self.root.ids.validityp.text += f' {validity}\n'
            self.root.ids.deptp.text += f' {promo_id}\n'

    def employeepress(self):
        c.execute("select max(EMPLOYEE_ID) from employees;")
        val = c.fetchall()
        top = val[0][0]
        print(top)

        top = top + 1
        sal=self.root.ids.salary.text
        c.execute("insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s)",(top,self.root.ids.empname.text,self.prod,self.root.ids.address.text,self.value,sal,self.value_2,self.value_3))
        conn.commit()

    def empdel(self):
        c.execute("delete from employees where employee_id=%s",(self.root.ids.empid_d.text,))
        conn.commit()

    def employeeundercust(self):
        c.execute(
            "select employee_name from employees where employee_id in(select employee_id from customer where cid=%s)",
            (self.root.ids.check.text,))
        t=c.fetchall()
        for row in t:
            cname = row[0]
            self.root.ids.outputofemp.text += f' {cname}\n'

    def delpromo(self):
        c.execute("delete from promo where promo_id =%s",(self.root.ids.promo_id_delete.text,))
        conn.commit()

    def pressedempall(self):
        c.execute("select * from employees;")
        t=c.fetchall()
        print(t)
        for i in t:
            cname=i[1]
            self.root.ids.outputofemp.text+=f' {cname}\n'

    def addtransaction(self):
        nig=int(self.root.ids.data.text)
        print(nig)
        print(type(nig))
        c.execute("select cp from product where pid =%s",(nig,))
        t=c.fetchall()
        val=t[0][0]*int(self.root.ids.quant.text)
        self.root.ids.curprice.text='Price        '+str(val)
        self.z.append(val)
        val=0
    def addtobill(self):
        total=sum(self.z)
        self.root.ids.curprice.text="Price      Rs:0"
        self.root.ids.bill.text = str(total)

    def empupdate(self):
        emp_id=int(self.root.ids.emp_id.text)
        c.execute('update employees set DEPARTMENT=%s where employee_id=%s',(self.prod,emp_id,))
        c.execute('update employees set ADDRESS=%s where employee_id=%s', (self.root.ids.address_u.text, emp_id,))
        c.execute('update employees set EMPLOYEE_SALARY=%s where employee_id=%s', (self.root.ids.salary_u.text, emp_id,))
        c.execute('update employees set EMPLOYEE_END_DATE=%s where employee_id=%s', (self.value_3, emp_id,))
        conn.commit()

    def displaydeptproduct(self):
        c.execute("select pname from product where product_type in(select dept_name from department where did in(select did from department where dept_name=%s));",(self.root.ids.productdeptdisplayed.text,))
        t=c.fetchall()
        print(t)
        for i in t:
            cname = i[0]
            self.root.ids.prodnameout.text += f' {cname}\n'

    def displayedallproduct(self):
        c.execute("select pname,pid from product")
        t=c.fetchall()
        for i in t:
            pname=i[0]
            pid=i[1]
            self.root.ids.prodidout.text += f' {pid}\n'
            self.root.ids.prodnameout.text += f' {pname}\n'

    def updateprod(self):
        c.execute("update product set mrp = %s where pid=%s",(self.root.ids.updatedmrp.text,self.root.ids.produpdate.text,))
        conn.commit()

    def delprod(self):
        c.execute("delete from product where pid=%s",(self.root.ids.proddelid.text,))
        conn.commit()

    def employeeidsel(self):
        self.emp_id=int(self.root.ids.curemp.text)

    def fulltransaction(self):
        l = sum(self.z)
        c.execute("select discount from promo where promo_id = %s", (self.root.ids.prm.text,))
        t = c.fetchall()
        x = t[0][0]
        l = l - (l * (x / 100))
        self.root.ids.bill.text="Bill is:"+str(l)
        self.root.ids.add.disabled=True
        c.execute("update customer set money_spent=%s where cid=%s",(l,self.root.ids.custid.text,))
        c.execute("update customer set employee_id=%s where cid=%s", (self.emp_id, self.root.ids.custid.text,))
        conn.commit()

    def checkedlog(self):
        if self.root.ids.username.text=="admin" and self.root.ids.password.text=='duggi11#':
            self.root.ids.loggedin.disabled=False
        else:
            self.root.ids.loggedin.disabled=True
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return self.screen

Example().run()