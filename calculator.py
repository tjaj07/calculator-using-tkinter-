from tkinter import *
import tkinter.messagebox

#Main calculator function
def calculator(root):

    #assigning title
    root.title("calculator")

    #setting up dimenshion
    root.geometry("212x244")

    #block resizing of window
    root.resizable(height = False, width =  False)


    #function the clear the entry window
    def clear_(event=None):
        entry.delete(0, "end")
        print("current value cleared")


    #function to clear the memory for new calculation from scratch
    def clear_AC(event=None):
        entry.delete(0, "end")
        num1.set("")
        num2.set("")
        operate.set("")
        val.set("")
        print("memory cleared")


    #function to display the number pressed on the calculator
    def number_button(num):
        val.set(entry.get() + num)


    #function to store the operator and first number
    #and to clear the entry window for seconf number
    def math_button(operator):
        #checking if the number is entered or not
        if entry.get() =="":
            #messafe to be displayed if no number is entered
            tkinter.messagebox.showinfo("window box","enter number please")

        else:
            #setting number 1
            num1.set(entry.get())
            #setting entry variable to none
            val.set("")
            #setting operator
            operate.set(operator)


    #function to display the result i.e when = is pressed
    def result():
        #checking wheather second number is entered or not
        if entry.get() =="":
            tkinter.messagebox.showinfo("window box","enter number please")

        else:
            #assigning num2
            num2.set(entry.get())
            entry.delete(0, "end")

            if operate.get() == "+":
                result = float(num1.get()) + float(num2.get())

            elif operate.get() == "-":
                result = float(num1.get()) - float(num2.get())

            elif operate.get() == "*":
                result = float(num1.get()) * float(num2.get())

            elif operate.get() == "/":
                #checking for division by zero
                if num2.get() == "0":
                    tkinter.messagebox.showinfo("window box","division by zero")
                else:
                    result = float(num1.get()) / float(num2.get())

            elif operate.get() == "%":
                result = (float(num1.get()) % float(num2.get()))/100

            #displaying the result of calculation
            print()
            print("{} {} {} = {}".format(num1.get(),operate.get(),num2.get(),result))
            entry.insert(0,result)


    #declaring varibles used in functions above
    num1 = StringVar()
    num2 = StringVar()
    operate = StringVar()
    val = StringVar()


    #row1
    #creating entry box
    entry = Entry(root, width = 33, textvariable = val)
    entry.grid(row= 1, columnspan = 4, pady = 5)


    #row2
    #button to clear entire memory
    clearall = Button(root, text = 'AC',fg="red", height = 2, width = 6, command = clear_AC)
    clearall.grid(row = 2,column = 0)

    #button t clear current entry
    clear = Button(root, text = 'C',fg="red", height = 2, width = 6, command = clear_)
    clear.grid(row = 2,column = 1,pady = 3)

    #equals button to print result
    equal = Button(root, text = '=', height = 2, width = 6, command = result)
    equal.grid(row = 2, column = 3 )


    #row3
    seven = Button(root, text = '7', height = 2, width = 6,command = lambda : number_button("7"))
    seven.grid(row = 3, column = 0 )
    eight = Button(root, text = '8', height = 2, width = 6,command = lambda : number_button("8"))
    eight.grid(row = 3, column = 1 )
    nine = Button(root, text = '9', height = 2, width = 6,command = lambda : number_button("9"))
    nine.grid(row = 3, column = 2 )

    #divide button
    divide = Button(root, text = '/', height = 2, width = 6, command = lambda : math_button("/"))
    divide.grid(row = 3 , column = 3)


    #row4
    four = Button(root, text = '4', height = 2, width = 6,command = lambda : number_button("4"))
    four.grid(row = 4, column = 0 )
    five = Button(root, text = '5', height = 2, width = 6,command = lambda : number_button("5"))
    five.grid(row = 4, column = 1 )
    six = Button(root, text = '6', height = 2, width = 6,command = lambda : number_button("6"))
    six.grid(row = 4, column = 2 )

    #button to sum 2 numbers
    plus = Button(root, text = '+', height = 2, width = 6, command = lambda : math_button("+"))
    plus.grid(row = 4, column = 3 )


    #row5
    one = Button(root, text = '1', height = 2, width = 6, command = lambda : number_button("1"))
    one.grid(row = 5, column = 0 )
    two = Button(root, text = '2', height = 2, width = 6, command = lambda : number_button("2"))
    two.grid(row = 5, column = 1 )
    three = Button(root, text = '3', height = 2, width = 6, command = lambda : number_button("3"))
    three.grid(row = 5, column = 2 )

    #button tp multiply two numbers
    multiply = Button(root, text = '*', height = 2, width = 6, command = lambda : math_button("*"))
    multiply.grid(row = 5, column = 3)


    #row6
    dot = Button(root, text = '.', height = 2, width = 6, command = lambda : number_button("."))
    dot.grid(row = 6, column = 1 )
    zero = Button(root, text = '0', height = 2, width = 6, command = lambda : number_button("0"))
    zero.grid(row = 6, column = 0 )

    #button to calculate percentage
    percent = Button(root, text = '%', height = 2, width = 6, command = lambda : math_button("%"))
    percent.grid(row = 6, column = 2 )

    #buttton to subtract 2 numbers
    minus = Button(root, text = '-', height = 2, width = 6, command = lambda : math_button("-") )
    minus.grid(row = 6, column = 3, padx=2 )

#end to calculator function


#get root window object
root = Tk()
#calling calculator function
calculator(root)
#runs the app until exicted
root.mainloop()
