# Private Picture Database (PrivatePicDB)

PrivatePicDB wants to help you organize your private picture: tag them with the persons on them or scenery they were taken and let them be filtered by date<sup id="a1">[1](#f1)</sup>. First you will have to tag the pictures manually - the idea behind is to use machine learning algorithms later to let the tags be determined automatically.

The basis for the program is a SQLite-database (lightweight, local) with search options. Add persons to a database table and sceneries in the background to label pictures based on the location.

## Details

Use face-recognition to generate labels based on persons on the pictures:
- take the available open source tools - see e.g. the face recognition toolbox in the repository [ageitgey/face_recognition](https://github.com/ageitgey/face_recognition) - to generate "face-features"
- train a rather simple model on these features for a few pictures of your friends and family
- let the software recognize your relatives automatically: it shall ask you if it is really them once in a while and if there is a high uncertainty in the final model
- if there is somebody knew appearing on the pictures: PrivatePicDB shall ask you who it is and eihter make a knew entry as unknwon person or a name you chose

Use a pretrained neural network for object detection to recognize the scenery of the pictures.

<b id="f1">1</b>: If available taken directly from the image file metainformation. [↩](#a1)  
