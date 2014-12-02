# The task is simple, print the password and username for the input key word.
# First step run as: DONE
#   #python idkeeper.py gmail
#   #wang@gmail.com:123456
#
# Then next step may provide interactive mode: DONE
#   #python idkeeper.py
#   #Input the web name:
#    > gmail
#   #Your account for gmail is:
#   #wang@gmail.com:123456
#
# Then next step may provide fuzzy matching in case you can't remember the full/correct name of the web: DONE
#   #python idkeeper.py
#   #Input the web name:
#     > mail
#   #Do you mean:
#    gmail
#    amail
#    bmail
#   Select the correct name and input again:
#    >gmail
#   #Your account for gmail is:
#   #wang@gmail.com:123456
#
# Then next step should provide encrypt for the accounts content, some accounts are critical. DONE
#
# Then next step should move the critical data to another file, and encrypt that file with a different way.
#
# Then next step may provide binary file to run directly, for both linux and windows.
from sys import argv
from code import decode

box = {
        "wifi":"aacZEknf9G7kKGBbolNjaEBI9dHI4X2dlE9TgtepYnc=",
        "126mail":"4/Z0jtUFUsk2vUt4yks/Xi1pYnLpDPLW7Vnym1J+x1Q=",
        "douban":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "dangdang":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "amazon":"5fHvJfeWPc+g0JS+unEq0HBcQPu8D1F2e2fMRVJwoU8=",
        "jd":"2bsS5howcenNxeVNkJQye0BI9dHI4X2dlE9TgtepYnc=",
        "suning":"2cDxfRliFDLflROCyDCCS9Cgwsh/sDxFEHsiSuDDp8s=",
        "facebook":"5fHvJfeWPc+g0JS+unEq0GH/1PrT0gVzcAYFrEst84o=",
        "twitter":"aacZEknf9G7kKGBbolNjaEBI9dHI4X2dlE9TgtepYnc=",
        "pinterest":"aacZEknf9G7kKGBbolNjaEBI9dHI4X2dlE9TgtepYnc=", 
        "kanbox":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "dropbox":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "115":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "box":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "jinshan box":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "58":"Xcwy2fogGcZSOveDeK2rd0BI9dHI4X2dlE9TgtepYnc=",
        "skype":"CgDPTnLwaPj25hhIrzo39ObVNCgs4+uxLBVxmORcDis=",
        "battlecn":"TQVefQF00lHYsnDFJD+tEkBI9dHI4X2dlE9TgtepYnc=",
        "csdn":"3pGNOhaH3CAv2cFoFva/NkBI9dHI4X2dlE9TgtepYnc=",
        "luexiao":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "linkedin":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "baidu":"aacZEknf9G7kKGBbolNjaEBI9dHI4X2dlE9TgtepYnc=",
        "sanbeidanchi":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "yihaodian":"5fHvJfeWPc+g0JS+unEq0EJbFZJYumZ63yUtAX5v1VU=",
        "shuishouji":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "evernote":"5fHvJfeWPc+g0JS+unEq0HBcQPu8D1F2e2fMRVJwoU8=",
        "51job":"WtnuafI18sVeKwQYnehzAEBI9dHI4X2dlE9TgtepYnc=",
        "windnle":"5fHvJfeWPc+g0JS+unEq0Ey/ls5ycdiNWdwrb7nYEpg=",
        "8europ":"aacZEknf9G7kKGBbolNjaEBI9dHI4X2dlE9TgtepYnc=",
        "dingxiangyuan":"AmjQfq6AwJsWEOWDWsrP30BI9dHI4X2dlE9TgtepYnc=",
        "topcoder":"D3oWBKoUJUzFadk7MQsUzPPGzu2o3Mwqa1u6m+PMiqw=",
        "pbccrc":"YuKyl1P8pAPqkWQ6JohLQkBI9dHI4X2dlE9TgtepYnc=",
        "github":"UFYPpswX6ehwiS3r41WzqEBI9dHI4X2dlE9TgtepYnc=",
        "slideshare":"VawSGufaDgVg1H8k1ZV7zkBI9dHI4X2dlE9TgtepYnc=",
        "gmail old":"KVn59Plvd9MoQ8hjCJyVu4HKMQ6A89FTj48jT/6QrOo=",
        "chinahr":"O8dL1iqBec29XYsYhykB+EBI9dHI4X2dlE9TgtepYnc=",
        "liepin":"pP9sLMbF9xQF+jmM4TgmwkBI9dHI4X2dlE9TgtepYnc=",
        "stackoverflow":"Ud7eGPY39HL8oqXWDG44NVxio7D2o7US6VLh7y6HfHo=",
        "slideshare":"QYfI5X9qpFe9JcW9ciCXR2GkRSW/3ZbGAuk0c1gNYvM=",
        "suishouji":"SEGuMENUQ0aTsSsG2plVKEBI9dHI4X2dlE9TgtepYnc=",
        "POJ":"aacZEknf9G7kKGBbolNjaEBI9dHI4X2dlE9TgtepYnc=",
        "leetcode":"NlsrKYu/W13jOFHk6OUAKkBI9dHI4X2dlE9TgtepYnc=",
        "7yes":"fVLRjakX8NUNYY1X6IrnR/68Q7lfGfEqGcBjH73NVo0=",
        "siemens":"hTed5CRoKJkm2RbTwTp9bkBI9dHI4X2dlE9TgtepYnc=",
        "live":"jlls3y89Vpc44E8aPaWVlEqgiNM37TlN93nLnYJGw53QeNK68tGEV707TsOsfpH5QlsVkli6ZnrfJS0Bfm/VVQ=="
        }

if len(argv) == 2:
    script_name, account = argv
else:
    account = raw_input("Input the web name:")

candidate = []
if account == 'all':
    for name in box.keys():
        print name,
        print "\t\t",
        print decode(box[name])
elif box.has_key(account) == False:
    for name in box.keys():
        if name.find(account) == -1:
            pass
        else:
            candidate.append(name)
    if len(candidate):
        print "Do you mean:"
        for n in candidate:
            print "\t\t",
            print n
        account = raw_input(">")    
        print decode(box[account])
    else:
        print "Can't find the account '%s', try the correct name." % account
        exit(1)
else:
    print decode(box[account])

