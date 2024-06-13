BUILTIN = "__builtins__"

FALLBACK_DJANGO_DATA = {
    "file_watcher_globs": ["**/templates/**", "**/templatetags/**", "**/static/**"],
    "static_files": [],
    "urls": [],
    "libraries": {
        "__builtins__": {
            "tags": {
                "autoescape": {"inner_tags": [], "closing_tag": "endautoescape"},
                "comment": {"inner_tags": [], "closing_tag": "endcomment"},
                "cycle": {},
                "csrf_token": {},
                "debug": {},
                "filter": {"inner_tags": [], "closing_tag": "endfilter"},
                "firstof": {},
                "for": {"inner_tags": ["empty"], "closing_tag": "endfor"},
                "if": {"inner_tags": ["else", "elif"], "closing_tag": "endif"},
                "ifchanged": {"inner_tags": [], "closing_tag": "endifchanged"},
                "load": {},
                "lorem": {},
                "now": {},
                "regroup": {},
                "resetcycle": {},
                "spaceless": {"inner_tags": [], "closing_tag": "endspaceless"},
                "templatetag": {},
                "url": {},
                "verbatim": {"inner_tags": [], "closing_tag": "endverbatim"},
                "widthratio": {},
                "with": {"inner_tags": [], "closing_tag": "endwith"},
                "block": {"inner_tags": [], "closing_tag": "endblock"},
                "extends": {},
                "include": {},
            },
            "filters": [
                "addslashes",
                "capfirst",
                "escapejs",
                "json_script",
                "floatformat",
                "iriencode",
                "linenumbers",
                "lower",
                "make_list",
                "slugify",
                "stringformat",
                "title",
                "truncatechars",
                "truncatechars_html",
                "truncatewords",
                "truncatewords_html",
                "upper",
                "urlencode",
                "urlize",
                "urlizetrunc",
                "wordcount",
                "wordwrap",
                "ljust",
                "rjust",
                "center",
                "cut",
                "escape",
                "force_escape",
                "linebreaks",
                "linebreaksbr",
                "safe",
                "safeseq",
                "striptags",
                "dictsort",
                "dictsortreversed",
                "first",
                "join",
                "last",
                "length",
                "length_is",
                "random",
                "slice",
                "unordered_list",
                "add",
                "get_digit",
                "date",
                "time",
                "timesince",
                "timeuntil",
                "default",
                "default_if_none",
                "divisibleby",
                "yesno",
                "filesizeformat",
                "pluralize",
                "phone2numeric",
                "pprint",
            ],
        },
        "cache": {
            "tags": {"cache": {"inner_tags": [], "closing_tag": "endcache"}},
            "filters": [],
        },
        "i18n": {
            "tags": {
                "get_available_languages": {},
                "get_language_info": {},
                "get_language_info_list": {},
                "get_current_language": {},
                "get_current_language_bidi": {},
                "trans": {},
                "translate": {},
                "blocktrans": {},
                "blocktranslate": {},
                "language": {"inner_tags": [], "closing_tag": "endlanguage"},
            },
            "filters": [
                "language_name",
                "language_name_translated",
                "language_name_local",
                "language_bidi",
            ],
        },
        "l10n": {
            "tags": {"localize": {"inner_tags": [], "closing_tag": "endlocalize"}},
            "filters": ["localize", "unlocalize"],
        },
        "static": {
            "tags": {"get_static_prefix": {}, "get_media_prefix": {}, "static": {}},
            "filters": [],
        },
        "tz": {
            "tags": {
                "localtime": {"inner_tags": [], "closing_tag": "endlocaltime"},
                "timezone": {"inner_tags": [], "closing_tag": "endtimezone"},
                "get_current_timezone": {},
            },
            "filters": ["localtime", "utc", "timezone"],
        },
    },
    "templates": {},
    "global_template_context": {
        "csrf_token": {},
    },
}
