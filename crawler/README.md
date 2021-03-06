About xpath, recommend this [xpath tutorial](http://www.zvon.org/comp/r/tut-XPath_1.html)       
[Scrapy offcial install doc](http://doc.scrapy.org/en/latest/intro/install.html)
`pip install -r requirements.txt`     

## crawler名稱和功能

-	councilors: 現任議員資料
-	councilors\_terms: 歷屆議員資料（不一定包含現任的資料）
-	bills: 議案資料
-	meeting\_minutes: 議事錄資料（開會出缺席、表決）
-   suggestions: 議員配合款

## 各縣市
以下缺漏，可能也是暫時找不到資料來源        

### 北部

`X` 表示找不到原始文字可讀取資料        
`O` 表示已做        
`*` 表市議會官網無資料，來源改採[地方議會議事資料管理平台](http://digital.tpa.gov.tw/)      
空白表示還沒開工

| 縣市   | 代號      | 現任議員 | 工程建議款 | 議案 | 議事錄 |
|--------|-----------|----------|------------|------|--------|
| 基隆市 | kmc       |    O     |     O      |  *   |   O    |
| 臺北市 | tcc       |    O     |     O      |  O   |   O    |
| 新北市 | ntp       |    O     |     O      |  O   |   O    |
| 桃園市 | tycc      |    O     |     O      |  *   |   O    |
| 新竹市 | hsinchucc |    O     |     O      |  *   |   X    |
| 新竹縣 | hcc       |    O     |     O      |  O   |   X    |
| 苗栗縣 | mcc       |    O     |     O      |  *   |   X    |
| 宜蘭縣 | ilcc      |    O     |     O      |  O   |   O    |


### 中部

| 縣市   | 代號  | 現任議員 | 工程建議款 | 議案 | 議事錄 |
|--------|-------|----------|------------|------|--------|
| 臺中市 | tccc  |    O     |     O      |  O   |        |
| 彰化縣 | chcc  |    O     |     O      |  O   |        |
| 南投縣 | ntcc  |    O     |     O      |  X   |        |
| 雲林縣 | ylcc  |    O     |     O      |  *   |        |
| 嘉義縣 | cyscc |    O     |     O      |  O   |        |
| 嘉義市 | cycc  |    O     |     O      |  O   |        |

### 東部

| 縣市   | 代號      | 現任議員 | 工程建議款 | 議案 | 議事錄 |
|--------|-----------|----------|------------|------|--------|
| 花蓮縣 | hlcc      |    O     |     O      |  *   |   X    |
| 臺東縣 | taitungcc |    O     |     O      |  O   |        |

### 南部

| 縣市   | 代號 | 現任議員 | 工程建議款 | 議案 | 議事錄 |
|--------|------|----------|------------|------|--------|
| 臺南市 | tncc |    O     |     O      |  O   |   O    |
| 高雄市 | kcc  |    O     |     O      |  O   |   O    |
| 屏東縣 | ptcc |    O     |     O      |  O   |   X    |

### 外島

| 縣市   | 代號      | 現任議員 | 工程建議款 | 議案 | 議事錄 |
|--------|-----------|----------|------------|------|--------|
| 連江縣 | mtcc      |    O     |     O      |  *   |        |
| 金門縣 | kmcc      |    O     |     O      |  O   |   X    |
| 澎湖縣 | phcouncil |    O     |     O      |  O   |        |

## councilors.json 格式範例說明

### 議員所在的選區資訊

```json
{
    "county": "臺中市", 
    "constituency": "第01選區",
    "district": "大甲區、大安區、外埔區", 
}
```

| 欄位名稱     | 說明                  |
|--------------|-----------------------|
| county       | 選區所在的縣市        |
| constituency | 選區編號 ex. 第一選區 |
| district     | 選區所包含的區域      |

### 議員個人資料

```json
{
    "name": "王大名", 
    "party": "g0v黨", 
    "education": [
        "g0v畢業"
    ],
    "experience": [
        "g0v 議員投票指南第 100 屆黑客松主辦", 
        "g0v 議員投票指南第 101 屆黑客松主辦"
    ], 
    "image": "https://fbcdn-sphotos-d-a.akamaihd.net/hphotos-ak-xap1/t31.0-8/10704199_786019718105983_5468670294645501330_o.png", 
}
```

| 欄位名稱   | 說明                 |
|------------|----------------------|
| name       | 議員姓名             |
| party      | 所屬政黨             |
| education  | 教育, 以 `list` 儲存 |
| experience | 經歷, 以 `list` 儲存 |
| image      | 議員照片             |

### 議員的聯絡方式

議員的聯絡方式是以一個 `list` 來儲存在 `contact_details` 欄位，內部儲存的格式為

```json
"contact_details": [
    {
        "label": "服務處地址", 
        "type": "address", 
        "value": "臺中市大甲區中山路二段1005號"
    }
]
``` 

| 欄位名稱 | 說明                       |
|----------|----------------------------|
| label    | 議員網頁上，他所顯示的說明 |
| type     | 此筆聯絡方式的種類         |
| value    | 值                         |

其中 type 的內容是固定的，目前種類有

| type    | 說明           |
|---------|----------------|
| address | 地址之類的資訊 |
| voice   | 電話           |
| fax     | 傳真           |
| email   | 電子郵件信箱   |
| cell    | 行動電話       |

### 擔任議員時期的資料

```json
{
    "title": "議員",
    "election_year": "2010", 
    "in_office": true, 
    "platform": [
        "致力於開發公民參與社會的資訊平臺與工具", 
    ], 
    "term_end": {
        "date": "2018-12-24"
    }, 
    "term_start": "2014-12-25", 
    "links": [
        {
            "note": "議會個人官網", 
            "url": "http://www.ilcc.gov.tw/Html/H_05/H_0501.asp?GoOut=&pic=1&clique=KMT&User_id=A1701"
        }
    ], 
}

```

| 欄位名稱      | 說明               |
|---------------|--------------------|
| title         | 職稱 (議員或議長等)|
| election_year | 當選的年份         |
| in_office     | 是否還在職         |
| platform      | 競選時的政見       |
| term_start    | 議員任職起始的時間 |
| term_end      | 議員任職終止的時間 |
| links         | 相關的網站連結 |

* term_end 的儲存格式是 `dict` 
* 目前 links 至少會放議員在議會的網站網址

#### 完整範例

```json
{
    "constituency": "宜蘭縣第1選區", 
    "contact_details": [
        {
            "label": "服務處所", 
            "type": "address", 
            "value": "宜蘭市復興路2段16號"
        }, 
        {
            "label": "服務處所電話", 
            "type": "voice", 
            "value": "9331589"
        }, 
        {
            "label": "E-mail", 
            "type": "email", 
            "value": "ccr@ilcc.gov.tw"
        }
    ], 
    "county": "宜蘭縣", 
    "district": "宜蘭", 
    "education": [
        "宜蘭市光復國小畢業"
    ], 
    "election_year": "2009", 
    "experience": [
        "宜蘭縣議會第十七屆議長。", 
        "(一)宜蘭縣議會議員、副議長、議長", 
        "(二)宜蘭市民代表會副主席、主席", 
        "(三)宜蘭縣商業總會理事長", 
        "(四)宜蘭縣義消總隊總隊長", 
        "(五)國際獅子會300F區總監", 
        "(六)宜蘭市照應宮、三清宮主任委員", 
        "(七)宜蘭縣張、廖、簡宗親會理事長", 
        "(八)宜蘭縣土木包工業公會理事長", 
        "(九)宜蘭縣社會福利聯合勸募基金會常務監察人"
    ], 
    "image": "http://www.ilcc.gov.tw/pictures/people/A1701.JPG", 
    "in_office": true, 
    "links": [
        {
            "note": "議會個人官網", 
            "url": "http://www.ilcc.gov.tw/Html/H_05/H_0501.asp?GoOut=&pic=1&clique=KMT&User_id=A1701"
        }
    ], 
    "name": "張建榮", 
    "party": "中國國民黨", 
    "platform": [
        "一、促請政府儘速規闢北宜直線鐵路及宜蘭市鐵路全面高架。", 
        "二、北宜高速公路側車道，促請全線開通。", 
        "三、北宜高速公路東西向五條連絡道路，促請全面開通。", 
        "四、督促政府加速宜蘭市污水下水道早日全面完工。", 
        "五、促請政府充實消防設備，保障人民生命財產安全。", 
        "六、促進政府加強治安設備，充實村里監視系統，以維護社會安寧。", 
        "七、督促政府設立資訊研發中心，獎勵高科技產業設廠。", 
        "八、建請政府落實老人福利，照顧殘障、維護婦女權益及弱勢族群。", 
        "九、督促政府創造勞工就業，爭取勞工權益。", 
        "十、推動社區藝文活動，落實文化紮根，提升生活素養。", 
        "十一、督促縣政府廢除容積、建蔽率限制，回歸中央政府訂頒標準，以利土地開發，保障", 
        "縣民權益。", 
        "十二、督促縣政府落實國軍眷利興建工程早日啟用。"
    ], 
    "term_end": {
        "date": "2014-12-25"
    }, 
    "term_start": "2009-12-25", 
    "title": "議長"
} 
```

## bills.json 的格式說明

### 議案的基本資訊

| 欄位名稱           | 說明                                                          |
|--------------------|---------------------------------------------------------------|
| county             | 議案所屬縣市                                                  |
| election_year      | 議案所屬屆期，例如臺北市第11屆: 2010~2014                     |
| id                 | 議案在議會資料庫的 id，一般可以從網址或者 request body 中取得 |
| bill_no            | 議案在縣議會的編號，例如 `甲01號` 之類                        |
| type               | 議案的種類，例如 `議員提案`, `市府提案`等                     |
| category           | 議案的種類，例如 `建設`, `農業` 等                            |
| proposed_by        | 提議此議案的議員，儲存型態為 `list`，第一個即為第一提案人     |
| petitioned_by      | 連署此議案的議員，儲存型態為 `list`                           |
| abstract           | 議案的摘要或 Title                                            |
| description        | 議案的詳細內容描述                                            |
| methods            | 議案所提議的處理方式                                          |
| execution          | 議案執行情形                                                  |
| last_action        | 議案最新狀態(motion)                                          |
| links              | 議案的網址                                                    |

### motions

| 欄位名稱 | 說明                 |
|----------|----------------------|
| motions  | 議案決議過程與結果   |

議案決議過程 (motions) 可能分成好幾個階段，且每個議會所紀錄的過程都不太相同。
每個階段的儲存格式為

| 欄位名稱   | 說明                        |
|------------|-----------------------------|
| data       | 日期，儲存格式為 yyyy/mm/dd |
| motion     | 此階段的描述                |
| resolution | 此階段的執行結果            |
| sitting    | 執行此階段時的會議名稱      |

### 完整範例

```json
{
    "abstract": "建請市政府於高鐵門戶地區60公尺綠園道規劃足夠排水斷面容量之雨水、污水箱涵設施，以解決本地區淹水問題及造福地方案。", 
    "bill_no": "議都字 第004號", 
    "category": "水利", 
    "committee": "工務建設委員會", 
    "county": "臺中市", 
    "description": "一、市政府規劃辦理之高鐵臺中車站門戶地區位於本市南端，其北方有第七、八期重劃區，第十三期公辦重劃開發中；另外，屬自辦重劃的第二、三單元接近完工階段，第四、五單元亦緊鑼密鼓開發中。\n\n二、前述都市計畫之開發，增加大量雨水、污水量，勢必對於比較低窪之高鐵臺中車站門戶地區之排水，造成極大之壓力，況之位於該區之南屯溪，目前已面臨逢雨必溢堤之窘境。\n\n三、高鐵臺中車站門戶地區規劃有一六十米之綠園道，建請市政府於此六十米綠園道規劃足夠排水斷面容量之雨水、污水箱涵設施，以澈底解決本地區之淹水問題。", 
    "election_year": "2010", 
    "execution": "", 
    "id": "2340-1-14-1", 
    "links": "http://163.29.76.77/tccc/jsp/b_0_1.jsp?sn=2340&term=1&timeorder=14&type=1", 
    "methods": "如案由。", 
    "motions": [
        {
            "date": null, 
            "motion": "分組審查意見", 
            "resolution": ""
        }, 
        {
            "date": null, 
            "motion": "大會意見", 
            "resolution": "照審查意見通過。"
        }
    ], 
    "petitioned_by": [
        "黃馨慧", 
        "李中", 
        "朱暖英", 
        "洪嘉鴻", 
        "陳有江", 
        "楊正中"
    ], 
    "proposed_by": [
        "張耀中", 
        "陳淑華", 
        "張廖萬堅"
    ] 
}

```
