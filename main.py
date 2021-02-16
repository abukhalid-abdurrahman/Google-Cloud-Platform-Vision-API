import application as app
import image as img
import services

clientApp = app.CreateApplication()
image = img.GetImage(r'', "")
response = services.GetTextResponse(image=image, client=clientApp)
print(response)
