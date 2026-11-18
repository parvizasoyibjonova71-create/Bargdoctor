import json
def svg(t,c):
    f=f'fill="{c}" fill-opacity=".8"'
    if t=='flower':
        b=''.join(f'<ellipse cx="50" cy="22" rx="6" ry="13" transform="rotate({i*45} 50 38)" {f}/>' for i in range(8))
        b+=f'<circle cx="50" cy="38" r="6" fill="currentColor"/><path d="M50 46V92M50 72q-18-4-22-18q16 0 22 18M50 78q18-4 22-18q-16 0-22 18"/>'
    elif t=='tulip':
        b=f'<path d="M33 24Q33 54 50 56Q67 54 67 24L58 34L50 20L42 34Z" {f}/><path d="M50 56V92M50 86Q28 80 27 58Q46 64 50 86"/>'
    elif t=='tree':
        b=f'<path d="M50 92V58M50 76l-12-12M50 70l12-12"/><circle cx="50" cy="36" r="22" {f}/><circle cx="32" cy="50" r="13" {f}/><circle cx="68" cy="50" r="13" {f}/>'
    elif t=='leafy':
        b='<path d="M50 92V16"/>'+''.join(f'<path d="M50 {y}q-22-4-26-22q22 0 26 22" {f}/><path d="M50 {y-10}q22-4 26-22q-22 0-26 22" {f}/>' for y in (86,64,42))
    elif t=='cactus':
        b=f'<rect x="38" y="20" width="24" height="72" rx="12" {f}/><path d="M38 66h-10q-6 0-6-6V44M62 54h10q6 0 6-6V34"/>'
    elif t=='fern':
        b='<path d="M50 94Q48 50 66 10"/>'+''.join(f'<path d="M{50+(-(k)*0.5)} {90-k*9}l-20 -8M{50+(-(k)*0.5)} {90-k*9}l20 -10"/>' for k in range(1,8))
    elif t=='bulb':
        b=f'<path d="M50 38C16 44 20 90 50 90C80 90 84 44 50 38Z" {f}/><path d="M50 38Q48 18 64 10M42 90v7M50 90v8M58 90v7"/>'
    elif t=='fruit':
        b=f'<circle cx="50" cy="60" r="28" {f}/><path d="M50 32q0-10 8-14M50 34q-14-10-24-2q10 10 24 2"/>'
    elif t=='root':
        b=f'<path d="M34 30Q50 20 66 30L54 92Q50 98 46 92Z" {f}/><path d="M50 26V8M44 26q-8-12-10-18M56 26q8-12 10-18"/>'
    elif t=='grain':
        b='<path d="M50 94V30"/>'+''.join(f'<ellipse cx="43" cy="{y}" rx="4" ry="9" transform="rotate(-25 43 {y})" {f}/><ellipse cx="57" cy="{y}" rx="4" ry="9" transform="rotate(25 57 {y})" {f}/>' for y in (44,32,20))+f'<ellipse cx="50" cy="10" rx="4" ry="9" {f}/>'
    else:
        b=f'<circle cx="50" cy="54" r="34" {f}/><path d="M50 22Q30 50 50 86M50 22Q70 50 50 86M18 54Q50 44 82 54"/>'
    return f'<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{b}</svg>'
