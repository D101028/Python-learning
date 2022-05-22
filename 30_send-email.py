# 寄送 Email 的程式
# 準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
# msg["From"]="寄件人"
# msg["To"]="收件人"
# msg["Subject"]="內容"
msg["From"]="Damont101028@gmail.com"
msg["To"]="Damont0976318970@gmail.com"
msg["Subject"]="你好大"

# 寄送純文字內容
msg.set_content("測試看看")

# 寄送比較多樣式的內容
msg.add_alternative("<h3>優惠券</h3>滿五百送一百喔", subtype="html")

# 連線到 SMKTP Server, 驗證寄件人身分
import smtplib
# 到網路上查詢 gmail smtp server
# server=smtplib.SMTP_SSL("主機名稱", 連接埠號)
server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.login("帳號", "密碼")
server.login("Damont101028@gmail.com", "ztugbahhicfseasz")
server.send_message(msg)
server.close()
