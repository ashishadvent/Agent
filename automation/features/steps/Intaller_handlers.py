from behave import *
from Config_File import configuration
from WLA_Installer import WLA_Installer


cfg_path=r'C:\Users\administrator\test\automation\features\config_file\WLA\config.txt' #config file =contails all the path for installer and managers.
temp=configuration(cfg_path)    
temp1=temp.get_values()                     #fetching values from config file


#assigning values into variable 
default_path_file=temp1['default_path_file'].encode('string-escape')
non_default_path=temp1['non_default_path'].encode('string-escape')
def_agent_path=temp1['def_agent_path'].encode('string-escape')
non_def_agent_path=temp1['non_def_agent_path'].encode('string-escape')
dotnet_pre_check=temp1['dotnet_pre_check'].encode('string-escape')
win_driver=temp1['win_driver'].encode('string-escape')
silent_install_file=temp1['default_msi_file'].encode('string-escape')
#assigning end 

#silent install command making#
silent_command_install="msiexec /i "+silent_install_file+" /qn REBOOT=ReallySuppress"
silent_command_uninstall="msiexec /x "+silent_install_file+" /qn REBOOT=ReallySuppress"
#end#



@given('dotnet pre-requisite check')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.install_prereq(dotnet_pre_check)

@when('install WLA agent at default location')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.install_agent(win_driver)

@when('WLA agent is installed at default location')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.validate_install()
    
@when('Silent install WLA agent')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.silent_install(silent_command_install)


@then('Remove WLA agent')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.remove_agent(win_driver)
    
@then('Silent remove WLA agent')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.silent_uninstall(silent_command_uninstall)
    
@when('install WLA agent at non-default location')
def step_impl(context):
    temp=WLA_Installer(default_path_file,inst_path=non_default_path)
    temp.install_agent(win_driver)
    
@then('WLA agent is installed at non-default location')
def step_impl(context):
    temp=WLA_Installer(default_path_file,inst_path=non_default_path)
    temp.validate_install()

@when('repair WLA agent')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.repair_agent(win_driver)

@when('Remove WLA agent')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.remove_agent(win_driver)

@when('modify WLA agent')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.modify_agent(win_driver)

@when('Upgrade WLA agent')
def step_impl(context):
    temp=WLA_Installer(default_path_file)
    temp.WLA_Upgrade(win_driver)

@then('Enable WLA Agent at default location')
def step_impl(context):
    temp=WLA_Installer(default_path_file)

