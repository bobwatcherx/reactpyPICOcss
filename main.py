from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import html,component,use_state


# NOW FOR INTEGRATE CSS FRAMEWORK 
# REACT PY SUPPORT PICO CSS

url = "https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css"

pico_css = html.link({"rel":"stylesheet","href":url})




@component
def Mysample():
	myselect,set_myselect = use_state("dog")
	show,set_show = use_state(False)
	myrange,set_myrange = use_state(40)

	def togglemodal(event):
		set_show(True)

	return html.div({
		"class":"container"
		},
		# INSERT HERE
		pico_css,
		
		# FIRST I CREATE CARD
		html.article(
			html.header("This card"),
			# THIS BODY
			html.h3("this body text "),
			# AND FOOTER
			html.footer("i am footer")
			),

		# AND TWO I CREATE SELECT DROPDOWN
		html.div(
			html.h3(f"you select {myselect}"),
			html.select({
				"on_change":lambda event:set_myselect(event['target']['value'])

				},
				html.option({
					"value":"dog",
					},"dogs"),
				html.option({
					"value":"cats",
					},"cats"),
				)
			),
		# AND 3 I CREATE DIALOG MODAL
		html.button({
			"on_click":togglemodal
			},"Open dialog"),
		html.dialog({
			"open":show
			},
			html.article(
				html.h3("THis DIALOG"),
				html.footer(
					html.button({
						"on_click":lambda event:set_show(False)

						},"CLose Dialog")
					)
				)
			),

		# AND NEXT I CREATE PROGRESS BAR AND RANGE SLIDER
		html.progress(),
		# AND I CREATE RANGE SLIDER
		html.h3(f"you range is {myrange}"),
		html.input({
			"type":"range",
			"min":10,
			"max":100,
			"value":myrange,
			"on_change":lambda event:set_myrange(event['target']['value'])

			})


		)

app = FastAPI()
configure(app,Mysample)