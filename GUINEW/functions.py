def all_children (window) :
    _list = window.winfo_children()
    for item in _list :
        if item.winfo_children() :
            print(item)
            _list.extend(item.winfo_children())
    return _list

