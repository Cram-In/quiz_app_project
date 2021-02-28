import pytest
from os import close, unlink
from tempfile import mkstemp
from itertools import count
from sqlalchemy import create_engine
from unittest.mock import Mock

from quiz.models import User, Score

User = Mock(query=Mock(all=Mock(return_value=[Mock(id=7, username="Guido", password="Klinkier1")])))
