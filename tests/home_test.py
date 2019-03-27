import time
import unittest
from ddt import ddt, data, unpack

from tests.config_test import BaseTest
from pages.home import Home
from utilities.test_status import TestStatus
# from utilities.read_data import get_csv_data


@ddt
class HomeTest(BaseTest):
    def setUp(self):
        self.page = Home(self.driver)
        self.ts = TestStatus(self.driver)

    @data(('http://giadinh.net.vn/', ),
          ('http://giadinh.net.vn/gia-dinh.htm',),
          ('http://giadinh.net.vn/phap-luat/vu-kien-tac-quyen-vo-ngay-xua-tuan-chau-ha-noi-phai-tra-10-tien-ban-ve-cho-dao-dien-viet-tu-20190320102329201.htm',),
          ('http://kenh14.vn/',),
          ('http://kenh14.vn/an-ca-the-gioi.chn',),
          ('http://kenh14.vn/dien-ma-quen-cam-mic-fan-treu-ariana-grande-nho-mang-day-du-dung-cu-khi-hanh-nghe-chi-oi-20190320145433714.chn',),
          ('http://soha.vn/',),
          ('http://soha.vn/quoc-te.htm',),
          ('http://soha.vn/neu-be-gai-9-tuoi-bi-xam-hai-co-gai-bi-cuong-hon-la-con-cac-ong-ay-20190320102159289.htm',),
          ('http://afamily.vn/',),
          ('http://afamily.vn/doi-song.chn',),
          ('http://afamily.vn/doi-tu-be-boi-cua-sao-nu-trum-so-trong-vu-an-jang-ja-yeon-vung-trom-chan-goi-voi-trai-tre-kem-17-tuoi-bi-to-thue-sat-thu-giet-tra-thu-20190318150338082.chn',),
          ('http://cafef.vn/',),
          ('http://cafef.vn/thoi-su.chn',),
          ('http://cafef.vn/luong-co-phieu-do-ty-phu-pham-nhat-vuong-nam-giu-da-tang-len-10-ty-usd-20190320112101742.chn',),
          ('http://cafebiz.vn/',),
          ('http://cafebiz.vn/thoi-su.chn',),
          ('http://cafebiz.vn/tro-choi-vuong-quyen-ty-do-tai-macau-tham-cung-noi-chien-giua-4-nguoi-vo-khien-ca-de-che-casino-huyen-thoai-dung-tren-bo-sup-do-20190319164718523.chn',),
          ('https://autopro.com.vn/',),
          ('https://autopro.com.vn/tin-tuc.chn',),
          ('https://autopro.com.vn/mitsubishi-trinh-lang-mini-xpander-co-ten-ek-x-20190319163118585.chn',),
          ('http://gamek.vn/',),
          ('http://gamek.vn/game-online.chn',),
          ('http://gamek.vn/he-lo-nhung-thong-tin-dau-tien-ve-tua-game-ban-tia-sniper-elite-5-20190320121524851.chn',),
          ('http://sport5.vn/',),
          ('http://sport5.vn/bong-da-viet-nam.htm',),
          ('http://sport5.vn/chot-danh-sach-u23-viet-nam-trong-dem-tien-linh-bi-loai-dinh-trong-duoc-trao-co-hoi-20190320103106123.htm',),
          ('http://genk.vn/', ),
          ('http://genk.vn/internet.chn',),
          ('http://genk.vn/google-ra-mat-nen-tang-stadia-choi-game-khung-khong-can-may-tinh-xin-chi-can-trinh-duyet-chrome-20190320015205167.chn',),
          ('https://thethao.tuoitre.vn/',),
          ('https://thethao.tuoitre.vn/tin-tuc.htm',),
          ('https://thethao.tuoitre.vn/tien-dao-nguyen-tien-linh-toi-khong-co-duyen-voi-giai-u-23-chau-a-20190320105931608.htm',),
          ('https://congnghe.tuoitre.vn/',),
          ('https://congnghe.tuoitre.vn/nhip-song-so.htm',),
          ('https://congnghe.tuoitre.vn/facebook-luu-lai-video-ngay-ca-khi-ban-chua-dang-len-20180403110149061.htm',),
          ('https://dulich.tuoitre.vn/',),
          ('https://dulich.tuoitre.vn/co-hoi-du-lich.htm',),
          ('https://dulich.tuoitre.vn/du-lich-phap-thuy-si-duc-ha-lan-20170617890.htm',),
          ('https://tv.tuoitre.vn/',),
          ('https://tv.tuoitre.vn/dac-sac.htm',),
          ('https://tv.tuoitre.vn/tuyen-duong-10-guong-mat-tre-viet-nam-tieu-bieu-2018-62785.htm',),
          ('https://phunu.nld.com.vn/',),
          ('https://phunu.nld.com.vn/lam-dep.htm',),
          ('https://phunu.nld.com.vn/tam-su/suyt-tan-vo-gia-dinh-chi-vi-tro-choi-tinh-mot-dem-20190314101326024.htm',),
          ('https://thitruong.nld.com.vn/',),
          ('https://thitruong.nld.com.vn/du-lich.htm',),
          ('https://thitruong.nld.com.vn/du-lich/du-lich-viet-nam-can-nguon-cung-nhieu-hon-nua-de-du-khach-quay-tro-lai-20190320135210313.htm',),
          ('https://diaoc.nld.com.vn/',),
          ('https://diaoc.nld.com.vn/du-an.htm',),
          ('https://diaoc.nld.com.vn/nha-dep/11-mon-noi-that-thu-vi-ban-co-the-tu-lam-cho-can-nha-cua-minh-20190225133154706.htm',),
          ('https://tv.nld.com.vn/',),
          ('https://tv.nld.com.vn/thoi-su-trong-nuoc.htm',),
          ('https://tv.nld.com.vn/thoi-su-quoc-te/iphone-xs-xs-max-xr-ra-mat-camera-va-pin-tot-hon-co-ban-2-sim-12965.htm',),
          ('http://vneconomy.vn/',),
          ('http://vneconomy.vn/thoi-su.htm',),
          ('http://vneconomy.vn/nam-cau-hoi-phac-thao-mo-hinh-tang-truong-kinh-te-2021-2030-20190320145127379.htm',),
          ('http://toquoc.vn/',),
          ('http://toquoc.vn/thoi-su.htm',),
          ('http://toquoc.vn/chu-tich-lien-doan-o-to-quoc-te-to-chuc-giai-dua-xe-cong-thuc-1-la-co-hoi-de-viet-nam-phat-trien-du-lich-dam-bao-an-toan-giao-thong-20190320103605359.htm',),
          ('https://vietnammoi.vn/',),
          ('https://vietnammoi.vn/thoi-su.htm',),
          ('https://vietnammoi.vn/neu-uong-tra-ca-phe-cach-nay-nguy-co-ung-thu-tang-gap-doi-20190322105119216.htm',),
          ('https://vietnambiz.vn/',),
          ('https://vietnambiz.vn/thoi-suhtm',),
          ('https://vietnambiz.vn/chinh-thuc-tang-gia-dien-836-tu-hom-nay-20-3-2019032011432987.htm',),
          )
    @unpack
    def test_domain(self, domain):
        time.sleep(4)
        flag, msg = self.page.verify_domain(domain)
        self.ts.mark_final('Kiểm tra domain', flag, msg)


if __name__ == '__main__':
    unittest.main()
