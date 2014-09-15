from waliki.plugins import BasePlugin, register


class GitPlugin(BasePlugin):

    slug = 'git'
    urls_page = ['waliki.git.urls']
    extra_page_actions = [('waliki_history', 'History')]

register(GitPlugin)
