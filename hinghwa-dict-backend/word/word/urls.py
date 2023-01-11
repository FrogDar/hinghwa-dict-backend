from django.urls import path

from .views import *

app_name = "word.word"

urlpatterns = [
    path("", searchWords),  # WD0102POST WD0201GET WD0202PUT
    path("/<int:id>", manageWord),  # WD0101GET WD0103PUT
    path("/add", load_word),  # WD0301POST
    path("/upload_standard", upload_standard),  # WD0302POST
    path("/phonetic_ordering", csrf_exempt(PhoneticOrdering.as_view())),  # WD0501
    path("/dictionary_search", csrf_exempt(DictionarySearch.as_view())),  # WD0502
    path(
        "/dictionary_search_initial", csrf_exempt(DictionarySearchInitial.as_view())
    ),  # WD0503
]
