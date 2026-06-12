"""
Taiwan ETF data sourced from TWSE/公開資訊.
Updated: 2026-06. Covers all actively-traded domestic ETFs on TWSE.
"""

ETF_DATA = [
    # 元大投信
    {"securities_code": "0050", "securities_abbreviation": "元大台灣50", "issuer": "元大投信", "target_index": "臺灣50指數", "management_fee": "0.32", "custody_fee": "0.035", "dividend_frequency": "semi_annual", "dividend_bank": ""},
    {"securities_code": "0051", "securities_abbreviation": "元大中型100", "issuer": "元大投信", "target_index": "臺灣中型100指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0052", "securities_abbreviation": "富邦科技", "issuer": "富邦投信", "target_index": "臺灣資訊科技指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0053", "securities_abbreviation": "元大電子", "issuer": "元大投信", "target_index": "臺灣電子類加權股價指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0054", "securities_abbreviation": "元大台商50", "issuer": "元大投信", "target_index": "標智滬深300中國指數", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0055", "securities_abbreviation": "元大MSCI金融", "issuer": "元大投信", "target_index": "MSCI台灣金融指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0056", "securities_abbreviation": "元大高股息", "issuer": "元大投信", "target_index": "臺灣高股息指數", "management_fee": "0.34", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "0057", "securities_abbreviation": "富邦摩台", "issuer": "富邦投信", "target_index": "MSCI台灣指數", "management_fee": "0.35", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0058", "securities_abbreviation": "富邦發達", "issuer": "富邦投信", "target_index": "臺灣發達指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0059", "securities_abbreviation": "富邦金融", "issuer": "富邦投信", "target_index": "FactSet台灣金融指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0060", "securities_abbreviation": "元大新台灣", "issuer": "元大投信", "target_index": "道瓊斯台灣指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "0061", "securities_abbreviation": "元大寶滬深", "issuer": "元大投信", "target_index": "標智滬深300指數", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    # 006x 系列
    {"securities_code": "006201", "securities_abbreviation": "元大富櫃50", "issuer": "元大投信", "target_index": "富櫃50指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "006203", "securities_abbreviation": "元大MSCI台灣", "issuer": "元大投信", "target_index": "MSCI台灣指數", "management_fee": "0.32", "custody_fee": "0.035", "dividend_frequency": "semi_annual", "dividend_bank": ""},
    {"securities_code": "006204", "securities_abbreviation": "永豐臺灣加權", "issuer": "永豐投信", "target_index": "臺灣加權股價指數", "management_fee": "0.35", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "006208", "securities_abbreviation": "富邦台50", "issuer": "富邦投信", "target_index": "臺灣50指數", "management_fee": "0.15", "custody_fee": "0.035", "dividend_frequency": "semi_annual", "dividend_bank": ""},
    # 00600 系列
    {"securities_code": "00625", "securities_abbreviation": "富邦臺灣優質高息", "issuer": "富邦投信", "target_index": "臺灣優質高息指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00631L", "securities_abbreviation": "元大台灣50正2", "issuer": "元大投信", "target_index": "臺灣50指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00632R", "securities_abbreviation": "元大台灣50反1", "issuer": "元大投信", "target_index": "臺灣50指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00633L", "securities_abbreviation": "富邦上証正2", "issuer": "富邦投信", "target_index": "上証180指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00634R", "securities_abbreviation": "富邦上証反1", "issuer": "富邦投信", "target_index": "上証180指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00636", "securities_abbreviation": "國泰臺灣低波動30", "issuer": "國泰投信", "target_index": "臺灣低波動精選30指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00637L", "securities_abbreviation": "元大滬深300正2", "issuer": "元大投信", "target_index": "滬深300指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00638R", "securities_abbreviation": "元大滬深300反1", "issuer": "元大投信", "target_index": "滬深300指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00639", "securities_abbreviation": "富邦深100", "issuer": "富邦投信", "target_index": "深證100價格指數", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00640L", "securities_abbreviation": "富邦日本正2", "issuer": "富邦投信", "target_index": "日經225指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00641R", "securities_abbreviation": "富邦日本反1", "issuer": "富邦投信", "target_index": "日經225指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00642U", "securities_abbreviation": "元大S&P原油正2", "issuer": "元大投信", "target_index": "S&P高盛原油ER指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00643", "securities_abbreviation": "群益深証中小", "issuer": "群益投信", "target_index": "深証中小板指數", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00644L", "securities_abbreviation": "群益深証正2", "issuer": "群益投信", "target_index": "深証中小板指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00645", "securities_abbreviation": "富邦臺灣科技", "issuer": "富邦投信", "target_index": "FactSet台灣高科技指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00646", "securities_abbreviation": "元大S&P500", "issuer": "元大投信", "target_index": "S&P500指數", "management_fee": "0.58", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00647L", "securities_abbreviation": "元大美債正2", "issuer": "元大投信", "target_index": "ICE美國政府7-10年期債券指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00648R", "securities_abbreviation": "元大美債反1", "issuer": "元大投信", "target_index": "ICE美國政府7-10年期債券指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00649", "securities_abbreviation": "元大高評級公司債", "issuer": "元大投信", "target_index": "Markit iBoxx美元液態投資級公司債指數", "management_fee": "0.30", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00650", "securities_abbreviation": "元大美債1-3", "issuer": "元大投信", "target_index": "ICE美國政府1-3年期債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00651", "securities_abbreviation": "元大美債7-10", "issuer": "元大投信", "target_index": "ICE美國政府7-10年期債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00652", "securities_abbreviation": "富邦印度", "issuer": "富邦投信", "target_index": "NIFTY50指數", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00653L", "securities_abbreviation": "富邦台灣加權正2", "issuer": "富邦投信", "target_index": "臺灣加權股價指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00654R", "securities_abbreviation": "富邦台灣加權反1", "issuer": "富邦投信", "target_index": "臺灣加權股價指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00655", "securities_abbreviation": "富邦亞太", "issuer": "富邦投信", "target_index": "MSCI亞太指數(日本除外)", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00656", "securities_abbreviation": "國泰股利精選30", "issuer": "國泰投信", "target_index": "臺灣股利精選30指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00657", "securities_abbreviation": "國泰臺灣加權正2", "issuer": "國泰投信", "target_index": "臺灣加權股價指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00658", "securities_abbreviation": "國泰臺灣加權反1", "issuer": "國泰投信", "target_index": "臺灣加權股價指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00659", "securities_abbreviation": "元大美元指數正2", "issuer": "元大投信", "target_index": "彭博美元即期指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00660", "securities_abbreviation": "元大歐洲50", "issuer": "元大投信", "target_index": "EURO STOXX 50指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00661", "securities_abbreviation": "元大日經225", "issuer": "元大投信", "target_index": "日經225指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00662", "securities_abbreviation": "富邦NASDAQ", "issuer": "富邦投信", "target_index": "NASDAQ-100指數", "management_fee": "0.58", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00663L", "securities_abbreviation": "國泰臺灣加權正2", "issuer": "國泰投信", "target_index": "臺灣加權股價指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00664R", "securities_abbreviation": "國泰臺灣加權反1", "issuer": "國泰投信", "target_index": "臺灣加權股價指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00665L", "securities_abbreviation": "富邦恒生正2", "issuer": "富邦投信", "target_index": "恒生指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00666R", "securities_abbreviation": "富邦恒生反1", "issuer": "富邦投信", "target_index": "恒生指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00668", "securities_abbreviation": "國泰美國道瓊", "issuer": "國泰投信", "target_index": "道瓊工業平均指數", "management_fee": "0.58", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00669", "securities_abbreviation": "富邦臺灣產業龍頭等權重", "issuer": "富邦投信", "target_index": "臺灣產業龍頭等權重指數", "management_fee": "0.35", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00670L", "securities_abbreviation": "富邦NASDAQ正2", "issuer": "富邦投信", "target_index": "NASDAQ-100指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00671R", "securities_abbreviation": "富邦NASDAQ反1", "issuer": "富邦投信", "target_index": "NASDAQ-100指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00672", "securities_abbreviation": "元大新興市場債10+", "issuer": "元大投信", "target_index": "彭博新興市場美元主權債券10年期以上指數", "management_fee": "0.30", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00673R", "securities_abbreviation": "元大S&P500反1", "issuer": "元大投信", "target_index": "S&P500指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00674R", "securities_abbreviation": "元大S&P黃金反1", "issuer": "元大投信", "target_index": "S&P高盛黃金ER指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00675L", "securities_abbreviation": "富邦臺灣中小", "issuer": "富邦投信", "target_index": "中小型指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00676", "securities_abbreviation": "凱基新台灣", "issuer": "凱基投信", "target_index": "凱基新台灣指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00677U", "securities_abbreviation": "富邦VIX", "issuer": "富邦投信", "target_index": "S&P500 VIX短期期貨指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00678", "securities_abbreviation": "群益臺灣精選高息", "issuer": "群益投信", "target_index": "臺灣精選高息指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00679B", "securities_abbreviation": "元大美債20年", "issuer": "元大投信", "target_index": "ICE美國政府20年期以上債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00680L", "securities_abbreviation": "元大美債正2", "issuer": "元大投信", "target_index": "ICE美國政府20年期以上債券指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00681R", "securities_abbreviation": "元大美債反1", "issuer": "元大投信", "target_index": "ICE美國政府20年期以上債券指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00682", "securities_abbreviation": "富邦MSCI台灣", "issuer": "富邦投信", "target_index": "MSCI台灣指數", "management_fee": "0.35", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00683", "securities_abbreviation": "富邦新興市場", "issuer": "富邦投信", "target_index": "MSCI新興市場指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00684R", "securities_abbreviation": "群益2X台灣反1", "issuer": "群益投信", "target_index": "臺灣加權股價指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00685L", "securities_abbreviation": "群益台灣加權正2", "issuer": "群益投信", "target_index": "臺灣加權股價指數", "management_fee": "1.00", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00686", "securities_abbreviation": "國泰20年美債", "issuer": "國泰投信", "target_index": "ICE美國政府20年期以上債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00687B", "securities_abbreviation": "國泰10年美債", "issuer": "國泰投信", "target_index": "ICE美國政府7-10年期債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00688", "securities_abbreviation": "國泰美國費城半導體", "issuer": "國泰投信", "target_index": "費城半導體指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00689", "securities_abbreviation": "凱基台灣ESG永續", "issuer": "凱基投信", "target_index": "臺灣ESG永續指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "semi_annual", "dividend_bank": ""},
    {"securities_code": "00690", "securities_abbreviation": "兆豐藍籌30", "issuer": "兆豐投信", "target_index": "臺灣藍籌30指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00692", "securities_abbreviation": "富邦公司治理", "issuer": "富邦投信", "target_index": "臺灣公司治理100指數", "management_fee": "0.35", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00694B", "securities_abbreviation": "富邦中國政策債", "issuer": "富邦投信", "target_index": "彭博中國政策性銀行債券指數", "management_fee": "0.30", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00695B", "securities_abbreviation": "富邦美債10+", "issuer": "富邦投信", "target_index": "彭博美國政府長期債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00696B", "securities_abbreviation": "富邦新興債券", "issuer": "富邦投信", "target_index": "彭博新興市場美元主權債券指數", "management_fee": "0.30", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00697B", "securities_abbreviation": "元大投資級公司債", "issuer": "元大投信", "target_index": "彭博美元投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00698", "securities_abbreviation": "群益道瓊美國地產", "issuer": "群益投信", "target_index": "道瓊美國精選不動產指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00701", "securities_abbreviation": "國泰低波動因子", "issuer": "國泰投信", "target_index": "MSCI台灣選取因子指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00702", "securities_abbreviation": "國泰主動式ETF", "issuer": "國泰投信", "target_index": "道瓊工業平均指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00710B", "securities_abbreviation": "復華彭博新興高收債", "issuer": "復華投信", "target_index": "彭博新興市場高收益債券指數", "management_fee": "0.60", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00711B", "securities_abbreviation": "復華美國短期高收益債", "issuer": "復華投信", "target_index": "彭博美國高收益短期債券指數", "management_fee": "0.60", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00712", "securities_abbreviation": "復華富時不動產", "issuer": "復華投信", "target_index": "富時EPRA/NAREIT全球指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00713", "securities_abbreviation": "元大台灣高息低波", "issuer": "元大投信", "target_index": "台灣指數公司特選高息低波指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00714", "securities_abbreviation": "群益道瓊美國地產", "issuer": "群益投信", "target_index": "道瓊美國精選不動產指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00715L", "securities_abbreviation": "期元大S&P500正2", "issuer": "元大投信", "target_index": "S&P500指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00716R", "securities_abbreviation": "期元大S&P500反1", "issuer": "元大投信", "target_index": "S&P500指數", "management_fee": "1.00", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00717", "securities_abbreviation": "富邦科技", "issuer": "富邦投信", "target_index": "FactSet台灣高科技指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00718B", "securities_abbreviation": "群益投資級金融債", "issuer": "群益投信", "target_index": "彭博美元投資等級金融債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00719B", "securities_abbreviation": "元大美國政府1-3年", "issuer": "元大投信", "target_index": "彭博美國政府1-3年債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00720B", "securities_abbreviation": "元大投資級公司債", "issuer": "元大投信", "target_index": "彭博美元投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00721B", "securities_abbreviation": "元大美國高收益企業債", "issuer": "元大投信", "target_index": "彭博美國高收益企業債券指數", "management_fee": "0.60", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00722B", "securities_abbreviation": "群益15年IG公司債", "issuer": "群益投信", "target_index": "彭博美元投資等級公司債15+年指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00723B", "securities_abbreviation": "群益投資級電信債", "issuer": "群益投信", "target_index": "彭博美元投資等級電信業公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00724B", "securities_abbreviation": "群益投資級科技債", "issuer": "群益投信", "target_index": "彭博美元投資等級科技業公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00725B", "securities_abbreviation": "國泰投資級公司債", "issuer": "國泰投信", "target_index": "彭博美元投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00726B", "securities_abbreviation": "元大AAA至A公司債", "issuer": "元大投信", "target_index": "彭博美元AAA至A級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00727B", "securities_abbreviation": "兆豐美元投資級債", "issuer": "兆豐投信", "target_index": "彭博美元投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00728B", "securities_abbreviation": "國泰20年美債", "issuer": "國泰投信", "target_index": "ICE美國政府20+年債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00730", "securities_abbreviation": "富邦臺灣優質高息", "issuer": "富邦投信", "target_index": "臺灣優質高息指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00731", "securities_abbreviation": "復華富時台灣全市場", "issuer": "復華投信", "target_index": "富時台灣全市場指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00733", "securities_abbreviation": "富邦臺灣中小", "issuer": "富邦投信", "target_index": "中小型指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00734", "securities_abbreviation": "國泰台灣ESG永續", "issuer": "國泰投信", "target_index": "MSCI台灣ESG永續領袖指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00737", "securities_abbreviation": "台新MSCI台灣", "issuer": "台新投信", "target_index": "MSCI台灣指數", "management_fee": "0.35", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00739", "securities_abbreviation": "元大台灣ESG永續", "issuer": "元大投信", "target_index": "臺灣永續指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "semi_annual", "dividend_bank": ""},
    {"securities_code": "00742", "securities_abbreviation": "新光臺灣半導體30", "issuer": "新光投信", "target_index": "臺灣半導體30指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00751B", "securities_abbreviation": "台新美國短期公司債", "issuer": "台新投信", "target_index": "彭博美元1-5年投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00752B", "securities_abbreviation": "台新北美科技債", "issuer": "台新投信", "target_index": "彭博美元北美科技業投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00757", "securities_abbreviation": "統一FANG+", "issuer": "統一投信", "target_index": "NYSE FANG+指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00762", "securities_abbreviation": "凱基優選高股息30", "issuer": "凱基投信", "target_index": "凱基優選高股息30指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00763", "securities_abbreviation": "群益半導體收益", "issuer": "群益投信", "target_index": "費城半導體指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00770", "securities_abbreviation": "國泰中國A150", "issuer": "國泰投信", "target_index": "MSCI中國A150指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00771", "securities_abbreviation": "元大美國政府20年", "issuer": "元大投信", "target_index": "彭博美國政府20+年債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00772B", "securities_abbreviation": "中信高評級公司債", "issuer": "中信投信", "target_index": "彭博美元BBB級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00773B", "securities_abbreviation": "中信優先金融債", "issuer": "中信投信", "target_index": "彭博美元優先金融業公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00774B", "securities_abbreviation": "安聯投資級公司債", "issuer": "安聯投信", "target_index": "彭博美元投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00775B", "securities_abbreviation": "新光投資級公司債", "issuer": "新光投信", "target_index": "彭博美元投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00776B", "securities_abbreviation": "凱基AAA至AA公司債", "issuer": "凱基投信", "target_index": "彭博美元AAA至AA級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00777B", "securities_abbreviation": "永豐15年IG銀行債", "issuer": "永豐投信", "target_index": "彭博美元銀行業15+年投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00778B", "securities_abbreviation": "瀚亞投資級公司債", "issuer": "瀚亞投信", "target_index": "彭博美元投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00779B", "securities_abbreviation": "凱基美國投等債20+", "issuer": "凱基投信", "target_index": "彭博美國政府20+年債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00780B", "securities_abbreviation": "富邦全球投等債", "issuer": "富邦投信", "target_index": "彭博全球投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00781", "securities_abbreviation": "永豐台灣ESG", "issuer": "永豐投信", "target_index": "永豐台灣ESG永續指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00783", "securities_abbreviation": "富邦韓國", "issuer": "富邦投信", "target_index": "KOSPI200指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00784", "securities_abbreviation": "富邦印度", "issuer": "富邦投信", "target_index": "Nifty50指數", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00786", "securities_abbreviation": "元大MSCI金融", "issuer": "元大投信", "target_index": "MSCI台灣金融指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00787", "securities_abbreviation": "元大全球AI", "issuer": "元大投信", "target_index": "彭博全球人工智慧指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00795B", "securities_abbreviation": "富邦美債10+", "issuer": "富邦投信", "target_index": "彭博美國政府長期債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00796B", "securities_abbreviation": "富邦美債", "issuer": "富邦投信", "target_index": "彭博美國政府1-3年債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00797B", "securities_abbreviation": "富邦新興市場主權債", "issuer": "富邦投信", "target_index": "彭博新興市場美元主權債券指數", "management_fee": "0.30", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    # 熱門新型ETF
    {"securities_code": "00850", "securities_abbreviation": "元大臺灣ESG永續", "issuer": "元大投信", "target_index": "臺灣永續指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "semi_annual", "dividend_bank": ""},
    {"securities_code": "00851", "securities_abbreviation": "台新臺灣ESG優選", "issuer": "台新投信", "target_index": "台新臺灣ESG優選指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00858", "securities_abbreviation": "中信中國50", "issuer": "中信投信", "target_index": "MSCI中國50指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00861", "securities_abbreviation": "元大全球AI", "issuer": "元大投信", "target_index": "彭博全球人工智慧指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00864B", "securities_abbreviation": "中信美國公司債15+", "issuer": "中信投信", "target_index": "彭博美元投資等級公司債15+年指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00865B", "securities_abbreviation": "中信美國公司債(1-5年)", "issuer": "中信投信", "target_index": "彭博美元1-5年投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00867B", "securities_abbreviation": "中信美國公司債(7-10年)", "issuer": "中信投信", "target_index": "彭博美元7-10年投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00870", "securities_abbreviation": "元大台灣半導體", "issuer": "元大投信", "target_index": "臺灣半導體指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00875", "securities_abbreviation": "國泰智能電動車", "issuer": "國泰投信", "target_index": "MSCI ACWI IMI精選電動車及電池指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00878", "securities_abbreviation": "國泰永續高股息", "issuer": "國泰投信", "target_index": "MSCI台灣ESG永續高股息精選指數", "management_fee": "0.25", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00881", "securities_abbreviation": "國泰台灣5G+", "issuer": "國泰投信", "target_index": "臺灣5G+指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00882", "securities_abbreviation": "中信中國高股息", "issuer": "中信投信", "target_index": "恒生中國高股息率指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00883", "securities_abbreviation": "中信越南", "issuer": "中信投信", "target_index": "VNM指數", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00884", "securities_abbreviation": "國泰全球品牌50", "issuer": "國泰投信", "target_index": "STOXX全球品牌50指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00885", "securities_abbreviation": "富邦越南", "issuer": "富邦投信", "target_index": "越南VN30指數", "management_fee": "0.99", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00887", "securities_abbreviation": "元大MSCI台灣ESG永續", "issuer": "元大投信", "target_index": "MSCI台灣ESG領袖指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "semi_annual", "dividend_bank": ""},
    {"securities_code": "00888", "securities_abbreviation": "永豐ESG低碳高息", "issuer": "永豐投信", "target_index": "臺灣指數公司特選ESG低碳高息60指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00891", "securities_abbreviation": "中信關鍵半導體", "issuer": "中信投信", "target_index": "ICE FactSet台灣關鍵半導體指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00892", "securities_abbreviation": "富邦台灣科技指數", "issuer": "富邦投信", "target_index": "FactSet台灣科技指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "semi_annual", "dividend_bank": ""},
    {"securities_code": "00893", "securities_abbreviation": "國泰電池及儲能", "issuer": "國泰投信", "target_index": "MSCI ACWI IMI精選電動車及電池指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00894", "securities_abbreviation": "中信小台灣", "issuer": "中信投信", "target_index": "臺灣中小型100指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00895", "securities_abbreviation": "富邦未來車", "issuer": "富邦投信", "target_index": "MSCI ACWI精選電動及無人駕駛指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00896", "securities_abbreviation": "中信綠能及電動車", "issuer": "中信投信", "target_index": "ICE FactSet台灣綠能及電動車指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00900", "securities_abbreviation": "富邦特選高股息30", "issuer": "富邦投信", "target_index": "臺灣指數公司特選高股息30指數", "management_fee": "0.34", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00907", "securities_abbreviation": "永豐優息存股", "issuer": "永豐投信", "target_index": "臺灣指數公司特選優息存股指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00910", "securities_abbreviation": "第一金太空衛星", "issuer": "第一金投信", "target_index": "S&P Kensho最終邊界指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00912", "securities_abbreviation": "中信臺灣智慧50", "issuer": "中信投信", "target_index": "ICE FactSet臺灣智慧50指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00915", "securities_abbreviation": "凱基優選高股息30", "issuer": "凱基投信", "target_index": "凱基優選高股息30指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00916", "securities_abbreviation": "國泰全球品牌50", "issuer": "國泰投信", "target_index": "STOXX全球品牌50指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00917", "securities_abbreviation": "中信特選金融股", "issuer": "中信投信", "target_index": "ICE FactSet中信特選金融指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00918", "securities_abbreviation": "大華優利高填息30", "issuer": "大華投信", "target_index": "臺灣指數公司特選優利高填息30指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00919", "securities_abbreviation": "群益台灣精選高息", "issuer": "群益投信", "target_index": "臺灣精選高息指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00920", "securities_abbreviation": "富邦未來車", "issuer": "富邦投信", "target_index": "MSCI ACWI精選電動及自駕車指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00921", "securities_abbreviation": "兆豐永續高息等權", "issuer": "兆豐投信", "target_index": "臺灣指數公司特選永續高息等權30指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00922", "securities_abbreviation": "國泰半導體收益", "issuer": "國泰投信", "target_index": "費城半導體指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00923", "securities_abbreviation": "群益台ESG低碳55", "issuer": "群益投信", "target_index": "臺灣指數公司特選ESG低碳55指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00924", "securities_abbreviation": "元大台灣價值高息", "issuer": "元大投信", "target_index": "臺灣指數公司特選台灣價值高息指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00925", "securities_abbreviation": "台新臺灣IC設計", "issuer": "台新投信", "target_index": "臺灣IC設計指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00926", "securities_abbreviation": "凱基金融高息動能", "issuer": "凱基投信", "target_index": "凱基金融高息動能指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00927", "securities_abbreviation": "群益半導體收益", "issuer": "群益投信", "target_index": "費城半導體指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00928", "securities_abbreviation": "中信高評級公司債", "issuer": "中信投信", "target_index": "彭博美元BBB+至A+級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00929", "securities_abbreviation": "復華台灣科技優息", "issuer": "復華投信", "target_index": "臺灣指數公司特選科技優息指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00930", "securities_abbreviation": "永豐ESG低碳高息", "issuer": "永豐投信", "target_index": "臺灣指數公司特選ESG低碳高息60指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00931", "securities_abbreviation": "永豐美國大型成長100", "issuer": "永豐投信", "target_index": "Russell 1000成長指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00932", "securities_abbreviation": "兆豐龍頭等權重", "issuer": "兆豐投信", "target_index": "臺灣指數公司特選龍頭等權重指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00933B", "securities_abbreviation": "國泰10Y+金融債", "issuer": "國泰投信", "target_index": "彭博美元金融業10+年投資等級公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00934", "securities_abbreviation": "中信成長高息", "issuer": "中信投信", "target_index": "ICE FactSet中信成長高息指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00935", "securities_abbreviation": "野村臺灣新科技50", "issuer": "野村投信", "target_index": "臺灣指數公司臺灣新科技50指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00936", "securities_abbreviation": "台新臺灣高息動能", "issuer": "台新投信", "target_index": "臺灣指數公司特選高息動能指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00937B", "securities_abbreviation": "群益ESG投等債20+", "issuer": "群益投信", "target_index": "彭博美元ESG投資等級20+年公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00939", "securities_abbreviation": "統一台灣高息動能", "issuer": "統一投信", "target_index": "臺灣指數公司特選高息動能指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00940", "securities_abbreviation": "元大台灣價值高息", "issuer": "元大投信", "target_index": "臺灣指數公司特選台灣價值高息指數", "management_fee": "0.40", "custody_fee": "0.035", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00941", "securities_abbreviation": "台新臺美航太及國防", "issuer": "台新投信", "target_index": "標普美國航太及國防精選指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00942B", "securities_abbreviation": "台新美國債10+", "issuer": "台新投信", "target_index": "彭博美元投資等級公司債10+年指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00943B", "securities_abbreviation": "群益ESG投等債10+", "issuer": "群益投信", "target_index": "彭博美元ESG投資等級10+年公司債券指數", "management_fee": "0.25", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00944", "securities_abbreviation": "第一金S&P500", "issuer": "第一金投信", "target_index": "S&P500指數", "management_fee": "0.58", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00945", "securities_abbreviation": "國泰半導體(00922等同)", "issuer": "國泰投信", "target_index": "費城半導體指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00946", "securities_abbreviation": "元大全球AI收益成長", "issuer": "元大投信", "target_index": "彭博全球人工智慧指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00947", "securities_abbreviation": "野村AI人工智慧50", "issuer": "野村投信", "target_index": "ICE FactSet野村AI人工智慧50指數", "management_fee": "0.65", "custody_fee": "0.20", "dividend_frequency": "quarterly", "dividend_bank": ""},
    {"securities_code": "00948", "securities_abbreviation": "凱基NASDAQ100", "issuer": "凱基投信", "target_index": "NASDAQ-100指數", "management_fee": "0.58", "custody_fee": "0.20", "dividend_frequency": "annual", "dividend_bank": ""},
    {"securities_code": "00949", "securities_abbreviation": "元大美國政府7-10年", "issuer": "元大投信", "target_index": "彭博美國政府7-10年債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
    {"securities_code": "00950", "securities_abbreviation": "台新美國政府20年+", "issuer": "台新投信", "target_index": "彭博美國政府20+年債券指數", "management_fee": "0.20", "custody_fee": "0.20", "dividend_frequency": "monthly", "dividend_bank": ""},
]


def fetch_twse_etfs():
    return [dict(item) for item in ETF_DATA]


def _parse_roc_date(date_str):
    """民國年日期 '115年01月22日' → datetime.date"""
    import re
    from datetime import date
    m = re.match(r'(\d+)年(\d+)月(\d+)日', date_str or '')
    if not m:
        return None
    return date(int(m.group(1)) + 1911, int(m.group(2)), int(m.group(3)))


def _fetch_twse_dividend_dates(securities_code, years):
    """TWSE rwd ETF API: 取得除息日 + 配息金額"""
    import time
    import requests
    from datetime import date

    today = date.today()
    start_date = date(today.year - years, today.month, today.day)

    url = "https://www.twse.com.tw/rwd/zh/ETF/etfDiv"
    params = {
        "response": "json",
        "stockNo": securities_code,
        "startDate": start_date.strftime("%Y%m%d"),
        "endDate": today.strftime("%Y%m%d"),
    }
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Referer": "https://www.twse.com.tw/zh/ETF/dividend",
        "Accept-Language": "zh-TW,zh;q=0.9",
    }

    last_err = None
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            break
        except Exception as e:
            last_err = e
            time.sleep(3 * (attempt + 1))
    else:
        raise last_err

    # fields: [證券代號, 證券簡稱, 除息交易日, 基準日, 發放日, 配息金額, 說明, 年度]
    results = []
    for row in data.get("data") or []:
        if row[0] != securities_code:
            continue
        ex_date = _parse_roc_date(row[2])
        if not ex_date:
            continue
        try:
            amount = round(float(row[5] or 0), 4)
        except (ValueError, TypeError):
            amount = 0
        results.append({"ex_dividend_date": ex_date, "dividend_amount": amount})
    return results


def _fetch_twse_prices(securities_code, dates):
    """TWSE STOCK_DAY API: 批次取得指定日期的收盤價，以 (year, month) 分組"""
    import time
    import requests
    from datetime import date

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
    }
    price_map = {}
    needed_months = sorted({(d.year, d.month) for d in dates})

    for year, month in needed_months:
        try:
            query_date = date(year, month, 1).strftime("%Y%m%d")
            resp = requests.get(
                "https://www.twse.com.tw/exchangeReport/STOCK_DAY",
                params={"response": "json", "date": query_date, "stockNo": securities_code},
                headers=headers,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            if data.get("stat") != "OK":
                continue
            # fields: [日期(115/01/02), 成交股數, 成交金額, 開盤價, 最高價, 最低價, 收盤價, ...]
            for row in data.get("data", []):
                try:
                    parts = row[0].split("/")
                    row_date = date(int(parts[0]) + 1911, int(parts[1]), int(parts[2]))
                    price_map[row_date] = float(row[6].replace(",", ""))
                except (ValueError, IndexError):
                    pass
            time.sleep(0.3)
        except Exception:
            pass

    return price_map


def fetch_etf_dividends(securities_code, years=10):
    dividends = _fetch_twse_dividend_dates(securities_code, years)
    if not dividends:
        return []

    dates = [d["ex_dividend_date"] for d in dividends]
    price_map = _fetch_twse_prices(securities_code, dates)

    return [
        {
            "ex_dividend_date": d["ex_dividend_date"],
            "dividend_amount": d["dividend_amount"],
            "closing_price": round(price_map.get(d["ex_dividend_date"], 0), 2),
        }
        for d in dividends
    ]
