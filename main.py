from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        

        #first image
        img1=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\4915647.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.phtoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.phtoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)


        
        #second image
        img2=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\collge_pic.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.phtoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.phtoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #third image
        img3=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\6550636.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.phtoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.phtoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #BG IMAGE
        img4=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\7103022.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.phtoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.phtoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45)
  
        #STUDENT BUTTON
        img5=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\Screenshot 2024-06-14 055512.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.phtoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.phtoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)
 
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=300,width=220,height=40)



         #DETECT FACE BUTTON
        img6=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\7103052.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.phtoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.phtoimg6,cursor="hand2")
        b1.place(x=400,y=100,width=220,height=220)
 
        b1_1=Button(bg_img,text="face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=300,width=220,height=40)


        #Attendence BUTTON
        img7=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\Screenshot 2024-06-14 055427.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.phtoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.phtoimg7,cursor="hand2")
        b1.place(x=700,y=100,width=220,height=220)
 
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=300,width=220,height=40)


         #Help BUTTON
        img8=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\Screenshot 2024-06-14 070014.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.phtoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.phtoimg8,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=220)
 
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)



         #trainBUTTON
        img9=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\Screenshot 2024-06-14 065918.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.phtoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.phtoimg9,cursor="hand2")
        b1.place(x=100,y=350,width=220,height=220)
 
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=550,width=220,height=40)


         #photos face button
        img10=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\photo.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.phtoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.phtoimg10,cursor="hand2")
        b1.place(x=400,y=350,width=220,height=220)
 
        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=550,width=220,height=40)


        #Developer 
        img11=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\developer.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.phtoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.phtoimg11,cursor="hand2")
        b1.place(x=700,y=350,width=220,height=220)
 
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=550,width=220,height=40)

         #Exit
        img12=Image.open(r"C:\Users\KALATRI\Desktop\Project_face_recognition\college image\exit.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.phtoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.phtoimg12,cursor="hand2")
        b1.place(x=1000,y=350,width=220,height=220)
 
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=550,width=220,height=40)





        #==================================function buttons========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)






























if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()