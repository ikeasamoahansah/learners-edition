from sys import argv

my_list = [{"on my way": "omw"},{"be right back": "brb"},{"what you doing": "wyd"}]
search_key = argv[1]
for my_dict in my_list:
    for key, value in my_dict.items():
        if search_key in key:
            print(value)
            break
        
