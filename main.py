from organizer import FileOrganizer

folder = input("Enter the folder path to organize: ")
organizer = FileOrganizer(folder)
organizer.organize()
organizer.show_summary()