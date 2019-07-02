from behave import *
import subprocess
import pywinauto
import time
import pyautogui
from pywinauto.application import Application
from pywinauto.application import *
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver import start
import time
import os

class WLA_Installer:
    def __init__(self,path,u_name=None,org_name=None,inst_path=r"C:\Program Files\SafeNet\Windows Logon",pri_ip=None,pri_ssl=None,sec_ip=None,sec_ssl=None,exempt =None,logonmode=None,grid=None):
        self.path=path
        self.u_name=u_name
        self.org_name=org_name
        self.inst_path=inst_path
        self.pri_ip=pri_ip
        self.pri_ssl=pri_ssl
        self.sec_ip=sec_ip
        self.sec_ssl=sec_ssl
        self.validate_install_path=inst_path+r"\WinLogonManager.exe"
        self.exempt =exempt
        self.logonmode=logonmode
        self.grid=grid

    def install_prereq(self,dotnet_pre_check):
        p = subprocess.Popen(['powershell.exe',dotnet_pre_check],stdout=subprocess.PIPE, universal_newlines=True)
        temp=[]
      
        for i in p.communicate():
            temp.append(i)

        st=temp[0]
        l = st.split("\n")
        d = {}

        for i in l:
                a = i.split(":")
                if len(a) >= 2:
                        d[a[0]] = a[1]

        assert (4.5 <= d['Version       '])
        

    def install_agent(self,win_driver):
        
        temp=start(win_driver)
        temp.stop()
        temp.start()
        time.sleep(10)
        driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app":self.path
            })
        wait = ui.WebDriverWait(driver,60)
        wait.until(EC.element_to_be_clickable((By.NAME,"Next >")))
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('I accept the terms in the license agreement').click()
        driver.find_element_by_name('Next >').click()
        if (self.u_name !=None):
            driver.find_element_by_id('3181').send_keys("self.u_name")
        if (self.org_name !=None):
            driver.find_element_by_id('3223').send_keys("self.org_name")
        driver.find_element_by_name('Next >').click()
        if (self.inst_path !=r"C:\Program Files\SafeNet\Windows Logon"):
            driver.find_element_by_name('Change...').click()
            driver.find_element_by_id('3095').send_keys(self.inst_path)
            driver.find_element_by_name('OK').click()
        driver.find_element_by_name('Next >').click()
        if (self.pri_ip !=None):
            driver.find_element_by_id('3180').send_keys(self.pri_ip)
        if (self.pri_ssl !=None):
            driver.find_element_by_id('3143').click()
        if (self.sec_ip !=None):
            driver.find_element_by_id('3166').click()
            driver.find_element_by_id('1951').send_keys(self.sec_ip)
        if (self.sec_ssl !=None):
            driver.find_element_by_id('1949').click()
        driver.find_element_by_name('Next >').click()
        if(self.exempt !=None):
            driver.find_element_by_name('Exempt Local and Domain Administrator groups from SafeNet Authentication').click()
        if(self.logonmode !=None):
            driver.find_element_by_name('SafeNet will cache Windows passwords after the first use').click()
        if(self.grid != None):
            driver.find_element_by_name('Display an option for users to logon with GrIDsure tokens').click()
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('Install').click()
        wait.until(EC.element_to_be_clickable((By.NAME,"Finish")))
        driver.find_element_by_name('Finish').click()
        wait.until(EC.element_to_be_clickable((By.NAME,"No")))
        driver.find_element_by_name('No').click()
        temp.stop()

    def silent_install(self,cmd):
        os.system(cmd)

    def repair_agent(self,win_driver):
        temp=start(win_driver)
        temp.stop()
        temp.start()
        time.sleep(10)
        driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app":self.path
            })
        wait = ui.WebDriverWait(driver,60)
        wait.until(EC.element_to_be_clickable((By.NAME,"Next >")))
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('Repair').click()
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('Install').click()
        wait = ui.WebDriverWait(driver,60)
        wait.until(EC.element_to_be_clickable((By.NAME,"Finish")))
        driver.find_element_by_name('Finish').click()
        wait.until(EC.element_to_be_clickable((By.NAME,"No")))
        driver.find_element_by_name('No').click()
        temp.stop()
        
    def remove_agent(self,win_driver):
        temp=start(win_driver)
        temp.stop()
        temp.start()
        time.sleep(10)
        driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app":self.path
            })
        wait = ui.WebDriverWait(driver,60)
        wait.until(EC.element_to_be_clickable((By.NAME,"Next >")))
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('Remove').click()
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('Remove').click()
        wait = ui.WebDriverWait(driver,60)
        wait.until(EC.element_to_be_clickable((By.NAME,"Finish")))
        driver.find_element_by_name('Finish').click()
        driver.find_element_by_name('No').click()
        temp.stop()

    def modify_agent(self,win_driver):
        temp=start(win_driver)
        temp.stop()
        temp.start()
        time.sleep(10)
        driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app":self.path
            })
        wait = ui.WebDriverWait(driver,60)
        wait.until(EC.element_to_be_clickable((By.NAME,"Next >")))
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('Modify').click()
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('Next >').click()
        driver.find_element_by_name('Install').click()
        wait = ui.WebDriverWait(driver,60)
        wait.until(EC.element_to_be_clickable((By.NAME,"Finish")))
        driver.find_element_by_name('Finish').click()
        wait.until(EC.element_to_be_clickable((By.NAME,"No")))
        driver.find_element_by_name('No').click()
        temp.stop()

    def silent_uninstall(self,cmd):
        os.system(cmd)

    def WLA_Upgrade(self,win_driver):
        temp=start(win_driver)
        temp.stop()
        temp.start()
        time.sleep(10)
        driver = webdriver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                "debugConnectToRunningApp": 'false',
                "app":self.path
            })
        wait = ui.WebDriverWait(driver,60)
        wait.until(EC.element_to_be_clickable((By.NAME,"Yes")))
        driver.find_element_by_name('Yes').click()
        wait.until(EC.element_to_be_clickable((By.NAME,"Next >")))
        driver.find_element_by_name('Next >').click()
        wait.until(EC.element_to_be_clickable((By.NAME,"Finish")))
        driver.find_element_by_name('Finish').click()
    
    
    def validate_install(self):
        
        app=Application(backend="uia").start(self.validate_install_path)
        time.sleep(2)
        app['SAS - Windows Logon Agent Configuration Management']["Cancel"].click()

        if (self.pri_ip !=None):
            app=Application(backend="uia").start(self.validate_install_path)
            time.sleep(2)
            tabc = app['SAS MFA Plug-In Manager']['Communications'].select()
            app=Application().connect(path=self.validate_install_path)
            t=app['SAS MFA Plug-In Manager']['Primary Server IPEdit'].WindowText()
            assert(self.pri_ip == t)
            app['SAS MFA Plug-In Manager']["Cancel"].click()
        if (self.pri_ssl !=None):
            app=Application(backend="uia").start(self.validate_install_path)
            time.sleep(2)
            tabc = app['SAS MFA Plug-In Manager']['Communications'].select()                          
            t=app['SAS MFA Plug-In Manager']["Use SSL (requires a valid certificate)2"].get_toggle_state()
            assert(t == 1)
            app['SAS MFA Plug-In Manager']["Cancel"].click()
                                  
        if (self.sec_ip !=None):
            app=Application(backend="uia").start(self.validate_install_path)
            time.sleep(2)
            tabc = app['SAS MFA Plug-In Manager']['Communications'].select()
            app=Application().connect(path=self.validate_install_path)                    
            t=app['SAS MFA Plug-In Manager']['Edit10'].WindowText()
            assert(self.sec_ip == t)
            app['SAS MFA Plug-In Manager']["Cancel"].click()
            
        if (self.sec_ssl !=None):
            app=Application(backend="uia").start(self.validate_install_path)
            time.sleep(2)
            tabc = app['SAS MFA Plug-In Manager']['Communications'].select()
            t=app['SAS MFA Plug-In Manager']["Use SSL (requires a valid certificate)"].get_toggle_state()
            assert(t == 1)
            app['SAS MFA Plug-In Manager']["Cancel"].click()

    def validate_uninstall(self):
        try :
            app=Application().start(self.self.validate_install_path)
            app['SAS - Windows Logon Agent Configuration Management']['Cancel'].click()
            raise Exception('agent uninstallation failed!')

        except AppStartError:
            print ("test complete")
