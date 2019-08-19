import math, random,smtplib
def generateOTP() :
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6):
        OTP += string[math.floor(random.random() * length)]
    return OTP
if __name__ == "__main__" :
    print("OTP of length 6:", generateOTP())
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("tanaypatankar.2000@gmail.com", "password_here")
    message = "Here is the requested OTP : "+ generateOTP()
    s.sendmail("tanaypatankar.2000@gmail.com", "tanaypatankar.2000@gmail.com", message)
    s.quit()
    otp=input("Enter the OTP")
    if otp is generateOTP():
        print("OTP is correct")
    else:
        print("OTP is wrong :(")