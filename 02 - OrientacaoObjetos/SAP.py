# Importing the Libraries
import win32com.client
import sys
import subprocess
import time

class Sap():

    SESSION = None
    CONNECTION = None
    APPLICATION = None
    SAPGUIAUTO = None
    
    def saplogin():

        try:
            
            # ABRIR O SAP
            #path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
            #subprocess.Popen(path)
            #time.sleep(10)

            SAPGUIAUTO = win32com.client.GetObject('SAPGUI')
            if not type(SAPGUIAUTO) == win32com.client.CDispatch:
                return

            APPLICATION = SAPGUIAUTO.GetScriptingEngine
            if not type(APPLICATION) == win32com.client.CDispatch:
                SAPGUIAUTO = None
                return
            connection = APPLICATION.OPENCONNECTION("ConnectionName", True)

            if not type(CONNECTION) == win32com.client.CDispatch:
                APPLICATION = None
                SAPGUIAUTO = None
                return

            SESSION = CONNECTION.Children(0)
            if not type(SESSION) == win32com.client.CDispatch:
                CONNECTION = None
                APPLICATION = None
                SAPGUIAUTO = None
                return

            time.sleep(5)
            SESSION.findById("wnd[0]/usr/txtRSYST-BNAME").text = "USERNAME"
            SESSION.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "PASSWORD"
            SESSION.findById("wnd[0]").sendVKey(0)
            

            
            

        except:
            print(sys.exc_info()[0])

        finally:
            SESSION = None
            CONNECTION = None
            APPLICATION = None
            SAPGUIAUTO = None