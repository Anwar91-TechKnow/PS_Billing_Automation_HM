import configparser

config = configparser.RawConfigParser()
config.read("C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//Configurations//locators.ini")


class TestReadConfig:
    @staticmethod
    def test_getapplicationURL():
        url = config.get("common_data", 'url')
        return url

    @staticmethod
    def test_chaticon():
        chaticon = config.get("common_data", 'chaticon')
        return chaticon

    @staticmethod
    def test_frameswitch():
        frameswitch = config.get("common_data", 'frameswitch')
        return frameswitch

    @staticmethod
    def test_chattextarea():
        chattextarea = config.get("common_data", 'chattextarea')
        return chattextarea

    @staticmethod
    def test_initialmsg():
        initialmsg = config.get("common_data", 'initialmsg')
        return initialmsg

    @staticmethod
    def test_chatinfo():
        chatinfo = config.get("common_data", 'chatinfo')
        return chatinfo

    @staticmethod
    def test_chatwindow():
        chatwindow = config.get("common_data", 'chatwindow')
        return chatwindow

    @staticmethod
    def test_sendbutton():
        sendbutton = config.get("common_data", 'sendbutton')
        return sendbutton

    @staticmethod
    def test_closechat():
        closechat = config.get("common_data", 'closechat')
        return closechat

    @staticmethod
    def test_humburger():
        humburger = config.get("common_data", 'humburger')
        return humburger

    @staticmethod
    def test_email():
        email = config.get("common_data", 'email')
        return email

    @staticmethod
    def test_emailtextarea():
        emailtextarea = config.get("common_data", 'emailtextarea')
        return emailtextarea

    @staticmethod
    def test_emailsend():
        emailsend = config.get("common_data", 'emailsend')
        return emailsend

    @staticmethod
    def test_emailwindowclose():
        emailwindowclose = config.get("common_data", 'emailwindowclose')
        return emailwindowclose

    @staticmethod
    def test_emailaddress():
        emailaddress = config.get("common_data", 'email-address')
        return emailaddress

    @staticmethod
    def test_endchat():
        endchat = config.get("common_data", 'endchat')
        return endchat

    @staticmethod
    def test_closechat2():
        closechat2 = config.get("common_data", 'closechat2')
        return closechat2

    @staticmethod
    def test_endchat2():
        endchat2 = config.get("common_data", 'endchat2')
        return endchat2



class Test_ndepdetails:
    @staticmethod
    def test_username():
        username = config.get("ndep_data", 'username')
        return username

    @staticmethod
    def test_password():
        password = config.get("ndep_data", 'password')
        return password

    @staticmethod
    def test_ndepurl():
        ndepurl = config.get("ndep_data", 'ndepurl')
        return ndepurl

    @staticmethod
    def test_authentication():
        otptext = config.get("ndep_data", 'otptext')
        return otptext

    @staticmethod
    def test_iframendep():
        ndepiframe = config.get("ndep_data", 'ndepiframe')
        return ndepiframe

    @staticmethod
    def test_usernamefield():
        usernamelocator = config.get("ndep_data", 'usernamelocator')
        return usernamelocator

    @staticmethod
    def test_passwordfield():
        passwordlocator = config.get("ndep_data", 'passwordlocator')
        return passwordlocator

    @staticmethod
    def test_engagementdetails():
        engagementdetails = config.get("ndep_data", 'engagementdetails')
        return engagementdetails

    @staticmethod
    def test_engagementtextbox():
        engagementtextbox = config.get("ndep_data", 'engagementtextbox')
        return engagementtextbox

    @staticmethod
    def test_engagementsearchbutton():
        engagementsearchbutton = config.get("ndep_data", 'engagementsearchbutton')
        return engagementsearchbutton

    @staticmethod
    def test_chatsummary():
        chatsummary = config.get("ndep_data", 'chatsummary')
        return chatsummary

    @staticmethod
    def test_ndeplogin():
        loginbutton = config.get("ndep_data", 'loginbutton')
        return loginbutton

    @staticmethod
    def test_sumamrywindow():
        chatsummarywindow = config.get("ndep_data", 'chatsummarywindow')
        return chatsummarywindow

    @staticmethod
    def test_loginfailed():
        privacyform = config.get("ndep_data", 'privacyform')
        return privacyform

    @staticmethod
    def test_backbutton():
        backbutton = config.get("ndep_data", 'backbutton')
        return backbutton

    @staticmethod
    def test_alertbox():
        alertbox = config.get("ndep_data", 'alertbox')
        return alertbox

    @staticmethod
    def test_projectname():
        projectname = config.get("ndep_data", 'projectname')
        return projectname

    @staticmethod
    def test_projectselect():
        projectselect = config.get("ndep_data", 'projectselect')
        return projectselect

    @staticmethod
    def test_projectlist():
        projectlist = config.get("ndep_data", 'projectlist')
        return projectlist

    @staticmethod
    def test_ActiveReports():
        ActiveReports = config.get("ndep_data", 'ActiveReports')
        return ActiveReports

    @staticmethod
    def test_reporting():
        reporting = config.get("ndep_data", 'reporting')
        return reporting

    @staticmethod
    def test_standradreport():
        standradreport = config.get("ndep_data", 'standradreport')
        return standradreport

    @staticmethod
    def test_vareport():
        vareport = config.get("ndep_data", 'vareport')
        return vareport

    @staticmethod
    def test_billablevareport():
        billablevareport = config.get("ndep_data", 'billablevareport')
        return billablevareport

    @staticmethod
    def test_daterangereport():
        daterangereport = config.get("ndep_data", 'daterangereport')
        return daterangereport

    @staticmethod
    def test_reportcountwindow():
        reportcountwindow = config.get("ndep_data", 'reportcountwindow')
        return reportcountwindow

    @staticmethod
    def test_tqb():
        tqb = config.get("ndep_data", 'tqb')
        return tqb

    @staticmethod
    def test_tqbframe():
        tqbframe = config.get("ndep_data", 'tqbframe')
        return tqbframe

    @staticmethod
    def test_selectvirtualagent():
        selectvirtualagent = config.get("ndep_data", 'selectvirtualagent')
        return selectvirtualagent

    @staticmethod
    def test_filterfield():
        filterfield = config.get("ndep_data", 'filterfield')
        return filterfield

    @staticmethod
    def test_searchtqb():
        searchtqb = config.get("ndep_data", 'searchtqb')
        return searchtqb

    @staticmethod
    def test_filters():
        filters = config.get("ndep_data", 'filters')
        return filters

    @staticmethod
    def test_tqbintractionwindow():
        tqbintractionwindow = config.get("ndep_data", 'tqbintractionwindow')
        return tqbintractionwindow