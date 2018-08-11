import pytube 

linke=input("Enter the URL linke:")
video=pytube.YouTube(linke)
opt=0
vid=video.streams.all()
for i in video.streams.all():
	print(str(opt)+". "+str(i))
	opt=opt+1
vid=vid[int(input("enter num:"))]
path=input("Enter the path:")
vid.download(path)
