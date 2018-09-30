import allure
import pytest


class Test():
    @allure.step('执行更新学院操作')
    def test01(self):
        print('执行更新学院操作')
    @allure.step('执行更新学院操作')

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test02(self):
        allure.attach('断言开始','更新学院操作')
        print('执行更新学院操作')
        allure.attach('断言结束','更新学院成功')
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        print('test03被执行')
        assert 0

