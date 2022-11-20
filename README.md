# Huki

Stores information about several entries.

## Design Document

If you want to add a new page with certain information and functionality, you will need to tweak some files. First in the urls.py file you will need to add the pathway of your new page/url. Next you will need to add a html file in the templates/encyclopedia directory, this is where you store all your html pages. If you want your page to have some functionality with the help of Python and Django you need to edit the views.py file.

The HTML-pages you will need to complete this assignment:
index.html
layout.html
entry.html
error.html
search.html
new_entry.html
edit_entry.html

Not a sketch, but a good description of the workflow:
On the index page you will see a list of all the entries/pages you have made on the Huki website. On the left of your screen you will see a sidebar with information I will cover in a second, but this sidebar will always appear on screen. When you click on an entry you will be directed to the html page of that entry. On this page you will have the option to edit the content of the page, which brings you to the edit_entry page. This is the same for all the entries you will see appear on the index page. Regarding the sidebar you have several options to choose from. On the top you have the search function. Here you can type the exact name of an entry and this will redirect you to that page, but if you type a substring of certain entries you will go the the search page with a list of the entries including your input substring. You can click those entries in this list to redirect to that entrypage. The second option is the Home function which simply redirects you to the index page. The third option in the sidebar is the create new page function, which brings you to the new_entry page. Here you can create your new entry page with a title and the content in Markdown. When you save this information you will be redirected to this new entry page and it will also appear in the list of total entries on the index page. Finally you have the random page function which redirects you to a random entry page of all the entries you have created. 
