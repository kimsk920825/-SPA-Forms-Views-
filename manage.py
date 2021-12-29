#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    #프로젝트 진입점은 manage.py
    #실제 서비스 구동할 때는 wsgi.py
    #manage.py, wsgi.py, asgi.py 공통점은 장고 settings 경로를 보여줌
    #아래 코드 해석: 프로그래밍을 시작했을 때, 환경변수 목록에서 DJANGO_SETTINGS_MODUEL이 없다면
    #   askcompany.settings를 환경변수로 지정하겠다.  
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askcompany.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
