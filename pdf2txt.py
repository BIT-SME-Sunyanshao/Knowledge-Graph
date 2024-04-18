from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator

fp = open('./data/document/某型号级间分离技术研究与应用_曾铁.pdf', "rb")
# 来创建一个pdf文档分析器
parser = PDFParser(fp)
# 创建一个PDF文档对象存储文档结构
document = PDFDocument(parser)
# 检查文件是否允许文本提取
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    # 创建一个PDF资源管理器对象来存储共赏资源
    rsrcmgr = PDFResourceManager()
    # 设定参数进行分析
    laparams = LAParams()
    # 创建一个PDF设备对象
    # device=PDFDevice(rsrcmgr)
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # 处理每一页
    for page in PDFPage.create_pages(document):
        print(page)
        interpreter.process_page(page)
        # 接受该页面的LTPage对象
        layout = device.get_result()
        for x in layout:
            if (isinstance(x, LTTextBoxHorizontal)):
                txt = x.get_text()
                with open("./data/process/pdf2txt1.txt", "a", encoding='utf-8') as f:
                    f.write(txt)
                    f.write("\n")
