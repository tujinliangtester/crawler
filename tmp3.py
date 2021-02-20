from collections import Counter

a='''
pGameData->m_mjHuType.byTianHu=4;
	//32番
	pGameData->m_mjHuType.byDiHu=4;
	//88番牌型（5种）
	pGameData->m_mjHuType.byDaSiXi=255;
	pGameData->m_mjHuType.byDaSanYuan=255;
	pGameData->m_mjHuType.byJiuLianBaoDeng=255;
	pGameData->m_mjHuType.bySiGang=4;
	pGameData->m_mjHuType.byLianQiDui=255;
	//64番牌型（5种）
	pGameData->m_mjHuType.byXiaoSiXi=255;
	pGameData->m_mjHuType.byXiaoSanYuan=255;
	pGameData->m_mjHuType.byZiYeSe=255;
	pGameData->m_mjHuType.bySiAnKe=255;
	pGameData->m_mjHuType.byYSShuangLongHui=255;
	//48番牌型（2种）
	pGameData->m_mjHuType.byYSSiTongShun=255;
	pGameData->m_mjHuType.byYSSiJieGao=255;
	//32番牌型（3种）
	pGameData->m_mjHuType.byYiSeSiBuGao=255;
	pGameData->m_mjHuType.byHunYaoJiu=255;
	pGameData->m_mjHuType.bySanGang=255;
	//24番牌型（4种）
	pGameData->m_mjHuType.byQiDui=2;
	pGameData->m_mjHuType.byLongQiDui=3;
	pGameData->m_mjHuType.byQingYiSe=2;
	pGameData->m_mjHuType.byYiSSTongShun=255;
	pGameData->m_mjHuType.byYiSSJieGao=255;
	//16番牌型（3种）
	pGameData->m_mjHuType.byQiangLong=255;
	pGameData->m_mjHuType.byYiSeSanBuGao=255;
	pGameData->m_mjHuType.bySanAnKe=255;
	//12番牌型（3种）
	pGameData->m_mjHuType.byDaYuWu=255;
	pGameData->m_mjHuType.byXiaoYuWu=255;
	pGameData->m_mjHuType.bySanFengKe=255;
	//8番牌型（4种）
	pGameData->m_mjHuType.byMiaoShouHuiChun=1;
	pGameData->m_mjHuType.byHaiDiLaoYue=1;
	pGameData->m_mjHuType.byGSH=1;
	pGameData->m_mjHuType.byQiangGangHu=1;
	pGameData->m_mjHuType.byGHP=1;
	//6番牌型（5种）
	pGameData->m_mjHuType.byPengPengHu=1;
	pGameData->m_mjHuType.byHunYiSe=255;
	pGameData->m_mjHuType.byQuanQiuRen=255;
	pGameData->m_mjHuType.byShuangAnGang=255;
	pGameData->m_mjHuType.byShuangJianKe=255;
	//4番牌型（4种）
	pGameData->m_mjHuType.byQuanDaiYao=2;
	pGameData->m_mjHuType.byBuQiuRen=255;
	pGameData->m_mjHuType.byShuangMingGang=255;
	pGameData->m_mjHuType.byHuJueZhang=255;
	//2番牌型（7种）
	pGameData->m_mjHuType.byJianKe=255;
	pGameData->m_mjHuType.byMenQianQing=1;
	pGameData->m_mjHuType.byPingHu=255;
	pGameData->m_mjHuType.bySiGuiYi=255;
	pGameData->m_mjHuType.byShuangAnKe=255;
	pGameData->m_mjHuType.byAnGang=255;
	pGameData->m_mjHuType.byDuanYao=1;		
	//1番牌型（10种）
	pGameData->m_mjHuType.byYiBanGao=255;
	pGameData->m_mjHuType.byLianLiu=255;
	pGameData->m_mjHuType.byLaoShaoFu=255;
	pGameData->m_mjHuType.byYaoJiuKe=255;
	pGameData->m_mjHuType.byMingGang=255;
	pGameData->m_mjHuType.byBianZhang=255;
	pGameData->m_mjHuType.byKanZhang=255;
	pGameData->m_mjHuType.byDanDiao=1;
	pGameData->m_mjHuType.byZiMo=255;
	pGameData->m_mjHuType.byQingYiSeQiDui=255;
	pGameData->m_mjHuType.byQingYiSeYiTiaoLong=255;
	pGameData->m_mjHuType.byQuanBuKao=255;
	pGameData->m_mjHuType.byQiXingBuKao=255;
	pGameData->m_mjHuType.byDaPiao=255;
	pGameData->m_mjHuType.byJiangDui=3;
	'''
b=a.split(';')
s={}
for i in b:
    c=i.split('=')
    if(len(c)<2):
        print('len(c)<2')
        print(c)
    elif(c[1]!='255'):
        s[c[0]]=c[1]

c=Counter(s).most_common() #返回一个列表，按照dict的value从大到小排序
for i in c:

    print(i)# 返回值是一个list，list里面的元素是tuple的形式


