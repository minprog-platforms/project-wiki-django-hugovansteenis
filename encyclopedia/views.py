from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def md_converter(title):
    entry = util.get_entry(title)
    markdowner = Markdown()
    if entry == None:
        return None
    else:
        return markdowner.convert(entry)

def return_entry(request, title):
    conversion = md_converter(title)
    if conversion == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry has not been found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": conversion
        })

def return_search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        conversion = md_converter(entry_search)
        if conversion != None:
            return render(request, "encyclopedia/entry.html",{
                "title": entry_search,
                "content": conversion
            })
        else:
            entries = util.list_entries()
            options = []
            for entry in entries:
                if entry_search.lower() in entry.lower():
                    options.append(entry)
            return render(request, "encyclopedia/search.html",{
                "options": options
            })

def new_entry(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_entry.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        title_exist = util.get_entry(title)
        if title_exist != None:
            return render(request, "encyclopedia/error.html",{
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title, content)
            conversion = md_converter(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": conversion
            })

def edit_entry(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_entry.html", {
                "title": title,
                "content": content
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        conversion = md_converter(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": conversion
        })

def randomize(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    conversion = md_converter(random_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": random_entry,
        "content": conversion
    })
