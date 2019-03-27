import utilities.custom_logger as cl
import logging
from base.base_page import BasePage


class NavigationPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _trang_moi_nhat = ('//*[@id="cat9999"]/a', 'xpath')
    _all_courses = "My Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _tin_noi_bat = ('//*[@id="LoadHLHome"]/div[1]/h2/a', 'xpath')
    _video_noi_bat = ('//*[@id="TotalBox9"]/div[1]/div[2]/div[1]/div/a/img', 'xpath')

    def navigate_to_trang_moi_nhat(self):
        self.element_click(locator=self._trang_moi_nhat[0], locator_type=self._trang_moi_nhat[1])

    def navigate_to_trang_video(self):
        self.driver.get('http://giadinh.net.vn/video-page.htm')

    def navagate_to_trang_xa_hoi(self):
        self.driver.get('http://giadinh.net.vn/xa-hoi.htm')

    def navigate_to_trang_gia_dinh(self):
        self.driver.get('http://giadinh.net.vn/gia-dinh.htm')

    def navigate_to_trang_song_khoe(self):
        self.driver.get('http://giadinh.net.vn/song-khoe.htm')

    def navigate_to_trang_giai_tri(self):
        self.driver.get('http://giadinh.net.vn/giai-tri.htm')

    def navigate_to_trang_phap_luat(self):
        self.driver.get('http://giadinh.net.vn/phap-luat.htm')

    def navigate_to_trang_vong_tay_nhan_ai(self):
        self.driver.get('http://giadinh.net.vn/vong-tay-nhan-ai.htm')

    def navigate_to_trang_thi_truong(self):
        self.driver.get('http://giadinh.net.vn/thi-truong.htm')

    def navigate_to_trang_bon_phuong(self):
        self.driver.get('http://giadinh.net.vn/bon-phuong.htm')

    def navigato_to_trang_detail_tin(self):
        tin_noi_bat = self.get_element(self._tin_noi_bat[0], self._tin_noi_bat[1])
        self.element_click(element=tin_noi_bat)
        # self.driver.get('http://giadinh.net.vn/gia-dinh/biet-chong-trot-say-nang-vo-ra-ke-hoach-yeu-lai-tu-dau-khien-ke-thu-ba-ngam-dang-nuot-cay-20190226225052786.htm')

    def navigate_to_trang_video_detail(self):
        video_noi_bat = self.get_element(self._video_noi_bat[0], self._video_noi_bat[1])
        self.element_click(element=video_noi_bat)