R,O,G,P,Y,W,B,V='#D9534F','#F0A030','#5FAE6B','#D86A9A','#F2C94C','#F4F1EC','#9C6B43','#7C5CBF'
L=[
('fruit',R,'veg','Pomidor','Помидор','Tomato','Solanum lycopersicum'),
('leafy',G,'veg','Bodring','Огурец','Cucumber','Cucumis sativus'),
('fruit',O,'veg','Qalampir','Перец','Pepper','Capsicum annuum'),
('bulb',B,'veg','Kartoshka','Картофель','Potato','Solanum tuberosum'),
('bulb',W,'veg','Piyoz','Лук','Onion','Allium cepa'),
('root',O,'veg','Sabzi','Морковь','Carrot','Daucus carota'),
('cab',G,'veg','Karam','Капуста','Cabbage','Brassica oleracea'),
('fruit',V,'veg','Baqlajon','Баклажан','Eggplant','Solanum melongena'),
('fruit',O,'veg','Qovoq','Тыква','Pumpkin','Cucurbita pepo'),
('bulb',W,'veg','Sarimsoq','Чеснок','Garlic','Allium sativum'),
('fruit',V,'fruit','Uzum','Виноград','Grape','Vitis vinifera'),
('tree',R,'fruit','Olma','Яблоня','Apple tree','Malus domestica'),
('tree',O,'fruit','Oʻrik','Абрикос','Apricot','Prunus armeniaca'),
('fruit',R,'fruit','Anor','Гранат','Pomegranate','Punica granatum'),
('tree',V,'fruit','Anjir','Инжир','Fig','Ficus carica'),
('tree',P,'fruit','Shaftoli','Персик','Peach','Prunus persica'),
('tree',R,'fruit','Olcha','Вишня','Cherry','Prunus cerasus'),
('tree',V,'fruit','Tut','Шелковица','Mulberry','Morus alba'),
('cab',Y,'fruit','Qovun','Дыня','Melon','Cucumis melo'),
('cab',G,'fruit','Tarvuz','Арбуз','Watermelon','Citrullus lanatus'),
('grain',Y,'field','Bugʻdoy','Пшеница','Wheat','Triticum aestivum'),
('flower',W,'field','Paxta','Хлопчатник','Cotton','Gossypium hirsutum'),
('grain',G,'field','Guruch','Рис','Rice','Oryza sativa'),
('grain',Y,'field','Makkajoʻxori','Кукуруза','Maize','Zea mays'),
('flower',P,'flower','Atirgul','Роза','Rose','Rosa'),
('tulip',R,'flower','Lola','Тюльпан','Tulip','Tulipa'),
('flower',Y,'flower','Kungaboqar','Подсолнух','Sunflower','Helianthus annuus'),
('flower',W,'flower','Moychechak','Ромашка','Chamomile','Matricaria chamomilla'),
('flower',V,'flower','Lavanda','Лаванда','Lavender','Lavandula'),
('flower',P,'flower','Pion','Пион','Peony','Paeonia'),
('flower',O,'flower','Gulxayri','Календула','Marigold','Calendula officinalis'),
('tulip',V,'flower','Susan','Ирис','Iris','Iris'),
('leafy',G,'herb','Yalpiz','Мята','Mint','Mentha'),
('leafy',G,'herb','Rayhon','Базилик','Basil','Ocimum basilicum'),
('fern',G,'herb','Shivit','Укроп','Dill','Anethum graveolens'),
('leafy',G,'herb','Jaʼfari','Петрушка','Parsley','Petroselinum crispum'),
('cactus',G,'herb','Aloe','Алоэ','Aloe vera','Aloe vera'),
('leafy',G,'indoor','Monstera','Монстера','Monstera','Monstera deliciosa'),
('cactus',G,'indoor','Kaktus','Кактус','Cactus','Cactaceae'),
('leafy',G,'indoor','Sansevieriya','Сансевиерия','Snake plant','Dracaena trifasciata'),
('flower',P,'indoor','Orxideya','Орхидея','Orchid','Phalaenopsis'),
('fern',G,'indoor','Paporotnik','Папоротник','Fern','Nephrolepis'),
('tree',G,'tree','Chinor','Чинара','Plane tree','Platanus orientalis'),
('tree',G,'tree','Terak','Тополь','Poplar','Populus'),
('tree',G,'tree','Qaragʻay','Сосна','Pine','Pinus'),
('tree',G,'tree','Yongʻoq','Грецкий орех','Walnut','Juglans regia'),
('tree',P,'tree','Bodom','Миндаль','Almond','Prunus dulcis'),
('tree',G,'tree','Pista','Фисташка','Pistachio','Pistacia vera'),
('fern',B,'tree','Saksovul','Саксаул','Saxaul','Haloxylon'),
]
RARE=[('tree',Y,'EN','Ginkgo','Гинкго','Ginkgo','Ginkgo biloba',''),
('fern',G,'CR','Vollemiya','Воллемия','Wollemi pine','Wollemia nobilis','≈100'),
('leafy',R,'VU','Venera pashshaxoʻri','Венерина мухоловка','Venus flytrap','Dionaea muscipula',''),
('leafy',G,'VU','Velvichiya','Вельвичия','Welwitschia','Welwitschia mirabilis',''),
('flower',V,'CR','Qust (Saussurea)','Соссюрея костус','Costus','Saussurea costus',''),
('tree',G,'EN','Araukariya','Араукария','Monkey puzzle','Araucaria araucana',''),
('tulip',P,'EN','Paphiopedilum','Пафиопедилум','Slipper orchid','Paphiopedilum','')]
plants=[dict(i=i,s=svg(t,c),c=cat,n=[uz,ru,en],l=lat) for i,(t,c,cat,uz,ru,en,lat) in enumerate(L)]
rare=[dict(s=svg(t,c),k=k,n=[uz,ru,en],l=lat,q=q) for (t,c,k,uz,ru,en,lat,q) in RARE]
tpl=open('template.html',encoding='utf-8').read()
out=tpl.replace('__PLANTS__',json.dumps(plants,ensure_ascii=False)).replace('__RARE__',json.dumps(rare,ensure_ascii=False))
open('index.html','w',encoding='utf-8').write(out)
print(len(out))