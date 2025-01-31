import requests
from auth import conf_token, staging_conf_token
import json
from config import confluence, confluence_staging, conf_base


class Confluence:
    def __init__(self, is_staging=False):
        self.token = staging_conf_token if is_staging else conf_token
        self.conf_url = confluence_staging if is_staging else confluence
        self.conf_base = conf_base


