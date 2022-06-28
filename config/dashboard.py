from django.utils.translation import gettext_lazy as _
from grappelli.dashboard import Dashboard, modules


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for jorevi
    """

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        self.children.append(
            modules.Group(
                _("Applications"),
                column=1,
                collapsible=True,
                children=[
                    modules.AppList(
                        _("My applications"),
                        column=1,
                        css_classes=("collapse closed",),
                        models=(
                            "jorevi.companies.models.Company",
                            "jorevi.jobs.models.Category",
                            "jorevi.jobs.models.Job",
                            "jorevi.blog.models.Category",
                            "jorevi.blog.models.Post",
                            "jorevi.resumes.models.ResumeFile",
                        ),
                    ),
                    modules.AppList(
                        _("Third-Party applications"),
                        column=1,
                        css_classes=("collapse closed",),
                        models=(
                            "taggit.models.Tag",
                            "taggit.models.TaggedItem",
                            "revision.models.Revision",
                            "revision.models.Version",
                        ),
                    ),
                ],
            )
        )
        self.children.append(
            modules.AppList(
                _("Administration"),
                column=2,
                css_classes=("collapse closed",),
                models=(
                    "django.contrib.*",
                    "rest_framework.authtoken.models.Token",
                    "rest_framework.authtoken.models.TokenProxy",
                    "jorevi.users.models.Social",
                    "jorevi.users.models.Avatar",
                    "jorevi.users.models.User",
                    "jorevi.users.models.Profile",
                    "jorevi.users.models.Newsletter",
                    "jorevi.users.models.Contact",
                ),
            ),
        )

        # append another link list module for "support".
        self.children.append(
            modules.LinkList(
                _("Media Management"),
                column=3,
                children=[
                    {
                        "title": _("FileBrowser"),
                        "url": "/jadmin/filebrowser/browse/",
                        "external": False,
                    },
                ],
            )
        )

        # append another link list module for "support".
        self.children.append(
            modules.LinkList(
                _("Support"),
                column=3,
                children=[
                    {
                        "title": _("Grappelli Documentation"),
                        "url": "https://django-grappelli.readthedocs.io/en/latest/",
                        "external": True,
                        "target": "True",
                    },
                    {
                        "title": _("Grappelli Google-Group"),
                        "url": "https://groups.google.com/g/django-grappelli",
                        "external": True,
                        "target": "True",
                    },
                    {
                        "title": _("Remote Job Github"),
                        "url": "https://github.com/remoteintech/remote-jobs",
                        "external": True,
                        "description": "A list of semi to fully remote-friendly companies in or around tech.",
                        "target": "True",
                    },
                ],
            )
        )
        # append a feed module
        self.children.append(
            modules.Feed(
                _("Latest Django News"),
                column=3,
                feed_url="http://www.djangoproject.com/rss/weblog/",
                limit=5,
            )
        )
        self.children.append(
            modules.LinkList(
                _("Job References"),
                column=4,
                children=[
                    {
                        "title": _("Remote Job List"),
                        "url": "https://github.com/remoteintech/remote-jobs",
                        "external": True,
                        "description": "A list of semi to fully remote-friendly companies in or around tech.",
                        "target": "True",
                    },
                    {
                        "title": _("Public Job API"),
                        "url": "https://github.com/public-apis/public-apis#jobs",
                        "external": True,
                        "description": "A collective list of free APIs for use in software and web development(job)",
                        "target": "True",
                    },
                ],
            )
        )
        # append a recent actions module
        self.children.append(
            modules.RecentActions(
                _("Recent actions"),
                column=4,
                limit=5,
                collapsible=True,
            )
        )
