def main():
    file_name = input("File name: ").strip().casefold()
    num = len(file_name.split("."))

    if num == 2:
        name, ext = file_name.split(".")
    elif num == 1:
        ext = None
    else:
        name, ext1, ext = file_name.split(".")

    match ext:
        case "jpeg"| "jpg" | "gif" | "png":
            if ext == "jpg":
                ext = "jpeg"
            print(f"image/{ext}")
        case "pdf" | "zip":
            print(f"application/{ext}")
        case "txt":
            print(f"text/plain")
        case _:
            print("application/octet-stream")

main()

