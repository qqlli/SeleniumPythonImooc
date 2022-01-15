#coding = utf-8

import sys
sys.path.append('D:/Python/testframework')
from handle.register_handle import RegisterHandle
from page.register_page import RegisterPage
from selenium_frame.register_code import GetCode

class RegisterBusiness():
    def __init__(self,driver) -> None:
        self.driver = driver
        self.register_handle = RegisterHandle(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.get_code = GetCode(self.driver)

    def register_base(self,emailv,userv,passv,verifiv):
        self.register_handle.send_email(emailv)
        self.register_handle.send_user(userv)
        self.register_handle.send_password(passv)
        self.register_handle.send_verifi(verifiv)
        self.register_handle.click_register()

    def register_sucess(self):
        register_button = self.register_page.get_register_button()
        if register_button == None:
            return True
        else:
            return False

    def register_function(self,info):
        mess = self.register_handle.get_register_error(info)
        if mess != None:
            return True
        else:
            return False

    def email_error(self):
        email_mess = self.register_page.get_email_error_mess()
        if email_mess != None:
            # message = self.register_handle.get_email_error_message()
            # print('邮箱错误测试通过,错误提示:' + message)
            return True
        else:
            return False

    def user_error(self):
        user_mess = self.register_page.get_user_error_mess()
        if user_mess != None:
            # message = self.register_handle.get_user_error_message()
            # print('用户名错误测试通过,错误提示:' + message)
            return True
        else:
            return False

    def password_error(self):
        password_mess = self.register_page.get_password_error_mess()
        if password_mess != None:
            # message = self.register_handle.get_password_error_message()
            # print('密码错误测试通过,错误提示:' + message)
            return True
        else:
            return False 

    def verifi_error(self):
        verifi_mess = self.register_page.get_verifi_error_mess()
        if verifi_mess != None:
            # message = self.register_handle.get_verifi_error_message()
            # print('验证码错误测试通过,错误提示:' + message)
            return True
        else:
            return False

    def get_user_text(self):
        user = self.get_code.get_range_user()
        email = user + '@163.com'
        imgpath = 'D:/Python/testframework/image/imooc.png'
        self.get_code.get_image(imgpath)
        text = self.get_code.get_code(imgpath)
        return user,email,text



