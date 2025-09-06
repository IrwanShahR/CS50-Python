filename = input("What is the filename? ").strip()

stripfilename = filename.split(".")[-1]

match stripfilename:
    case "gif" | "png":
        print("image"+"/"+stripfilename)
    case "jpg" | "jpeg":
        print("image"+"/"+"jpeg")
    case "PDF" | "pdf":
        print("application"+"/"+"pdf")
    case "zip":
        print("application"+"/"+stripfilename)
    case "txt":
        print("text"+"/"+"plain")
    case _:
        print("application/octet-stream")

