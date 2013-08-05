from xml.dom import getDOMImplementation as dom
dom = dom()

class webdoc:
	def __init__(self):
		self.doctype = dom.createDocumentType("html", None, None)
		self.doc = dom.createDocument(None, "html", self.doctype)
		self.head = self.doc.createElement("head")
		self.body = self.doc.createElement("body")
		self.doc.documentElement.appendChild(self.head)
		self.doc.documentElement.appendChild(self.body)
	def gen_elem(self, name, text):
		elem = self.doc.createElement(name)
		if text: elem.appendChild(self.doc.createTextNode(text))
		return elem
	def set_title(self, title):
		title_elem = self.gen_elem("title", title)
		self.head.appendChild(title_elem)
	def set_h1(self, text):
		#create title
		h1_elem_l = self.gen_elem("h1", text)
		h1_elem_l.setAttribute("id", "h1large")
		h1_elem_s = self.gen_elem("h1", text)
		h1_elem_s.setAttribute("id", "h1small")

		#large
		h1_div_large = self.gen_elem("div", None)
		h1_div_large.setAttribute("class", "visible-lg")
		h1_div_large.appendChild(h1_elem_l)

		#small
		h1_div_small = self.gen_elem("div", None)
		h1_div_small.setAttribute("class", "visible-sm")
		h1_div_small.appendChild(h1_elem_s)

		self.body.appendChild(h1_div_large)
		self.body.appendChild(h1_div_small)
	def attach_stylesheet(self, target):
		link_elem = self.gen_elem("link", None)
		link_elem.setAttribute("rel", "stylesheet")
		link_elem.setAttribute("type", "text/css")
		link_elem.setAttribute("href", target)
		self.head.appendChild(link_elem)
	def add_meta(self, name, content):
		meta_elem = self.gen_elem("meta", None)
		meta_elem.setAttribute("name", name)
		meta_elem.setAttribute("content", content)
		self.head.appendChild(meta_elem)
