
class XpathRelation():
    def __init__(self):
        pass
    def findParent(self,el,elTarget='*'):
        return el+'/parent::'+elTarget

    def findChildren(self,el,elTarget='*'):
        return el+'/child::'+elTarget

    def findBrotherBehand(self,el,elTarget='*'):
        return el+'/following-sibling::'+elTarget

    def findBrotherAhead(self,el,elTarget='*'):
        return el+'/preceding-sibling::'+elTarget

    def findAncestor(self,el,elTarget='*'):
        return el+'/ancestor::'+elTarget

    def findText(self,el,text):
        return '//{}[normalize-space(text()) and normalize-space(.)="{}"]'.format(el,text)

    def findDisplayByClass(self,driver,className):
        '''
        页面中有多个class相同的，但只有一个是display显示时进行查找，返回xpath
        多数情况下同一页面的下拉框、树形选择框等可能是这种方式
        :param driver:
        :param className:
        :return:
        '''
        target='//*[@class="{}"]'.format(className)
        els = driver.find_elements_by_xpath(target)
        for i, el in enumerate(els):
            style = el.get_attribute('style')
            # print('style:', style)
            if (style.find('display: none') == -1):
                return '({})[{}]'.format(target,i + 1)
