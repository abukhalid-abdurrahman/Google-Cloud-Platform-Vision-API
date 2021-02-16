def GetTextResponse(image, client):
    response = client.text_detection(image=image)
    return response.text_annotations[0].description

def GetHandwrittenTextResponse(image, client):
    response = client.document_text_detection(image=image)
    return response.full_text_annotation.text

def GetFaceResponse(image, client):
    response = client.face_detection(image=image)
    return response.face_annotations

def GetLabelsResponse(image, client):
    response = client.label_detection(image=image)
    return response.label_annotations

def GetObjectResponse(image, client):
    response = client.object_localization(image=image)
    return response.localized_object_annotations
