import schedule
import make_img as mk
import send_msg_tel as smt
import send_msg_wpp as smw


def send_daily():
    mk.new()
    smt.send_photo()
    smw.send_photo()


schedule.every().day.at("17:02").do(send_daily)

while True:
    schedule.run_pending()
